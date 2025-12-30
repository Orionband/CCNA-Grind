const startBtn = document.getElementById('startBtn');
const quizContainer = document.getElementById('quizContainer');
const resultsContainer = document.getElementById('resultsContainer');
const mainScreen = document.getElementById('mainScreen');
const categorySelect = document.getElementById('categorySelect');
const modeSelect = document.getElementById('modeSelect');
const questionNavigator = document.getElementById('questionNavigator');

const CATEGORY_MAP = {
    "NETFD": "1.0 Network Fundamentals",
    "NETAC": "2.0 Network Access",
    "IPCON": "3.0 IP Connectivity",
    "IPSVC": "4.0 IP Services",
    "SEC": "5.0 Security Fundamentals",
    "AUTO": "6.0 Automation & Programmability"
};

let allQuestions = [];
let currentQuizQuestions = [];
let quizHistory = [];
let bookmarkedQuestions = [];
let chartInstances = {};
let quizTimerInterval;
let quizStartTime;

function setUIView(view) {
    if (view === 'quiz') {
        mainScreen.classList.add('hidden');
        quizContainer.classList.remove('hidden');
        questionNavigator.classList.remove('hidden');
        resultsContainer.innerHTML = '';
    } else { // 'main' view
        mainScreen.classList.remove('hidden');
        quizContainer.classList.add('hidden');
        questionNavigator.classList.add('hidden');

        // Clean up content from the previous quiz to prevent lingering elements
        quizContainer.innerHTML = ''; 
        resultsContainer.innerHTML = '';
        document.getElementById('navigatorList').innerHTML = ''; 
        document.getElementById('timerDisplay').textContent = 'Time: 00:00';
    }
}


document.addEventListener('DOMContentLoaded', () => {
    setUIView('main');
    
    Chart.register(ChartDataLabels);
    loadDataFromStorage();
    populateCategoryFilter();
    populateCategoryDescriptions();
    loadQuestions();

    startBtn.addEventListener('click', loadAndDisplayQuiz);
    modeSelect.addEventListener('change', updateMaxQuestions);
    document.getElementById('clearDataBtn').addEventListener('click', clearAllData);
    
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
        renderDashboard();
        const summaryCtx = document.getElementById('quizSummaryChart')?.getContext('2d');
        if (summaryCtx) {
            const latestAttempt = quizHistory[quizHistory.length - 1];
            if (latestAttempt) {
                renderQuizSummaryChart(latestAttempt);
            }
        }
    });
});

function getChartThemeOptions() {
    const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const gridColor = isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)';
    const textColor = isDark ? '#e2e8f0' : '#1e293b';
    return { color: textColor, grid: { color: gridColor }, ticks: { color: textColor } };
}

function loadDataFromStorage() {
    quizHistory = JSON.parse(localStorage.getItem('quizHistory')) || [];
    bookmarkedQuestions = JSON.parse(localStorage.getItem('bookmarkedQuestions')) || [];
}
function saveDataToStorage() {
    localStorage.setItem('quizHistory', JSON.stringify(quizHistory));
    localStorage.setItem('bookmarkedQuestions', JSON.stringify(bookmarkedQuestions));
}
function clearAllData() {
    if (confirm("Are you sure? This will erase all your progress.")) {
        quizHistory = [];
        bookmarkedQuestions = [];
        saveDataToStorage();
        renderDashboard();
        updateMaxQuestions();
        alert("All study data has been cleared.");
    }
}
function populateCategoryDescriptions() {
    const listElement = document.getElementById('categoryList');
    if (!listElement) return;
    listElement.innerHTML = '';
    const sortedCategories = Object.entries(CATEGORY_MAP).sort((a, b) => a[1].localeCompare(b[1]));
    for (const [code, description] of sortedCategories) {
        const listItem = document.createElement('li');
        listItem.innerHTML = `<strong>${code}</strong> - ${description}`;
        listElement.appendChild(listItem);
    }
}
function populateCategoryFilter() {
    const sortedCategories = Object.entries(CATEGORY_MAP).sort((a, b) => a[1].localeCompare(b[1]));
    for (const [code, description] of sortedCategories) {
        const option = document.createElement('option');
        option.value = code;
        option.textContent = description;
        categorySelect.appendChild(option);
    }
}

