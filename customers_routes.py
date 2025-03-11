from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from database import db

customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_customer():
    if request.method == 'POST':
        domain = request.form['domain']
        product = request.form['product']
        sku = request.form['sku']
        creation_date = request.form['creation_date']
        renew_date = request.form['renew_date']
        sub_status = request.form['sub_status']
        payment_plan = request.form['payment_plan']
        assigned_licence = request.form['assigned_licence']
        purchaced_licence = request.form['purchaced_licence']
        customer_id = request.form['customer_id']
        cloud_id = request.form['cloud_id']
        provision_id = request.form['provision_id']

        cur = db.connection.cursor()
        cur.execute("INSERT INTO customers (domain, product, sku, creation_date, renew_date, sub_status, payment_plan, assigned_licence, purchaced_licence, customer_id, cloud_id, provision_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)", (domain, product, sku, creation_date, renew_date, sub_status, payment_plan, assigned_licence, purchaced_licence, customer_id, cloud_id, provision_id))
        db.connection.commit()
        cur.close()

        return redirect(url_for('customers.view_customers'))

    return render_template('add_customer.html')

@customers_bp.route('/view')
def view_customers():
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM customers")
    customers = cur.fetchall()
    cur.close()

    return render_template('customers.html', customers=customers)
