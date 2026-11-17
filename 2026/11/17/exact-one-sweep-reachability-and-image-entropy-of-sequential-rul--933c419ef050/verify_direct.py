"""Independent Rule 30 in-place sweep and constructive inverse checks."""

def sweep(bits):
    a = list(bits)
    n = len(a)
    for i in range(n):
        a[i] = a[(i-1) % n] ^ (a[i] | a[(i+1) % n])
    return tuple(a)


def inverse_from_differences(y):
    n = len(y)
    d = [y[i-1] ^ y[i] for i in range(1, n)]
    for first in (0, 1):
        paths = {first: (first,)}
        for e in d[:-1]:
            new = {}
            for a, path in paths.items():
                for b in (0, 1):
                    if (a | b) == e and b not in new:
                        new[b] = path + (b,)
            paths = new
        for last, path in paths.items():
            if d[-1] != (last | y[0]):
                continue
            need = y[0] ^ last
            if path[0] > need:
                continue
            x0 = need
            x = (x0,) + path
            assert len(x) == n and sweep(x) == tuple(y)
            return x
    return None


def bits(k, n):
    return tuple((k >> i) & 1 for i in range(n))


def main():
    for n in range(3, 17):
        ys = {sweep(bits(x, n)) for x in range(1 << n)}
        if n <= 12:
            from_inverse = {bits(j, n) for j in range(1 << n)
                            if inverse_from_differences(bits(j, n)) is not None}
            assert ys == from_inverse, (n, len(ys), len(from_inverse))
        recurrence = [4, 8, 14, 25]
        for k in range(7, n+1):
            recurrence.append(2*recurrence[-1]-recurrence[-2]+recurrence[-3])
        assert len(ys) == recurrence[n-3], (n, len(ys), recurrence[n-3])
        print(f'n={n}: image={len(ys)} exact; inverse {"checked" if n <= 12 else "not enumerated"}')
    print('PASS: independent forward simulation, constructive inversion, and exact-count recurrence')

if __name__ == '__main__':
    main()
