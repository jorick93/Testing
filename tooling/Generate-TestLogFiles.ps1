<#
================================================================================
Script Name : Generate-TestLogFiles.ps1
Author      : Jorick van Brunschot
Version     : 1.0
Date        : 2026-04-26

Description :
This script creates 30 empty .log files in a specified folder.
Each file is assigned a unique creation date, ranging from today
back to the previous 29 days.

The filenames follow this format:
    File_yyyyMMdd.log

Use Case :
Ideal for testing scenarios such as:
- Log rotation / cleanup scripts
- File retention policies
- Automation testing with date-based files

Requirements :
- Windows PowerShell 5.1 or higher
- Write permissions to the target folder

Usage :
1. Open PowerShell
2. (Optional) Adjust the folder path below
3. Run the script:
   .\Generate-TestLogFiles.ps1

Notes :
- Existing files with the same name will cause an error
- Only the CreationTime is modified (not LastWriteTime)

================================================================================
#>

# Folder to be filled
$folderPath = "C:\Log\test"

# Check if the folder exists
if (-not (Test-Path -Path $folderPath)) {
    New-Item -ItemType Directory -Path $folderPath | Out-Null
}

# Start with today
$today = Get-Date

# make 30 empty files with creation date of last 30 days
for ($i = 0; $i -lt 30; $i++) {
    # calculate the date
    $fileDate = $today.AddDays(-$i)
    
    # Use date in filename
    $fileName = "File_$($fileDate.ToString('yyyyMMdd')).log"
    $filePath = Join-Path -Path $folderPath -ChildPath $fileName

    # Create empty file
    New-Item -ItemType File -Path $filePath | Out-Null

    # change creationdate
    $(Get-Item $filePath).CreationTime = $fileDate
}

Write-Host "30 files are created in $folderPath with custom creation dates."