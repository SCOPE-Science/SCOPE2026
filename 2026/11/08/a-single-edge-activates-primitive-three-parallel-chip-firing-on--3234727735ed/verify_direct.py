"""Direct degree-threshold synchronous chip-firing, independent of firing-pattern proof."""
from collections import Counter
from itertools import product
from math import comb

def update(x, n):
    d = n + 1
    fires = [x[0] >= d, x[1] >= d] + [v >= 2 for v in x[2:]]
    b = sum(fires[2:]); a = int(fires[0]) + int(fires[1])
    return (x[0] + int(fires[1]) + b - d * int(fires[0]),
            x[1] + int(fires[0]) + b - d * int(fires[1]),
            *(v + a - 2 * int(f) for v, f in zip(x[2:], fires[2:])))

def expected(n):
    ans = Counter()
    for j in range(n):
        c = 6 * sum(comb(n, k) for k in range(j + 1))
        m = 2*n+1+j
        ans[m] += c
        ans[7*n+2-m] += c
    return ans

for n in range(1, 7):
    obs = Counter(); examined = 0
    for x in product(range(2*n+2), repeat=2):
        for leaf in product(range(4), repeat=n):
            a = x+leaf
            b = update(a,n); c = update(b,n); d = update(c,n)
            if d == a and b != a: obs[sum(a)] += 1
            examined += 1
    assert obs == expected(n), (n, obs, expected(n))
    print(f"n={n} checked={examined} primitive3={sum(obs.values())} support={sorted(obs)}")
print('PASS direct-simulation')
