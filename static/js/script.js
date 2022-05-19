document.addEventListener("DOMContentLoaded", () => {
	console.log("Hello World!");

	let availableChars = 6;
	let guessChars = document.querySelectorAll("#guess")
	console.log(guessChars);

	document.addEventListener('keydown', (event) => {
		var code = event.code;
		var key = event.key;
		if (code == "Enter") {
			// handleSubmitWord()
			console.log("Enter detectado")
			return;
		}
		
		if (code == "Backspace" || code == "Delete") {
			// handleDeleteLetter()
			console.log("Backspace detectado")
			return;
		}
		
		if (/^[0-9]$/i.test(key) || /^[-*+/]$/i.test(key)) {
			// updateGuessedWords(key);
			console.log("Número ou sinal detectado")
			if (availableChars)
			{
				guessChars[6 - availableChars].textContent = key;
				// document.getElementById("guess").textContent = key;
				availableChars--;
			}
		}
	
	}, false);
})


