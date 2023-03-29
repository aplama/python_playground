# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def factors(n):
    for k in range(1, n+1):
        if n % k == 0:
            yield k


def fib(n):
    a = 0
    b = 1
    mark = 0
    while mark < n:
        yield a
        future = a + b
        a = b
        b = future
        mark += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
