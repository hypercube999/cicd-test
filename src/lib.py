import numpy as np

# Назовем функциию неправильно, чтобы показать, как работает анализатор кода
def ReverseArray(arr: np.array):
    arr = arr.copy()
    arr_len = len(arr)
    for i in range(arr_len // 2):
        arr[i], arr[arr_len - 1 - i] = arr[arr_len - 1 - i], arr[i]
    return arr
