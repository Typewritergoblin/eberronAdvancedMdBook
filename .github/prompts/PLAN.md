# Eberron Sourcebook Cleanup & Extraction — Master Plan

## Context / Why This File Exists
The source files in `sourcebooks/BeyondChunks/` are poorly formatted D&D Beyond HTML-to-MD exports.
This plan drives an iterative, prompt-by-prompt workflow to:
1. Clean them (Phase 1) → save to `sourcebooks/Cleaned/`
2. Extract content by type (Phase 2) → save to `sourcebooks/Extracted2/`

Track per-prompt progress in `PROGRESS.md` (same folder).

---

## ⚠️ CRITICAL REQUIREMENT — VERBATIM CONTENT PRESERVATION

**This is the single most important rule in this entire plan.**

All rules text, feature descriptions, flavor text, table data, dice expressions, ranges, durations, damage types, conditions, and any other game content **MUST be copied exactly word-for-word from the source file.**

- **DO NOT paraphrase** — not even slightly.
- **DO NOT summarize** — even if the text seems repetitive.
- **DO NOT truncate** — even if a description is very long.
- **DO NOT omit** — even if two features seem similar.
- **DO NOT reword for clarity** — preserve the original author's exact phrasing.

If you are in the middle of processing a file and approaching context limits, **STOP and write what you have so far**, then note in `PROGRESS.md` where you stopped (last heading/entry processed). A follow-up prompt will continue from that point. **It is always better to stop early than to truncate or compress content.**

The only things that change between source and output are:
1. Removal of D&D Beyond navigation/boilerplate/broken images (Phase 1 only)
2. Markdown formatting fixes — heading levels, list syntax (Phase 1 only)
3. Addition of `**Source:**` attribution at the end of each entry (Phase 2 only)

Everything else is preserved exactly as written.

---

## Decisions

| Decision | Choice |
|---|---|
| Original files | Preserved untouched in `BeyondChunks/` |
| Cleaned output | `sourcebooks/Cleaned/` |
| Extracted output | `sourcebooks/Extracted2/` (fresh, not appending old `Extracted/`) |
| Monster Manual | **Excluded** — 31 files skipped |
| Class scope | All 12 PHB 2024 core classes + Artificer + all Eberron/FR subclasses |
| Prompt granularity | Content-appropriate (species = 1–2 prompts; large classes = 1+ each) |
| Workflow structure | **4 phases:** Character Creation (MVP) → Spells → Combat/Equipment → Deferred |

---

## Agent Tool Usage

When inspecting or reading files, always prefer internal file tools over terminal commands:
- **`read_file`** — reading file contents
- **`grep_search`** — checking patterns or counts within files
- **`file_search`** — finding files by name pattern

Only use the terminal (`run_in_terminal`) when actually executing scripts (e.g., running a Python cleaner).

---

## Phase 1: Character Creation (MVP — Do First)

### Cleaning Rules (Apply to All Phases)

- **Strip:** top nav headers, duplicate headings, `Posted by [user]` lines, broken image markdown (`[![](https://media.dndbeyond.com/...)](url)`), all D&D Beyond hyperlinks (convert `[text](dndbeyond-url)` → plain `text`), chapter nav footers
- **VERBATIM COPY:** Every single word of rules text, feature descriptions, flavor text, tables, and stat block data must be reproduced exactly as it appears in the source. Only the D&D Beyond navigation wrapper is removed — nothing inside the actual content is changed, shortened, or reworded.
- **Output format:** clean ATX headings (`##`, `###`), proper list formatting, no trailing whitespace
- **If context limits loom:** Stop, write the output file with what you have, record the last heading processed in `PROGRESS.md`, and wait for a follow-up prompt.

### Extraction Rules (Apply to All Phases)

- **VERBATIM COPY:** Feature descriptions, trait text, and rules content must be copied exactly from the cleaned source file — word for word, sentence for sentence. Do not paraphrase, condense, or rewrite any game content.
- Every entry must end with `**Source:** [Book Name Year]`
- Organize alphabetically within each category
- **No invention** — if content for an entry isn't present in the source file, write nothing; do not fill gaps from memory or general knowledge
- No D&D Beyond links in output
- **If context limits loom:** Stop, write the partial output file, record the last entry processed in `PROGRESS.md`, and wait for a follow-up prompt.

