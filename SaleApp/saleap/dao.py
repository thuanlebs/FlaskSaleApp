import json

def load_categories():
    with open('Data/categories.json', encoding='utf-8') as f:
        return  json.load(f)


def load_product(kw = None, categories_id = None):
    with open('Data/product.json', encoding='utf-8') as f:
        product = json.load(f)


        if kw:
            product = [kw for kw in product if kw['name'].find(kw) >=0]

        if categories_id:
            product = [kw for kw in product if kw[categories_id] == (int(categories_id))]

        return product


if __name__ == '__main__':
    print (load_categories())

