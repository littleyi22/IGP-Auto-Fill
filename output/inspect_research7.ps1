# 讀取 114學年度個別IGP七年級專題研究.docx 的表格結構
$word = New-Object -ComObject Word.Application
$word.Visible = $false

$docPath = "I:\我的雲端硬碟\語文資優\114學年度\IGP\114學年度個別IGP七年級專題研究.docx"
$outPath = "I:\我的雲端硬碟\語文資優\114學年度\IGP\output\research7_inspect.txt"

# 使用 Shell 開啟方式
$doc = $word.Documents.Open($docPath)

$lines = New-Object System.Collections.ArrayList

$tableIdx = 0
foreach ($table in $doc.Tables) {
    [void]$lines.Add("=== Table $tableIdx ($($table.Rows.Count) rows x $($table.Columns.Count) cols) ===")
    for ($ri = 1; $ri -le $table.Rows.Count; $ri++) {
        $cellTexts = @()
        for ($ci = 1; $ci -le $table.Columns.Count; $ci++) {
            try {
                $cell = $table.Cell($ri, $ci)
                $txt = ($cell.Range.Text).Trim() -replace "`r|`n|\x07", "|"
                if ($txt.Length -gt 50) { $txt = $txt.Substring(0, 50) + "..." }
                $cellTexts += "[$ci]:$txt"
            } catch { 
                $cellTexts += "[$ci]:MERGED"
            }
        }
        [void]$lines.Add("  row[$($ri-1)]: $($cellTexts -join ' | ')")
    }
    $tableIdx++
}

$doc.Close($false)
$word.Quit()

$output = $lines -join "`n"
[System.IO.File]::WriteAllText($outPath, $output, [System.Text.Encoding]::UTF8)
Write-Host "Done. Total lines: $($lines.Count)"
$lines | Select-Object -First 80
