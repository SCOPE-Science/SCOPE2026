#!/usr/bin/env python3
"""Exact integer verification for two special-linear summands over p-power rings."""
from collections import Counter
from itertools import product
import random


def det(a, q):
    return (a[0]*a[3]-a[1]*a[2]) % q


def sl2(p, k):
    q = p**k
    ans = []
    for a in range(q):
        if a % p:
            ia = pow(a, -1, q)
            for b, c in product(range(q), repeat=2):
                ans.append((a, b, c, ((1+b*c)*ia) % q))
        else:
            for b in range(q):
                if b % p:
                    ib = pow(b, -1, q)
                    for d in range(q):
                        ans.append((a, b, ((a*d-1)*ib) % q, d))
    assert len(ans) == p**(3*k-2)*(p*p-1)
    assert len(set(ans)) == len(ans)
    return ans


def val(a, p, k):
    if a == 0:
        return k
    t = 0
    while a % p == 0:
        t += 1
        a //= p
    return t


def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1


def rho(D, p, h):
    if h == 0:
        return 1
    ph = p**h
    D %= ph
    if D == 0:
        return p**(h//2)
    v = val(D, p, h)
    if v % 2:
        return 0
    s = v//2
    return 2*p**s if chi(D//(p**(2*s)),p) == 1 else 0


def predicted(S, p, k):
    j = min(val(a, p, k) for a in S)
    if j == k:
        return p**(3*k-2)*(p*p-1)
    m = k-j
    qm = p**m
    S0 = tuple((x//(p**j)) % qm for x in S)
    delta = det(S0, qm)
    if delta % p == 0:
        return p**(2*k+j-1)*(p-1)
    if j:
        return p**(2*k+j-1)*(p+chi(-delta,p))
    D = (1-4*pow(delta, -1, qm))%qm
    phi = qm-qm//p
    return phi*sum(p**(k-h)*rho(D,p,h) for h in range(k)) + qm*rho(D,p,k)


def count_by_definition(S, p, k, G):
    q = p**k
    return sum(det(tuple((S[i]-A[i]) % q for i in range(4)),q) == 1 for A in G)


def main():
    for p in (3,5,7):
        for h in range(1,5):
            for x in range(p**h):
                brute = sum((z*z-x)%(p**h)==0 for z in range(p**h))
                assert rho(x,p,h)==brute, (p,h,x)
    for p,k in ((3,2),(5,1),(3,3),(5,2)):
        q = p**k
        G = sl2(p,k)
        rng = random.Random(7343+p*100+k)
        if (p,k) in ((3,2),(5,1)):
            targets=list(product(range(q),repeat=4))
        else:
            targets=[tuple(rng.randrange(q) for _ in range(4)) for _ in range(90)]
            targets += [(0,0,0,0),(1,0,0,0),(1,0,0,1),(q//p,0,0,q//p)]
            targets += [(a,0,0,d) for a in range(min(8,q)) for d in range(min(8,q))]
        for S in targets:
            expected=predicted(S,p,k)
            observed=count_by_definition(S,p,k,G)
            assert expected==observed, (p,k,S,expected,observed)
        if (p,k)==(3,2):
            frequency=Counter(predicted(S,p,k) for S in targets)
            minimum=p**(2*k-1)*(p-1)
            multiplicity=(p-1)*(p+1)*(p*p+p+2)*p**(4*k-4)//2
            assert min(frequency)==minimum
            assert frequency[minimum]==multiplicity
            assert all(frequency[r]>0 for r in frequency)
        print(f"p={p} depth={k}: {len(targets)} targets, {len(G)} group points PASS")
    print('LOCAL_SPECIAL_LINEAR_TWO_SUM_CHECK_PASS')

if __name__ == '__main__':
    main()
