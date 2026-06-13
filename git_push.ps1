Set-Location "C:\Users\dagle\OneDrive\Documents\Questions"

git status

git add questions.json

$msg = Read-Host "Enter commit message"

git commit -m $msg

git push