#!/usr/bin/env python3
"""Exact small-field checks for Frobenius on a Fermat quartic 48-point scheme.
Public mathematical verification only; no external dependencies.
"""
from math import gcd


def prime(n):
    if n < 2: return False
    return all(n % d for d in range(2, int(n**0.5) + 1))


def n1_formula(q):
    g=gcd(4,q-1)
    return 3*g*g if pow((-2)%q,(q-1)//g,q)==1 else 0


def fp2_data(p):
    nsq=next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
    return nsq


def mul(a,b,p,d):
    return ((a[0]*b[0]+d*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)


def power(a,n,p,d):
    r=(1,0)
    while n:
        if n&1:r=mul(r,a,p,d)
        a=mul(a,a,p,d);n//=2
    return r


def count_fp(p):
    a4=[pow(a,4,p) for a in range(p)]
    total=0;pieces=[0,0,0]
    for y in range(1,p):
        for z in range(1,p):
            if (1+a4[y]+a4[z])%p==0:
                flags=(a4[y]==1, a4[y]==a4[z],a4[z]==1)
                if any(flags):
                    assert sum(flags)==1,(p,y,z,flags)
                    total+=1;pieces[flags.index(True)]+=1
    return total,pieces


def count_fp2(p):
    d=fp2_data(p)
    elts=[(a,b) for a in range(p) for b in range(p)]
    one=(1,0); zero=(0,0)
    powers={a:power(a,4,p,d) for a in elts}
    count=0;parts=[0,0,0]
    for y in elts:
        if y==zero:continue
        for z in elts:
            if z==zero:continue
            uy,uz=powers[y],powers[z]
            if ((1+uy[0]+uz[0])%p,(uy[1]+uz[1])%p)==zero:
                flags=(uy==one,uy==uz,uz==one)
                if any(flags):
                    assert sum(flags)==1,(p,y,z,flags)
                    count+=1;parts[flags.index(True)]+=1
    return count,parts


def expected_n2(p):
    q=p*p;g=gcd(4,q-1)
    # For z in F_p, and q=p^2, z^((q-1)/g) lies in F_p.
    return 3*g*g if pow(p-2,(q-1)//g,p)==1 else 0


def cycle_type(p):
    n1=n1_formula(p)
    n2=expected_n2(p)
    assert (48-n2)%4==0
    a1=n1;a2=(n2-n1)//2;a4=(48-n2)//4
    assert a1+2*a2+4*a4==48
    return (a1,a2,a4)


def main():
    hits={}
    for p in range(11,200):
        if not prime(p):continue
        a, parts=count_fp(p)
        assert a==n1_formula(p),(p,a,n1_formula(p))
        assert parts==[a//3]*3,(p,parts)
        typ=cycle_type(p)
        hits.setdefault(typ,[]).append(p)
        if p in (11,13,17,19,23):
            b, parts2=count_fp2(p)
            assert b==expected_n2(p),(p,b,expected_n2(p))
            assert parts2==[b//3]*3,(p,parts2)
    assert set(hits)=={(48,0,0),(0,24,0),(12,18,0),(0,0,12)},hits
    for k,v in sorted(hits.items()):print(f'Frobenius cycles {k}: sample prime {v[0]}, tested {len(v)} primes')
    print('ALL_FINITE_FIELD_CHECKS_OK')

if __name__=='__main__':main()
