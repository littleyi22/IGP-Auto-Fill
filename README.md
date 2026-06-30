# 資優班個別輔導計畫 (IGP) 自動化填寫專案

這是一個自動化處理資優班 IGP (個別輔導計畫) 文件的專案。透過讀取課程計畫表（`.doc` 或 `.docx`），並將「特需領域核心素養」與「每週教學目標、評量方式、評量紀錄」等資料，自動化寫入至空白的 IGP Word 表格中，以節省教師手動填寫的繁瑣工作。

## 執行與啟動方式

本專案採用 Python 腳本直接處理 Word 文件。主要的填寫腳本存放在 `output/` 資料夾中。
請確認已安裝 `python-docx` 以及 `pywin32` 模組：
```bash
pip install python-docx pywin32 markitdown
```
若要執行新的填寫，可參考 `output/` 內的 `.py` 腳本（例如 `fill_igp_research7.py`），或是直接將空白 IGP 檔案與課程計畫交由 AI 助理透過 `auto_fill_igp` Skill 自動處理。

## 開發歷史 (Changelog)

### [2026-06-30] 專案進度存檔
- 新增功能：完成 114 學年度 IGP 七年級與八年級「專題研究」填寫作業（自動隨機分配評量分數，並填入獨立研究與創造力核心素養）。
- 新增功能：完成 115 學年度 IGP 八年級「國文」填寫作業。
- 新增功能：將特需領域核心素養從 PDF 文件中結構化抽取為 `special_ed_competencies_J.json`，方便未來重複調用。
- 新增功能：封裝了 `auto_fill_igp` Skill，未來可自動化處理任何學年的空白 IGP 檔案。
