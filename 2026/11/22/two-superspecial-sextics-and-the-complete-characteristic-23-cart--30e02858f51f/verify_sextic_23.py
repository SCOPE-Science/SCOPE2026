#!/usr/bin/env python3
"""Exact characteristic-23 Cartier calculation for the symmetric smooth sextic pencil.

No external packages or network requests are required. Coefficients lie in F_23.
"""
from itertools import product
from math import factorial

P = 23
MON = [(i, j, 3-i-j) for i in range(4) for j in range(4-i)]
FAC = [factorial(i) % P for i in range(23)]
IFAC = [pow(f, -1, P) for f in FAC]


def trim(c):
    c = [x % P for x in c]
    while c and c[-1] == 0:
        c.pop()
    return c


def mul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i+j] = (out[i+j] + v*w) % P
    return trim(out)


def product_poly(fs):
    out = [1]
    for f, power in fs:
        for _ in range(power):
            out = mul(out, f)
    return out


def mod_poly(a, b):
    a = trim(a)
    b = trim(b)
    assert b
    while len(a) >= len(b):
        v = (a[-1] * pow(b[-1], -1, P)) % P
        offset = len(a)-len(b)
        for i, y in enumerate(b):
            a[offset+i] = (a[offset+i] - v*y) % P
        a = trim(a)
    return a


def gcd_poly(a, b):
    while b:
        a, b = b, mod_poly(a, b)
    return [(v*pow(a[-1], -1, P))%P for v in a]


def value(a, t):
    x=0
    for c in reversed(a): x = (x*t+c)%P
    return x


def coefficient_polynomials():
    result = {}
    for i, a in enumerate(MON):
        for j, b in enumerate(MON):
            wanted = [P*(v+1)-(w+1) for v,w in zip(a,b)]
            if any(v%3 for v in wanted):
                continue
            q = [v//3 for v in wanted]
            poly = [0]*23
            # F^22: six terms X^6,Y^6,Z^6,t X^3Y^3,t X^3Z^3,t Y^3Z^3.
            for n3 in range(23):
                for n4 in range(23-n3):
                    for n5 in range(23-n3-n4):
                        rest = [q[0]-n3-n4, q[1]-n3-n5, q[2]-n4-n5]
                        if min(rest)<0 or any(v%2 for v in rest):
                            continue
                        n0,n1,n2 = [v//2 for v in rest]
                        n = [n0,n1,n2,n3,n4,n5]
                        if sum(n)!=22:
                            continue
                        c = FAC[22]
                        for z in n: c = c * IFAC[z] % P
                        degree = n3+n4+n5
                        poly[degree] = (poly[degree] + c) % P
            if any(poly):
                result[i,j] = trim(poly)
    return result


def full_expand_specialization(t):
    # Independent coefficient extraction: multiply F_t twenty-two times.
    terms={(6,0):1, (0,6):1, (0,0):1,
           (3,3):t, (3,0):t, (0,3):t}
    p={(0,0):1}
    for _ in range(22):
        q={}
        for (a,b),c in p.items():
            for (u,v),d in terms.items():
                ij=(a+u,b+v)
                q[ij]=(q.get(ij,0)+c*d)%P
        p={k:v for k,v in q.items() if v}
    out={}
    for i,a in enumerate(MON):
        for j,b in enumerate(MON):
            exp=[P*(v+1)-(w+1) for v,w in zip(a,b)]
            coefficient=p.get(tuple(exp[:2]),0)
            if coefficient:
                out[i,j]=coefficient
    return out


def main():
    h=coefficient_polynomials()
    star_in={(0,5),(3,5),(9,5)}
    star_out={(5,0),(5,3),(5,9)}
    pairs={(1,4),(4,1),(2,6),(6,2),(7,8),(8,7)}
    assert set(h)==star_in|star_out|pairs
    A=h[0,5]; B=h[5,0]; U=h[1,4]
    assert all(h[k]==A for k in star_in)
    assert all(h[k]==B for k in star_out)
    assert all(h[k]==U for k in pairs)
    Q=product_poly([([4,1],1),([10,1],1),([-11,1],1),([-9,1],1),
                    ([-5,1],1),([-9,3,1],1),([-1,8,1],1)])
    R=product_poly([([8,1],1),([10,1],1),([11,1],1),([-4,1],1),([2,2,1],1)])
    expected_A=mul([0,5],mul(product_poly([([2,1],4)]),Q))
    expected_B=mul([0,5],mul(product_poly([([-2,1],12)]),Q))
    expected_U=mul([0,-1],mul(product_poly([([2,1],4),([-2,1],11)]),R))
    assert A==expected_A
    assert B==expected_B
    assert U==expected_U
    assert gcd_poly(gcd_poly(A,B),U)==[0,10,1]
    # All three quadratics are irreducible over F_23; all other roots are simple
    quadratics=[[-9,3,1],[-1,8,1],[2,2,1]]
    assert all(all(value(q,t)!=0 for t in range(P)) for q in quadratics)
    assert gcd_poly(Q,R)==[10,1]
    # Rank/Cartier a-number on F_23-rational smooth parameters.
    seen={0:[],2:[],6:[],8:[]}
    for t in range(P):
        if t in (2,P-2,P-1): continue
        a,b,u=value(A,t),value(B,t),value(U,t)
        assert (a==0)==(b==0)
        rank=(2 if a!=0 else 0)+(6 if u!=0 else 0)
        seen[rank].append(t)
        full=full_expand_specialization(t) if t in [0,1,4,5,13] else None
        if full is not None:
            assert {k:value(v,t) for k,v in h.items() if value(v,t)}==full
    assert seen[0]==[0,13]
    assert seen[2]==[4,12,15]
    assert seen[6]==[5,9,11,19]
    assert len(seen[8])==11
    # Over algebraic closure: two common roots, five rank-2-only roots,
    # eight rank-6-only roots; all are distinct smooth parameters.
    assert [len(trim(Q))-1,len(trim(R))-1]==[9,6]
    assert len(seen[0])+len(seen[2])+len(seen[6])+len(seen[8])==20
    # Independent finite field point count consistency at superspecial values.
    for t in (0,13):
        affine=sum((x**6+y**6+1+t*(x**3*y**3+y**3+x**3))%P==0
                    for x in range(P) for y in range(P))
        infinity=sum((1+y**6+t*y**3)%P==0 for y in range(P))
        assert affine+infinity==24
    print('VERIFIED_P23_SUPERSPECIAL_2_RANK2_5_RANK6_8_GENERIC_RANK8')
    print('RATIONAL_PROFILE:',{rank:members for rank,members in seen.items()})
    print('COMMON_CARTIER_ZERO_POLYNOMIAL:t(t+10)')


if __name__=='__main__':
    main()
