"""Independent direct three-step dynamics check for periodic points on cycle squares."""
from itertools import product


def update(x, threshold):
    n = len(x)
    y = []
    for i, v in enumerate(x):
        if v == 1:
            y.append(2)
        elif v == 2:
            y.append(0)
        else:
            c = sum(x[(i + j) % n] == 1 for j in (-2, -1, 1, 2))
            y.append(int(c >= threshold))
    return tuple(y)


def check(n, threshold):
    count = 0
    total = 0
    for x in product(range(3), repeat=n):
        total += 1
        y = update(x, threshold)
        z = update(y, threshold)
        w = update(z, threshold)
        if w == x and y != x:
            count += 1
            if threshold == 2:
                assert n % 3 == 0
                assert all(x[i] != x[(i + 1) % n] for i in range(n))
    return count, total


def main():
    grand = 0
    for n in range(5, 12):
        out = []
        for th in (1, 2, 3):
            count, tested = check(n, th)
            if th == 2:
                assert count == (6 if n % 3 == 0 else 0)
            if th == 3:
                assert count == 0
            out.append(count)
            grand += tested
        print(f"n={n} threshold_1_2_3={out}")
    print(f"DIRECT_OK states_tested={grand}")

if __name__ == '__main__':
    main()
