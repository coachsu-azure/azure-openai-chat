function clearForm() {
    // Clear form fields
    document.querySelector('#role').value = "";
    document.querySelector('#q').value = "";

    // Remove answer box if it exists
    const answerBox = document.querySelector('.answer-box');
    if (answerBox) {
        answerBox.remove();
    }
}