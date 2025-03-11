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
        return render_template('index.html', customers=customers)
    except Exception as e:
        return f"Error: {e}"

# ➕ Add Customer Page (Form)
@app.route('/add', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'GET':
        

        try:
            print(request.form)
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO customers (domain, product, sku, creation_date, renew_date, sub_status, payment_plan, assigned_licence, purchaced_licence, customer_id, cloud_id, provision_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (request.form['domain'], request.form['product'], request.form['sku'], request.form['creation_date'], request.form['renew_date'], request.form['sub_status'], request.form['payment_plan'], request.form['assigned_licence'], request.form['purchaced_licence'], request.form['customer_id'], request.form['cloud_id'], request.form['provision_id'],))
            mysql.connection.commit()
            cur.close()
            flash("Customer added successfully!", "success")
            return redirect(url_for('index'))
        except Exception as e:
            return f"Error: {e}"

    return render_template('add_customer.html')

# 🏆 Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)
