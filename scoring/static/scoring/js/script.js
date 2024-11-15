// static/scoring/js/script.js
document.addEventListener('DOMContentLoaded', () => {
    const questions = JSON.parse(document.getElementById('questionsData').textContent);
    const form = document.getElementById('questionForm');
    const container = document.getElementById('questionContainer');
    const nextBtn = document.getElementById('nextQuestionBtn');

    let currentIndex = 0;

    function loadQuestion() {
        if (currentIndex >= questions.length) {
            form.submit();
            return;
        }

        const question = questions[currentIndex];
        container.innerHTML = `
            <h5>${question.question_text}</h5>
            <div>
                <input type="radio" name="answer" value="A" required> ${question.option_a}<br>
                <input type="radio" name="answer" value="B"> ${question.option_b}<br>
                <input type="radio" name="answer" value="C"> ${question.option_c}<br>
                <input type="radio" name="answer" value="D"> ${question.option_d}
            </div>
        `;
    }

    nextBtn.addEventListener('click', (e) => {
        e.preventDefault();
        currentIndex++;
        loadQuestion();
    });

    loadQuestion();
});