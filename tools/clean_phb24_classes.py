"""
Clean PHB24 character-classes source file → Cleaned/PHB24-character-classes.md

Applies these transformations:
- Strip nav boilerplate (first ~14 lines before first # heading)
- Convert HTML Core Traits <table> blocks → markdown tables
- Remove artist-credit+image lines (ARTIST NAME [![](url)](url))
- Remove image caption lines that follow artist lines
- Remove standalone image lines
- Convert [text](url) → text
- Convert * * * → ---
- Remove *Source: https://...* footer
- Collapse 3+ blank lines → 2 blank lines
"""

import re
import html as html_lib
import sys
import os


def html_to_text(html_str):
    """Strip HTML tags and decode entities to plain text."""
    # Recursively strip tags
    text = re.sub(r'<[^>]+>', ' ', html_str)
    text = html_lib.unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def convert_html_core_traits_tables(content):
    """Find <table>...</table> blocks and replace with markdown tables."""

    def replace_table(match):
        table_html = match.group(0)

        # Extract the heading text from <caption><h3>...<a ...></a>HEADING TEXT</h3></caption>
        # The anchor tag is always empty (aria-hidden), the real text follows it
        heading_match = re.search(
            r'<caption>.*?<h3[^>]*>.*?<a[^>]*></a>(.*?)</h3>.*?</caption>',
            table_html, re.DOTALL
        )
        heading = ''
        if heading_match:
            h3_text = html_to_text(heading_match.group(1))
            heading = f'### {h3_text}\n\n'

        # Extract <tr> rows from <tbody>
        rows = re.findall(r'<tr>(.*?)</tr>', table_html, re.DOTALL)
        table_lines = []
        for row in rows:
            # Each row may use <th>/<td> or <td>/<td> for its two columns
            cells = re.findall(r'<(?:th|td)[^>]*>(.*?)</(?:th|td)>', row, re.DOTALL)
            if len(cells) >= 2:
                col1 = html_to_text(cells[0])
                col2 = html_to_text(cells[1])
                table_lines.append(f'| {col1} | {col2} |')

        if table_lines:
            header = '| | |'
            separator = '| --- | --- |'
            return heading + header + '\n' + separator + '\n' + '\n'.join(table_lines)
        return ''

    return re.sub(r'<table[^>]*>.*?</table>', replace_table, content, flags=re.DOTALL)


def clean_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- Step 1: Convert HTML tables before splitting into lines ---
    content = convert_html_core_traits_tables(content)

    lines = content.split('\n')

    # --- Step 2: Find the real chapter heading (skip nav boilerplate) ---
    start_idx = 0
    for i, line in enumerate(lines):
        if line.startswith('# Chapter 3:'):
            start_idx = i
            break
    lines = lines[start_idx:]

    # --- Step 3: Line-by-line cleaning ---
    cleaned = []
    # caption_state: 'off' | 'looking' (saw image, seeking caption) | 'in' (inside caption block)
    caption_state = 'off'

    for line in lines:
        stripped = line.strip()

        # Any line containing a D&D Beyond media image URL → artist+image line
        # Covers: "ARTIST [![](url)](url)", "ARTIST ![](url)", "[![](url)](url)"
        if 'media.dndbeyond.com' in stripped:
            caption_state = 'looking'
            continue  # drop this line

        if caption_state == 'looking':
            if stripped == '':
                continue  # skip blank lines between image and caption start
            # Distinguish captions (short plain text) from real content
            is_content = (stripped.startswith('#') or
                          stripped.startswith('|') or
                          stripped.startswith('-') or
                          stripped.startswith('>') or
                          stripped.startswith('*') or
                          len(stripped) > 80)
            if is_content:
                # Real content follows the image with no caption — keep it
                caption_state = 'off'
                # fall through to normal processing below
            else:
                # Short plain text → image caption, drop it
                caption_state = 'in'
                continue

        if caption_state == 'in':
            if stripped == '':
                # Blank line ends the caption block - include blank for spacing
                caption_state = 'off'
                cleaned.append('')
            else:
                continue  # drop additional caption lines (multi-line captions)
            continue

        # Source URL footer
        if re.match(r'^\*Source: https://', stripped):
            continue

        # * * * → ---
        if stripped == '* * *':
            cleaned.append('---')
            continue

        # [text](url) → text  and  [](url) → ''  (must not match images: ![)
        # Pattern: [not-!][text?](url)
        line = re.sub(r'(?<!!)\[([^\]]*)\]\([^)]+\)', r'\1', line)

        cleaned.append(line)

    result = '\n'.join(cleaned)

    # --- Step 4: Collapse excessive blank lines ---
    result = re.sub(r'\n{3,}', '\n\n', result)
    result = result.strip() + '\n'

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)

    line_count = result.count('\n')
    print(f"Done. {line_count} lines written to:\n  {output_path}")


if __name__ == '__main__':
    BASE = r'g:\GitRepos\eberronAdvancedMdBook'
    # A2 — character-classes
    # input_path = os.path.join(
    #     BASE,
    #     r'sourcebooks\BeyondChunks\PHB24',
    #     'character-classes-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md'
    # )
    # output_path = os.path.join(BASE, r'sourcebooks\Cleaned', 'PHB24-character-classes.md')

    # A3 — character-classes (continued)
    input_path = os.path.join(
        BASE,
        r'sourcebooks\BeyondChunks\PHB24',
        'character-classes-(continued)-player-s-handbook-dungeons-dragons-sources-d-d-beyond.md'
    )
    output_path = os.path.join(BASE, r'sourcebooks\Cleaned', 'PHB24-character-classes-continued.md')
    clean_file(input_path, output_path)
