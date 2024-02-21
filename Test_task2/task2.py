def sqrt(num):
    return num*num

def cos_distance(vector1, vector2):
    if len(vector1) != len(vector2):
        print("Разная длина векторов")
        return

    scale = sum(x * y for x, y in zip(vector1, vector2))
    vector1_length = sqrt(sum(x ** 2 for x in vector1))
    vector2_length = sqrt(sum(y ** 2 for y in vector2))

    if vector1_length == 0 or vector2_length == 0:
        print("Нулевой вектор")
        return

    return scale / (vector1_length * vector2_length)