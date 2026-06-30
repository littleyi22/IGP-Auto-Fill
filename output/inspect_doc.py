"""
用於檢查 IGP docx 表格結構的腳本
"""
import sys
from docx import Document

doc = Document(r"h:\我的雲端硬碟\語文資優\114學年度\IGP\114學年度IGP-七年級國文.docx")

for t_idx, table in enumerate(doc.tables):
    print(f"\n=== Table {t_idx} === ({len(table.rows)} rows x {len(table.columns)} cols)")
    for r_idx, row in enumerate(table.rows):
        cells_text = []
        for c_idx, cell in enumerate(row.cells):
            text = cell.text.strip()[:30].replace('\n', '|')
            cells_text.append(f"[{c_idx}]{text}")
        print(f"  Row {r_idx}: {' | '.join(cells_text[:8])}")  # print first 8 cells
        if r_idx > 25:
            print(f"  ... ({len(table.rows) - 26} more rows)")
            break
