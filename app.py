from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1 style="text-align:center;padding:50px;font-family:sans-serif;background:#0f172a;color:white;min-height:100vh">
    🎉 MUS AWWAL BUSINESS CENTER<br><br>
    APP IS LIVE!<br><br>
    <a href="https://wa.me/2347037530754" style="background:#25D366;color:white;padding:12px 20px;border-radius:10px;text-decoration:none">Chat on WhatsApp</a>
    </h1>
    """
