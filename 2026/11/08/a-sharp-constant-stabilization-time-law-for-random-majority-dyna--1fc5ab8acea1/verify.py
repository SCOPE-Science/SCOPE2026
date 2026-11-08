"""Exact rational independent transition checks and global finite certificate.

Uses only Python 3 standard library; no external data or libraries.
"""
from fractions import Fraction as F
from math import comb


def pq(n):
    assert n >= 1
    p = F(comb(n, n//2), 2**n) if n%2 == 0 else F(0)
    q = F(2, 2**n)
    return p, q


def expected_types(a,b):
    pa,qa = pq(a)
    pb,qb = pq(b)
    d=1-pa*pb
    A=(2-pb-qb+pb*(2-pa-qa))/d
    B=(2-pa-qa+pa*(2-pb-qb))/d
    C=(2-pa-pb+pa*pb-qa*qb+pa*(1-pb)*A+(1-pa)*pb*B)/d
    return A,B,C


def t(a,b,x,y):
    if x in (0,a) and y in (0,b): return F(0)
    if 2*x==a and 2*y==b: return expected_types(a,b)[2]
    if 2*x==a: return expected_types(a,b)[0]
    if 2*y==b: return expected_types(a,b)[1]
    return F(1)


def transitions(n, other_n, opposite_blue):
    if 2*opposite_blue<other_n:
        return [(0,F(1))]
    if 2*opposite_blue>other_n:
        return [(n,F(1))]
    return [(k,F(comb(n,k),2**n)) for k in range(n+1)]


def independent_bellman_checks():
    checked=0
    for a in range(1,9):
        for b in range(1,9):
            for x in range(a+1):
                for y in range(b+1):
                    val=t(a,b,x,y)
                    if (x in (0,a) and y in (0,b)):
                        assert val==0
                        continue
                    nxt=sum((px*py*t(a,b,xx,yy)
                            for xx,px in transitions(a,b,y)
                            for yy,py in transitions(b,a,x)),F(0))
                    assert val==1+nxt,(a,b,x,y,val,nxt)
                    checked+=1
    return checked


def sharp_finite_check():
    best=(F(-1),None)
    pairs=0
    maximizers=[]
    for a in range(2,41,2):
        for b in range(2,41,2):
            A,B,C=expected_types(a,b)
            for label,u in [('one-A-tie',A),('one-B-tie',B),('both-tie',C)]:
                if u>best[0]: best=(u,(a,b,label))
                if u==F(79,27): maximizers.append((a,b,label))
            pairs+=1
    assert best==(F(79,27),(2,6,'both-tie')),best
    assert set(maximizers)=={(2,6,'both-tie'),(6,2,'both-tie')},maximizers
    return pairs,best


def tail_certificate():
    # p_(2m) decreases and p_42 < 1/8; odd sizes have zero tie probability.
    assert 8*comb(42,21)<2**42
    X,Y,Z=F(11,5),F(13,5),F(41,15)
    pa,pb=F(1,2),F(1,8)
    assert X==2-pb+pb*Y
    assert Y==2-pa+pa*X
    assert Z==1+(1-pa)*(1-pb)+pa*(1-pb)*X+(1-pa)*pb*Y+pa*pb*Z
    assert Z<F(79,27)
    assert X>=1 and Y>=1 and Z>=X and Z>=Y
    return (X,Y,Z)

if __name__=='__main__':
    n=independent_bellman_checks()
    n2,best=sharp_finite_check()
    vals=tail_certificate()
    print(f'VERIFY_OK: {n} full-chain Bellman checks; {n2} exact finite parameter pairs; sharp={best}; tail={vals}')
