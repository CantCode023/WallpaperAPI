from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
import requests, json, uvicorn, random

tags_metadata = [
    {
        "name": "Main",
        "description": "Redirects to endpoint."
    },
    {
        "name": "Wallpaper API",
        "description": "Wallpaper API."
    }
]


app = FastAPI(openapi_tags=tags_metadata, title="Wallpaper API", description="Get random wallpaper with Wallpaper API", version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get("/", tags=["Main"])
def main():
    return RedirectResponse(url="/docs")

@app.get("/getwallpaper", tags=["Wallpaper API"])
def getwallpaper():
    a = json.loads(requests.get("https://www.reddit.com/r/wallpaper/new.json").text)

    b = []

    for i in a["data"]["children"]:
        if i["data"]["domain"] == "i.redd.it":
            b.append(i["data"]["url"])

    return random.choice(b)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)