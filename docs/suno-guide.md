# Suno guide

What we know about Suno, and what we've learned from our own takes. "Check" means it's unverified: confirm it in the app and update this file.

## Limits (Zafar, 30 Oct 2026)

- **Style field:** 1,000 characters. **Lyrics field:** 5,000 characters. Both count line breaks.
- **Our caps are 90% of those: style 900, lyrics 4,500**, to leave a buffer. `python3 tools/count.py songs/<file>.md` checks a song file.
- **Exclude styles** is a separate box (about 1,000 characters) for sounds to avoid.
- **Model:** one site reports v6 came out in Sept 2026. Check which model the account uses.

## Style prompt: best practice

The online guides agree that shorter and front-loaded beats long:
- **Aim for about 300 to 600 characters.** 900 is the ceiling, not the target. A v6 guide suggests 250 to 600 characters. A Reddit roundup reports that past about 100 words Suno starts treating parts of the prompt as optional.
- **Order matters, because the earliest words carry the most weight:** genre or blend and BPM, then the instruments and what each one does, then the vocal type and delivery, then the production and mix.
- **For v6, write 2 or 3 plain sentences** rather than a long list of tags.
- **One clear idea per style.** Too many competing descriptors muddy the result.
- **Put negatives in Exclude styles**, not "no X" in the style box.
- **Don't use artist names.** Suno rejects them or silently drops them, so describe era, instruments and texture instead.
- **Settings (check in the app):**
  - Raise **Style Influence** above its 50% default before rewriting the prompt.
  - Set **Variety** low when testing.
  - Set the vocal gender in More Options.
  - Set the duration to custom, because the default runs to about 3 minutes.
- **Lyrics carry the detail.** Structure, dynamics and sound cues go in the lyrics as section tags, not in the style box.

Sources: [HookGenius: Suno character limits](https://hookgenius.app/learn/suno-character-limits/), [Roo: best Suno prompts after v6](https://roo.beehiiv.com/p/best-suno-prompts-v6), [Medium: Reddit tips roundup](https://medium.com/@aitooldiscovery/suno-reddit-tips-and-prompts-what-r-sunoai-users-actually-do-65b59d51bcad). These are blogs and forum summaries, not Suno's own documentation.

## Lyrics conventions

- Put structure tags on their own line in square brackets: `[Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Rap Verse]`, `[Outro]`.
- One cue per bracket, kept short, for example `[Chorus | fuller harmonies]`. Without cues, verses and choruses can sound the same.
- Lines of about 6 to 10 syllables sing most naturally.
- Brackets can also carry performance notes, for example `[Female vocal]`, `[Male vocal]`, `[Duet]`, `[Scratch break]` or `[Beat drops out]`. Check how reliably each one works.
- Text in brackets is not sung. Text in round brackets is usually sung as backing vocals or ad-libs.

## What we've learned from our own takes

(Add a line after each session: what we tried, what happened, what to do next time.)
