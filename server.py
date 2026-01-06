from flask import Flask, send_from_directory, request
import pyautogui

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

# -------- VOLUME --------
@app.route("/volume/up")
def volume_up():
    pyautogui.press("volumeup")
    return "OK"

@app.route("/volume/down")
def volume_down():
    pyautogui.press("volumedown")
    return "OK"

# -------- MEDIA --------
@app.route("/media/playpause")
def play_pause():
    pyautogui.press("playpause")
    return "OK"

@app.route("/media/forward")
def forward():
    pyautogui.press("right")
    return "OK"

@app.route("/media/backward")
def backward():
    pyautogui.press("left")
    return "OK"

@app.route("/media/next")
def next_track():
    pyautogui.press("nexttrack")
    return "OK"

@app.route("/media/prev")
def prev_track():
    pyautogui.press("prevtrack")
    return "OK"

# -------- MOUSE --------
@app.route("/mouse/move", methods=["POST"])
def mouse_move():
    data = request.json
    dx = data.get("dx", 0)
    dy = data.get("dy", 0)
    pyautogui.moveRel(dx, dy)
    return "OK"

@app.route("/mouse/click")
def mouse_click():
    pyautogui.click()
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
