"""
This is a correct implementation of mergesort
(hopefully) and is only here for reference,
do not fucking copy and paste this.
"""


def merge(left, right):
    lflen = len(left)
    rtlen = len(right)

    result = []

    i = 0
    j = 0
    while i < lflen and j < rtlen:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < lflen:
        result.append(left[i])
        i += 1
    while j < rtlen:
        result.append(right[j])
        j += 1

    return result


def mergesort(array):
    if len(array) < 2:
        return array[:]
    else:
        mid = len(array) // 2
        left = mergesort(array[:mid])
        right = mergesort(array[mid:])
        return merge(left, right)


if __name__ == '__main__':
    from random import shuffle

    array = list(range(10))
    shuffle(array)
    print(mergesort(array))