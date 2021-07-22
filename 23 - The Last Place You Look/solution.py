def return_range_list(x, y, r, range_list=[]):
    if r > 0:
        range_list.extend(return_range_list(x - 1, y, r - 1))
        range_list.extend(return_range_list(x + 1, y, r - 1))
        range_list.extend(return_range_list(x, y - 1, r - 1))
        range_list.extend(return_range_list(x, y + 1, r - 1))
    else:
        range_list.append((x, y))
    return range_list

for _ in range(int(input())):
    line = input()
    x1, y1, r1, x2, y2, r2, x3, y3, r3 = list(map(int, line.split()))

    range_list_1 = return_range_list(x1, y1, r1)
    # range_list_1 = return_range_list(0, 0, 2)

    print(range_list_1)