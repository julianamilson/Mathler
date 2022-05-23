document.addEventListener("DOMContentLoaded", () => {
	
	var guess = "";
	let availableChars = 6;
	
	let guessChars = document.querySelectorAll("#guess")
	
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
			).then((response) => {
				if (!response.ok) {
					throw Error()
				}
				console.log("deu bom!!");
				console.log(response.body);
			}).catch(() => {
				window.alert("Deu ruim, body no console log");
				console.log(response.body);
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
			// updateGuessedWords(key);
			if (availableChars)
			{
				guessChars[6 - availableChars].textContent = key;
				guess += key;
				availableChars--;
			}
		}
	
	}, false);
})


