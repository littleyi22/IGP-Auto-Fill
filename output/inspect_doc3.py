"""
分析合併儲存格結構
"""
from docx import Document

doc = Document(r"h:\我的雲端硬碟\語文資優\114學年度\IGP\114學年度IGP-七年級國文.docx")

table = doc.tables[0]
print(f"Table: {len(table.rows)} rows x {len(table.columns)} cols\n")

# 分析一個資料行的唯一儲存格
for r_idx in [8, 10]:
    row = table.rows[r_idx]
    seen = set()
    unique_cells = []
    for c_idx, cell in enumerate(row.cells):
        tc_id = id(cell._tc)
        if tc_id not in seen:
            seen.add(tc_id)
            unique_cells.append((c_idx, cell))
    print(f"\nRow {r_idx} - unique cells ({len(unique_cells)} total):")
    for c_idx, cell in unique_cells:
        text = cell.text.strip()[:40].replace('\n', '|')
        print(f"  unique_col[{c_idx}]: {repr(text)}")
