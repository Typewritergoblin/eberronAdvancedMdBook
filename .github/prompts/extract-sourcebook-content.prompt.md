---
mode: agent
description: Parse sourcebook markdown files and extract species, classes/subclasses, feats, and spells into organized output files under sourcebooks/Extracted/
---

# Sourcebook Content Extraction Task

## STRICT BOUNDARIES — READ FIRST
- You may **only** read files under `sourcebooks/`
- You may **only** write files under `sourcebooks/Extracted/`
- Do **not** read, write, or modify anything in `src/`, `.github/`, or any other directory
- Do **not** run any terminal commands — **this means no PowerShell, no `run_in_terminal`, no shell commands of any kind**. Use only file tools: `grep_search` to find line numbers, `read_file` to read content, `create_file` / `replace_string_in_file` to write output. Terminal commands will hang and block progress.
- Do **not** ask the user for confirmation on individual entries — work fully autonomously to completion

Your job is to read through the sourcebook files listed below and extract content into clean, organized markdown files. Work through each source file, extract the relevant entries, and write them to the output files.

## Source Files to Parse

### PHB 2024 (D&D Beyond chunks)
- `sourcebooks/BeyondChunks/PHB24/character-origins-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` — Species
- `sourcebooks/BeyondChunks/PHB24/character-classes-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` — Classes
- `sourcebooks/BeyondChunks/PHB24/character-classes-(continued)-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` — Classes (continued)
- `sourcebooks/BeyondChunks/PHB24/feats-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` — Feats
- `sourcebooks/BeyondChunks/PHB24/spells-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` — Spell list/index
- `sourcebooks/BeyondChunks/PHB24/spell-descriptions-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md` — Spell descriptions
- `sourcebooks/BeyondChunks/PHB24/spell-descriptions-player-s-handbook-dungeons-dragons-sources-d-d-beyond (1).md` — Spell descriptions (continued)

### Forge of the Artificer 2024
- `sourcebooks/BeyondChunks/Forge of the Artificer24/chapter-1-the-artificer-eberron-forge-of-the-artificer-dungeons-dragons-sources-d-d-beyond.md` — Artificer class
- `sourcebooks/BeyondChunks/Forge of the Artificer24/chapter-2-character-options-eberron-forge-of-the-artificer-dungeons-dragons-sources-d-d-beyond.md` — Species, subclasses, feats

### Forgotten Realms: Heroes of Faerûn 2024
- `sourcebooks/BeyondChunks/ForgottenRealmsHeroesOfFaerun24/chapter-1-character-options-forgotten-realms-heroes-of-faer-n-dungeons-dragons-sources-d-d-beyond.md` — Species, subclasses, feats
- `sourcebooks/BeyondChunks/ForgottenRealmsHeroesOfFaerun24/chapter-5-magic-of-faer-n-forgotten-realms-heroes-of-faer-n-dungeons-dragons-sources-d-d-beyond.md` — Spells

### Exploring Eberron 2024
- `sourcebooks/Exploring_Eberron24.md` — Species, subclasses, feats, spells

### Frontiers of Eberron 2024
- `sourcebooks/Frontiers_Eberron_24.md` — Species, subclasses, feats, spells
- `sourcebooks/Frontiers24CharacterOptions.md` — Character options

---

## Output Files

Write all output to the following files under `sourcebooks/Extracted/`. Create the directory and files if they don't exist.

| Output File | Contents |
|:---|:---|
| `sourcebooks/Extracted/species.md` | All species from all sources |
| `sourcebooks/Extracted/classes/[classname].md` | One file per class (e.g. `cleric.md`, `wizard.md`) containing the full base class AND all subclasses from all sources |
| `sourcebooks/Extracted/feats.md` | All feats from all sources |
| `sourcebooks/Extracted/spells.md` | All spells from all sources |

Create one file per class under `sourcebooks/Extracted/classes/`. Use lowercase filenames with no spaces (e.g. `artificer.md`, `barbarian.md`, `cleric.md`). If a subclass is found in any source for a class that has no base class entry in the sourcebooks (e.g. an Eberron-only subclass for Fighter), still create the class file and append the subclass under the `# Subclasses` section.

---

## Formatting Rules

### General
- Strip all D&D Beyond navigation links, breadcrumbs, image tags, and "Posted by" attribution lines
- Strip broken image markdown like `[![](...)](...)`
- Keep all rules text, feature descriptions, and tables
- Use clean ATX headings (`#`, `##`, `###`)

### species.md
Each species entry:
```
## [Species Name]

[Description paragraph(s)]

**Source:** [Book name]

### Traits
- **Creature Type:** ...
- **Size:** ...
- **Speed:** ...
- **[Trait Name]:** [Description]
```
Group species alphabetically. Add a top-level `# Species` heading.

### classes/[classname].md
One file per class. Structure:
```
# [Class Name]

[Class description]

**Source:** [Book name]

## Class Table
[Markdown table of levels, proficiency bonus, features, spell slots etc.]

## Features
### [Feature Name]
[Feature description]

---

# Subclasses

## [Subclass Name]

[Subclass description]

**Source:** [Book name]

### [Subclass Feature Name]
[Feature description]
```
Append all subclasses from all sources into the same file under the `# Subclasses` heading, sorted alphabetically by subclass name.

### feats.md
```
# Feats

## [Category Name] Feats
_(e.g. Origin, General, Fighting Style, Epic Boon)_

### [Feat Name]
**Prerequisite:** [prerequisite or "None"]  
**Category:** [category]

[Feat description]

**Source:** [Book name]
```
Sort alphabetically within each category.

### spells.md
```
# Spells

### [Spell Name]
**Level:** [cantrip or 1–9]  
**School:** [school]  
**Casting Time:** [time]  
**Range:** [range]  
**Components:** [V/S/M and material if any]  
**Duration:** [duration]  
**Classes:** [class list]

[Spell description]

**Source:** [Book name]
```
Sort alphabetically.

---

## Handling Duplicates
- If a species, feat, or spell appears in multiple sources, keep one entry and append `**Also appears in:** [other sources]` at the end of the entry.
- If descriptions differ, use the more complete/detailed version.

## Task Steps
1. Read each source file in the order listed above
2. Identify and extract all entries of the relevant type(s)
3. Write species, feats, and spells to their respective output files
4. For each class found, write or append to `sourcebooks/Extracted/classes/[classname].md` — base class content first, then all subclasses from all sources appended under `# Subclasses`
5. After finishing all sources, do a deduplication pass on each output file
6. Write a file `sourcebooks/Extracted/extraction-log.md` listing every entry written, grouped by output file, with the source it came from
7. If a source file cannot be read or a section is ambiguous, log the issue in `sourcebooks/Extracted/extraction-log.md` under an `## Issues` heading and continue — do not stop
8. Report a final summary of counts: how many species, classes, subclasses, feats, and spells were written
