import math
import librosa

import pandas as pd

from .extraction import enrich_song_features, partition

def predic_genre(y, sampling_rate, model, genre_encoder, partition_length = 3):
    segment_count =  math.ceil(librosa.get_duration(y = y, sr = sampling_rate) / partition_length)
    all_partitions = partition(y, segment_count)

    result = []
    
    for current_partition in all_partitions:
        enriched_song_features = enrich_song_features(current_partition, sampling_rate)
        result.append(enriched_song_features)
    
    song_df = pd.DataFrame(result)
    song_df = song_df.dropna()

    partition_genres = []

    for index in song_df.index.values:
        row = song_df.iloc[[index]]
        row = pd.DataFrame(row, columns=song_df.columns)
        result = model.predict(row)
        partition_genres.append(genre_encoder.inverse_transform(result))

    return pd.DataFrame(partition_genres)