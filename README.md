# Song Creation

Making a series of original songs in Suno, in the styles Zafar likes, on themes he picks.

## Why

Suno won't take a reference song. The workaround that worked with ChatGPT: paste in songs he likes, analyse what he likes about them, and turn that into a Suno **style prompt** (the sound) and **lyrics** (with structure tags) on a chosen theme. The results were good. A Punjabi wedding duet made this way was the first dance at a friend's wedding.

## Outcomes

1. **A style map:** every reference song analysed and grouped into a handful (probably 4 to 8) of styles different enough to need separate style prompts, each with a tested Suno style prompt.
2. **Songs:** about 4 or 5 song ideas per style, each with a ready-to-paste style prompt and lyrics, made in Suno, with the best take noted.
3. **Know-how:** what works in Suno, written down as we learn it (`docs/suno-guide.md`), so later prompts get better.

The styles we know about so far:
- 90s hip hop, jazzy and sample-based: most of his taste.
- Songs for his son to play in the car (the example in the ChatGPT chat). More of these.
- Language-blend pop, such as the Spanish/Arabic reggaeton style done in Italian (Sarah and the pasta love story, with pasta names woven in), and the Punjabi wedding duet (a boy and a girl trading lines, with a rap about two-thirds of the way through).

## Method

1. **Replication test.** Zafar shares a ChatGPT conversation. Claude researches the same song independently and compares its conclusions with ChatGPT's (`research/replication-test.md`). If Claude falls short, we add another source, for example the same prompt run in Gemini and pasted back.
2. **Analyse.** Zafar shares his playlist and a few other songs. One short analysis per song: genre, era, tempo and key, drums, bass, samples and harmony, instruments, vocals and flow, structure, mood, production texture, lyrical devices, what he probably likes about it, and Suno-ready descriptors.
3. **Group.** Cluster the songs into distinct styles, take the common features of each group and write one Suno style prompt per style (`styles/`). Zafar approves the grouping.
4. **Brainstorm.** One style at a time: 4 or 5 lyric themes. Zafar steers and Claude has creative freedom inside each theme.
5. **Write and make.** Claude writes the final style prompt, lyrics and settings (`songs/`). Zafar makes them in Suno and reports back. We note what worked and refine.
