from flask import Flask, render_template, request

app = Flask(__name__)

# Data sementara (nanti kita ganti pakai database SQLite seperti sebelumnya)
dummy_addons = [
    {"id": 1, "title": "Pedang Laser AI", "desc": "Addon pedang bercahaya custom."},
    {"id": 2, "title": "Map Kota Modern", "desc": "Roleplay map super luas."},
    {"id": 3, "title": "Kendaraan Terbang", "desc": "Mobil terbang masa depan."}
]

# Halaman Utama (Menu Pilihan & Foto)
@app.route('/')
def home():
    return render_template('index.html')

# Halaman Addon Preview & Search Engine
@app.route('/addons')
def addons():
    # Fitur Search Engine: Mengambil kata kunci dari kotak pencarian
    query = request.args.get('q', '').lower()
    
    if query:
        # Filter addon yang judulnya mengandung kata kunci
        hasil_pencarian = [addon for addon in dummy_addons if query in addon['title'].lower()]
    else:
        hasil_pencarian = dummy_addons
        
    return render_template('addons.html', addons=hasil_pencarian, query=query)

# Halaman AI Web (Kosongan dulu)
@app.route('/ai')
def ai_web():
    return render_template('ai.html')

if __name__ == '__main__':
    app.run(debug=True)
  
