import win32com.client
import os
import sys

word = win32com.client.Dispatch("Word.Application")
word.Visible = False

base = r"h:\我的雲端硬碟\語文資優\114學年度\IGP"
files = [
    ("114一上國文(三次段考)課程總表.doc", "output/schedule_s1.txt"),
    ("114一下國文(三次段考)課程總表.doc", "output/schedule_s2.txt"),
]

for src, out in files:
    full_path = os.path.join(base, src)
    doc = word.Documents.Open(full_path, False, True)
    text = doc.Content.Text
    doc.Close(False)
    out_path = os.path.join(base, out.replace("/", "\\"))
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Done: {out}")

word.Quit()
print("All done.")
