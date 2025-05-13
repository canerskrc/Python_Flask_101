from flask import Flask, render_template,request

app = Flask(__name__) # Flask uygulamanı başlatır

@app.route('/') # Ana sayfa route'u başlatır.

def home():
    return render_template("home.html") # templates klasöründeki HTML'i döndürür.

@app.route('/iletisim', methods=['GET', 'POST'])
def iletisim():
    if request.method == "POST": # formdan gelen veriler alınır.
        isim = request.form.get("isim")
        mesaj= request.form.get("mesaj")
        return render_template("sonuc.html", isim=isim, mesaj=mesaj)
    return render_template("iletisim.html")
if __name__ == '__main__':
    app.run(debug=True) # Sunucuyu başlatır. debug=True ifadesi Flask'in sunucuyu geliştirme modunda başlatması anlamını taşır

