import sys
import io
from markitdown import MarkItDown

file_path = sys.argv[1]
md = MarkItDown()
result = md.convert(file_path)

# 輸出到檔案，避免終端機編碼問題
out_path = sys.argv[2] if len(sys.argv) > 2 else "output/temp_output.txt"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(result.text_content)
print(f"已輸出至 {out_path}")