// --- FIXED MISTAKE LOGIC ---
function getMistakeQuestionIds() {
    const questionStatus = {}; // Map of questionId (string) -> isCorrect (boolean)

    // Iterate through history chronologically
    quizHistory.forEach(quiz => {
        quiz.questions.forEach(q => {
            // Ensure ID is string for consistent key usage
            const id = String(q.questionId);
            // Update the status to the most recent result
            questionStatus[id] = q.isCorrect;
        });
    });

    // Return only IDs where the most recent status is false (incorrect)
    return Object.keys(questionStatus).filter(id => questionStatus[id] === false);
}

function getLocalExhibitPath(fullUrl) {
    if (!fullUrl) return '';
    try {
        const url = new URL(fullUrl);
        let rawPath = fullUrl.substring(url.origin.length);
        rawPath = rawPath.replaceAll(':', '_');
        return `./images${rawPath}`;
    } catch (e) {
        console.error(`Could not parse URL: "${fullUrl}".`, e);
        let filename = fullUrl.split('/').pop().replaceAll(':', '_');
        return `./images/${filename}`;
    }
}
function updateMaxQuestions() {
    const mode = modeSelect.value;
    const category = categorySelect.value;
    const numInput = document.getElementById('numQuestions');
    const categoryInput = document.getElementById('categorySelect');
    const randomizeInput = document.getElementById('randomize');
    let pool = [];

    if (mode === 'exsim') {
        numInput.value = 120;
        numInput.disabled = true;
        categoryInput.disabled = true;
        randomizeInput.disabled = true;
        randomizeInput.checked = true;
        startBtn.disabled = false;
        startBtn.textContent = 'Start ExSim';
        return;
    }

    numInput.disabled = false;
    categoryInput.disabled = false;
    randomizeInput.disabled = false;

    if (mode === 'standard') {
        pool = (category === 'ALL') ? allQuestions : allQuestions.filter(q => q.cat === category);
    } else if (mode === 'mistakes') {
        const mistakeIds = getMistakeQuestionIds();
        // Strict string comparison for IDs
        pool = allQuestions.filter(q => mistakeIds.includes(String(q.questionId)));
        if (category !== 'ALL') {
            pool = pool.filter(q => q.cat === category);
        }
    } else if (mode === 'flagged') {
        pool = allQuestions.filter(q => bookmarkedQuestions.includes(String(q.questionId)));
        if (category !== 'ALL') {
            pool = pool.filter(q => q.cat === category);
        }
    }

    numInput.max = pool.length;

    if (pool.length > 0) {
        if (parseInt(numInput.value) > pool.length || parseInt(numInput.value) === 0) {
                numInput.value = Math.min(10, pool.length);
        }
        startBtn.disabled = false;
        startBtn.textContent = 'Start Test';
    } else {
        numInput.value = 0;
        startBtn.disabled = true;
        startBtn.textContent = 'No Questions in Pool';
    }
}

// --- FIXED ID GENERATION ---
function normalizeQuestions(data) {
    return data.map((q, index) => {
        // Ensure every question has a stable ID (String)
        if (!q.questionId) {
            // Fallback: Use a hash of the text or the index if text is missing
            // Simple hash function for text
            const text = q.questionText || "";
            let hash = 0;
            for (let i = 0; i < text.length; i++) {
                hash = ((hash << 5) - hash) + text.charCodeAt(i);
                hash |= 0; 
            }
            q.questionId = "gen-" + Math.abs(hash) + "-" + index;
        } else {
            q.questionId = String(q.questionId);
        }

        if (q.answerType === 'MS' && q.rawAnswer && q.rawAnswer.MultipleChoice) {
            q.answerChoices = q.rawAnswer.MultipleChoice.map(choice => ({
                Text: choice.Text.replace(/ltpgt-open|ltpgt-close/g, '').trim(),
                IsCorrect: choice.IsCorrect
            }));
        } else if (!q.answerType && q.answerChoices) {
            const correctCount = q.answerChoices.filter(c => c.IsCorrect).length;
            q.answerType = correctCount > 1 ? 'MS' : 'MC';
        }
        return q;
    });
}

