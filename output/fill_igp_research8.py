"""
填寫 114學年度個別IGP八年級專題研究.docx 的空白欄位
僅填寫特需領域核心素養（row 6）以及評量紀錄（每週6個分數及評量日期）。
"""
import random
from docx import Document

DOC_PATH = r"h:\我的雲端硬碟\語文資優\114學年度\IGP\114學年度個別IGP八年級專題研究.docx"
OUT_PATH = r"h:\我的雲端硬碟\語文資優\114學年度\IGP\114學年度個別IGP八年級專題研究（已填寫）.docx"

doc = Document(DOC_PATH)
table = doc.tables[0]

def set_cell(cell, text):
    cell.text = str(text)

# 1. 填寫核心素養
core_competencies = """【獨立研究】
1. 特獨-J-A1：透過獨立研究，評估自我興趣傾向與優勢能力，擬定適切生涯發展方向與目標。
2. 特獨-J-A2：提出適切的探究問題，依據習得的知識，透過獨立思考與分析，提出可能的問題解決模式，並實際驗證及解析。
3. 特獨-J-A3：能有效整合資源，規劃、執行研究計畫，具備創新求變的精神，從歷程中反思、發展適切的研究態度。
4. 特獨-J-B1：能分析歸納、製作圖表，整理蒐集之資訊或數據，並彈性選用適切的發表形式，展現具說服力的獨立研究成果。
5. 特獨-J-B2：能善用科技、資訊與媒體，分辨資料蒐集可信程度，以獲得獨立研究資訊。
6. 特獨-J-B3：具備運用藝術感知、創作與鑑賞能力於獨立研究過程、產出及報告中。
7. 特獨-J-C1：透過獨立研究，養成研究倫理、道德思辨與實踐能力，並主動關注公領域的社會議題。
【創造力】
8. 特創-J-A2：具備批判思考能力與習慣，區辨關鍵性問題，構思反省各種困難與解決策略，有效重組與提出最可能的問題解決模式。
9. 特創-J-A3：具備規劃及執行創意產品的能力，從不同角度與新穎獨特方式解決問題，發揮主動學習與創新求變的素養。
【情意發展】
10. 特情-J-A3：具備主動與執行規劃學習的能力，發展對努力與成就關聯的合宜觀點，透過多元管道試探生涯發展的機會與目標。"""

set_cell(table.rows[6].cells[2], core_competencies)
print("✅ 特需領域核心素養已填入")

# 2. 填寫評量紀錄
for i in range(10, len(table.rows)):
    row = table.rows[i]
    cells = row.cells
    
    date_text = cells[4].text.strip()
    
    # 若 cells[4] 為日期，表示該列為一週的課程
    if date_text and date_text[0].isdigit():
        scores = [random.choices([5, 4, 3], weights=[80, 15, 5])[0] for _ in range(6)]
        
        set_cell(cells[8], scores[0])
        set_cell(cells[9], scores[1])  
        set_cell(cells[11], scores[2]) 
        set_cell(cells[12], scores[3]) 
        set_cell(cells[13], scores[4]) 
        set_cell(cells[14], scores[5]) 
        
        set_cell(cells[15], date_text)
        print(f"  ✅ 填入資料：日期 {date_text}")

doc.save(OUT_PATH)
print(f"\n🎉 完成！已儲存至：{OUT_PATH}")
