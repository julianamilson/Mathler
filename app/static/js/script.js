document.addEventListener("DOMContentLoaded", () => {
	
	var guess = "";
	let availableChars = 6;
	
	let guessChars = document.querySelectorAll("#guess")
	let clueChars = document.querySelectorAll("#clue")
	let attemptChars = document.querySelectorAll("#last_attempt")
	
	document.addEventListener('keydown', (event) => {
		var code = event.code;
		var key = event.key;

		if (key == "Enter" && availableChars == 0) {
			var jsonBody = `{"guess" : "${guess}"}`
			fetch(
				`http://localhost:5000/clues`,
				{
					headers: {
						'Content-Type': 'application/json'
					},
					method: "POST",
					body: jsonBody
				}
			).then(response=>response.json())
			.then(data=>{
				if (data.error)
					window.alert(data.error);
				else if (data.clue)
				{
					printClueOnScreen(data.clue)
					printLastAttemptOnScreen(guess)
					clearGuessOnScreen()
				}
			})
			return;
		}
		
		if (code == "Backspace" || code == "Delete") {
			if (availableChars < 6)
			{
				guessChars[5 - availableChars].textContent = "";
				guess = guess.slice(0, -1);
				availableChars++;
			}
			return;
		}
		
		if (/^[0-9]$/i.test(key) || /^[-*+/]$/i.test(key)) {
			if (availableChars)
			{
				guessChars[6 - availableChars].textContent = key;
				guess += key;
				availableChars--;
			}
		}
	
	}, false);

	function printClueOnScreen(clue)
	{
		for (var i = 0; i < clue.length; i++) {
			clueChars[i].textContent = clue.charAt(i);
		}

		if (clue == "CCCCCC")
			window.alert("🎉 You won! ! ! 🎉");
	}
	
	function printLastAttemptOnScreen(attempt)
	{
		for (var i = 0; i < attemptChars.length; i++) {
			attemptChars[i].textContent = attempt.charAt(i);
		}
	}

	function clearGuessOnScreen()
	{
		for (var i = 0; i < guessChars.length; i++) {
			guessChars[i].textContent = "";
		}
		availableChars = 6;
		guess = "";
	}
})
