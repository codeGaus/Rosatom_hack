import csv
import json
import os

import numpy as np
import pandas as pd
from Square import Point


def get_data(file):
    fname = 'data/' + file
    data = pd.read_csv(fname)
    return data


# info = get_count_business('Одежда, обувь, аксессуары', Point(46.942035, 142.745165), Point(46.952035, 142.756165))

def get_business_objects(tag: int = 1,
                         point_1: Point = Point(46.942035, 142.745165),
                         point_2: Point = Point(46.952035, 142.756165),
                         data=get_data('trans.csv')):

    square_data = data[(data['Latitude'] >= point_1.latitude) & (data['Latitude'] <= point_2.latitude)
                       & (data['Longitude'] <= point_2.longitude) & (data['Longitude'] >= point_1.longitude)
                       & (data['Tag'] == tag)][['Name', 'Latitude', 'Longitude']]
    square_data = square_data.drop_duplicates(subset=['Name'])

    return square_data.to_dict(orient='records')


def get_sum_business(tag: int = 1,
                     point_1: Point = Point(46.942035, 142.745165),
                     point_2: Point = Point(46.952035, 142.756165),
                     data=get_data('trans.csv')):

    square_data = data[(data['Latitude'] >= point_1.latitude) & (data['Latitude'] <= point_2.latitude)
                       & (data['Longitude'] <= point_2.longitude) & (data['Longitude'] >= point_1.longitude)
                       & (data['Tag'] == tag)]

    return int(np.round(square_data[' sum'].sum()))


def get_count_business(tag: int = 1,
                       point_1: Point = Point(46.942035, 142.745165),
                       point_2: Point = Point(46.952035, 142.756165),
                       data=get_data('trans.csv')):

    square_data = data[(data['Latitude'] >= point_1.latitude) & (data['Latitude'] <= point_2.latitude)
                       & (data['Longitude'] <= point_2.longitude) & (data['Longitude'] >= point_1.longitude)
                       & (data['Tag'] == tag)]

    return square_data['Name'].nunique()


def local_get_buy_count(tag: int = 1,
                        point_1: Point = Point(46.942035, 142.745165),
                        point_2: Point = Point(46.952035, 142.756165),
                        data=get_data('trans.csv')):

    square_data = data[(data['Latitude'] >= point_1.latitude) & (data['Latitude'] <= point_2.latitude)
                       & (data['Longitude'] <= point_2.longitude) & (data['Longitude'] >= point_1.longitude)
                       & (data['Tag'] == tag)]

    return square_data.shape[0]


def local_get_buyers_count(tag: int = 1,
                           point_1: Point = Point(46.942035, 142.745165),
                           point_2: Point = Point(46.952035, 142.756165),
                           data=get_data('trans.csv')):

    square_data = data[(data['Latitude'] >= point_1.latitude) & (data['Latitude'] <= point_2.latitude)
                       & (data['Longitude'] <= point_2.longitude) & (data['Longitude'] >= point_1.longitude)
                       & (data['Tag'] == tag)]

    return square_data['card_id'].nunique()


def full_statistic(tag: int = 1,
                   point_1: Point = Point(46.942035, 142.745165),
                   point_2: Point = Point(46.952035, 142.756165),
                   data=get_data('trans.csv')):

    value1 = get_business_objects(tag, point_1, point_2, data)
    value2 = get_count_business(tag, point_1, point_2, data)
    value3 = get_sum_business(tag, point_1, point_2, data)
    value4 = local_get_buy_count(tag, point_1, point_2, data)
    value5 = local_get_buyers_count(tag, point_1, point_2, data)

    return {'objects_in_square': value1, 'count_objects': value2,
            'transactions_sum': value3, 'transaction_count': value4,
            'buyers_count': value5}


def sum_population(data):
    s = 0
    for index in list(data.index.values):
        if data['humans'][index] != 'Нет' and pd.isnull(data['humans'][index]) == False:
            s += data['humans'][index]
    return s


# Это функция, которая считает индекс квадрата. Сюда передаются стандартные данные,
# но вместе с этим словарь коэффициентов вида
# (тэг_статистики : (коэф_важности, нужное число))
# (ЕСЛИ НЕ ТАК, ТО НАДО БУДЕТ РАБОТУ С КОЭФАМИ МЕНЯТЬ)
# коэф_важности может принимать [0, 0.5, 1]
def square_business_index(tag, point_1, point_2, coefs, data=get_data('trans.csv'), houses=get_data('house.csv')):
    meter_lat = 0.00000911
    meter_long = 0.00000911 * 1.5
    square_data = data[(data['Latitude'] >= point_1.latitude - meter_lat * 300) & (
                data['Latitude'] <= point_2.latitude + meter_lat * 300)
                       & (data['Longitude'] <= point_2.longitude + meter_long * 300) & (
                                   data['Longitude'] >= point_1.longitude - meter_long * 300)
                       & (data['Tag'] == tag)]
    houses = houses[
        (houses['lat'] >= point_1.latitude - meter_lat * 300) & (houses['lat'] <= point_2.latitude + meter_lat * 300)
        & (houses['lon'] <= point_2.longitude + meter_long * 300) & (
                    houses['lon'] >= point_1.longitude - meter_long * 300)]

    max_index = 0
    for key in coefs.keys():
        max_index += coefs[key][0]
    green_min = 0.75 * max_index
    yellow_min = 0.5 * max_index

    objects = square_data['Name'].nunique()
    mean_unique_buyers = np.round(square_data['card_id'].nunique() / objects)
    mean_money = square_data[' sum'].sum() / objects
    population = sum_population(houses) / objects
    buys_count = square_data.shape[0] / objects

    index = (coefs[0][0] * int(coefs[0][1] < objects) + coefs[1][0] * int(coefs[1][1] > mean_unique_buyers)
             + coefs[2][0] * int(coefs[2][1] > mean_money) + coefs[3][0] * int(coefs[3][1] > population)
             + coefs[4][0] * int(coefs[4][1] > buys_count))

    if index > green_min:
        return 'green'
    elif (index > yellow_min) and (index < green_min):
        return 'yellow'
    else:
        return 'red'

