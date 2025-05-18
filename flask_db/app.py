import os.path

from adodbapi import IntegrityError
from flask import Flask, render_template, redirect, url_for
from models import db, FintechData
import json
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # sqlite veritabanı dosyalarının yolunu belirtir.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Gereksiz performans maliyetlerini önlemek için kullanılır.

db.init_app(app) #SQLAlchemy başlatıldı.

with app.app_context(): # context açılarak veritabanı işlemlerine izin verilir.

    db.create_all() # models.py dosyasında tanımlanan tüm veritabanı modellerinin tablolarını otomatik oluşturur.

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/upload',methods=['POST'])
def upload():
    if not os.path.exists('Fintech_data.json'):
        return "JSON dosya bulunamadı.", 404

    with open('fintech_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data: # json içindeki her kayıt için bir döngü
        existing = FintechData.query.filter_by(customer_id = item['customer_id']).first()
        if not existing:
            transaction = FintechData(  # yeni bir veritabanı nesnesi.
                transaction_id=item['transaction_id'],
                customer_id=item['customer_id'],
                transaction_type=item['transaction_type'],
                transaction_date=item['transaction_date'],
                amount=item['amount'],
                status=item['status'],
            )
            db.session.add(transaction)
    # nesne veritabanı oturumuna eklenir.
    db.session.commit()#Tüm işlemler kalıcı olarak veritabanına yazılır.
    return redirect(url_for('index'))#işlemler tamamlandıktan sonra anasayfaya yönlendirilir.

if __name__ == '__main__':
    app.run(debug=True)




# if not existing:
  # db.session.add(transaction)

# İkinci alternatif try except bloğu ile IntegrationError yönetilir.


# id sütununu önceden almak gerekirse db.session.flush() çağrısından sonra erişilebilir hale gelir.


