"""Exhaustive original-identity checks for rank-at-most-one Rota--Baxter systems.

Only standard Python is required. Field GF(4) uses polynomial X^2+X+1.
"""
from collections import Counter
from itertools import product
import sys


def field(q):
    if q in (2, 3, 5):
        return (lambda a, b: (a + b) % q), (lambda a, b: (a*b) % q)
    if q == 4:
        def mul(a, b):
            v = 0
            for i in range(2):
                if (b >> i) & 1:
                    v ^= a << i
            if v & 8: v ^= 0b1100
            if v & 4: v ^= 0b111
            return v
        return (lambda a, b: a ^ b), mul
    raise ValueError(q)


def normalized_lines(q, n, mul):
    out = []
    # Normalize first nonzero coordinate of each line to 1.
    for u in product(range(q), repeat=n):
        if not any(u): continue
        first = next(x for x in u if x)
        inv = next(x for x in range(1,q) if mul(first,x) == 1)
        v = tuple(mul(t, inv) for t in u)
        if v not in out: out.append(v)
    return out


def map_records(q, n, mul):
    lines=normalized_lines(q,n,mul)
    z=tuple(0 for _ in range(n))
    maps=[(z,z,tuple(z for _ in range(n)))]
    for u in lines:
        for phi in product(range(q), repeat=n):
            if not any(phi): continue
            cols=tuple(tuple(mul(c,phi[j]) for c in u) for j in range(n))
            maps.append((u,phi,cols))
    return maps


def original_equations(R,S,add,mul,n):
    rc=R[2]; sc=S[2]
    z=tuple(0 for _ in range(n))
    def plus(a,b): return tuple(add(a[j],b[j]) for j in range(n))
    def prod(a,b):
        r=[mul(a[0],b[0])]+[add(mul(a[0],b[j]),mul(b[0],a[j])) for j in range(1,n)]
        return tuple(r)
    def apply(cols,x):
        s=list(z)
        for j in range(n):
            if x[j]:
                for t in range(n): s[t]=add(s[t],mul(x[j],cols[j][t]))
        return tuple(s)
    for i in range(n):
        for j in range(n):
            t=plus(prod(rc[i],tuple(1 if z==j else 0 for z in range(n))),
                   prod(tuple(1 if z==i else 0 for z in range(n)),sc[j]))
            if prod(rc[i],rc[j]) != apply(rc,t): return False
            if prod(sc[i],sc[j]) != apply(sc,t): return False
    return True


def expected(q,m):
    L=(q**m-1)//(q-1)
    return {"zero_zero":1,
            "one_zero":q**(m+1)-1+L*(q**m-1),
            "zero_one":q**(m+1)-1+L*(q**m-1),
            "scalar_radical":q**m*(q**m-1),
            "radical_scalar":q**m*(q**m-1),
            "radical_radical_same":L*(q**m-1)**2,
            "radical_radical_distinct":L*(L-1)*(q**(m-1)-1)**2}


def typ(R,S):
    if not any(R[0]) and not any(S[0]): return 'zero_zero'
    if not any(S[0]): return 'one_zero'
    if not any(R[0]): return 'zero_one'
    if R[0][0]:
        assert not S[0][0]
        return 'scalar_radical'
    if S[0][0]: return 'radical_scalar'
    return 'radical_radical_same' if R[0] == S[0] else 'radical_radical_distinct'


def run(q,m):
    n=m+1
    add,mul=field(q)
    maps=map_records(q,n,mul)
    got=Counter()
    for R in maps:
        for S in maps:
            if original_equations(R,S,add,mul,n):
                got[typ(R,S)]+=1
    want=expected(q,m)
    assert all(got[k] == v for k,v in want.items()) and set(got)<=set(want), (q,m,dict(got),want)
    print(f'q={q} m={m} maps={len(maps)} pairs={len(maps)**2} accepted={sum(got.values())}')
    for k,v in want.items(): print(f'  {k}: {v}')

if __name__=='__main__':
    for a in sys.argv[1:]:
        q,m=map(int,a.split(':'))
        run(q,m)
    print('ROTA_BAXTER_SYSTEM_RANK_ONE_ORIGINAL_IDENTITIES_OK')
