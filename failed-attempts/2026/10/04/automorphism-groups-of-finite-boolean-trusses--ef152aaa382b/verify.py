import itertools
import math

def elements(r, gmod, hmod):
    ps = list(itertools.product(range(2), repeat=r)) if r else [()]
    gs = list(range(gmod))
    hs = list(range(hmod))
    return [(p, g, h) for p in ps for g in gs for h in hs]

def heap(a, b, c, gmod, hmod):
    p = tuple((x - y + z) % 2 for x, y, z in zip(a[0], b[0], c[0]))
    return (p, (a[1] - b[1] + c[1]) % gmod,
            (a[2] - b[2] + c[2]) % hmod)

def mult(a, b, gmod, hmod):
    p = tuple(x * y for x, y in zip(a[0], b[0]))
    return (p, a[1] % gmod, b[2] % hmod)

def brute_count(r, gmod, hmod):
    es = elements(r, gmod, hmod)
    n = len(es)
    index = {x: i for i, x in enumerate(es)}
    heaps = [[[index[heap(es[i], es[j], es[k], gmod, hmod)]
               for k in range(n)] for j in range(n)] for i in range(n)]
    prods = [[index[mult(es[i], es[j], gmod, hmod)]
              for j in range(n)] for i in range(n)]
    count = 0
    for perm in itertools.permutations(range(n)):
        ok = True
        for i in range(n):
            for j in range(n):
                if perm[prods[i][j]] != prods[perm[i]][perm[j]]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            continue
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if perm[heaps[i][j][k]] != heaps[perm[i]][perm[j]][perm[k]]:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break
        if ok:
            count += 1
    return count

def aut_cyclic(n):
    return sum(1 for a in range(n) if math.gcd(a, n) == 1)

def predicted(r, gmod, hmod):
    return math.factorial(r) * gmod * aut_cyclic(gmod) * hmod * aut_cyclic(hmod)

cases = [
    (1, 2, 1),
    (2, 1, 1),
    (0, 3, 1),
    (0, 2, 2),
    (1, 2, 2),
]
for case in cases:
    got = brute_count(*case)
    want = predicted(*case)
    print(case, got, want)
    assert got == want
print("CHECK_OK")
