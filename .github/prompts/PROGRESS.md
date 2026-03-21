# Extraction Progress Tracker

Reference `PLAN.md` for full details on each step.
Update this file after each prompt session. Mark steps: ⬜ Not started | 🔄 In progress | ✅ Done | ⚠️ Needs review

When resuming in a new chat session: read PLAN.md first, then this file. Note the "Last stopped at" field for any in-progress steps so you know exactly where to resume.

---

## Phase 1: Cleaning

### Group A — Character-Creation Critical

| # | Task | Status | Last stopped at | Notes |
|---|---|---|---|---|
| A1 | Clean PHB character-origins | ✅ | — | Complete |
| A2 | Clean PHB character-classes | ✅ | — | Complete |
| A3 | Clean PHB character-classes-continued | ✅ | — | Complete. Fixed td/td table bug in script; all 7 classes (Paladin–Wizard) cleaned verbatim. |
| A4 | Clean PHB feats | ✅ | — | Complete. 1091 lines. No HTML tables. Script: tools/clean_phb24_feats.py |
| A5 | Clean Forge chapter-1 (Artificer) | ✅ | — | Complete. 884 lines. HTML Core Traits table converted. Script: tools/clean_forge_chapter1_artificer.py |
| A6 | Clean Forge chapter-2 (char options) | ✅ | — | Complete. 1038 lines. 17 backgrounds, 5 species, 14 Dragonmark feats, 14 General feats, 1 Epic Boon. Script: tools/clean_forge_chapter2_character_options.py |
| A7 | Clean Frontiers24CharacterOptions | ⬜ | — | |
| A8 | Clean Frontiers_Eberron_24 | ⬜ | — | Check if needs split |
| A9 | Clean FR chapter-1 (char options) | ⬜ | — | |
| A10 | Clean Exploring_Eberron24 | ⬜ | — | Check if needs split |

### Group B — Supplemental

| # | Task | Status | Last stopped at | Notes |
|---|---|---|---|---|
| B1 | Clean PHB spell-descriptions pt 1 | ⬜ | — | |
| B2 | Clean PHB spell-descriptions pt 2 `(1)` | ⬜ | — | |
| B3 | Clean PHB spells rules chapter | ⬜ | — | Full Chapter 7 spellcasting rules (slots, components, etc.) — not individual spell descriptions |
| B4 | Clean PHB creature-stat-blocks | ⬜ | — | |
| B5 | Clean Forge appendix magic-items | ⬜ | — | |
| B6 | Clean FR chapter-5 magic | ⬜ | — | |
| B7 | Clean FR chapter-8 magic-items | ⬜ | — | |
| B8 | Clean FR chapter-4 Aurora catalog | ⬜ | — | |
| B9 | Clean PHB equipment | ⬜ | — | |
| B10 | Clean PHB creating-a-character | ⬜ | — | |
| B11 | Clean PHB playing-the-game | ⬜ | — | |
| B12 | Clean PHB rules-glossary | ⬜ | — | |
| B13 | Clean Forge introduction | ⬜ | — | |
| B14 | Clean Forge chapter-3 bastions `(1)` | ⬜ | — | |
| B15 | Clean Forge chapter-7 airships | ⬜ | — | |
| — | Forge_Artificer_24.md | ⬜ | — | Evaluate for redundancy first |

---

## Phase 2: Extraction

| # | Task | Status | Last stopped at | Notes |
|---|---|---|---|---|
| 2.1 | Extract species → species.md | ⬜ | — | Depends on A1, A6, A7, A9 |
| 2.2 | Extract feats → feats.md | ⬜ | — | Depends on A4, A6, A7, A9 |
| 2.3 | Extract Artificer class | ⬜ | — | Depends on A5, A6 |
| 2.4 | Extract Barbarian class | ⬜ | — | Depends on A2 |
| 2.5 | Extract Bard class | ⬜ | — | Depends on A2 |
| 2.6 | Extract Cleric class | ⬜ | — | Depends on A2 |
| 2.7 | Extract Druid class | ⬜ | — | Depends on A2 |
| 2.8 | Extract Fighter class | ⬜ | — | Depends on A2; may need 2 prompts |
| 2.9 | Extract Monk class | ⬜ | — | Depends on A2 |
| 2.10 | Extract Paladin class | ⬜ | — | Depends on A3; may need 2 prompts |
| 2.11 | Extract Ranger class | ⬜ | — | Depends on A3 |
| 2.12 | Extract Rogue class | ⬜ | — | Depends on A3 |
| 2.13 | Extract Sorcerer class | ⬜ | — | Depends on A3 |
| 2.14 | Extract Warlock class | ⬜ | — | Depends on A3 |
| 2.15 | Extract Wizard class | ⬜ | — | Depends on A3; may need 2 prompts |
| 2.16 | Extract spells → spells.md | ⬜ | — | Depends on B1, B2, B4 |
| 2.17 | Extract magic items → magic-items.md | ⬜ | — | Depends on B3, B5, A8 |

---

## Session Log

| Date | Session Goal | Outcome |
|---|---|---|
| 2026-03-18 | Planning — designed full workflow | Plan restructured into 4 phases: Character Creation (MVP), Spells, Combat/Equipment, Deferred |
| 2026-03-18 | 1A-1: Clean PHB character-origins | Output written to sourcebooks/Cleaned/PHB24-character-origins.md. All 16 backgrounds and 10 species cleaned verbatim. Nav/images/links stripped. |
| (resumed) | 1A-2: Clean PHB character-classes | Output written to sourcebooks/Cleaned/PHB24-character-classes.md. All 6 classes (Barbarian–Monk), spell lists, subclasses cleaned. HTML Core Traits tables converted to markdown. Images/captions/links stripped. tools/clean_phb24_classes.py created. |
| 2026-03-18 | 1A-4: Clean PHB feats | Output written to sourcebooks/Cleaned/PHB24-feats.md. All feat categories (Origin, General, Fighting Style, Epic Boon) cleaned verbatim. Feat list table preserved. Script: tools/clean_phb24_feats.py |
| 2026-03-18 | 1A-5: Clean Forge chapter-1 (Artificer) | Output written to sourcebooks/Cleaned/Forge-chapter-1-artificer.md. Core Artificer Traits table converted, all class features and 4 subclasses cleaned verbatim. Homunculus Servant stat block and spell included. Script: tools/clean_forge_chapter1_artificer.py |
| 2026-03-18 | 1A-6: Clean Forge chapter-2 (char options) | Output written to sourcebooks/Cleaned/Forge-chapter-2-character-options.md. 17 backgrounds, 5 species, 14 Dragonmark feats (with spell tables), 13 Greater mark feats, Potent Dragonmark, Boon of Siberys. Script: tools/clean_forge_chapter2_character_options.py |