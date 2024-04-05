import json


def load_categories():
    with open('D:\OU\Sof\FlaskSaleApp\SaleDemo\saleapp\data\categories.json', encoding='utf-8') as f:
        return json.load(f)
    

def load_products(q= None,cate_id= None):
    with open('D:\OU\Sof\FlaskSaleApp\SaleDemo\saleapp\data\products.json', encoding ='utf-8') as f:
        products = json.load(f)   


        if q:
            products= [p for p in products if p['name'].find(q)>=0] 

        if cate_id:
            products = [p for p in products if p['category_id'].__eq__(int(cate_id))]

        return products
    

def get_products_by_id(product_id):
    with open('D:\OU\Sof\FlaskSaleApp\SaleDemo\saleapp\data\products.json', encoding='utf-8') as f:
        products =json.load(f)
        for p in products:
            if p['id'] == product_id:
                return p
 

if __name__ == '__main__':
    print(load_categories())