function loadQuestions() {
    startBtn.disabled = true;
    startBtn.textContent = 'Loading Deck...';
    fetch('questions.json')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            allQuestions = normalizeQuestions(data);
            updateMaxQuestions();
            renderDashboard();
        })
        .catch(error => {
            console.error(`Error fetching questions.json:`, error);
            mainScreen.innerHTML = `<p style="color: red; text-align: center;">CRITICAL ERROR: Could not load questions.json.</p>`;
            startBtn.textContent = 'Load Failed';
        });
}

function startTimer(durationInSeconds = null) {
    const timerDisplay = document.getElementById('timerDisplay');
    if (!timerDisplay) return;
    
    clearInterval(quizTimerInterval);
    quizStartTime = Date.now();

    if (durationInSeconds !== null) {
        let timeRemaining = durationInSeconds;
        const updateCountdown = () => {
            if (timeRemaining <= 0) {
                clearInterval(quizTimerInterval);
                timerDisplay.textContent = 'Time Up!';
                alert('Time is up! The quiz will be submitted automatically.');
                if (!resultsContainer.innerHTML) { 
                    showResults();
                }
                return;
            }
            const minutes = Math.floor(timeRemaining / 60).toString().padStart(2, '0');
            const seconds = (timeRemaining % 60).toString().padStart(2, '0');
            timerDisplay.textContent = `Time Left: ${minutes}:${seconds}`;
            timeRemaining--;
        };
        updateCountdown(); 
        quizTimerInterval = setInterval(updateCountdown, 1000);
    } else {
        timerDisplay.textContent = 'Time: 00:00';
        quizTimerInterval = setInterval(() => {
            const elapsed = Math.floor((Date.now() - quizStartTime) / 1000);
            const minutes = Math.floor(elapsed / 60).toString().padStart(2, '0');
            const seconds = (elapsed % 60).toString().padStart(2, '0');
            timerDisplay.textContent = `Time: ${minutes}:${seconds}`;
        }, 1000);
    }
}

async function loadAndDisplayQuiz() {
    const numQuestionsInput = document.getElementById('numQuestions');
    const randomize = document.getElementById('randomize').checked;
    const mode = modeSelect.value;
    const category = categorySelect.value;
    let questionPool = [];
    
    if (mode === 'exsim') {
        const EXSIM_CONFIG = {
            total: 120,
            distribution: {
                "NETFD": 0.20, "NETAC": 0.20, "IPCON": 0.25,
                "IPSVC": 0.10, "SEC": 0.15, "AUTO": 0.10
            }
        };
        currentQuizQuestions = [];
        for (const [cat, percentage] of Object.entries(EXSIM_CONFIG.distribution)) {
            const numToTake = Math.round(EXSIM_CONFIG.total * percentage);
            let categoryPool = allQuestions.filter(q => q.cat === cat);
            categoryPool.sort(() => Math.random() - 0.5);
            currentQuizQuestions.push(...categoryPool.slice(0, numToTake));
        }
        currentQuizQuestions.sort(() => Math.random() - 0.5);

    } else { 
        if (mode === 'mistakes') {
            const mistakeIds = getMistakeQuestionIds();
            // Strict string comparison
            questionPool = allQuestions.filter(q => mistakeIds.includes(String(q.questionId)));
        } else if (mode === 'flagged') {
            questionPool = allQuestions.filter(q => bookmarkedQuestions.includes(String(q.questionId)));
        } else {
            questionPool = allQuestions;
        }

        if (category !== 'ALL') {
            questionPool = questionPool.filter(q => q.cat === category);
        }

        if (questionPool.length === 0) {
            alert("There are no questions available for your selected criteria.");
            return;
        }
        const numQuestions = Math.min(parseInt(numQuestionsInput.value), questionPool.length);
        
        if (randomize) {
            currentQuizQuestions = [...questionPool].sort(() => Math.random() - 0.5).slice(0, numQuestions);
        } else {
            currentQuizQuestions = questionPool.slice(0, numQuestions);
        }
    }


    const exhibitPromises = currentQuizQuestions.flatMap(q => (q.exhibits || []).map(exhibit => {
        if (!exhibit.ExhibitFileName) return null;
        exhibit.localPath = getLocalExhibitPath(exhibit.ExhibitFileName);
        if (exhibit.localPath.toLowerCase().endsWith('.txt')) {
            return fetch(exhibit.localPath)
                .then(response => {
                    if (!response.ok) throw new Error(`Failed to fetch ${exhibit.localPath}`);
                    return response.text();
                })
                .then(text => { exhibit.textContent = text; })
                .catch(error => {
                    console.error('Error fetching exhibit:', error);
                    exhibit.textContent = `Error: Could not load exhibit.`;
                });
        }
        return null;
    })).filter(Boolean);

    await Promise.all(exhibitPromises);
    displayQuiz();
    
    if (mode === 'exsim') {
        startTimer(120 * 60);
    } else {
        startTimer();
    }
}

