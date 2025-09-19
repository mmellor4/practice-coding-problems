from fastapi import FastAPI, Response, Header, HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

# string query, headers, cookies


@app.get("/hello")
async def hello(name: str = None):
    if name is None:
        return "Hello, Welcome to GeeksForGeeks!"
    else:
        return "Hello, " + name + " Welcome to GeeksForGeeks!"

# need to tell it its a cookie
# cookie object in input
@app.get("/cookie-and-object/")
async def create_cookie(response: Response):
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return {"Come to the dark side, we have cookies"}

user_db = {
    "mmellor": "puppies"
}


@app.get("/login/")
async def login(username: str = Header(None), password: str = Header(None)):
    if username in user_db and password == user_db[username]:
        return {"message": "Login Successful"}
    else:
        raise HTTPException(status_code=401, detail="Authentication failed")


# next step --> call them programatcally
