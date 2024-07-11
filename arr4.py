arr_str = ["YY", "XX", "XY", "YOX", "OOOXOOYOXO", "OOOXXOY", "XOOOO"]


def max_length(str):
    min_length = 0
    current_length = 0
    lit = ''

    for s in str:
        if lit == '' and s != "O":
            lit = s
        elif s == "O" and lit != '':
            current_length += 1
        elif s != lit and s != "O":
            current_length += 1
            if current_length < min_length or min_length == 0:
                min_length = current_length
            current_length = 0
            lit = s

    if min_length == len(str) and current_length == 0:
        return 0
    return min_length


for str in arr_str:
    print(max_length(str))