function displayQuiz() {
    setUIView('quiz');
    
    quizContainer.innerHTML = `<h2>Quiz</h2>`;
    
    currentQuizQuestions.forEach((q, index) => {
        const questionDiv = document.createElement('div');
        questionDiv.className = 'question';
        questionDiv.id = `q-${index}`;
        questionDiv.dataset.questionId = q.questionId;

        const isBookmarked = bookmarkedQuestions.includes(String(q.questionId));
        const bookmarkedClass = isBookmarked ? 'bookmarked' : '';

        let questionTextHtml = `<div class="question-header"><button class="bookmark-btn ${bookmarkedClass}" onclick="toggleBookmark('${q.questionId}', this, ${index})">🚩</button><div class="question-text">${index + 1}. <span class="question-category">(${(q.cat || 'N/A')})</span> ${q.questionText}</div></div>`;
        if (q.answerType === 'FB') {
            const inputField = `<input type="text" class="fb-input" id="fb-input-${index}" autocomplete="off">`;
            questionTextHtml = questionTextHtml.replace(/___/g, inputField);
        }
        
        let exhibitsHtml = '';
        if (q.exhibits && q.exhibits.length > 0) {
            q.exhibits.forEach(exhibit => {
                const localPath = exhibit.localPath;
                if (!localPath) return;
                const filename = decodeURIComponent(localPath.split('/').pop());
                const filenameLower = filename.toLowerCase();
                if (filenameLower.endsWith('.txt')) {
                    exhibitsHtml += `<div class="exhibit-container"><strong>Exhibit: ${filename}</strong><pre class="question-exhibit-text">${exhibit.textContent || ''}</pre></div>`;
                } else if (filenameLower.endsWith('.html')) {
                    exhibitsHtml += `<iframe src="${localPath}" class="question-exhibit-frame" title="Exhibit: ${filename}"></iframe>`;
                } else if (/\.(png|jpg|jpeg|gif)$/i.test(filenameLower)) {
                    exhibitsHtml += `<img src="${localPath}" alt="Exhibit: ${filename}" class="question-exhibit">`;
                }
            });
        }
        
        let answersHtml = '';
        if ((q.answerType === 'MC' || q.answerType === 'MS') && q.answerChoices) {
            const inputType = q.answerType === 'MS' ? 'checkbox' : 'radio';
            q.answerChoices.forEach((choice, originalIndex) => {
                answersHtml += `<label class="answer-choice">${choice.Text}<input type="${inputType}" name="question-${index}" value="${originalIndex}"><span class="checkmark"></span></label>`;
            });
        }

        questionDiv.innerHTML = questionTextHtml + exhibitsHtml + answersHtml;
        quizContainer.appendChild(questionDiv);
    });

    const submitButton = document.createElement('button');
    submitButton.id = 'submitBtn';
    submitButton.className = 'submit-btn';
    submitButton.textContent = 'Submit Test';
    submitButton.addEventListener('click', showResults);
    quizContainer.appendChild(submitButton);

    const navigatorList = document.getElementById('navigatorList');
    navigatorList.innerHTML = '';
    currentQuizQuestions.forEach((q, index) => {
        const navBtn = document.createElement('button');
        navBtn.className = 'nav-btn';
        navBtn.innerHTML = `Q ${index + 1}`;
        navBtn.dataset.index = index;
        navBtn.onclick = () => document.getElementById(`q-${index}`).scrollIntoView();
        if (bookmarkedQuestions.includes(String(q.questionId))) {
            navBtn.classList.add('flagged');
        }
        navigatorList.appendChild(navBtn);
        
        const questionDiv = document.getElementById(`q-${index}`);
        const inputs = questionDiv.querySelectorAll('input[type="radio"], input[type="checkbox"], input.fb-input');
        inputs.forEach(input => input.addEventListener('input', () => navBtn.classList.add('answered')));
    });
}

