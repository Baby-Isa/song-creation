# Status

Rewritten at the end of every step (handover).

## Next chat

**Where things stand (30 Oct 2026):**
- The car-song series is done: all seven are written in `songs/car-01` to `car-07`, and Zafar is making them in Suno.
- What worked: the base style in `styles/00-car-songs.md` (modelled on the original song, which Zafar calls the best template), fresh words for each song, and fun rhymes.
- What didn't: new genres, new devices, and reusing tricks like "Yeh-boh". Lessons are in `docs/suno-guide.md`.

**Next steps, in order (a new chat):**
1. Zafar sends screenshots of his Spotify playlist and his other favourite songs. List every song in `research/playlist.md`.
2. Analyse each song (template `research/songs/_template.md`), short and practical, saying what came from sources and what is my own knowledge. Where my knowledge is thin, ask Zafar to run the song's YouTube link through Gemini.
3. Group them into distinct styles (most will be jazzy 90s hip hop, plus the language-blend pop such as Spanish/Arabic reggaeton and the Punjabi wedding duet). Zafar approves the grouping.
4. One style file per group, with a style prompt (aim for 300 to 600 characters, never over 900).
5. Then, one style at a time: brainstorm lyric ideas, then write one song per turn.
6. Any fixes to the car songs that Zafar reports go in their song files.

**Open questions to Zafar:** none.

**Starting prompt for a new chat:**
> Read `CLAUDE.md`, then `docs/status.md` "Next chat" only. We're starting the style analysis: I'll send screenshots of my playlist and favourite songs. List them, analyse each, then propose the style groups. Don't overthink it. Work in the song-creation repo on the branch named in the session.
