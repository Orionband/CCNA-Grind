# Get the full path to the directory where the script is located
$scriptPath = Split-Path -Parent $PSCommandPath

# Define the output file name
$outputFile = Join-Path -Path $scriptPath -ChildPath "questions.json"

# Get all .json files in the script's directory, excluding the output file itself
$inputFiles = Get-ChildItem -Path $scriptPath -Filter "*.json" | Where-Object { $_.FullName -ne $outputFile }

# Check if there are any JSON files to process
if ($inputFiles.Count -eq 0) {
    Write-Host "No JSON files found to combine."
    exit
}

# Create an empty array to hold all the questions from all files
$combinedQuestions = New-Object System.Collections.ArrayList

# Loop through each input file
foreach ($file in $inputFiles) {
    Write-Host "Processing file: $($file.Name)"
    try {
        # Read the content of the JSON file and convert it into a PowerShell object
        $questions = Get-Content -Path $file.FullName -Raw | ConvertFrom-Json

        # Add the questions from the current file to the combined list
        # We need to handle both cases where the JSON file contains a single object or an array of objects
        if ($questions -is [array]) {
            $combinedQuestions.AddRange($questions)
        } else {
            $combinedQuestions.Add($questions) | Out-Null
        }
    }
    catch {
        Write-Error "Failed to read or parse the file '$($file.Name)'. Please ensure it is a valid JSON format."
    }
}

# Convert the combined array of questions back to a JSON string
# The -Depth parameter ensures all nested objects are converted correctly
$jsonOutput = $combinedQuestions | ConvertTo-Json -Depth 10

# Write the final JSON output to the questions.json file
try {
    Set-Content -Path $outputFile -Value $jsonOutput
    Write-Host "Successfully combined $($inputFiles.Count) files into: $outputFile"
}
catch {
    Write-Error "Failed to write to the output file '$outputFile'."
}