import os 
import sys
import getopt
import time

import librosa

import numpy as np
import pandas as pd

from scipy.stats import kurtosis
from scipy.stats import skew


def partition(y, segment_count):
    if segment_count == 1:
        return [y]
    else:
        full_length = len(y)
        remainder = full_length % segment_count
        end =  full_length - remainder
        normalized_y = y[0:end]
        partitions =  np.split(normalized_y, segment_count)
        return partitions

def file_with_genre(genres, dir):    
    song_genres = []
    song_files = []
    
    for genre in genres:
        path = dir + "/" + genre
        
        for song in os.listdir(path):
            song_genres.append(genre)
            song_files.append(song)
        
    result = { "genre" : song_genres, "file": song_files }
    return pd.DataFrame.from_dict(result)

def extract_song_features(dir, file_and_genre, segments_count = 1):
    enriched_features_list = []
    file_and_genre = file_and_genre.sort_values("file")
    for _, row in file_and_genre.iterrows():
        song_file = dir + "/" + row["genre"] + "/" + row["file"]
        print("Extracting music features from: " + song_file)
        y, sampling_rate = librosa.load(song_file)
            
        segments =  partition(y, segments_count)
        
        for segment in segments:
            enriched_features_row = enrich_song_features(segment, sampling_rate)
            enriched_features_row["genre"] = row["genre"]
            enriched_features_row["file"] = row["file"]
        
            enriched_features_list.append(enriched_features_row)
    
    return pd.DataFrame(enriched_features_list)


def enrich_song_features(y, sampling_rate):
    features = {}
    features["zero_crossings"] = librosa.feature.zero_crossing_rate(y).ravel()
    features["centroid"] = librosa.feature.spectral_centroid(y = y, sr = sampling_rate).ravel()
    features["rolloff_frequency"] = librosa.feature.spectral_rolloff(y = y, sr = sampling_rate).ravel()
    features['chroma_stft']=librosa.feature.chroma_stft(y=y, sr=sampling_rate).ravel()
    features["rmse"] = librosa.feature.rms(y = y).ravel()
    features["flux"] = librosa.onset.onset_strength(y  = y, sr=sampling_rate).ravel()
    features["spectral_contrast"] = librosa.feature.spectral_contrast(y = y, sr=sampling_rate).ravel()
    features["bandwidth"] = librosa.feature.spectral_bandwidth(y = y, sr=sampling_rate).ravel()
    features["flatness"] = librosa.feature.spectral_flatness(y = y).ravel()
      
    mfcc = librosa.feature.mfcc(y = y, sr = sampling_rate, n_mfcc = 13)
    for idx, v_mfcc in enumerate(mfcc):
        features['mfcc_{}'.format(idx)] = v_mfcc.ravel()
    
    
    def statistical_measures(descriptors):
        result = {}
        for k, v in descriptors.items():
            result['{}_max'.format(k)] = np.max(v)
            result['{}_min'.format(k)] = np.min(v)
            result['{}_mean'.format(k)] = np.mean(v)
            result['{}_std'.format(k)] = np.std(v)
            result['{}_kurtosis'.format(k)] = kurtosis(v)
            result['{}_skew'.format(k)] = skew(v)
        return result
    
    features = statistical_measures(features)
    features["tempo"] = librosa.feature.tempo(y = y, sr = sampling_rate)[0]
    return features


def main(argv):
    outputfile = ""
    opts, _ = getopt.getopt(argv,"hs:o:",["segments=","out="])
    for opt, arg in opts:
      if opt == '-h':
         print (__file__ + " -s <segments> -o <outputfile>")
         sys.exit()
      elif opt in ("-s", "--segments"):
         segments_count = int(arg)
      elif opt in ("-o", "--out"):
         outputfile = arg
    print ("Segments counts:", segments_count)
    print ("Output file is", outputfile)

    os.chdir("../data")
    dat_dir = os.path.abspath(os.curdir)
    genres = ["pop", "country", "metal", "reggae", "jazz", "rock", "blues", "hiphop", "classical", "disco"]
    start_time = time.time()
    files = file_with_genre(genres, dat_dir)
    song_features = extract_song_features(dat_dir, files, segments_count)
    song_features.to_csv(outputfile, index=False)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Dataset generation time: ", int(elapsed_time / 60), "minutes")

if __name__ == "__main__":
    main(sys.argv[1:])