function toggleBookmark(questionId, buttonElement, questionIndex) {
    const id = String(questionId);
    const navBtn = document.querySelector(`.nav-btn[data-index="${questionIndex}"]`);
    const index = bookmarkedQuestions.indexOf(id);

    if (index > -1) {
        bookmarkedQuestions.splice(index, 1);
        buttonElement.classList.remove('bookmarked');
        if (navBtn) {
            navBtn.classList.remove('flagged');
        }
    } else {
        bookmarkedQuestions.push(id);
        buttonElement.classList.add('bookmarked');
        if (navBtn) {
            navBtn.classList.add('flagged');
        }
    }
    saveDataToStorage();
}

function showResults() {
    clearInterval(quizTimerInterval);
    questionNavigator.classList.add('hidden'); // Hide navigator for the results display

    let score = 0;
    const quizAttempt = {
        timestamp: Date.now(),
        score: 0,
        total: currentQuizQuestions.length,
        questions: []
    };
    
    currentQuizQuestions.forEach((q, index) => {
        let isQuestionCorrect = false;
        
        if (q.answerType === 'FB') {
            const userInput = document.querySelector(`#fb-input-${index}`);
            if (userInput) {
                const userValue = userInput.value.trim().toLowerCase();
                const correctAnswers = (q.blanks && q.blanks[0] ? q.blanks[0] : "").split(',').map(ans => ans.trim().toLowerCase());
                if (userValue && correctAnswers.includes(userValue)) {
                    isQuestionCorrect = true;
                }
            }
        } else if ((q.answerType === 'MC' || q.answerType === 'MS') && q.answerChoices) {
            const userChoices = Array.from(document.querySelectorAll(`input[name="question-${index}"]:checked`));
            const userAnswerIndices = userChoices.map(input => parseInt(input.value));
            const correctAnswerIndices = q.answerChoices.map((choice, i) => choice.IsCorrect ? i : -1).filter(i => i !== -1);
            
            isQuestionCorrect = userAnswerIndices.length === correctAnswerIndices.length && 
                                userAnswerIndices.sort().toString() === correctAnswerIndices.sort().toString();
        }
        
        if (isQuestionCorrect) {
            score++;
        }
        quizAttempt.questions.push({
            questionId: String(q.questionId),
            isCorrect: isQuestionCorrect,
            category: q.cat
        });
    });

    quizAttempt.score = score;
    quizHistory.push(quizAttempt);
    saveDataToStorage();
    renderDashboard();

    const answerInputs = quizContainer.querySelectorAll('.answer-choice input, .fb-input');
    answerInputs.forEach(input => {
        input.disabled = true;
        const label = input.closest('label.answer-choice');
        if (label) {
            label.style.cursor = 'default';
        }
    });
    document.getElementById('submitBtn')?.remove();

    const totalTimeSeconds = Math.floor((Date.now() - quizStartTime) / 1000);
    const scorePercentage = Math.round((score / currentQuizQuestions.length) * 100);
    const scoreHeader = document.createElement('h2');
    scoreHeader.innerHTML = `Your Score: ${score} out of ${currentQuizQuestions.length} (${scorePercentage}%) <br> <small style="font-weight: 500; color: var(--text-muted-color);">Time Taken: ${Math.floor(totalTimeSeconds / 60)}m ${totalTimeSeconds % 60}s</small>`;
    resultsContainer.appendChild(scoreHeader);
    
    const summaryContainer = document.createElement('div');
    summaryContainer.className = 'chart-summary-container';
    summaryContainer.innerHTML = `<h3>This Quiz Performance</h3><div class="chart-wrapper"><canvas id="quizSummaryChart"></canvas></div>`;
    resultsContainer.appendChild(summaryContainer);
    
    const uniqueCategoriesInQuiz = new Set(quizAttempt.questions.map(q => q.category || 'N/A'));
    const numCategories = uniqueCategoriesInQuiz.size;
    const dynamicHeight = Math.max(150, (numCategories * 40) + 80);
    const chartWrapper = summaryContainer.querySelector('.chart-wrapper');
    if (chartWrapper) {
        chartWrapper.style.height = `${dynamicHeight}px`;
    }
    
    renderQuizSummaryChart(quizAttempt);
    revealAnswers();
    
    const restartBtn = document.createElement('button');
    restartBtn.id = 'restartBtn';
    restartBtn.className = 'restart-btn';
    restartBtn.textContent = 'Take Another Test';
    restartBtn.onclick = () => {
        setUIView('main');
        updateMaxQuestions();
    };
    quizContainer.appendChild(restartBtn);
}

