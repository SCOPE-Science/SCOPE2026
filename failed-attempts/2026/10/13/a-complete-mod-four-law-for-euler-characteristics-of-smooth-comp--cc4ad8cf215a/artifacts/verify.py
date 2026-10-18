from itertools import combinations_with_replacement
from math import comb, prod

def euler_ci(n, degrees):
    c = len(degrees)
    series = [comb(n + c + 1, k) for k in range(n + 1)]
    for d in degrees:
        inv = [(-d) ** k for k in range(n + 1)]
        nxt = [0] * (n + 1)
        for i, a in enumerate(series):
            for j, b in enumerate(inv):
                if i + j <= n:
                    nxt[i + j] += a * b
        series = nxt
    return prod(degrees) * series[n]

def v2(n):
    n = abs(n)
    if n == 0:
        return 10**9
    out = 0
    while n % 2 == 0:
        out += 1
        n //= 2
    return out

def predicted_mod4(n, degrees):
    even = [d for d in degrees if d % 2 == 0]
    if len(even) >= 2 or any(d % 4 == 0 for d in even):
        return 0

    if len(even) == 1:
        assert even[0] % 4 == 2
        return 2 if n % 4 in (0, 1) else 0

    f = sum(d % 4 == 3 for d in degrees)
    return (((-1) ** f) * (n + 1 + 2 * f * n)) % 4

checks = odd_checks = layer_checks = 0
for n in range(1, 13):
    for c in range(1, 5):
        for degrees in combinations_with_replacement(range(2, 10), c):
            chi = euler_ci(n, degrees)
            assert chi % 4 == predicted_mod4(n, degrees), (n, degrees, chi)

            predicted_odd = (n % 2 == 0 and all(d % 2 == 1 for d in degrees))
            assert (chi % 2 == 1) == predicted_odd

            f = sum(d % 4 == 3 for d in degrees)
            branch_a = (
                sum(d % 2 == 0 for d in degrees) == 1
                and all(d % 4 != 0 for d in degrees)
                and n % 4 in (0, 1)
            )
            branch_b = (
                all(d % 2 == 1 for d in degrees)
                and n % 2 == 1
                and (((n + 1) // 2 + f) % 2 == 1)
            )
            assert (v2(chi) == 1) == (branch_a or branch_b), (n, degrees, chi)

            checks += 1
            odd_checks += 1
            layer_checks += 1

print("VERIFY_OK", checks, odd_checks, layer_checks)
