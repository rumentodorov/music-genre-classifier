import pandas as pd

from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_genre(songs):
    song_genres = songs["genre"]
    genre_encoder = LabelEncoder()
    transformation = genre_encoder.fit_transform(song_genres)
    return (transformation, genre_encoder.classes_)


def preprocess_song_features(songs):
    song_features = songs.drop(columns=["genre" , "file"], axis=1)
    scaler = StandardScaler()
    scaler.fit(song_features)
    return pd.DataFrame(scaler.transform(song_features), columns=song_features.columns)
