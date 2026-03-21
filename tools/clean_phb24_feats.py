"""
Clean PHB24 feats source file → Cleaned/PHB24-feats.md  (Task 1A-4)

Applies these transformations:
- Strip nav boilerplate (lines before first # Chapter heading)
- Remove artist-credit+image lines (ARTIST NAME [![](url)](url))
- Remove image caption lines that follow artist lines
- Remove standalone image lines
- Convert [text](url) → text
- Convert * * * → ---
- Remove *Source: https://...* footer
- Collapse 3+ blank lines → 2 blank lines

Note: No HTML <table> blocks in this source file.
"""

import re
import html as html_lib
import os


def html_to_text(html_str):
    """Strip HTML tags and decode entities to plain text."""
    text = re.sub(r'<[^>]+>', ' ', html_str)
    text = html_lib.unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def clean_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    # --- Step 1: Find the real chapter heading (skip nav boilerplate) ---
    start_idx = 0
    for i, line in enumerate(lines):
        if line.startswith('# Chapter'):
            start_idx = i
            break
    lines = lines[start_idx:]

    # --- Step 2: Line-by-line cleaning ---
    cleaned = []
    caption_state = 'off'  # 'off' | 'looking' | 'in'

    for line in lines:
        stripped = line.strip()

        # Any line containing a D&D Beyond media image URL → drop it
        if 'media.dndbeyond.com' in stripped:
            caption_state = 'looking'
            continue

        if caption_state == 'looking':
            if stripped == '':
                continue  # skip blank lines between image and caption
            is_content = (stripped.startswith('#') or
                          stripped.startswith('|') or
                          stripped.startswith('-') or
                          stripped.startswith('>') or
                          stripped.startswith('*') or
                          len(stripped) > 80)
            if is_content:
                caption_state = 'off'
                # fall through to normal processing
            else:
                caption_state = 'in'
                continue

        if caption_state == 'in':
            if stripped == '':
                caption_state = 'off'
                cleaned.append('')
            else:
                continue
            continue

        # Source URL footer
        if re.match(r'^\*Source: https://', stripped):
            continue

        # * * * → ---
        if stripped == '* * *':
            cleaned.append('---')
            continue

        # [text](url) → text  (skip images: ![)
        line = re.sub(r'(?<!!)\[([^\]]*)\]\([^)]+\)', r'\1', line)

        cleaned.append(line)

    result = '\n'.join(cleaned)

    # --- Step 3: Collapse excessive blank lines ---
    result = re.sub(r'\n{3,}', '\n\n', result)
    result = result.strip() + '\n'

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)

    line_count = result.count('\n')
    print(f"Done. {line_count} lines written to:\n  {output_path}")


if __name__ == '__main__':
    BASE = r'g:\GitRepos\eberronAdvancedMdBook'
    input_path = os.path.join(
        BASE,
        r'sourcebooks\BeyondChunks\PHB24',
        'feats-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md'
    )
    output_path = os.path.join(BASE, r'sourcebooks\Cleaned', 'PHB24-feats.md')
    clean_file(input_path, output_path)
