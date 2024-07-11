def max_distance_to_nearest(seats, current):
    n = len(seats)
    max_distance = 0

    # Находим максимальное расстояние до ближайшего занятого места
    for j in range(current + 1, n):
        if seats[j] == 1 or j == n - 1:
            max_distance = max(max_distance, j - current - 1)

    for j in range(current + 1, n, -1):
        if seats[j] == 1 or j == 0:
            max_distance = max(max_distance, j - current - 1)

    return max_distance
