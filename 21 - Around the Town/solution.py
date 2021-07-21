from math import sqrt
from typing import Union
from functools import reduce

class StopPoint:
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        self.x = x
        self.y = y
        self.city_points_cluster = []

    def get_city_points_group(self, city_points, stop_points) -> None:
        self.city_points_cluster.clear()
        for city_point in city_points:
            if city_point.is_this_stop_point_nearest(self, stop_points):
                self.city_points_cluster.append(city_point)

    def place_bus_in_cluster_center(self) -> None:
        cluster_size = len(self.city_points_cluster)
        cluster_sum_x = reduce(lambda x_sum, x: x_sum + x, [point.x for point in self.city_points_cluster])
        cluster_sum_y = reduce(lambda y_sum, y: y_sum + y, [point.y for point in self.city_points_cluster])
        self.x = round(cluster_sum_x / cluster_size, 1)
        self.y = round(cluster_sum_y / cluster_size, 1)

    def __str__(self) -> str:
        return f"{self.x} {self.y}"

class CityPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, x, y) -> float:
        return sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

    def is_this_stop_point_nearest(self, caller: StopPoint, stop_points: [StopPoint]) -> bool:
        distances = []
        for stop_point in stop_points:
            distances.append(self.get_distance(stop_point.x, stop_point.y))
        if min(distances) == self.get_distance(caller.x, caller.y):
            return True
        return False

def main():
    for _ in range(int(input())):
        number_of_city_points, number_of_stops = [int(i) for i in input().split(' ')]

        # CREATE POINTS
        city_points = []
        for _ in range(number_of_city_points):
            x, y = [int(i) for i in input().split(' ')]
            city_points.append(CityPoint(x, y))
        stop_points = []
        for _ in range(number_of_stops):
            x, y = [int(i) for i in input().split(' ')]
            stop_points.append(StopPoint(x, y))

        # OPTIMIZE STOP POINTS POSITIONS
        while True:
            old_points = [(point.x, point.y) for point in stop_points]
            for stop_point in stop_points:
                stop_point.get_city_points_group(city_points, stop_points)
                stop_point.place_bus_in_cluster_center()
            new_points = [(point.x, point.y) for point in stop_points]

            if old_points == new_points:
                break

        # PRINT OUTPUT
        for stop_point in stop_points:
            print(stop_point)

if __name__ == '__main__':
    main()
