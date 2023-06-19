from db.run_sql import run_sql

from models.brand import Brand
from models.cal_sneaker import CalSneaker


def save(brand):
    sql = "INSERT INTO brands (name) VALUES (%s) RETURNING *"
    values = [brand.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    brand.id = id
    return brand


def select_all():
    brands = []

    sql = "SELECT * FROM brands"
    results = run_sql(sql)

    for row in results:
        brand = Brand(row['name'], row['id'])
        brands.append(brand)
    return brands


def select(id):
    brand = None
    sql = "SELECT * FROM brands WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        brand = Brand(result['name'], result['id'])
    return brand


def delete_all():
    sql = "DELETE FROM brands"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM brands WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(brand):
    sql = "UPDATE brands SET (name) = (%s) WHERE id = %s"
    values = [brand.name, brand.id]
    run_sql(sql, values)

def cal_sneakers(brand):
    cal_sneakers = []

    sql = "SELECT * FROM cal_sneakers WHERE brand_id = %s"
    values = [brand.id]
    results = run_sql(sql, values)

    for row in results:
        cal_sneaker = cal_sneaker(row['brand_id'], row['model'], row['image_url'], row['id'] )
        cal_sneakers.append(cal_sneaker)
    return cal_sneakers