"""Exact integer checks for finite-base type spectra of lexicographic random tournaments.

Run: python3 verify.py
Only Python's standard library is required. The proof of the all-size statements
is in RESULT.md; these checks establish the finite cutoff exhaustively.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path
import csv


def partitions(n, smallest=1):
    """All nondecreasing positive partitions of n, once each."""
    if n == 0:
        yield ()
    for a in range(smallest, n+1):
        for suffix in partitions(n-a, a):
            yield (a,) + suffix


def low_counts(parts):
    k = len(parts)
    u = 1 << k
    b = sum(1 << m for m in parts)
    c = sum(1 << (2*m) for m in parts)
    d = sum(1 << (3*m) for m in parts)
    t1 = u+b
    t2 = t1*t1+c+u*u+2*u
    t3 = (b**3 + 3*b*c + 4*d + 3*u*(b*b+c)
          + 3*b*(2*u+2*u*u) + 8*u+12*u*u+8*u**3)
    return t1,t2,t3


def multiply(A,B,R):
    C=[Fraction(0)]*(R+1)
    for i in range(min(len(A),R+1)):
        for j in range(min(len(B),R-i+1)):
            C[i+j]+=A[i]*B[j]
    return C


def egf_counts(parts,R=3):
    k=len(parts)
    W=[Fraction(0)]+[Fraction(1<<(a*(a-1)//2),factorial(a)) for a in range(1,R+1)]
    Q=[Fraction(0)]*(R+1)
    P=[Fraction(1)]+[Fraction(0)]*R
    for s in range(R+1):
        weight=Fraction(1<<(k*s+s*(s-1)//2),factorial(s))
        Q=[q+weight*p for q,p in zip(Q,P)]
        P=multiply(P,W,R)
    F=Q
    for m in parts:
        B=[Fraction(1<<(m*a+a*(a-1)//2),factorial(a)) for a in range(R+1)]
        F=multiply(F,B,R)
    v=[F[i]*factorial(i) for i in range(R+1)]
    assert all(x.denominator == 1 for x in v)
    return [int(x) for x in v]


def direct_tuple_count(parts,r):
    """Independent tuple-label enumeration using canonical fresh block names."""
    k=len(parts); total=0
    for labels in product(range(k+r),repeat=r):
        fresh=[x-k for x in labels if x>=k]
        order=[]
        for x in fresh:
            if x not in order:
                order.append(x)
        if order != list(range(len(order))):
            continue
        s=len(order)
        w=1<<(k*s+s*(s-1)//2)
        for i,m in enumerate(parts):
            a=labels.count(i)
            w*=1<<(m*a+a*(a-1)//2)
        for j in range(s):
            a=labels.count(k+j)
            w*=1<<(a*(a-1)//2)
        total+=w
    return total


def polynomial_delta_identity():
    """Check the universal three-type gap as a polynomial in q=2**(t+1)."""
    def add(*ps):
        out={}
        for p in ps:
            for e,a in p.items():out[e]=out.get(e,0)+a
        return {e:a for e,a in out.items() if a}
    def scale(a,p):return {e:a*v for e,v in p.items() if a*v}
    def mul(a,b):
        out={}
        for e,x in a.items():
            for f,y in b.items():out[e+f]=out.get(e+f,0)+x*y
        return {e:a for e,a in out.items() if a}
    def cube(a):return mul(mul(a,a),a)
    def t3(u,b0,c0,d0):
        b={0:b0,1:1};c={0:c0,2:1};d={0:d0,3:1}
        constant={0:8*u+12*u*u+8*u**3}
        return add(cube(b),scale(3,mul(b,c)),scale(4,d),
                   scale(3*u,add(mul(b,b),c)),
                   scale(6*u+6*u*u,b),constant)
    A=t3(32,26,292,4232)
    B=t3(16,42,1092,33288)
    assert add(A,scale(-1,B))=={0:3200}
    return True


def run():
    expected_partition_counts=(1,2,3,5,7,11,15,22,30,42)
    expected_unique_signatures=(1,2,3,5,7,11,15,22,30,41)
    all_rows=[]
    for n in range(1,11):
        buckets=defaultdict(list)
        ps=list(partitions(n))
        assert len(ps)==expected_partition_counts[n-1]
        for p in ps:
            t1,t2,t3=low_counts(p)
            buckets[(t1,t2)].append(p)
            all_rows.append((n,','.join(map(str,p)),t1,t2,t3))
            assert egf_counts(p,3)[1:]==[t1,t2,t3]
        assert len(buckets)==expected_unique_signatures[n-1]
        collisions={key:value for key,value in buckets.items() if len(value)>1}
        if n<10:
            assert not collisions
        else:
            assert collisions=={(60,4984):[(1,1,2,2,4),(1,1,3,5)]}
    with (Path(__file__).parent/'profile_certificate.csv').open(newline='',encoding='utf-8') as fp:
        got=list(csv.reader(fp))
    rows=[['n','class_sizes','t1','t2','t3']]+[[str(v) for v in row] for row in all_rows]
    assert got==rows
    print('COMPLETE_PARTITION_CENSUS_OK: 139 signatures, 42 ten-point profiles, one collision at n=10')

    A=(1,1,2,2,4); B=(1,1,3,5)
    for p in (A,B):
        for r in (1,2,3):
            assert direct_tuple_count(p,r)==low_counts(p)[r-1]
    assert low_counts(A)==(60,4984,619552)
    assert low_counts(B)==(60,4984,616352)
    print('DIRECT_TUPLE_ENUMERATION_OK: t3 gap 3200')

    for t in range(0,20):
        q=1<<(t+1)
        a=tuple(sorted((t+1,1,2,2,4)))
        b=tuple(sorted((t+1,1,3,5)))
        ta=low_counts(a)
        tb=low_counts(b)
        assert ta[:2]==tb[:2]
        assert ta[0]==q+58
        assert ta[1]==(q+58)**2+q*q+1380
        assert ta[2]-tb[2]==3200
    assert polynomial_delta_identity()
    print('INFINITE_FAMILY_POLYNOMIAL_IDENTITY_OK: constant gap 3200')
    print('INFINITE_FAMILY_SPOTCHECK_OK: t=0..19')
    print('VERIFICATION_OK')

if __name__=='__main__':run()
