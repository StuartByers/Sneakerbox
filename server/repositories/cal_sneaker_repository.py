from db.run_sql import run_sql

from models.cal_sneaker import CalSneaker
from models.brand import Brand
import repositories.brand_repository as brand_repository


def save(cal_sneaker):
    sql = "INSERT INTO cal_sneakers (brand_id, model, date, image_url) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [ cal_sneaker.brand.id, cal_sneaker.model, cal_sneaker.date, cal_sneaker.image_url]
    results = run_sql(sql, values)
    id = results[0]['id']
    cal_sneaker.id = id
    return cal_sneaker


def select_all():
   
    cal_sneakers = []

    sql = "SELECT * FROM cal_sneakers"
    results = run_sql(sql)

    for row in results:
        brand = brand_repository.select(row['brand_id'])
        cal_sneaker = CalSneaker(brand, row['model'], row['date'], row['image_url'], row['id'])
        cal_sneakers.append(cal_sneaker)
    return cal_sneakers


def select(id):
    cal_sneaker = None
    sql = "SELECT * FROM cal_sneakers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        brand = brand_repository.select(result['brand_id'])
        cal_sneaker = CalSneaker(brand, result['model'], result['date'], result['image_url'], result['id'])
    return cal_sneaker


def delete_all():
    sql = "DELETE FROM cal_sneakers"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM cal_sneakers WHERE id = %s"
    values = [id]
    run_sql(sql, values)