function revealAnswers() {
    currentQuizQuestions.forEach((q, index) => {
        const questionElement = document.getElementById(`q-${index}`);
        if (!questionElement) {
            console.error(`Could not find question element for index ${index}`);
            return;
        }

        const bookmarkButton = questionElement.querySelector('.bookmark-btn');
        if (bookmarkButton) {
            bookmarkButton.style.display = 'none';
        }

        if (q.answerType === 'FB') {
            const userInput = questionElement.querySelector(`#fb-input-${index}`);
            if (!userInput) return;

            const userValue = userInput.value.trim().toLowerCase();
            const correctAnswers = (q.blanks && q.blanks[0] ? q.blanks[0] : "").split(',').map(ans => ans.trim().toLowerCase());

            if (userValue && correctAnswers.includes(userValue)) {
                userInput.classList.add('correct');
            } else {
                userInput.classList.add('incorrect');
            }
            
            const explanationText = `<strong>Correct Answer(s):</strong> ${q.blanks[0] || 'N/A'}<br><br>${q.explanation || 'No explanation provided.'}`;
            questionElement.insertAdjacentHTML('beforeend', `<div class="result-explanation">${explanationText}</div>`);

        } else if ((q.answerType === 'MC' || q.answerType === 'MS') && q.answerChoices) {
            const userChoices = Array.from(document.querySelectorAll(`input[name="question-${index}"]:checked`));
            const userAnswerIndices = userChoices.map(input => parseInt(input.value));
            const allChoiceLabels = questionElement.querySelectorAll('.answer-choice');

            allChoiceLabels.forEach((label) => {
                const choiceInput = label.querySelector('input');
                if (!choiceInput) return;

                const originalChoiceIndex = parseInt(choiceInput.value);
                const isCorrectChoice = q.answerChoices[originalChoiceIndex].IsCorrect;
                const wasSelectedByUser = userAnswerIndices.includes(originalChoiceIndex);

                if (isCorrectChoice) {
                    label.classList.add('correct');
                } else if (wasSelectedByUser && !isCorrectChoice) {
                    label.classList.add('incorrect');
                }
            });
            
            const explanationHtml = `<div class="result-explanation">${q.explanation || 'No explanation provided.'}</div>`;
            questionElement.insertAdjacentHTML('beforeend', explanationHtml);
        }
    });
}

function renderDashboard() {
    renderCategoryChart();
    renderHistoryChart();
}

function renderQuizSummaryChart(quizAttempt) {
    const ctx = document.getElementById('quizSummaryChart')?.getContext('2d');
    if (!ctx) return;
    if (chartInstances.summary) {
        chartInstances.summary.destroy();
    }
    const categoryStats = {};
    quizAttempt.questions.forEach(qResult => {
        const category = qResult.category || 'N/A';
        if (!categoryStats[category]) {
            categoryStats[category] = { correct: 0, total: 0 };
        }
        categoryStats[category].total++;
        if (qResult.isCorrect) {
            categoryStats[category].correct++;
        }
    });
    
    const includedCategories = Object.keys(categoryStats);
    const labels = includedCategories.map(cat => CATEGORY_MAP[cat] || cat);
    const data = includedCategories.map(cat => {
        const stats = categoryStats[cat];
        return stats.total > 0 ? (stats.correct / stats.total) * 100 : 0;
    });

    const themeOptions = getChartThemeOptions();
    chartInstances.summary = new Chart(ctx, {
        type: 'bar',
        data: { labels: labels, datasets: [{ label: '% Correct', data: data, backgroundColor: 'rgba(34, 197, 94, 0.7)', borderColor: 'rgb(34, 197, 94)', borderWidth: 1 }] },
        options: { indexAxis: 'y', scales: { x: { ...themeOptions, beginAtZero: true, max: 100, ticks: { ...themeOptions.ticks, callback: (v) => v + "%" } }, y: { ...themeOptions } }, plugins: { legend: { display: false }, title: { display: false }, datalabels: { anchor: 'end', align: 'end', color: themeOptions.color, font: { weight: 'bold' }, formatter: (v) => v.toFixed(0) + '%' } }, responsive: true, maintainAspectRatio: false }
    });
}