### Phase 1A — Clean (Character Creation Sources)

| # | Source File (in BeyondChunks/) | Output (in Cleaned/) |
|---|---|---|
| 1A-1 | `PHB24/character-origins-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` | `PHB24-character-origins.md` |
| 1A-2 | `PHB24/character-classes-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` | `PHB24-character-classes.md` |
| 1A-3 | `PHB24/character-classes-(continued)-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` | `PHB24-character-classes-continued.md` |
| 1A-4 | `PHB24/feats-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` | `PHB24-feats.md` |
| 1A-5 | `Forge of the Artificer24/chapter-1-the-artificer-eberron-forge-of-the-artificer-dungeons-dragons-sources-d-d-beyond.md` | `Forge-chapter-1-artificer.md` |
| 1A-6 | `Forge of the Artificer24/chapter-2-character-options-eberron-forge-of-the-artificer-dungeons-dragons-sources-d-d-beyond.md` | `Forge-chapter-2-character-options.md` |
| 1A-7 | `Frontiers24CharacterOptions.md` (root sourcebooks/) | `Frontiers-character-options.md` |
| 1A-8 | `Frontiers_Eberron_24.md` (root sourcebooks/) | `Frontiers-eberron.md` *(may need 2 prompts — check file size)* |
| 1A-9 | `ForgottenRealmsHeroesOfFaerun24/chapter-1-character-options-forgotten-realms-heroes-of-faer-n-dungeons-dragons-sources-d-d-beyond.md` | `FR-chapter-1-character-options.md` |
| 1A-10 | `Exploring_Eberron24.md` (root sourcebooks/) | `Exploring-eberron.md` *(may need 2 prompts — check file size)* |

### Phase 1B — Extract (Character Creation Output)

All extraction reads from `sourcebooks/Cleaned/`. All output goes to `sourcebooks/Extracted2/`.

#### 1B-1 — Species (1–2 prompts)
- **Read:** `PHB24-character-origins.md`, `Forge-chapter-2-character-options.md`, `FR-chapter-1-character-options.md`, `Frontiers-character-options.md`
- **Write:** `Extracted2/species.md`
- Format: alphabetical, grouped by source, each entry has Creature Type / Size / Speed / Traits / Source

#### 1B-2 — Feats (1–2 prompts)
- **Read:** `PHB24-feats.md`, `Forge-chapter-2-character-options.md`, `FR-chapter-1-character-options.md`, `Frontiers-character-options.md`, `Frontiers-eberron.md`
- **Write:** `Extracted2/feats.md`
- Format: organized by category (Origin Feats, General Feats, Fighting Style Feats, Epic Boon Feats, Dragonmark Feats), alphabetical within each

#### 1B-3 — Classes (1+ prompts per class)
One file per class. Each file includes: base class features + progression table + ALL subclasses from any source.

| Class | Primary Source | Subclass Sources |
|---|---|---|
| Artificer | `Forge-chapter-1-artificer.md` | `Forge-chapter-2-character-options.md` |
| Barbarian | `PHB24-character-classes.md` | Eberron/FR sources as applicable |
| Bard | `PHB24-character-classes.md` | Eberron/FR sources |
| Cleric | `PHB24-character-classes.md` | Eberron/FR sources |
| Druid | `PHB24-character-classes.md` | Eberron/FR sources |
| Fighter | `PHB24-character-classes.md` | Eberron/FR sources |
| Monk | `PHB24-character-classes.md` | Eberron/FR sources |
| Paladin | `PHB24-character-classes-continued.md` | Eberron/FR sources |
| Ranger | `PHB24-character-classes-continued.md` | Eberron/FR sources |
| Rogue | `PHB24-character-classes-continued.md` | Eberron/FR sources |
| Sorcerer | `PHB24-character-classes-continued.md` | Eberron/FR sources |
| Warlock | `PHB24-character-classes-continued.md` | Eberron/FR sources |
| Wizard | `PHB24-character-classes-continued.md` | Eberron/FR sources |

- **Write:** `Extracted2/classes/[classname].md` (e.g., `fighter.md`, `artificer.md`)
- *(Fighter, Paladin, Wizard are most content-dense — may need 2 prompts each)*

---

## Phase 2: Spells

### Phase 2A — Clean (Spell Sources)

