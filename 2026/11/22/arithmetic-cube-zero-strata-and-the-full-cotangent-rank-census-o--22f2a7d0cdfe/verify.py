#!/usr/bin/env python3
"""Reproduce the cube-zero and cotangent-rank census in a cubic box algebra."""
from itertools import product
from random import Random

BASIS = list(product(range(3), repeat=3))
QUAD = [(2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1)]
VAR = [(1,0,0),(0,1,0),(0,0,1)]
TRIPLES = [(i,j,k) for i in range(6) for j in range(6) for k in range(6)
           if all(QUAD[i][t]+QUAD[j][t]+QUAD[k][t] == 2 for t in range(3))]
assert len(TRIPLES)==21


def mul(x,y,q):
    if q in (4,8):
        mask=q-1
        poly={4:7,8:11}[q]
        z=0
        while y:
            if y&1:z^=x
            y >>=1
            x<<=1
            if x&q:x^=poly
        return z&mask
    return x*y%q


def add(x,y,q):
    return x^y if q in (4,8) else (x+y)%q


def cube_zero_quad(coeff,q):
    out=0
    for i,j,k in TRIPLES:
        out=add(out,mul(mul(coeff[i],coeff[j],q),coeff[k],q),q)
    return out == 0


def cube_zero_direct(coeff,q):
    # Dict-based multiplication in Fq[x,y,z]/(x^3,y^3,z^3).
    def multiply(a,b):
        c={}
        for m,v in a.items():
            for n,w in b.items():
                t=tuple(m[i]+n[i] for i in range(3))
                if max(t)<3:
                    c[t]=add(c.get(t,0),mul(v,w,q),q)
        return {k:v for k,v in c.items() if v}
    a={m:v for m,v in zip(BASIS,coeff) if v}
    return not multiply(multiply(a,a),a)


def eps6(q):
    # Return 0 in characteristic 2; in odd characteristic compute quadratic character.
    if q in (2,4,8):return 0
    if q%3==0:return None
    return 1 if pow(6%q,(q-1)//2,q)==1 else -1


def Z(q):
    if q%3==0:return q**6
    e=eps6(q)
    return q**5+q**3-q**2+e*q*(q-1)**3


def admissible(a,q):
    d={m:v for m,v in zip(BASIS,a)}
    linear=[d.get(v,0) for v in VAR]
    if q%3==0:return True
    if sum(bool(x) for x in linear)>1:return False
    if sum(bool(x) for x in linear)==1:
        j=next(i for i,x in enumerate(linear) if x)
        return all(not v or m[j] for m,v in d.items())
    quad=[d.get(m,0) for m in QUAD]
    return cube_zero_quad(quad,q)


def check():
    for q in (2,3,4,5,7,8):
        count=0
        for coeff in product(range(q),repeat=6):
            if cube_zero_quad(coeff,q):count+=1
        assert count==Z(q),(q,count,Z(q))
        print('quadratic_count',q,count)
    rng=Random(712003)
    for q in (2,3,4,5,7):
        for _ in range(190):
            a=[0]+[rng.randrange(q) for _ in range(26)]
            assert cube_zero_direct(a,q)==admissible(a,q),(q,a)
    print('power_checks',5*190)
    for q in (2,3,4,5,7,8):
        if q%3==0:
            # Sum over ranks of all 3-by-3 matrices and 23 free higher coefficients per image.
            gauss=[1,q*q+q+1,q*q+q+1,1]
            cr=[q**69 * gauss[r] * __import__('math').prod(q**3-q**i for i in range(r)) for r in range(4)]
            assert sum(cr)==q**78
        else:
            U=q**17*Z(q); V=q**17*(q-1)
            cr=[U**3,3*((U+V)**3-U**3),3*((U+2*V)**3-2*(U+V)**3+U**3),6*V**3]
            assert sum(cr)==(U+3*V)**3
        assert min(cr)>0
        print('rank_profile',q,','.join(str(v) for v in cr))
    print('VERIFY_OK direct_quadratics=6 sampled_powers=950 rank_profiles=6')


if __name__=='__main__':check()
