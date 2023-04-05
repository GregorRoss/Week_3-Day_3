from app import app
from flask import render_template
from models.order_list import orders

@app.route('/')
def index():
    return render_template('index.html',title='Orders', orderslist=orders )

@app.route('/<int:id>')
def single_order(id):
    return render_template('order.html', title='Single Order', order=orders[id])