# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  mood, energy, tempo_bpm, valence, danceability, acousticness
- What information does your `UserProfile` store
  favorite_genre, favorite_mood, target_energy, and likes_acoustic
- How does your `Recommender` compute a score for each song
  It turns different features into one score: matching genre and mood adds points, songs closer to the target energy get higher scores, and acousticness is either rewarded or penalized depending on the user’s preference.
- How do you choose which songs to recommend
  I score every song, sort by score from highest to lowest, break ties with stronger preference matches (then closer energy), and return the top k songs.

Real-world recommenders first pick a group of possible items, score how well each one matches the user, and then rank them while adding things like variety and freshness. They also keep improving based on feedback.

Algorithm Recipe:

1. Store one user taste profile with `favorite_genre`, `favorite_mood`, `target_energy`, and `likes_acoustic`.
2. Loop through every song in `data/songs.csv` and give it a score.
3. Add `+2.0` points for a genre match.
4. Add `+1.0` point for a mood match.
5. Add energy similarity points using `2.0 * (1 - min(1, abs(song_energy - target_energy)))` so songs closer to the target energy score higher.
6. Add an acousticness bonus or penalty depending on whether the user likes acoustic songs.
7. Sort all songs from highest score to lowest score.
8. Break ties by choosing the song with the smaller energy distance, then return the top `k` songs.

This simple content-based method works well for a small catalog because it rewards songs that match the user’s stated preferences while still letting the system compare every song in a consistent way.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood
- It may over-prioritize genre and mood matches, which could hide great songs that fit the user’s energy or acoustic preference better

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

I learned that recommender systems turn data into predictions by comparing item features with user preferences and combining those matches into a single score. Things like genre, mood, and energy can be measured and weighted to estimate how much a user will like a song. The system then ranks items based on these scores and can improve over time by learning from user feedback, like clicks or skips.


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

