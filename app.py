from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
   	return render_template("home.html")

@app.route('/shop')
def shop_page():
	items = ['MAXI FLORAL DRESS', 'DENIM JACKET', 'FAKE CHANEL PURSE']
	return render_template(
		"shop.html",
		items=items)

	
if __name__ == '__main__':
   app.run(debug = True)