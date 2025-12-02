Pythonfrom flask import Flask, Response

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice_webhook():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter1.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter2.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter3.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter4.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter5.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter6.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter7.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter8.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter9.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter10.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter11.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter12.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter13.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter14.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter15.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter16.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter17.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter18.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter19.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter20.mp3</Play>
    <Play>https://raw.githubusercontent.com/smokey831831-del/scaminater-backend/main/Skeeter21.mp3</Play>
</Response>"""
    return Response(xml, mimetype="application/xml")

if __name__ == "__main__":
    app.run()
