##### Table of Contents  
[API Documentation](#docs)  
[Application setup](#setup)  


<a name="docs"></a>
# API Documentation

Here's a quick guide of our application's endpoints, expected request format and possible response and status codes.


### `GET /home`
- This is a simple GET request to retrieve an index.html landing page. It's where you can play our game!

### `GET /README.md`
- This is a simple GET request to retrieve an index.html landing page. It's where you can learn how to play our game!

### `POST /clues`
- Required header:
```Content-Type': 'application/json'```

- Required field:
```
`guess` (type: `str`)
```

Examples:
Error response:
Request Body:
```
{
	"guess" : "15+12+15"
}
```
Response:
```
status: 200
body:
{
	"error": "Wrong size! Has to be 6 long."
}
```

Success response:
```
{
	"guess" : "40+1+1"
}
```
Response:
```
status: 200
body:
{
	"clue": "XXCCCT"
}
```


Response Example:
```

```


<a name="setup"></a>
# Application setup
  </a>
## Installing dependencies

To install the required dependencies to build and run this project, run:

```
pip install -r dependencies.txt
```

## Running webserver

To run the webserver, run:

```
cd 00_dontpanicbaby/
python3 webserver.py
```

Open your browser and connect to `localhost:5000/home` to play the game!

## Running unit tests

To run unit tests, run:

```
cd 00_dontpanicbaby/
python3 -m unittest -v
```
