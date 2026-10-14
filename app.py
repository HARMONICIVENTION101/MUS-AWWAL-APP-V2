from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MUS AWWAL - Business Center | Jos</title>
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#0f7a3a">
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:system-ui,-apple-system,sans-serif}
body{background:#f6fbf7;color:#111}
.header{background:#0f7a3a;color:white;padding:18px 16px;position:sticky;top:0;z-index:10;display:flex;justify-content:space-between;align-items:center}
.logo{font-weight:800;font-size:20px;letter-spacing:.5px}
.header a{background:white;color:#0f7a3a;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:700;font-size:13px}
.hero{background:linear-gradient(135deg,#0f7a3a 0%,#14a94e 100%);color:white;padding:40px 20px;text-align:center}
.hero h1{font-size:30px;line-height:1.15;margin-bottom:10px}
.hero p{opacity:.95;font-size:16px;margin-bottom:20px}
.btn{display:inline-block;background:white;color:#0f7a3a;padding:14px 22px;border-radius:12px;text-decoration:none;font-weight:800;margin:6px}
.btn-outline{background:transparent;border:2px solid white;color:white}
.services{padding:20px;display:grid;grid-template-columns:1fr 1fr;gap:12px;max-width:900px;margin:0 auto}
.card{background:white;border-radius:16px;padding:16px;box-shadow:0 4px 12px rgba(0,0,0,.06);text-align:center}
.card .icon{font-size:28px;margin-bottom:8px}
.card h3{font-size:15px;margin-bottom:4px}
.card p{font-size:12px;color:#555;line-height:1.4}
.section{padding:24px 16px;max-width:900px;margin:0 auto}
.section h2{font-size:22px;margin-bottom:12px;color:#0f7a3a}
.about{background:white;margin:16px;border-radius:16px;padding:18px;box-shadow:0 4px 12px rgba(0,0,0,.05)}
.list{display:grid;gap:8px}
.list div{background:#f0faf3;padding:10px 12px;border-radius:10px;font-size:14px}
.contact{background:#0f7a3a;color:white;margin:16px;border-radius:16px;padding:20px;text-align:center}
.contact a{display:block;background:white;color:#0f7a3a;margin:10px 0;padding:14px;border-radius:12px;text-decoration:none;font-weight:800}
.footer{text-align:center;padding:20px;color:#777;font-size:12px}
</style>
</head>
<body>
<div class="header">
  <div class="logo">MUS AWWAL</div>
  <a href="https://wa.me/2347076199919?text=Salam, I need service from MUS AWWAL">WhatsApp</a>
</div>

<div class="hero">
  <h1>Photocopy, Printing & Passport Services</h1>
  <p>Fast • Neat • Affordable – Your No.1 Business Center in Jos</p>
  <a class="btn" href="https://wa.me/2347076199919?text=Hello MUS AWWAL, I want to print/order">Order on WhatsApp</a>
  <a class="btn btn-outline" href="#services">Our Services</a>
  <p style="margin-top:14px;font-size:12px;opacity:.9">📍 Jos, Plateau State | 🕒 Open Daily 7am - 8pm</p>
</div>

<div class="section" id="services">
<h2>Our Services</h2>
<div class="services">
  <div class="card"><div class="icon">📄</div><h3>Photocopy</h3><p>Black & White and Color photocopy - A4, A3, Card</p></div>
  <div class="card"><div class="icon">🖨️</div><h3>Document Printing</h3><p>From phone, USB, Email, WhatsApp - PDF, Word</p></div>
  <div class="card"><div class="icon">🪪</div><h3>Passport Photo</h3><p>Instant passport, full photo, background change</p></div>
  <div class="card"><div class="icon">🛡️</div><h3>Lamination</h3><p>ID Card, Document, Certificate lamination</p></div>
  <div class="card"><div class="icon">📑</div><h3>Scanning</h3><p>Scan to phone, email, PDF - high quality</p></div>
  <div class="card"><div class="icon">⌨️</div><h3>Typing & Design</h3><p>Typing, CV, Application, Business Card, Poster</p></div>
  <div class="card"><div class="icon">📚</div><h3>Binding</h3><p>Spiral binding, project binding, file arrangement</p></div>
  <div class="card"><div class="icon">💳</div><h3>Online Services</h3><p>NIN, JAMB, CAC, Registration, Applications</p></div>
</div>
</div>

<div class="section">
<div class="about">
<h2>Why MUS AWWAL?</h2>
<div class="list">
<div>✅ Fast service - No long wait</div>
<div>✅ Very neat & clear printing</div>
<div>✅ Send document on WhatsApp & collect</div>
<div>✅ Student friendly</div>
<div>✅ Located in Jos - Easy to find</div>
</div>
</div>
</div>

<div class="contact">
<h2 style="color:white">Contact Us</h2>
<p style="margin:8px 0 14px">Send your document now, we print instantly</p>
<a href="https://wa.me/2347076199919?text=Hello MUS AWWAL, I have a document to print">💬 WhatsApp: 07076199919</a>
<a href="tel:08069730375">📞 Call: 08069730375</a>
<a href="tel:07061184552">📞 Call: 07061184552</a>
<p style="margin-top:12px;font-size:13px;opacity:.9">📍 Jos, Plateau State, Nigeria</p>
</div>

<div class="footer">
<b>MUS AWWAL BUSINESS CENTER</b><br>© 2026 - All Services Available<br><br>
<button onclick="installApp()" style="padding:10px 16px;border-radius:10px;border:1px solid #ccc;background:white">📲 Install App to Phone</button>
</div>

<script>
let deferredPrompt;
window.addEventListener('beforeinstallprompt',(e)=>{e.preventDefault();deferredPrompt=e;});
function installApp(){ if(deferredPrompt){deferredPrompt.prompt();} else{alert('To install: Tap browser menu (⋮) > Add to Home screen / Install app');} }
if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js');}
</script>
</body>
</html>
"""

MANIFEST = """{"name":"MUS AWWAL Business Center","short_name":"MUS AWWAL","start_url":"/","display":"standalone","background_color":"#0f7a3a","theme_color":"#0f7a3a","icons":[{"src":"https://cdn-icons-png.flaticon.com/512/3652/3652191.png","sizes":"512x512","type":"image/png"}]}"""
SW = """self.addEventListener('install',e=>self.skipWaiting());self.addEventListener('fetch',e=>{});"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/manifest.json")
def manifest():
    return MANIFEST, 200, {"Content-Type":"application/json"}

@app.route("/sw.js")
def sw():
    return SW, 200, {"Content-Type":"application/javascript"}

if __name__ == "__main__":
    app.run()
