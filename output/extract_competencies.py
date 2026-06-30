"""
從 core_competency.txt 抽取所有 特需領域核心素養（國中J級）
產出 structured JSON，供後續 IGP 撰寫使用
"""
import re, json

TXT_PATH  = r"h:\我的雲端硬碟\語文資優\114學年度\IGP\output\core_competency.txt"
JSON_PATH = r"h:\我的雲端硬碟\語文資優\114學年度\IGP\output\special_ed_competencies_J.json"

with open(TXT_PATH, encoding="utf-8") as f:
    lines = [l.rstrip("\r\n") for l in f]

# 所有目標 pattern：特情/特創/特領/特獨 - J - A1~C3
TARGET_PATTERN = re.compile(r'^(特情|特創|特領|特獨)-J-(A[123]|B[123]|C[123])$')

result = {}  # {code: description}

i = 0
while i < len(lines):
    line = lines[i].strip()
    m = TARGET_PATTERN.match(line)
    if m:
        code = line  # e.g. "特情-J-A1"
        # 收集緊接其後的說明文字（直到下一個 code 或空行組）
        desc_parts = []
        i += 1
        empty_count = 0
        while i < len(lines):
            next_line = lines[i].strip()
            # 如果碰到另一個 code，或碰到 頁碼 或附錄 標題，停止
            if TARGET_PATTERN.match(next_line):
                break
            if re.match(r'^(特情|特創|特領|特獨)-(E|U)-(A[123]|B[123]|C[123])$', next_line):
                break
            if re.match(r'^\d{1,3}$', next_line):  # 頁碼
                i += 1
                continue
            if next_line.startswith('\x0c') or '附錄' in next_line:  # 換頁
                break
            # 只要非空的行就收集
            if next_line:
                desc_parts.append(next_line)
                empty_count = 0
            else:
                empty_count += 1
                if empty_count >= 3:  # 連續3個空行視為段落結束
                    break
            i += 1
        if desc_parts:
            # 合併說明：去掉重複、清理
            desc = "".join(desc_parts)
            result[code] = desc
        continue
    i += 1

# 按 domain / dimension 整理
DOMAIN_MAP = {
    "特情": "情意發展",
    "特創": "創造力",
    "特領": "領導才能",
    "特獨": "獨立研究",
}
DIMENSION_MAP = {
    "A": "A 自主行動",
    "B": "B 溝通互動",
    "C": "C 社會參與",
}

structured = {}
for domain_key, domain_name in DOMAIN_MAP.items():
    structured[domain_name] = {}
    for dim_key, dim_name in DIMENSION_MAP.items():
        for num in ["1", "2", "3"]:
            code = f"{domain_key}-J-{dim_key}{num}"
            if code in result:
                structured[domain_name][code] = result[code]

# 輸出 JSON
with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(structured, f, ensure_ascii=False, indent=2)

# 印出摘要
total = sum(len(v) for v in structured.values())
print(f"共抽取 {total} 筆 J 級核心素養")
for domain, items in structured.items():
    print(f"\n【{domain}】{len(items)} 項")
    for code, desc in items.items():
        print(f"  {code}: {desc[:30]}...")
print(f"\n已儲存至 {JSON_PATH}")
