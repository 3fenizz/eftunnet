from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', title='Anasayfa - TE.net | Türkiye\'nin alışveriş platformu!')

@app.route('/urun')
def product_info():
	id = request.args.get('pid')
	
	if (id == '' or id == None):
		return redirect('/')
	else:
		if (id == '1'):
			return render_template('product.html', title='Ürün - TE.net | Türkiye\'nin alışveriş platformu!', seller='PUMA', description='Smash V2 Buck - Unisex Siyah Günlük Ayakkabı Smash V2 Buck 36516005', image='https://cdn.dsmcdn.com/ty666/product/media/images/20221227/11/247456700/15358051/4/4_org_zoom.jpg')

@app.route('/marka')
def brand_page():
	brand = request.args.get('marka')

	if (brand == 'puma'):
		return render_template('brand.html', title='PUMA - TE.net | Türkiye\'nin alışveriş platformu!', seller='PUMA', description='Smash V2 Buck - Unisex Siyah Günlük Ayakkabı Smash V2 Buck 36516005', image='https://cdn.dsmcdn.com/ty666/product/media/images/20221227/11/247456700/15358051/4/4_org_zoom.jpg')

if (__name__ == '__main__'):
	app.run(debug=True)