| # | Source File (in BeyondChunks/) | Output (in Cleaned/) |
|---|---|---|
| 2A-1 | `PHB24/spells-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` | `PHB24-spells-rules.md` |
| 2A-2 | `PHB24/spell-descriptions-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` | `PHB24-spell-descriptions-1.md` |
| 2A-3 | `PHB24/spell-descriptions-player-s-handbook-dungeons-dragons-sources-d-d-beyond (1).md` | `PHB24-spell-descriptions-2.md` |
| 2A-4 | `ForgottenRealmsHeroesOfFaerun24/chapter-5-magic-of-faer-n-forgotten-realms-heroes-of-faer-n-dungeons-dragons-sources-d-d-beyond.md` | `FR-chapter-5-magic.md` |

> **Note:** Spell description files are very large — each will likely need 2+ cleaning prompts. Record stopping points carefully in `PROGRESS.md`.

### Phase 2B — Extract (Spells Output)

#### 2B-1 — Spells (new/non-PHB spells only, 1–2 prompts)
- **Read:** `FR-chapter-5-magic.md`, `Forge-chapter-2-character-options.md` (already cleaned in Phase 1), `PHB24-spell-descriptions-1.md`, `PHB24-spell-descriptions-2.md` (cross-reference only — do not re-extract PHB spells)
- **Write:** `Extracted2/spells.md`
- Format: alphabetical, full spell text verbatim, source attribution on every entry

---

## Phase 3: Combat Rules & Equipment

### Phase 3A — Clean (Rules Sources)

| # | Source File (in BeyondChunks/) | Output (in Cleaned/) |
|---|---|---|
| 3A-1 | `PHB24/playing-the-game-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` | `PHB24-playing-the-game.md` |
| 3A-2 | `PHB24/equipment-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` | `PHB24-equipment.md` |
| 3A-3 | `PHB24/creating-a-character-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` | `PHB24-creating-a-character.md` |
| 3A-4 | `PHB24/rules-glossary-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` | `PHB24-rules-glossary.md` |
| 3A-5 | `PHB24/creature-stat-blocks-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` | `PHB24-creature-stat-blocks.md` |

### Phase 3B — Extract
No extraction targets defined yet — these are reference/rules files. Revisit after Phase 3A is complete to determine if any structured extraction is needed.

---

## Phase 4: Deferred

Do not start Phase 4 until Phases 1–3 are complete. Revisit to split into sub-phases as needed.

| File | Content | Notes |
|---|---|---|
| `Forge of the Artificer24/appendix-magic-items-eberron-forge-of-the-artificer-dungeons-dragons-sources-d-d-beyond.md` | Eberron magic items | |
| `ForgottenRealmsHeroesOfFaerun24/chapter-8-magic-items-forgotten-realms-adventures-in-faer-n-dungeons-dragons-sources-d-d-beyond.md` | FR magic items | |
| `ForgottenRealmsHeroesOfFaerun24/chapter-4-aurora-s-whole-realms-catalog-forgotten-realms-heroes-of-faer-n-dungeons-dragons-sources-d-d-beyond.md` | Aurora's catalog (equipment/items) | |
| `Forge of the Artificer24/introduction-forge-of-the-artificer-eberron-forge-of-the-artificer-dungeons-dragons-sources-d-d-beyond.md` | Forge introduction | |
| `Forge of the Artificer24/chapter-3-bastions-in-khorvaire-eberron-forge-of-the-artificer-dungeons-dragons-sources-d-d-beyond (1).md` | Bastions rules | |
| `Forge of the Artificer24/chapter-7-elemental-airships-eberron-forge-of-the-artificer-dungeons-dragons-sources-d-d-beyond.md` | Elemental airships | |
| `Forge_Artificer_24.md` | Possible compiled duplicate | Evaluate against individual chapter files before processing |
| Monster Manual (31 files) | Monster stat blocks | Currently excluded — revisit if needed |

---

## Verification Checklist (Run After Each Prompt)
- [ ] Output file exists and is non-empty
- [ ] No `dndbeyond.com` URLs in output
- [ ] Every extracted entry has `**Source:**` attribution
- [ ] Content volume is proportional to the source (no obvious missing sections)
- [ ] Spot-check 2–3 known features/entries verbatim against the cleaned source