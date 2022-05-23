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
			).then(response=>response.json())
			.then(data=>{
				console.log(data);
				if (data.error)
					window.alert(data.error);
				else if (data.clue)
					window.alert(data.clue);
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
})


