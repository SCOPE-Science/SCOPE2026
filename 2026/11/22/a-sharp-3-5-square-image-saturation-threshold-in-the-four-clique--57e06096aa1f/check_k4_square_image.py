#!/usr/bin/env python3
"""Exact finite-field certificate for squares in the K4 graph evolution algebra.

Uses only Python's standard library.  Elements of F_(3^r) are base-3 digit
vectors, and each selected defining polynomial is checked for irreducibility.
The bitset tests all q^3 target coordinates of the derived hyperplane.
"""
from itertools import product

MODULI = {
    1: (0, 1),               # x
    2: (1, 0, 1),            # x^2+1
    3: (1, 0, 2, 1),         # x^3+2x^2+1
    4: (1, 0, 1, 1, 1),      # x^4+x^3+x^2+1
    5: (1, 0, 0, 0, 2, 1),   # x^5+2x^4+1
}

def remainder(p, d):
    r = list(p)
    while len(r) >= len(d):
        a = r[-1] % 3
        if a:
            start = len(r)-len(d)
            for i,di in enumerate(d):
                r[start+i] = (r[start+i]-a*di)%3
        r.pop()
    return r

def irreducible(p):
    n=len(p)-1
    for k in range(1,n//2+1):
        for low in product(range(3),repeat=k):
            d=tuple(low)+(1,)
            if not any(remainder(p,d)):
                return False
    return True

def field(q_degree):
    r=q_degree
    q=3**r
    p=MODULI[r]
    assert irreducible(p), (r,p)
    digits = [tuple((a//(3**j))%3 for j in range(r)) for a in range(q)]
    place = [3**j for j in range(r)]
    add=[[sum(((a[j]+b[j])%3)*place[j] for j in range(r)) for b in digits] for a in digits]
    neg=[sum((-a[j]%3)*place[j] for j in range(r)) for a in digits]
    def times(a,b):
        u=digits[a];v=digits[b]
        c=[0]*(2*r-1)
        for i in range(r):
            for j in range(r):c[i+j]=(c[i+j]+u[i]*v[j])%3
        for k in range(2*r-2,r-1,-1):
            z=c[k]
            for j in range(r):c[k-r+j]=(c[k-r+j]-z*p[j])%3
        return sum(c[j]*place[j] for j in range(r))
    sq={times(a,a) for a in range(q)}
    assert len(sq)==(q+1)//2
    return q,add,neg,sq

def certificate(r):
    q,add,neg,sq=field(r)
    masks=[]
    for y in range(q):
        ny=neg[y]
        mask=sum(1<<t for t in range(q) if add[t][ny] in sq)
        masks.append(mask)
    missing=0
    witness=None
    for a in range(q):
        Aa=add[a];ma=masks[a]
        for b in range(q):
            ab=Aa[b];mab=ma&masks[b];Aab=add[ab]
            for c in range(q):
                d=neg[Aab[c]]
                if not (mab & masks[c] & masks[d]):
                    missing += 1
                    if witness is None:witness=(a,b,c,d)
    print(f'q={q} irreducible_modulus={MODULI[r]} target_count={q**3} missing={missing} image={q**3-missing} example_missing={witness}')
    return missing

if __name__=='__main__':
    expected={1:12,2:240,3:1248,4:240,5:0}
    for r,deficit in expected.items():
        observed=certificate(r)
        assert observed==deficit,(r,observed,deficit)
    # A separate direct square-coordinate enumeration checks the three smallest fields.
    for r in (1,2,3):
        q,add,neg,squares=field(r)
        images=set()
        for s in product(squares, repeat=4):
            t=add[add[s[0]][s[1]]][add[s[2]][s[3]]]
            images.add(tuple(add[t][neg[v]] for v in s))
        assert len(images)==q**3-expected[r]
        print(f'direct_coordinate_squares_q={q} image={len(images)} MATCH')
    print('ALL EXACT CERTIFICATES PASSED')
