# Get the full path to the directory where the script is located
$scriptPath = Split-Path -Parent $PSCommandPath

# Define the input file path relative to the script's location
$inputFile = Join-Path -Path $scriptPath -ChildPath "questions.json"

# Check if the input file exists
if (-not (Test-Path -Path $inputFile)) {
    Write-Error "The file '$inputFile' was not found."
    exit
}

# Read the content of the JSON file and convert it into a PowerShell object
try {
    $questions = Get-Content -Path $inputFile -Raw | ConvertFrom-Json
}
catch {
    Write-Error "Failed to parse the JSON file. Please ensure it is a valid JSON format."
    exit
}

# Group the questions by the 'cat' property
$groupedQuestions = $questions | Group-Object -Property cat

# Loop through each group of questions
foreach ($group in $groupedQuestions) {
    # Get the category name for the current group
    $categoryName = $group.Name

    # Define the output file name based on the category
    $outputFile = Join-Path -Path $scriptPath -ChildPath "$($categoryName).json"

    # Convert the questions in the current group back to JSON format
    # The -Depth parameter is used to ensure all nested objects are converted
    $jsonOutput = $group.Group | ConvertTo-Json -Depth 10

    # Write the JSON output to the new category-specific file
    try {
        Set-Content -Path $outputFile -Value $jsonOutput
        Write-Host "Successfully created file: $outputFile"
    }
    catch {
        Write-Error "Failed to write to the file '$outputFile'."
    }
}