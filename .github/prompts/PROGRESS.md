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
| A7 | Clean Frontiers24CharacterOptions | ✅ | — | Complete. 971 lines. PDF export source. 6 subclasses, 5 backgrounds, 7 species, feats, spells. Script: tools/clean_frontiers_character_options.py |
| A8 | Clean Frontiers_Eberron_24 | ⬜ | — | Check if needs split |
| A9 | Clean FR chapter-1 (char options) | ✅ | — | Complete. 1422 lines. 8 subclasses, species lore, backgrounds, feats. Script: tools/clean_fr_chapter1_character_options.py |
| A10 | Clean Exploring_Eberron24 | ✅ | — | Complete. 925 lines. Chapter 6 only (character options). 5 subclasses, 3 backgrounds, 9 species, 12 species feats (7 Origin, 5 General), 4 spells. Script: tools/clean_exploring_eberron_chapter6.py |

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
| B9 | Clean PHB equipment | ✅ | — | Complete. 1357 lines. Sections: Coins, Weapons, Armor, Tools, Adventuring Gear, Mounts & Vehicles, Services, Magic Item rules, Crafting rules. Script: tools/clean_phb24_equipment.py |
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
| 2.1 | Extract species → species.md | ✅ | — | Complete. 999 lines. 10 PHB species, 5 Forge species, 7 Frontiers species (incl. Tiefling variant + Warforged variant), 9 Exploring Eberron species (incl. Aasimar variants). Also sourced A10. |
| 2.2 | Extract feats → feats.md | ✅ | — | Complete. 2868 lines. 26 Origin, 89 General, 11 Fighting Style, 26 Epic Boon, 13 Dragonmark feats (165 total). Script: tools/extract_feats.py |
| 2.3 | Extract Artificer class | ✅ | — | Complete. 1104 lines. Base class + 7 subclasses (Alchemist, Armorer, Artillerist, Battle Smith, Cartographer from Forge ch1; Forge Adept, Maverick from Exploring Eberron) + Variant Capstones (all 7) + Homunculus Servant spell. Script: tools/extract_artificer.py |
| 2.4 | Extract Barbarian class | ✅ | — | Complete. 368 lines. Base class + 4 PHB subclasses (Berserker, Wild Heart, World Tree, Zealot) + Path of the Demonshard (Frontiers). Script: tools/extract_barbarian.py |
| 2.5 | Extract Bard class | ✅ | — | Complete. 589 lines. Base class + 7 subclasses: Dance, Glamour, Lore, Valor (PHB); College of Wands (Frontiers); College of the Moon (FR); College of the Dirge Singer (Exploring Eberron). Script: tools/extract_bard.py |
| 2.6 | Extract Cleric class | ✅ | — | Complete. 642 lines. Base class + 7 subclasses: Life, Light, Trickery, War (PHB); Commerce Domain (Frontiers); Knowledge Domain (FR); Mind Domain (Exploring Eberron). Script: tools/extract_cleric.py |
| 2.7 | Extract Druid class | ✅ | — | Complete. 698 lines. Base class + 5 subclasses: Land, Moon, Sea, Stars (PHB); Circle of the Forged (Exploring Eberron). Script: tools/extract_druid.py |
| 2.8 | Extract Fighter class | ✅ | — | Complete. 496 lines. Base class + 5 subclasses: Battle Master, Champion, Eldritch Knight, Psi Warrior (PHB); Banneret (FR). Script: tools/extract_fighter.py |
| 2.9 | Extract Monk class | ✅ | — | Complete. 418 lines. Base class + 4 PHB subclasses (Warrior of Mercy, Warrior of Shadow, Warrior of the Elements, Warrior of the Open Hand) + Warrior of the Living Weapon (Exploring Eberron). Script: tools/extract_monk.py |
| 2.10 | Extract Paladin class | ✅ | — | Complete. 548 lines. Base class + 4 PHB subclasses (Oath of Devotion, Oath of Glory, Oath of the Ancients, Oath of Vengeance) + Oath of the Noble Genies (FR). Script: tools/extract_paladin.py |
| 2.11 | Extract Ranger class | ✅ | — | Complete. 671 lines. Base class + 4 PHB subclasses (Beast Master, Fey Wanderer, Gloom Stalker, Hunter) + Winter Walker (FR) + Bloodhound (Frontiers). Script: tools/extract_ranger.py |
| 2.12 | Extract Rogue class | ✅ | — | Complete. 441 lines. Base class + 4 PHB subclasses (Arcane Trickster, Assassin, Soulknife, Thief) + Scion of the Three (FR). Script: tools/extract_rogue.py |
| 2.13 | Extract Sorcerer class | ✅ | — | Complete. 743 lines. Base class + 4 PHB subclasses (Aberrant, Clockwork, Draconic, Wild Magic) + Spellfire Sorcery (FR) + Nemesis Sorcery (Frontiers). Script: tools/extract_sorcerer.py |
| 2.14 | Extract Warlock class | ✅ | — | Complete. 802 lines. Base class + 4 PHB subclasses (Archfey, Celestial, Fiend, Great Old One) + Stone Sovereign Patron (Frontiers). Script: tools/extract_warlock.py |
| 2.15 | Extract Wizard class | ✅ | — | Complete. 636 lines. Base class + 4 PHB subclasses (Abjurer, Diviner, Evoker, Illusionist) + Bladesinger (FR). Script: tools/extract_wizard.py |
| 2.H | Append homebrew subclasses → Year1CharacterOptions/classes/ | ✅ | — | Complete. Appended College of Whispers (bard), Tempest Domain (cleric), Phantom (rogue), Undead Patron (warlock). Source: Homebrew. Script: tools/append_homebrew_subclasses.py |
| 2.B | Extract backgrounds → Year1CharacterOptions/backgrounds.md | ✅ | — | Complete. 1156 lines. 59 backgrounds: 16 PHB, 17 Forge, 3 Exploring Eberron, 18 FR, 5 Frontiers. Frontiers PDF artifacts reconstructed (Scion/Wandslinger split text rejoined). Script: tools/extract_backgrounds.py |
| 2.R | Reorganize species.md + backgrounds.md alphabetically | ✅ | — | Complete. Removed source grouping headers, sorted all entries A–Z, added linked TOC at top of each file. Script: tools/reorganize_species_and_backgrounds.py |
| 2.E1 | Extract weapons → Year1CharacterOptions/weapons.md | ✅ | — | Complete. 158 lines. Intro + Weapons table (Simple Melee/Ranged, Martial Melee/Ranged) + Properties (9 entries) + Mastery Properties (8 entries). Script: tools/extract_equipment.py |
| 2.E2 | Extract armor → Year1CharacterOptions/armor.md | ✅ | — | Complete. 65 lines. Intro + Armor table (Light/Medium/Heavy/Shield) + Armor Training rules. Script: tools/extract_equipment.py |
| 2.E3 | Extract tools → Year1CharacterOptions/tools.md | ✅ | — | Complete. 221 lines. Tool Proficiency intro + Artisan's Tools (16 entries) + Other Tools (8 entries) with Ability/Utilize/Craft details. Script: tools/extract_equipment.py |
| 2.E4 | Extract adventuring gear → Year1CharacterOptions/equipment.md | ✅ | — | Complete. 772 lines. Intro + Adventuring Gear table + ~80 item descriptions + Mounts & Vehicles + Services + Magic Item rules + Crafting rules. Script: tools/extract_equipment.py |
| 2.S0 | Extract Eberron spells → eberron2024-spells-condensed.json + eberron2024-spells-full.json | ✅ | — | Complete. 11 spells from Forge of the Artificer, Frontiers of Eberron, and Exploring Eberron. Matches dnd2024-spells-*.json format (Foundry VTT dnd5e). Includes Gray Gaze, Orien Step, Force Blast, Concussive Burst, Aundair's Silent Sanctum, Magecraft, Mold Earth, Earth Tremor, Earthbind, Enemies Abound, Homunculus Servant. |
| 2.16 | Extract spells → spells.md | ⬜ | — | Depends on B1, B2, B4. Also include Homunculus Servant spell (already extracted in classes/artificer.md — copy into spells.md as addendum, Source: Forge 2024) |
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
| 2026-03-20 | 1A-7: Clean Frontiers24CharacterOptions | Output written to sourcebooks/Cleaned/Frontiers-character-options.md. 971 lines. 6 subclasses (Barbarian/Bard/Cleric/Ranger/Sorcerer/Warlock), 5 backgrounds (Dragonmarked Bravo/Foundling/Scion, Magewright, Wandslinger), 7 species (Gargoyle, Gnoll, Harpy, Medusa, Tiefling, Warforged, Worg), feats, new spells/cantrips. Script: tools/clean_frontiers_character_options.py |
| 2026-03-20 | 1A-9: Clean FR chapter-1 (char options) | Output written to sourcebooks/Cleaned/FR-chapter-1-character-options.md. 1422 lines. Species lore (all PHB2024 species in FR context), 8 subclasses (College of Moon Bard, Knowledge Domain Cleric, Banneret Fighter, Oath of Noble Genies Paladin, Winter Walker Ranger, Scion of the Three Rogue, Spellfire Sorcery Sorcerer, Bladesinger Wizard), backgrounds, feats. Fixed artist-credit stripping for DDB export format. Script: tools/clean_fr_chapter1_character_options.py |
| 2026-04-09 | 2.2: Extract feats → feats.md | Output written to sourcebooks/Extracted2/feats.md. 2868 lines. 165 feats total: 26 Origin, 89 General, 11 Fighting Style, 26 Epic Boon, 13 Dragonmark. Sources: PHB24, Forge ch2, FR ch1, Frontiers, Exploring Eberron. Handled Frontiers PDF artifacts (bold-italic sub-labels at ## level). Script: tools/extract_feats.py |
| 2026-04-11 | B9 task defined + 2.E1–2.E4 extraction tasks defined | Added B9 (Clean PHB equipment) and extraction tasks 2.E1 (weapons), 2.E2 (armor), 2.E3 (tools), 2.E4 (adventuring gear + services + crafting) to PROGRESS.md. Source: PHB24 equipment chapter (1491 lines). |
| 2026-04-10 | B9 + 2.E1–2.E4: Clean and extract equipment | B9 complete (1357 lines, tools/clean_phb24_equipment.py). All four extraction tasks complete: weapons.md (158 lines), armor.md (65 lines), tools.md (221 lines), equipment.md (772 lines). Script: tools/extract_equipment.py |
| 2026-04-20 | 2.S0: Extract Eberron spells to JSON | Created eberron2024-spells-condensed.json and eberron2024-spells-full.json in sourcebooks/Spells/. 11 spells from 3 Eberron sources. Full JSON matches Foundry VTT dnd5e system structure. Sources: Forge of the Artificer (Homunculus Servant), Frontiers of Eberron (Gray Gaze, Orien Step, Earthbind, Earth Tremor, Enemies Abound, Mold Earth), Exploring Eberron (Aundair's Silent Sanctum, Concussive Burst, Force Blast, Magecraft). |