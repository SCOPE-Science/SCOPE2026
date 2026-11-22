"""Independent exhaustive check of quasinecklace counts and fixed-minimum-letter necklace counts."""
from itertools import product
from math import comb, gcd


def is_quasinecklace(w):
    a = min(w)
    if w[-1] == a:
        return all(v == a for v in w)
    ell = 0
    run = 0
    for c in w:
        run = run + 1 if c == a else 0
        ell = max(ell, run)
    if w[:ell] != (a,) * ell:
        return False
    if len(w) == ell:
        return True
    follower = w[ell]
    for j in range(1, len(w) - ell):
        if w[j:j + ell] == (a,) * ell and w[j + ell] < follower:
            return False
    return True


def is_necklace(w):
    return all(w <= w[j:] + w[:j] for j in range(1, len(w)))


def count_formula(s, r, m):
    if m == 0:
        return 1
    total = 0
    for ell in range(1, r + 1):
        for t in range(1, s + 1):
            poly = [s] * ell + [s - t + 1]
            arr = [1] + [0] * (r - ell)
            for _ in range(m - 1):
                out = [0] * len(arr)
                for i, ai in enumerate(arr):
                    for j, bj in enumerate(poly):
                        if i + j < len(arr):
                            out[i + j] += ai * bj
                arr = out
            total += arr[r - ell]
    return total


def phi(n):
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))


def neck_formula(s, r, m):
    n = r + m
    return sum(phi(d) * comb(n // d, r // d) * s ** (m // d)
               for d in range(1, gcd(r, m) + 1) if r % d == m % d == 0) // n


def test():
    cases = words = 0
    for s in range(1, 4):
        for n in range(1, 10):
            if (s+1)**n > 200000:
                continue
            qc = [0] * (n+1)
            nc = [0] * (n+1)
            for w in product(range(s + 1), repeat=n):
                if 0 not in w:
                    continue
                words += 1
                r = w.count(0)
                qc[r] += is_quasinecklace(w)
                nc[r] += is_necklace(w)
            for r in range(1, n+1):
                m=n-r
                assert qc[r] == count_formula(s,r,m), (s,r,m,qc[r],count_formula(s,r,m))
                assert nc[r] == neck_formula(s,r,m), (s,r,m,nc[r],neck_formula(s,r,m))
                cases +=1
    extra = 0
    for s in range(1, 6):
        for r in range(2, 13):
            for m in range(1, 15):
                v = count_formula(s,r,m)
                if r == 2 and m >= 2:
                    expected=s**m + (m-1)*s*(s+1)*s**(m-2)//2
                    assert v == expected
                assert v >= neck_formula(s,r,m)
                extra +=1
    print(f'PASS: {cases} exhaustive content instances, {words} words, {extra} larger arithmetic instances')
    for r in [2,3,4,6,10]:
        s=2
        asymptotic=r*sum(j**(r-1) for j in range(1,s+1))/s**r
        m=120
        numeric=count_formula(s,r,m)/neck_formula(s,r,m)
        print(f's={s} r={r}: exact ratio at m={m}: {numeric:.8f}; limit: {asymptotic:.8f}')

if __name__ == '__main__':
    test()
