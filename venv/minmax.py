def minmax():
    arr = [1, 2, 3, 4, 5]
    minimum = min(arr)
    maximum = max(arr)

    min_sum = sum(arr) - maximum
    max_sum = sum(arr) - minimum

    print("%s %s" % (min_sum, max_sum))


minmax()
