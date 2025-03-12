from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Database Configuration (Update with your MySQL credentials)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'rahul'  # Change if you have a different user
app.config['MYSQL_PASSWORD'] = 'Xh4dJ-J+'  # Add your MySQL password if set
app.config['MYSQL_DB'] = 'customerpanelapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Secret key for session (used for flash messages)
app.secret_key = "supersecretkey"

# 🏠 Index Page - View Customers
@app.route('/')
def index():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM customers")
        customers = cur.fetchall()
        cur.close()
        return render_template('customers.html', customers=customers)
    except Exception as e:
        return f"Error: {e}"

# ➕ Add Customer Page (Form)
@app.route('/add', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        try:
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
            cur.execute("INSERT INTO customers (domain, product, sku, creation_date, renew_date, sub_status, payment_plan, assigned_licence, purchaced_licence, customer_id, cloud_id, provision_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (domain, product, sku, creation_date, renew_date, sub_status, payment_plan, assigned_licence, purchaced_licence, customer_id, cloud_id, provision_id))
            db.connection.commit()
            cur.close()

            flash("Customer added successfully!", "success")
            return redirect(url_for('customers'))

        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            return redirect(url_for('add_customer'))

    return render_template('add_customer.html')


# 🏆 Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)
