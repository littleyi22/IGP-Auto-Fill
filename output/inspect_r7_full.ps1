$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open("I:\我的雲端硬碟\語文資優\114學年度\IGP\114學年度個別IGP七年級專題研究.docx")

$t = $doc.Tables.Item(1)
$outLines = @("Rows=$($t.Rows.Count) Cols=$($t.Columns.Count)", "")

for ($ri = 1; $ri -le $t.Rows.Count; $ri++) {
    $cells = @()
    for ($ci = 1; $ci -le $t.Columns.Count; $ci++) {
        try {
            $txt = $t.Cell($ri, $ci).Range.Text -replace "\x07|`r", ""
            $cells += "[$ci]:" + $txt.Substring(0, [Math]::Min(60, $txt.Length))
        } catch {
            $cells += "[$ci]:MRG"
        }
    }
    $outLines += "row[$($ri-1)]: $($cells -join ' | ')"
}

$doc.Close($false)
$word.Quit()

$out = $outLines -join "`n"
[System.IO.File]::WriteAllText(
    "I:\我的雲端硬碟\語文資優\114學年度\IGP\output\research7_inspect.txt",
    $out,
    [System.Text.Encoding]::UTF8
)
Write-Host "Saved. $($outLines.Count) lines."
$outLines | ForEach-Object { Write-Host $_ }
