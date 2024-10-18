x = [150, 180, 170, 175, 162, 168, 190, 157, 166, 171]
y = [55, 110, 63, 81, 80, 65, 84, 62, 71, 78]


def my_mean(array):
    summa = 0
    count = 0
    for i in array:
        summa += i
        count += 1
    return summa / count


def my_var(array):  # ((x - my_mean(x)) ** 2)
    mean = my_mean(array)
    l_1 = [(i - mean) ** 2 for i in array]
    return sum(l_1) / len(x)


def my_std(array):  # my_var(x) ** 0.5
    return my_var(x) ** 0.5


def my_cov(array1, array2):  # ((x - my_mean(x)) * (y - my_mean(y))).sum() / (len(x) - 1)
    if len(array1) != len(array2):
        raise ValueError("array1 != array 2")
    l_array1 = []
    l_array2 = []
    for i, j in zip(array1, array2):
        l_array1.append(i - my_mean(array1))
        l_array2.append(j - my_mean(array2))
    multy_array = []
    for m, n in zip(l_array1, l_array2):
        multy_array.append(m * n)
    return sum(multy_array) / (len(array1))


def my_corr(array1, array2):
    return my_cov(array1, array2) / (my_std(array1) * my_std(array2))


# print(my_cov(x, y))
# print(my_mean(x))
# print(my_var(x))
# print(my_std(x))
# print(my_corr(x, y))