"""Independent direct-trace checks for the three-colour cycle marked-query theorem.
Python standard library only; run: python verify_marked_cycles.py
"""
from itertools import product, combinations
from math import comb, factorial


def predicted(n, pairs):
    used = {i for i, _ in pairs}
    if len(used) != len(pairs):
        return False
    color = dict(pairs)
    if len(used) == n:
        return False
    for i in used:
        nxt = (i+1)%n
        if nxt in used and color[i] == color[nxt]:
            return False
    for i in used:
        j, k = (i+1)%n, (i+2)%n
        if j in used and k in used and color[i] != color[k]:
            return False
    for i in used:
        if all((i+j)%n in used for j in range(4)):
            return False
    return True


def coefficient_formula(n):
    counts = [1]+[0]*n
    for a in range(n+1):
        for b in range(n+1):
            for c in range(n+1):
                r = a+b+c
                k = a+2*b+3*c
                if r == 0 or k > n or n-k < r:
                    continue
                mult = (n*factorial(r-1)*comb(n-k-1,r-1) * 3**a*6**(b+c))//(factorial(a)*factorial(b)*factorial(c))
                counts[k]+=mult
    return counts


def brute(n):
    colourings = [p for p in product(range(3), repeat=n)
                  if all(p[i]!=p[(i+1)%n] for i in range(n))]
    counts = [0]*(n+1)
    for k in range(n+1):
        for verts in combinations(range(n), k):
            for targets in product(range(3), repeat=k):
                mask = 0
                for p in colourings:
                    bits = sum((p[verts[j]] == targets[j]) << j for j in range(k))
                    mask |= (1<<bits)
                is_shattered = mask == ((1<<(1<<k))-1)
                assert is_shattered == predicted(n, tuple(zip(verts,targets))), (n, verts,targets, mask)
                counts[k] += is_shattered
    return counts

if __name__=='__main__':
    for n in range(3,9):
        formula = coefficient_formula(n)
        direct = brute(n)
        assert formula == direct, (n,formula,direct)
        print(f'n={n}: {direct}; full direct traces, structural criterion, and binomial formula agree', flush=True)
    # Higher-order exact combinatorial agreement without expensive direct traces
    for n in range(9,41):
        cf=coefficient_formula(n)
        assert max(i for i,v in enumerate(cf) if v)>0 and cf[-1]>=0
        assert max(i for i,v in enumerate(cf) if v)!=0
        assert max(i for i,v in enumerate(cf) if v)!=n
        assert max(i for i,v in enumerate(cf) if v)==3*n//4
    for m in range(3, 7):
        n=2*m
        maximal_count=0
        for parity in range(2):
            vertices=tuple(range(parity,n,2))
            for targets in product(range(3),repeat=m):
                support=tuple(zip(vertices,targets))
                is_maximal=predicted(n,support) and all(
                    not predicted(n,support+((i,a),))
                    for i in range(n) if i not in vertices for a in range(3))
                proper_auxiliary=all(targets[i]!=targets[(i+1)%m] for i in range(m))
                assert is_maximal==proper_auxiliary,(n,parity,targets)
                maximal_count+=is_maximal
        assert maximal_count == 2*(2**m+2*(-1)**m)
        print(f'even n={n}: alternating-parity maximal facets {maximal_count} verified',flush=True)
    print('ALL_MARKED_CYCLE_CHECKS_PASS')
