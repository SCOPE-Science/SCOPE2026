"""Finite diagnostics for exact multi-step Lipschitz-free permutation norms.

These checks are supplemental; the general theorem is proved analytically.
"""
import itertools
import math

checks = 0


def orbit_len(f, pair):
    start = tuple(sorted(pair))
    cur = start
    seen = set()
    while cur not in seen:
        seen.add(cur)
        cur = tuple(sorted((f[cur[0]], f[cur[1]])))
    assert cur == start
    return len(seen)


def lengths_formula(n):
    if n == 2:
        return {1}
    result = set(range(1, n + 1))
    for a in range(1, n):
        for b in range(1, n - a + 1):
            result.add(math.lcm(a, b))
    return result


def B(n, k):
    return max((-k) % ell for ell in lengths_formula(n))


def construct(n, k, eps):
    assert n >= 3 and k >= 1 and B(n, k) > 0
    ell = max(lengths_formula(n), key=lambda q: (-k) % q)
    assert (-k) % ell == B(n, k)
    if ell <= n and ell >= 3:
        f = tuple(list(range(1, ell)) + [0] + list(range(ell, n)))
    else:
        found = next((a,b) for a in range(1, n) for b in range(1,n-a+1)
                     if math.lcm(a,b) == ell)
        a,b=found
        f=tuple(list(range(1,a)) + [0] + list(range(a+1,a+b)) + [a] + list(range(a+b,n)))
    pairs = list(itertools.combinations(range(n),2))
    pair = next(pair for pair in pairs if orbit_len(f,pair) == ell)
    orbit = []
    cur = pair
    for _ in range(ell):
        orbit.append(cur)
        cur = tuple(sorted((f[cur[0]],f[cur[1]])))
    assert cur == pair
    r = k % ell
    assert r > 0
    h = min(eps, 1/(ell-r))
    d = {pair:1.0 for pair in pairs}
    for j in range(r,ell):
        d[orbit[j]] = 1+(ell-j)*h
    def dst(x,y):return d[tuple(sorted((x,y)))] if x!=y else 0.0
    def power(x):
        for _ in range(k):x=f[x]
        return x
    defect = max(dst(*p) - dst(f[p[0]],f[p[1]]) for p in pairs)
    norm = max(dst(power(x),power(y))/dst(x,y) for x,y in pairs)
    assert defect <= eps+1e-10
    assert abs(norm - (1+min(1,eps*B(n,k)))) < 1e-9
    return d, f, defect, norm

# Every attainable pair-period agrees with the combinatorial formula.
for n in range(2,9):
    all_periods = set()
    for f in itertools.permutations(range(n)):
        for pair in itertools.combinations(range(n),2):
            all_periods.add(orbit_len(f,pair))
            checks+=1
    assert all_periods == lengths_formula(n), (n, all_periods, lengths_formula(n))
    checks+=1

# Sharp constructions and triangle inequalities at many times and scales.
for n in range(3,16):
    periods=lengths_formula(n)
    lcm_all=math.lcm(*range(1,n+1))
    assert all(B(n, k)==0 for k in (0,lcm_all,2*lcm_all))
    checks+=1
    L=max(periods)
    for k in range(1,min(80,lcm_all+1)):
        if 2*k<=L+1:
            assert B(n,k)==L-k
            checks+=1
        for eps in (0,0.002,0.1,0.6,2):
            if not B(n,k): continue
            d,f,defect,norm=construct(n,k,eps)
            for x,y,z in itertools.permutations(range(n),3):
                assert d[tuple(sorted((x,y)))]<=d[tuple(sorted((x,z)))]+d[tuple(sorted((z,y)))]+1e-10
                checks+=1
            checks+=1

print('MULTISTEP_FREE_PERMUTATION_DIAGNOSTIC_OK',checks)
