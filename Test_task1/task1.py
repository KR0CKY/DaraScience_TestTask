def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        current = array[0]
        less = [x for x in array[1:] if x <= current]
        greater = [x for x in array[1:] if x > current]
        return quick_sort(less) + [current] + quick_sort(greater)


def arr_validate(arr):
    unique = []

    for num in arr:
        if num in unique:
            continue
        else:
            unique.append(num)

    return quick_sort(unique)