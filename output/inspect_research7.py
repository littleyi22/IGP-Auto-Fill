# -*- coding: utf-8 -*-
"""
讀取並顯示 114學年度個別IGP七年級專題研究.docx 的表格結構
"""
import sys
from docx import Document

DOC_PATH = r"I:\我的雲端硬碟\語文資優\114學年度\IGP\114學年度個別IGP七年級專題研究.docx"
OUT_PATH = r"I:\我的雲端硬碟\語文資優\114學年度\IGP\output\research7_content.txt"

doc = Document(DOC_PATH)

lines = []
for t_idx, table in enumerate(doc.tables):
    lines.append(f"=== 表格 {t_idx} (共 {len(table.rows)} 行, {len(table.columns)} 列) ===")
    for r_idx, row in enumerate(table.rows):
        cells = row.cells
        unique_cells = []
        seen = set()
        for c in cells:
            if id(c) not in seen:
                seen.add(id(c))
                unique_cells.append(c)
        cell_texts = [c.text.strip()[:60] for c in unique_cells]
        lines.append(f"  row[{r_idx:02d}] ({len(unique_cells)} unique cells): {cell_texts}")

output = "\n".join(lines)
with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(output)

print("Done. Written to", OUT_PATH)
print(output[:3000])
