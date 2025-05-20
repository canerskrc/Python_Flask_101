from flask import Blueprint, render_template, request, flash, redirect,url_for
import json
from app import db
from app.models.fintech_data import FintechData

data_bp = Blueprint('data', __name__, url_prefix='/data')
#https://.........../data/import
@data_bp.route('/')

def index():
    data = FintechData.query.all()
    return render_template('data.html', title="Fintech Data", data=data)

@data_bp.route('/import', methods=['GET', 'POST'])
def import_data():
    if request.method =='POST':
        try:
            with open('fintech_data.json','r') as f:
                data = json.load(f)

            db.session.query(FintechData).delete()

            for item in data:
                fintech_entry = FintechData(
                    transaction_id = item['transaction_id'],
                    customer_id = item['customer_id'],
                    transaction_date = item['transaction_date'],
                    transaction_type = item['transaction_type'],
                    amount = item['amount'],
                    status = item['status'],
                )
                db.session.add(fintech_entry)
            db.session.commit(fintech_entry)

            flash('Data successfully imported from JSON file','success')
            return redirect(url_for('data.index'))
        except Exception as e:
            flash(f'Error importing Data: {str(e)}','danger')
    return render_template('import.html', title='Import DATA')

