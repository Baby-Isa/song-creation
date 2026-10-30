# Song Creation

Zafar is making songs in **Suno** (paid for one month, from about 30 Oct 2026). Claude researches the songs he likes, works out the distinct styles in them, and writes Suno prompts (a style prompt and lyrics) for new songs on themes he chooses. Zafar makes the songs in Suno and says what worked. He owns the project and has the final say.

The aims, outcomes and method are in `README.md`. The newest word from Zafar wins: if it clashes with a doc, follow him and update that doc in the same commit ("Zafar, <date>").

## Working agreement

- Short, plain replies. Ask decisions as a numbered list with my recommendations, so he can answer "yes to all except …".
- When he says more is coming, collect it and wait. Improve his ideas and push back when I disagree.
- Lyrics: he gives the theme, and I have creative freedom within it. Themes are woven in naturally (the pasta song should sound like a normal love song unless you listen closely).
- Be honest about evidence: say what came from a source (with a link), what is from my own knowledge and what is a guess. I can't listen to audio. I read about songs (lyrics sites, reviews, interviews, sample databases, BPM and key sites) and use what I already know.
- Don't paste whole copyrighted lyrics into the repo. Describe the techniques, quote a line at most. Every new lyric is original.
- Suno prompts: no artist or song names (describe the sound instead), important tags first, within the limits in `docs/suno-guide.md`.
- Stay within the month: aim for finished songs, not perfect docs.

## Where things live

| What | Where |
|---|---|
| Aims, outcomes, method | `README.md` |
| Where we are and the next step (handover) | `docs/status.md`, "Next chat" |
| Decisions (Zafar's yes and no, dated) | `docs/decisions.md` |
| Suno know-how: limits, tags, what works | `docs/suno-guide.md` |
| The ChatGPT replication test | `research/replication-test.md` |
| Songs to analyse and their status | `research/playlist.md` |
| One analysis per reference song | `research/songs/<artist>-<title>.md` (template `_template.md`) |
| One file per style, with its Suno style prompt | `styles/<nn>-<name>.md` (template `_template.md`) |
| One file per new song: brief, prompts, takes, verdict | `songs/<style>-<nn>-<name>.md` (template `_template.md`) |

## Starting a chat

Read `docs/status.md` "Next chat" only, then open what the task needs. At the end of each step, or at about 70% context, rewrite "Next chat" (where things stand, what's open, a starting prompt), then commit and push to the working branch.
