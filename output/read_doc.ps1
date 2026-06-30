$word = New-Object -ComObject Word.Application
$word.Visible = $false

$files = @(
    @{src="114一上國文(三次段考)課程總表.doc"; out="output/schedule_s1.txt"},
    @{src="114一下國文(三次段考)課程總表.doc"; out="output/schedule_s2.txt"}
)

foreach ($f in $files) {
    $fullPath = (Resolve-Path $f.src).Path
    $doc = $word.Documents.Open($fullPath, $false, $true)
    $text = $doc.Content.Text
    $doc.Close($false)
    [System.IO.File]::WriteAllText((Resolve-Path "output").Path + "\" + (Split-Path $f.out -Leaf), $text, [System.Text.Encoding]::UTF8)
    Write-Host "Done: $($f.out)"
}

$word.Quit()
