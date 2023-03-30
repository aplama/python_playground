def ratios():
    arr = [1, 1, 0, -1, -1]

    positive = 0
    negative = 0
    zero = 0

    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1

    print('{:.6f}'.format(positive/len(arr)))
    print('{:.6f}'.format(negative/len(arr)))
    print('{:.6f}'.format(zero/len(arr)))



ratios()
