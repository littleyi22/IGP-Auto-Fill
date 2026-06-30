"""
分析特需領域核心素養行的儲存格結構
"""
from docx import Document

doc = Document(r"h:\我的雲端硬碟\語文資優\114學年度\IGP\114學年度IGP-七年級國文.docx")
table = doc.tables[0]

# 分析 row 6 (特需領域核心素養)
row = table.rows[6]
seen = set()
unique_cells = []
for c_idx, cell in enumerate(row.cells):
    tc_id = id(cell._tc)
    if tc_id not in seen:
        seen.add(tc_id)
        unique_cells.append((c_idx, cell))

print(f"Row 6 unique cells ({len(unique_cells)} total):")
for c_idx, cell in unique_cells:
    text = cell.text.strip()[:60].replace('\n', '|')
    print(f"  unique_col[{c_idx}]: {repr(text)}")

# 也檢查 row 3 (教學時間) - 看看它的結構
print()
row = table.rows[3]
seen = set()
unique_cells = []
for c_idx, cell in enumerate(row.cells):
    tc_id = id(cell._tc)
    if tc_id not in seen:
        seen.add(tc_id)
        unique_cells.append((c_idx, cell))

print(f"Row 3 unique cells ({len(unique_cells)} total):")
for c_idx, cell in unique_cells:
    text = cell.text.strip()[:40].replace('\n', '|')
    print(f"  unique_col[{c_idx}]: {repr(text)}")
