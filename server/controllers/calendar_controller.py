from flask import Flask, render_template, request, redirect, jsonify
from flask import Blueprint
from models.cal_sneaker import CalSneaker
import repositories.cal_sneaker_repository as cal_sneaker_repository
import repositories.brand_repository as brand_repository

sneakerbox_blueprint = Blueprint("sneakers", __name__)

@sneakerbox_blueprint.route("/calendar")
def sneakers():
    cal_sneakers = cal_sneaker_repository.select_all()
    sneakers_serialised = []
    for cal_sneaker in cal_sneakers: 
        sneakers_serialised.append(cal_sneaker.serialise())
    return sneakers_serialised


@sneakerbox_blueprint.route("/calendar/new", methods=['GET'])
def new_sneaker():
    brands = brand_repository.select_all()
    brands_serialised = []
    for brand in brands: 
        brands_serialised.append(brand.serialise())
    return brands_serialised

@sneakerbox_blueprint.route("/calendar", methods=['POST'])
def create_sneaker():
    model       = request.json['model']
    brand_id    = request.json['brand_id']
    date       = request.json['date']
    image_url   = request.json['image_url']
    brand       = brand_repository.select(brand_id)
    cal_sneaker     = CalSneaker(brand, model, date, image_url)
    cal_sneaker_repository.save(cal_sneaker)
    return cal_sneaker.serialise()