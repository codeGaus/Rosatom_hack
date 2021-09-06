import math


class Point(object):
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude


class Vector(object):
    def __init__(self, x: Point, y: Point):
        self.x = x
        self.y = y


def square_corner(center: Point, size: float, i: float, baseVector: Vector):
    angle_deg = 90 * i + 45
    angle_rad = math.pi / 180 * angle_deg
    return Point(center.latitude + size*baseVector.y * math.cos(angle_rad),
                  center.longitude + size*baseVector.x * math.sin(angle_rad))


def square(center: Point, size: float, baseVector: Vector):
    return [
        square_corner(center, size, 0, baseVector),
        square_corner(center, size, 1, baseVector),
        square_corner(center, size, 2, baseVector),
        square_corner(center, size, 3, baseVector),
        square_corner(center, size, 4, baseVector)
    ]


# брать окражность с радиусом равным 1/2 * (a*a + b*b)**0.5