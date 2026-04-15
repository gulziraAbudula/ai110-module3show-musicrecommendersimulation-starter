import csv

from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


def _resolve_pref(user_prefs: Dict, primary_key: str, fallback_key: str, default):
    """Resolve a preference from either canonical or shorthand key names."""
    if primary_key in user_prefs:
        return user_prefs[primary_key]
    if fallback_key in user_prefs:
        return user_prefs[fallback_key]
    return default


def _score_song_components(song: Dict, favorite_genre: str, favorite_mood: str, target_energy: float) -> Tuple[float, float, float, float]:
    """Return total score and component values used by both recommenders."""
    genre_score = 2.0 if song.get("genre") == favorite_genre else 0.0
    mood_score = 1.0 if song.get("mood") == favorite_mood else 0.0

    energy_value = float(song.get("energy", 0.0))
    energy_distance = abs(energy_value - target_energy)
    energy_score = 2.0 * (1.0 - min(1.0, energy_distance))

    total_score = genre_score + mood_score + energy_score
    return total_score, genre_score, mood_score, energy_distance


def _song_to_dict(song: Song) -> Dict:
    """Normalize Song dataclass instances into a dict for shared scoring."""
    return {
        "id": song.id,
        "title": song.title,
        "artist": song.artist,
        "genre": song.genre,
        "mood": song.mood,
        "energy": song.energy,
        "tempo_bpm": song.tempo_bpm,
        "valence": song.valence,
        "danceability": song.danceability,
        "acousticness": song.acousticness,
    }

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored_songs: List[Tuple[Song, float, float]] = []
        for song in self.songs:
            score, _, _, energy_distance = _score_song_components(
                _song_to_dict(song),
                favorite_genre=user.favorite_genre,
                favorite_mood=user.favorite_mood,
                target_energy=user.target_energy,
            )
            scored_songs.append((song, score, energy_distance))

        ranked = sorted(scored_songs, key=lambda item: (-item[1], item[2]))
        return [song for song, _, _ in ranked[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        score, genre_score, mood_score, energy_distance = _score_song_components(
            _song_to_dict(song),
            favorite_genre=user.favorite_genre,
            favorite_mood=user.favorite_mood,
            target_energy=user.target_energy,
        )
        return (
            f"Score {score:.2f}: "
            f"genre={'match' if genre_score else 'no match'}, "
            f"mood={'match' if mood_score else 'no match'}, "
            f"energy distance={energy_distance:.2f}"
        )

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict] = []

    print(f"Loading songs from {csv_path}...")

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if not row:
                continue

            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    favorite_genre = str(_resolve_pref(user_prefs, "favorite_genre", "genre", ""))
    favorite_mood = str(_resolve_pref(user_prefs, "favorite_mood", "mood", ""))
    target_energy = float(_resolve_pref(user_prefs, "target_energy", "energy", 0.0))

    scored_songs = []
    for song in songs:
        total_score, genre_score, mood_score, energy_distance = _score_song_components(
            song,
            favorite_genre=favorite_genre,
            favorite_mood=favorite_mood,
            target_energy=target_energy,
        )
        explanation = (
            f"genre={'match' if genre_score else 'no match'}, "
            f"mood={'match' if mood_score else 'no match'}, "
            f"energy distance={energy_distance:.2f}"
        )
        scored_songs.append((song, total_score, explanation, energy_distance))

    ranked_songs = sorted(scored_songs, key=lambda item: (-item[1], item[3]))
    return [(song, score, explanation) for song, score, explanation, _ in ranked_songs[:k]]
