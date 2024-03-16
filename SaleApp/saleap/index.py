from flask import Flask, render_template, request
import dao

app = Flask(__name__)

@app.route("/")
def index():
    kw = request.args.get('kw')
    cate_id= request.args.get('categories_id')

    cate = dao.load_categories()
    prod = dao.load_product()
    return render_template('index.html', categories = cate, product = prod)


if __name__ == '__main__':
    with app.app_context():
        app.run(debug = True)