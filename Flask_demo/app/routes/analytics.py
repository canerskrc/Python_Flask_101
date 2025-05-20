from flask import Blueprint, render_template
from app.models.fintech_data import FintechData
from sqlalchemy import func
from app import db

analytics_bp = Blueprint('analytics', __name__, url_prefix='/analytics')

@analytics_bp.route('/')
def index():
    transaction_types = db.session.query(
        FintechData.transaction_type,
        func.count(FintechData.id).label('count')
    ).group_by(FintechData.transaction_type).all()

    status_counts = db.session.query(
        FintechData.status,
        func.count(FintechData.id).label('count')
    ).group_by(FintechData.status).all()

    total_amount = db.session.query(func.sum(FintechData.amount)).scalar() or 0

    top_customers = db.session.query(
        FintechData.customer_id,
        func.count(FintechData.id).label('transaction_count'),
        func.sum(FintechData.amount).label('total_amount')
    ).group_by(FintechData.customer_id).order_by(func.count(FintechData.id).desc()).limit(5).all()

    return render_template(
        'analytics.html',
        title='Analytics Dashboard',
        transaction_types=transaction_types,
        status_counts=status_counts,
        total_amount=total_amount,
        top_customers=top_customers,
    )
