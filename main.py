from fastapi import FastAPI
from Square import Point
from CSV_dispatcher import get_business_objects, get_count_business,\
    get_sum_business, local_get_buy_count, local_get_buyers_count, full_statistic


app = FastAPI()


# {'Аптеки и фармацевтика': 0, 'Продукты питания': 1, 'Одежда, обувь, аксессуары': 2}


@app.get('/get_objects_by_tag')
def get_objects_by_tag(tag: str = 'Одежда, обувь, аксессуары',
                       point_1_lat: float = 46.942035,
                       point_1_lon: float = 142.745165,
                       point_2_lat: float = 46.952035,
                       point_2_lon: float = 142.756165):

    point_1 = Point(point_1_lat, point_1_lon)
    point_2 = Point(point_2_lat, point_2_lon)
    info = get_business_objects(tag, point_1, point_2)

    return info


@app.get('/get_sum_transactions')
def get_sum_transactions(tag: str = 'Одежда, обувь, аксессуары',
                         point_1_lat: float = 46.942035,
                         point_1_lon: float = 142.745165,
                         point_2_lat: float = 46.952035,
                         point_2_lon: float = 142.756165):

    point_1 = Point(point_1_lat, point_1_lon)
    point_2 = Point(point_2_lat, point_2_lon)
    info = get_sum_business(tag, point_1, point_2)

    return info


@app.get('/get_count_transactions')
def get_count_transactions(tag: str = 'Одежда, обувь, аксессуары',
                           point_1_lat: float = 46.942035,
                           point_1_lon: float = 142.745165,
                           point_2_lat: float = 46.952035,
                           point_2_lon: float = 142.756165):

    point_1 = Point(point_1_lat, point_1_lon)
    point_2 = Point(point_2_lat, point_2_lon)
    info = get_count_business(tag, point_1, point_2)

    return info


@app.get('/get_local_buy_count')
def get_local_buy_count(tag: str = 'Одежда, обувь, аксессуары',
                        point_1_lat: float = 46.942035,
                        point_1_lon: float = 142.745165,
                        point_2_lat: float = 46.952035,
                        point_2_lon: float = 142.756165):

    point_1 = Point(point_1_lat, point_1_lon)
    point_2 = Point(point_2_lat, point_2_lon)
    info = local_get_buy_count(tag, point_1, point_2)

    return info


@app.get('/get_local_buyers_count')
def get_local_buyers_count(tag: str = 'Одежда, обувь, аксессуары',
                           point_1_lat: float = 46.942035,
                           point_1_lon: float = 142.745165,
                           point_2_lat: float = 46.952035,
                           point_2_lon: float = 142.756165):

    point_1 = Point(point_1_lat, point_1_lon)
    point_2 = Point(point_2_lat, point_2_lon)
    info = local_get_buyers_count(tag, point_1, point_2)

    return info


@app.get('/get_full_statistic')
def get_full_statistic(tag: str = 'Одежда, обувь, аксессуары',
                       point_1_lat: float = 46.942035,
                       point_1_lon: float = 142.745165,
                       point_2_lat: float = 46.952035,
                       point_2_lon: float = 142.756165):

    point_1 = Point(point_1_lat, point_1_lon)
    point_2 = Point(point_2_lat, point_2_lon)
    info = full_statistic(tag, point_1, point_2)

    return info


