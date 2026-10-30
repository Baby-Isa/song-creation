# Replication test

**Question:** can Claude research a song as well as ChatGPT did and reach the same conclusions?

**Test song:** Imogen Heap, "The Happy Song". Claude's analysis: `research/songs/imogen-heap-the-happy-song.md`.
**Caveat:** Zafar pasted the conversation with ChatGPT's findings already in it, so this wasn't a blind test. To compensate, every point below is backed by a source I found myself (30 Oct 2026).

## Comparison with ChatGPT

| Point | ChatGPT | Claude | Same? |
|---|---|---|---|
| Tempo | 163 BPM, 4/4, the slower of two fast versions | Same, plus the reason: it gave parents and babies more time to respond | Yes |
| Real sounds | Cat purr, giggles, sneezes, whistles, animals, hiccups | Has the parent-poll ranking: Boo! 66%, raspberries 57%, sneeze 51%, laughter 28%, animals 23%. Credited contributors: Scout's giggles, the dad's whistle, a Pomeranian dog. | Yes, and more detailed |
| A real cat purr | Says Heap credits one | Couldn't confirm: only a lyric about purring | ChatGPT may be wrong |
| Plosives | ba, pa, da, beep, pop | Same, plus the finding: plosives beat soft "la" sounds | Yes |
| Melody and structure | Simple and predictable, with a recurring chorus and a journey through places | Same, plus: the journey runs sky to ocean by bike, submarine and rocket (picked for its plosives); the chorus worked best | Yes, and more detailed |
| Key | "Bright major key" | E flat major (Scout's key) | More precise |
| Vocal | Warm female lead | Energetic sing-song "motherese" female lead; Heap's mum in the chorus | More precise |
| Surprise devices | Changing details, little surprises | Researchers' list: drum rolls, key changes, rising pitch glides | More precise |
| Limits of the research | Doesn't guarantee a copy will work | Same, plus: pilot study, not peer-reviewed, commercially funded | Yes |
| Instrumentation | Mbira, kalimba, pizzicato, synths: its own creative choices, not research | Not found. Neither of us can hear the track. | Gap for both |

## Notes on ChatGPT's prompt

- **The style prompt is 939 characters and 123 words.** That's over the 900 cap in the chat, and past the roughly 100 words where Suno reportedly starts treating parts of the prompt as optional. About half the length would probably hold better.
- **The sound effects are listed in the style box.** Cueing them where they happen in the lyrics should work better, and ChatGPT itself warned that Suno may sing the effects instead of making them.
- **It leaves out ingredients the research names:** the key change, drum rolls, rising glides and the sing-song vocal.

## Verdict

**Replicable.** I reached every one of ChatGPT's main conclusions from sources I found myself, with more specific detail, and I found one claim (the credited cat purr) I couldn't support.

**The gap, for both of us, is what the track actually sounds like** (its instruments and production). For songs where that matters, which is most of the 90s hip hop, there are two ways to fill it:
- I use what I already know about well-known records.
- Zafar puts the song's YouTube link into Gemini, which can analyse video audio, asks for the instrumentation, drums, bass and texture, and pastes the answer back.
