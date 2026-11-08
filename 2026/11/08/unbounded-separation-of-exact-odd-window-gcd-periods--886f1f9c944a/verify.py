"""Independent exact arithmetic checks for the odd-prime Lucas-window theorem."""
from math import gcd


def fibonacci(n):
    f0, f1 = 0, 1
    for _ in range(n):
        f0, f1 = f1, f0 + f1
    return f0


def lucas(n):
    return fibonacci(n - 1) + fibonacci(n + 1)


def prime(n):
    return n > 1 and all(n % t for t in range(2, int(n ** .5) + 1))


def window_gcd(seq, power, k, windows):
    terms = [x ** power for x in seq]
    sm = sum(terms[1:k + 1])
    acc = 0
    for n in range(windows):
        acc = gcd(acc, sm)
        sm += terms[n + k + 1] - terms[n + 1]
    return acc


def check():
    counts = 0
    max_k = 0
    prime_count = 0
    for h in range(5, 44):
        if not prime(h):
            continue
        prime_count += 1
        a, b = fibonacci(h), -(fibonacci(h - 1) + 1)
        ell = lucas(h)
        assert b*b - a*b - a*a == ell
        assert ell % 2 == 1 and ell % 3 != 0
        assert gcd(a,b) == 1
        kmax = 6*h + 3
        g = [a,b]
        for _ in range(kmax + 12):
            g.append(g[-1] + g[-2])
        for k in range(1, kmax + 1, 2):
            target1 = 2 if k % 3 == 0 else 1
            target2 = target1 * (ell if k % h == 0 else 1)
            # Independently evaluate the GCD over 8 consecutive windows.
            # Since term sums of squares satisfy an order-3 recurrence,
            # this is enough to identify their infinite GCD.
            actual1 = window_gcd(g, 1, k, 8)
            actual2 = window_gcd(g, 2, k, 8)
            assert actual1 == target1, (h,k,'linear',actual1,target1)
            assert actual2 == target2, (h,k,'squared',actual2,target2)
            counts += 1
            max_k = max(max_k,k)
        # Exact antipodal identity modulo the Lucas number.
        x,y=a,b
        for _ in range(h):
            x,y=y,x+y
        assert x % ell == (-a) % ell
        assert y % ell == (-b) % ell
    print(f'VERIFY_OK primes={prime_count} tested_odd_window_lengths={counts} largest_k={max_k}')


if __name__ == '__main__':
    check()
