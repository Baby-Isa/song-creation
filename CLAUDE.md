# Song Creation — Project Guide

This repo holds songs written for **Suno**: a style prompt and lyrics for each song.
Everything written here gets pasted straight into Suno, so it must follow the Suno rules below.

## Workflow

1. **Research**: analyse the reference songs and save the notes under `research/`. The user approves them before anything else happens.
2. **One song per chat turn**: write the style prompt and lyrics for one song, wait for the user's feedback, then do the next. Never write two songs in one turn, because the styles bleed into each other.
3. Save each finished song as `songs/<song-slug>.md`, with a **Style** section and a **Lyrics** section that can be copied straight into Suno.

## Suno formatting rules

- **The Style box gets sound descriptions only.** Use genre, era, instruments, tempo, mood, vocal type and production words. Put the most important words first, because Suno gives more weight to earlier ones. Aim for 6–12 focused descriptors.
- **Don't put artist, singer, composer, film or song names in the Style box.** Suno blocks them or ignores them. Describe the sound instead: "bright smooth Indian male tenor" rather than a singer's name.
- **Keep the Style box under about 1,000 characters on v4.5/v5** (about 200 on older models). Shorter and sharper usually works better.
- **The Lyrics box gets the lyrics plus [bracket] metatags**: `[Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Break]`, `[Outro]`, `[Instrumental]`, `[Dhol Break]`, `[Male Vocal]`, `[Female Vocal]`, `[Duet]`, `[Group Chorus]`, `[Spoken]`.
- `(parentheses)` in the lyrics are sung as backing vocals or ad-libs, for example `(hoye!)`, `(balle balle)`, `(oh-ho)`.
- **Write Hindi and Punjabi in Roman script (Hinglish)** with phonetic spellings, so Suno pronounces them properly. Mix in English the way 2000s Bollywood songs do.
- Keep lines short and singable, with matching syllable counts in parallel lines.
- **Make every lyric original.** Don't copy lines or hooks from the reference songs. Match their shape, energy and devices, not their words.
- Mark duets clearly so Suno switches voices: `[Male Vocal]`, `[Female Vocal]`, `[Both]`.

## The story (source material for all songs)

This is a love story between **Zafar Abbas** and **Hana**. Lyrics can state details outright or hint at them, in the style of the reference songs.

- **An ocean apart:** Zafar lived in London and Hana in America.
- **The phone calls:** they talked for hours, all night, until dawn.
- **The proposal:** at first Hana said **no**, then **"I'll think about it"**, and then, after only two weeks, **"I will marry you"**. This happened before they had ever met in person.
- **The courtship:** they sent each other gifts and wrote each other poems and stories.
- **Hard times:** they faced difficulties and challenges, overcame them together, and came out stronger.
- **Flights:** she flew to him and he flew to her. They had golden days together, then long stretches apart again.
- **Meeting in person:** on the first day Zafar was too nervous to say "I love you". On the second day he said it, and she said it back.
- **The wedding:** Zafar flew over with his whole family and married Hana in her own home. It was a very blessed wedding.
- **Zafar:** a businessman, laid-back and funny.
- **Hana:** president of her sorority, very popular, a bit highly strung, confident and tough on the outside. Underneath she's a "cupcake with hundreds of thousands of sprinkles", which can become an Indian sweet (for example kaju katli with silver varq, a jalebi, or a gulab jamun).

## Reference songs

Both are from *Kabhi Khushi Kabhie Gham...* (K3G, 2001). The full analysis is in `research/k3g-reference-analysis.md`.

- **You Are My Soniya:** a flirty Hinglish pop duet.
- **Say Shava Shava:** a big ensemble Punjabi bhangra celebration.
