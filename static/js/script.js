document.addEventListener("DOMContentLoaded", () => {
	
	var guess = "";
	let availableChars = 6;
	
	let guessChars = document.querySelectorAll("#guess")
	
	document.addEventListener('keydown', (event) => {
		var code = event.code;
		var key = event.key;
		
		if (code == "Enter" && availableChars == 0) {
			// handleSubmitWord()
			var temp = `{"guess": "${guess}"}`
			var fileJson = JSON.parse(temp)
			fetch(
				`http://localhost:5000/clues`,
				{
					method: "POST",
					body: fileJson
				}
			).then((res) => {
				if (!res.ok) {
					throw Error()
				}
				console.log("deu bom!!");
				console.log(res.body);
			}).catch(() => {
				window.alert("Deu ruim, body no console log");
				console.log(res.body);
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


