def get_distance_between(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

def bfs(start_key, finish_key, keys_count, fn_check_edge_exist):
    visited = set()
    queue = [(start_key, 0)]
    visited.add(start_key)

    while queue:
        current_key, count = queue.pop(0)

        if current_key == finish_key:
            return count

        for key in range(keys_count):
            # Вместо графа используем простой цикл, т.к. "Дороги есть между всеми парами городов."
            if key not in visited and fn_check_edge_exist(current_key, key):
                queue.append((key, count + 1))
                visited.add(key)

    return -1

def input_processing(lines):
    city_n = int(lines[0])  # (2 ≤ n ≤ 1000)
    cities_xy = [list(map(int, line.split())) for line in lines[1:city_n + 1]]

    max_distance = int(lines[city_n + 1])  # >= 1
    from_city_index, to_city_index = map(lambda x: int(x) - 1, lines[city_n + 2].split())  # >= 1

    if from_city_index == to_city_index:
        return 0

    return bfs(
        from_city_index,
        to_city_index,
        city_n,
        lambda key_a, key_b: get_distance_between(cities_xy[key_a], cities_xy[key_b]) <= max_distance
    )

def get_input(n):
    lines = [n]
    for _ in range(n+2):
        lines.append(input())

    return input_processing(lines)

print(get_input(int(input())))