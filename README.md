# python-todo

To build open the project directory (`.../python-todo`)

Create virtual environment:

```
py -m venv .venv 
```
Enter your newly created virtual environment:
```
.venv/Scripts/activate
```
Install packages that this project requires (we will use same `requirements.txt` file that docker would use to create a build)

the result of this:

```
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install pydantic
pip install httpx
pip install pytest
```
and this:

```
pip install -r requirements.txt     
```

Then build and run the app with docker:
```
docker compose up --build
```

______
By default the app is running on `http://localhost:8080`.
To start testing your changes locally open .../web/test-web-app.html file in your browser. There's a textfield where you can input remote API URL to test remote APP with remote DB. By default the html points at local api with local db

have fun