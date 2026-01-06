from flask import Flask, send_from_directory, request
import pyautogui
import keyboard
import qrcode
from PIL import Image
import socket
import threading
import time

app = Flask(__name__, static_folder="static")

# -------- Routes Flask --------
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

# -------- QR CODE --------
def get_local_ip():
    """Retourne l'IP locale pour générer le QR code"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def show_qr_code(url, duration=30):
    """Génère et affiche le QR code pendant `duration` secondes"""
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.show()  # ouvre l'image dans le visualiseur par défaut
    time.sleep(duration)
    try:
        img.close()
    except:
        pass

def listen_for_qr():
    """Surveille la combinaison Shift + Q + R pour afficher le QR code"""
    while True:
        if keyboard.is_pressed("shift") and keyboard.is_pressed("q") and keyboard.is_pressed("r"):
            ip = get_local_ip()
            url = f"http://{ip}:5111"  # port mis à jour
            threading.Thread(target=show_qr_code, args=(url, 30), daemon=True).start()
            # Evite que ça se déclenche en boucle instantanée
            time.sleep(1)
        time.sleep(0.1)

# -------- MAIN --------
if __name__ == "__main__":
    # Lancer le listener QR code en arrière-plan
    threading.Thread(target=listen_for_qr, daemon=True).start()
    app.run(host="0.0.0.0", port=5111)
