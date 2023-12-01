function initChatGPT(apiUrl, chatElement, promptInput, submitButton) {
    function scrollToBottom() {
        chatElement.scrollTop = chatElement.scrollHeight;
    }

    submitButton.addEventListener('click', async () => {
        const promptText = promptInput.value;
        if (!promptText) return;

        const userMessage = document.createElement('div');
        userMessage.className = 'message user';
        userMessage.innerHTML = '<b>Пользователь: </b> ' + promptText;
        chatElement.appendChild(userMessage);
        document.querySelector('#prompt').value = ''
        scrollToBottom();

        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: promptText }),
        });

        const jsonResponse = await response.json();

        const gptMessage = document.createElement('div');
        gptMessage.className = 'message gpt';
        gptMessage.innerHTML = '<b>Новатор:</b> ' + (jsonResponse.response || 'Ошибка: ' + jsonResponse.error);
        chatElement.appendChild(gptMessage);
        document.querySelector('.business-helper__body').classList.add('response_completed')
        scrollToBottom();

        promptInput.value = '';
    });

    promptInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            submitButton.click();
        }
    });
}
