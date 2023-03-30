

def diagonal_sum():
    m = [[8, 14, -6], [12, 7, 4], [-11, 3, 21]]

    m_size = len(m)
    position_left = 0
    position_right = m_size

    left_sum = 0
    right_sum = 0

    for i in range(m_size):
        left_sum = left_sum + m[i][position_left]
        position_left = position_left + 1

    for j in range(m_size):
        right_sum = right_sum + m[j][position_right-1]
        position_right = position_right - 1

    absolute_difference = abs(left_sum - right_sum)

    print(absolute_difference)


diagonal_sum()


