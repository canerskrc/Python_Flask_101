#Veritabanı modelleri yönetim dosyası

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
class FintechData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_id= db.Column(db.String(50), unique=True , nullable=False)
    customer_id = db.Column(db.String(50), unique=True, nullable=False)
    transaction_date= db.Column(db.String(30), nullable=False)
    transaction_type=db.Column(db.String(50), nullable=False)
    amount=db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20),nullable=False)
    crated_at = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return f"<FintechData { self.customer_id }>"