function renderCategoryChart() {
    const ctx = document.getElementById('categoryChart')?.getContext('2d');
    if (!ctx) return;
    if (chartInstances.category) {
        chartInstances.category.destroy();
    }
    const categoryStats = {};
    for(const code in CATEGORY_MAP) {
        categoryStats[code] = { correct: 0, total: 0 };
    }
    quizHistory.forEach(quiz => {
        quiz.questions.forEach(qResult => {
            const questionData = allQuestions.find(q => String(q.questionId) === String(qResult.questionId));
            if (questionData && questionData.cat && categoryStats[questionData.cat]) {
                categoryStats[questionData.cat].total++;
                if(qResult.isCorrect) {
                    categoryStats[questionData.cat].correct++;
                }
            }
        });
    });

    const sortedCategoryCodes = Object.keys(CATEGORY_MAP).sort((a,b) => CATEGORY_MAP[a].localeCompare(CATEGORY_MAP[b])); 
    const labels = sortedCategoryCodes.map(code => CATEGORY_MAP[code]); 
    const data = sortedCategoryCodes.map(code => {
        const stats = categoryStats[code];
        return stats.total > 0 ? (stats.correct / stats.total) * 100 : 0;
    });
    
    const themeOptions = getChartThemeOptions();
    chartInstances.category = new Chart(ctx, {
        type: 'bar',
        data: { labels: labels, datasets: [{ label: '% Correct by Topic', data: data, backgroundColor: 'rgba(59, 130, 246, 0.7)', borderColor: 'rgba(59, 130, 246, 1)', borderWidth: 1 }] }, 
        options: {
            indexAxis: 'y',
            scales: { x: { ...themeOptions, beginAtZero: true, max: 100, ticks: { ...themeOptions.ticks, callback: (v) => v + "%" } }, y: { ...themeOptions } },
            plugins: {
                legend: { display: false },
                title: { display: true, text: 'Overall Performance by Topic', color: themeOptions.color },
                datalabels: {
                    anchor: 'end',
                    align: (context) => (context.dataset.data[context.dataIndex] > 90 ? 'start' : 'end'),
                    color: (context) => (context.dataset.data[context.dataIndex] > 90 ? (themeOptions.color === '#e2e8f0' ? '#1e293b' : 'white') : themeOptions.color),
                    font: { weight: 'bold' },
                    formatter: (value, context) => {
                        const code = sortedCategoryCodes[context.dataIndex];
                        const stats = categoryStats[code];
                        if (stats.total === 0) return '';
                        return `${value.toFixed(0)}% (${stats.correct}/${stats.total})`;
                    },
                    offset: 4,
                    padding: 0
                }
            },
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

function renderHistoryChart() {
    const ctx = document.getElementById('historyChart')?.getContext('2d');
    if (!ctx) return;
    if (chartInstances.history) {
        chartInstances.history.destroy();
    }
    const chartData = quizHistory.map(quiz => ({ x: quiz.timestamp, y: (quiz.score / quiz.total) * 100 }));
    const themeOptions = getChartThemeOptions();
    chartInstances.history = new Chart(ctx, {
        type: 'line',
        data: { datasets: [{ label: 'Quiz Score %', data: chartData, fill: false, borderColor: 'rgb(34, 197, 94)', tension: 0.1 }] },
        options: {
            scales: { x: { type: 'time', time: { unit: 'day', tooltipFormat: 'PP' }, title: { display: true, text: 'Date', color: themeOptions.color }, ...themeOptions }, y: { beginAtZero: true, max: 100, title: { display: true, text: 'Score %', color: themeOptions.color }, ...themeOptions } },
            plugins: {
                legend: { display: false },
                title: { display: true, text: 'Score Over Time', color: themeOptions.color },
                datalabels: { align: 'top', backgroundColor: 'rgba(34, 197, 94, 0.7)', borderRadius: 4, color: 'white', font: { size: 10, weight: 'bold' }, formatter: (v) => Math.round(v.y) + '%', display: 'auto' }
            },
            responsive: true,
            maintainAspectRatio: false
        }
    });
}
