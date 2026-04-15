# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeMatch Mini 1.0

---

## 2. Intended Use  

This recommender suggests the top 5 songs from a small catalog based on a user's preferred genre, preferred mood, and target energy level. It assumes the user can be represented by a single taste profile (one favorite genre, one favorite mood, and one energy target). 
---

## 3. How the Model Works  

Each song includes genre, mood, and numeric audio features like energy. The user profile includes favorite genre, favorite mood, and target energy. For each song, the system adds points for genre match (+2.0) and mood match (+1.0), then adds an energy-similarity score (up to +2.0) based on how close the song energy is to the user's target. Songs are ranked by total score from highest to lowest, with a tie-break that prefers smaller energy distance. Compared with the starter version, this model now has an explicit scoring rule, a deterministic ranking rule, and explanation text for why each song scored the way it did.

---

## 4. Data  

The dataset currently contains 10 songs in data/songs.csv. It includes genres such as pop, lofi, rock, ambient, jazz, synthwave, and indie pop, and moods such as happy, chill, intense, relaxed, moody, and focused. This is a very small and curated catalog, so many musical styles, languages, and cultural contexts are missing.

---

## 5. Strengths  

The system works well for users with clear and simple preferences, especially when they care strongly about one genre/mood pair and a general energy level (for example, chill lofi with low energy). The scoring is easy to explain, and recommendation outputs are deterministic and reproducible. 

---

## 6. Limitations and Bias 

The model is narrow and can over-prioritize genre and mood bonuses over nuanced musical similarity. It does not use tempo, valence, danceability, acousticness, lyrical content, context, or listening history in scoring. Because the catalog is small, underrepresented genres and moods are less likely to be recommended fairly. 

---

## 7. Evaluation 

---

## 8. Future Work  

I would add diversity constraints so the top 5 are not too similar, and improve explanations by reporting exact score components in a user-friendly format.

---

## 9. Personal Reflection  

I learned that recommendation systems are not only about a scoring formula, but also about ranking behavior, tie-breaks, and input quality. A simple rule can feel accurate in many cases, but edge cases quickly reveal hidden assumptions and bias. 
