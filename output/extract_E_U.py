"""
從 core_competency.txt 抽取所有 特需領域核心素養（國小E級與高中U級）
產出 structured JSON
"""
import re, json

TXT_PATH  = r"h:\我的雲端硬碟\語文資優\114學年度\IGP\output\core_competency.txt"

def extract_level(level_code, json_path):
    with open(TXT_PATH, encoding="utf-8") as f:
        lines = [l.rstrip("\r\n") for l in f]

    # 目標 pattern：特情/特創/特領/特獨 - level_code - A1~C3
    TARGET_PATTERN = re.compile(rf'^(特情|特創|特領|特獨)-{level_code}-(A[123]|B[123]|C[123])$')

    result = {}  # {code: description}

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        m = TARGET_PATTERN.match(line)
        if m:
            code = line
            desc_parts = []
            i += 1
            empty_count = 0
            while i < len(lines):
                next_line = lines[i].strip()
                # 碰到另一個 code，停止
                if re.match(r'^(特情|特創|特領|特獨)-(E|J|U)-(A[123]|B[123]|C[123])$', next_line):
                    break
                if re.match(r'^\d{1,3}$', next_line):  # 頁碼
                    i += 1
                    continue
                if next_line.startswith('\x0c') or '附錄' in next_line:  # 換頁
                    break
                
                if next_line:
                    desc_parts.append(next_line)
                    empty_count = 0
                else:
                    empty_count += 1
                    if empty_count >= 3:
                        break
                i += 1
            if desc_parts:
                desc = "".join(desc_parts)
                result[code] = desc
            continue
        i += 1

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
                code = f"{domain_key}-{level_code}-{dim_key}{num}"
                if code in result:
                    structured[domain_name][code] = result[code]

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(structured, f, ensure_ascii=False, indent=2)

    total = sum(len(v) for v in structured.values())
    print(f"[{level_code} 級] 共抽取 {total} 筆核心素養 -> 儲存至 {json_path}")
    return structured

if __name__ == "__main__":
    out_e = r"h:\我的雲端硬碟\語文資優\114學年度\IGP\output\special_ed_competencies_E.json"
    out_u = r"h:\我的雲端硬碟\語文資優\114學年度\IGP\output\special_ed_competencies_U.json"
    
    extract_level("E", out_e)
    extract_level("U", out_u)
