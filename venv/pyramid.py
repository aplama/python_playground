def pyramid(n):

    spaces = n - 1
    hashes = n - spaces

    while spaces >= 0:
        print(" "*spaces + "#" * hashes)
        spaces -= 1
        hashes = n - spaces


pyramid(6)
