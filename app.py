from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

# Data Addon Sementara
dummy_addons = [
    {"id": 1, "title": "Pedang Laser AI", "desc": "Addon pedang bercahaya custom."},
    {"id": 2, "title": "Map Kota Modern", "desc": "Roleplay map super luas."},
    {"id": 3, "title": "Kendaraan Terbang", "desc": "Mobil terbang masa depan."}
]

# --- KODE KEBAL ERROR (PENGGANTI FILE HTML) ---
# Jika folder templates kamu bermasalah, Python akan pakai template cadangan ini otomatis!
HTML_UTAMA = '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hub Pusat</title>
    <style>
        body { background-color: #121212; color: #ffffff; font-family: sans-serif; text-align: center; padding: 50px 20px; }
        .foto-profil { width: 180px; height: 180px; border-radius: 50%; border: 4px solid #38bdf8; margin-bottom: 20px; animation: melayangGlow 3s ease-in-out infinite; }
        @keyframes melayangGlow { 0% { transform: translateY(0px); box-shadow: 0 0 15px #38bdf8; } 50% { transform: translateY(-15px); box-shadow: 0 0 35px #0ea5e9; } 100% { transform: translateY(0px); box-shadow: 0 0 15px #38bdf8; } }
        .menu-container { display: flex; justify-content: center; gap: 15px; margin-top: 30px; flex-wrap: wrap; }
        .btn-menu { background: #1f2937; color: #38bdf8; padding: 15px 30px; text-decoration: none; border-radius: 10px; font-weight: bold; border: 1px solid #38bdf8; transition: all 0.3s; }
        .btn-menu:hover { background: #38bdf8; color: #121212; transform: scale(1.05); }
    </style>
</head>
<body>
    <img src="https://api.dicebear.com/7.x/bottts/svg?seed=Cyber&backgroundColor=1f2937" alt="Foto Custom" class="foto-profil">
    <h1>Selamat Datang di Hub Buatanku! 🤖</h1>
    <p>Web berhasil nyala tanpa error! Silakan pilih menu:</p>
    <div class="menu-container">
        <a href="/addons" class="btn-menu">📦 Addon Preview & Search</a>
        <a href="/ai" class="btn-menu">🤖 AI Web Tools</a>
        <a href="https://youtube.com/" target="_blank" class="btn-menu">📺 YouTubeku</a>
    </div>
</body>
</html>
'''

HTML_ADDONS = '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Addon & Search</title>
    <style>
        body { background-color: #121212; color: #ffffff; font-family: sans-serif; text-align: center; padding: 30px; }
        .search-box { padding: 10px; width: 80%; max-width: 400px; border-radius: 5px; border: 1px solid #38bdf8; background: #222; color: white; margin-bottom: 20px; }
        .card { background: #1f2937; padding: 20px; margin: 15px auto; max-width: 500px; border-radius: 10px; text-align: left; border-left: 5px solid #38bdf8; }
        .btn-back { color: #38bdf8; text-decoration: none; display: block; margin-bottom: 20px; font-weight: bold; }
        .btn-cari { background: #38bdf8; color: #111; padding: 10px 20px; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <a href="/" class="btn-back">⬅ Kembali ke Menu Utama</a>
    <h2>🔍 Cari Addon / Roleplay</h2>
    <form action="/addons" method="GET">
        <input type="text" name="q" class="search-box" placeholder="Ketik nama addon..." value="{{ query }}">
        <button type="submit" class="btn-cari">Cari</button>
    </form>
    <hr style="border-color: #333; margin: 30px 0;">
    <h2>📦 Preview Addon</h2>
    {% if addons %}
        {% for addon in addons %}
        <div class="card">
            <h3 style="margin-top:0; color:#38bdf8;">{{ addon.title }}</h3>
            <p>{{ addon.desc }}</p>
        </div>
        {% endfor %}
    {% else %}
        <p>Addon tidak ditemukan. 😢</p>
    {% endif %}
</body>
</html>
'''

HTML_AI = '''
<!DOCTYPE html>
<html lang="id">
<head><title>AI Tools</title></head>
<body style="background:#121212; color:white; font-family:sans-serif; text-align:center; padding-top:50px;">
    <a href="/" style="color:#38bdf8; font-weight:bold; text-decoration:none;">⬅ Kembali</a>
    <h1>🤖 Halaman AI Web</h1>
    <p>Fitur AI siap diracik setelah ini!</p>
</body>
</html>
'''

# --- JALUR ROUTING WEB ---
@app.route('/')
def home():
    # Coba pakai folder templates dulu, kalau gagal langsung pakai template kebal error di atas
    try:
        return render_template('index.html')
    except:
        return render_template_string(HTML_UTAMA)

@app.route('/addons')
def addons():
    query = request.args.get('q', '').lower()
    if query:
        hasil = [a for a in dummy_addons if query in a['title'].lower()]
    else:
        hasil = dummy_addons
        
    try:
        return render_template('addons.html', addons=hasil, query=query)
    except:
        return render_template_string(HTML_ADDONS, addons=hasil, query=query)

@app.route('/ai')
def ai_web():
    try:
        return render_template('ai.html')
    except:
        return render_template_string(HTML_AI)

if __name__ == '__main__':
    app.run(debug=True)
