"""
詳細檢查 IGP docx 表格結構
"""
from docx import Document

doc = Document(r"h:\我的雲端硬碟\語文資優\114學年度\IGP\114學年度IGP-七年級國文.docx")

table = doc.tables[0]
print(f"Table: {len(table.rows)} rows x {len(table.columns)} cols\n")

# 檢查特定行的所有欄位
for r_idx in [6, 7, 8, 9, 10]:
    row = table.rows[r_idx]
    print(f"\n--- Row {r_idx} ---")
    for c_idx, cell in enumerate(row.cells):
        text = cell.text.strip()[:50].replace('\n', '|')
        print(f"  col[{c_idx}]: {repr(text)}")
