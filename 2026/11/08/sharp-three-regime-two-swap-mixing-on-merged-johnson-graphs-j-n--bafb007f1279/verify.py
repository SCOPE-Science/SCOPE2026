#!/usr/bin/env python3
"""Independent rational checks for two-swap mixing on three-subsets.

Standard-library only. Finite checks are not a proof for arbitrary n;
the accompanying algebraic proof establishes the all-n statements.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb

def modes(n):
    k1 = 3 * (n - 3)
    k2 = 3 * comb(n - 3, 2)
    p1 = [k1, 2*n-9, n-7, -3]
    p2 = [k2, (n-4)*(n-9)//2, 11-2*n, 3]
    c = [(Q(1)-Q(p1[j],k1), Q(1)-Q(p2[j],k2)) for j in (1,2,3)]
    return c

def candidate(n):
    if n<=9:
        den=(n-2)*(7*n-4)
        w1=Q(6*(10-n)*(n-3),den)
        w2=Q(12*(n-4)*(n-3),den)
        t=Q(n-4,7*n-4)
    elif n<=12:
        den=5*n*n-25*n+14
        w1=Q(0)
        w2=Q(6*(n-4)*(n-3),den)
        t=Q((n-7)*(n-2),den)
    else:
        w1,w2=Q(0),Q(1)
        t=Q(n-9,3*(n-3))
    return w1,w2,1-w1-w2,t

def check(n):
    c=modes(n)
    x,y,s,t=candidate(n)
    assert min(x,y,s,t)>=0
    eig=[Q(1)-a*x-b*y for a,b in c]
    assert max(abs(v) for v in eig)==t
    if n<=9:
        assert eig==[t,-t,t]
        a1=Q(3*(n-4)*(n-1),(n-3)*(7*n-4))
        a2=Q(3*n,7*n-4)
        a3=Q(n*(n-1),(n-3)*(7*n-4))
        assert a1+a2+a3==1 and min(a1,a2,a3)>0
        assert a1*c[0][0]-a2*c[1][0]+a3*c[2][0]==0
        assert a1*c[0][1]-a2*c[1][1]+a3*c[2][1]==0
        assert a1-a2+a3==t
    elif n<=12:
        assert eig[0]==t and eig[1]==-t
        den=5*n*n-25*n+14
        a1=Q((n-1)*(3*n-14),den)
        a2=Q(2*n*(n-4),den)
        assert a1+a2==1 and min(a1,a2)>0
        assert a1*c[0][1]-a2*c[1][1]==0
        assert (-a1*c[0][0]+a2*c[1][0])==Q(n*(n-2)*(n-1),3*(n-3)*den)>0
        assert a1-a2==t
    else:
        assert eig[0]==t
        assert c[0][1]>c[0][0]>0
        assert 1-c[0][1]==t
        assert abs(eig[1])<=t and abs(eig[2])<=t

# Independently reconstruct all four shells of adjacency-square by counting neighbors.
def check_graph(n):
    triples=list(combinations(range(n),3))
    sets=[set(s) for s in triples]
    near=[[j for j,t in enumerate(sets) if len(s & t)==2] for s in sets]
    assert len(near)==len(triples) and all(len(a)==3*(n-3) for a in near)
    for i,s in enumerate(sets):
        neighbors=set(near[i])
        for j,t in enumerate(sets):
            dist=3-len(s & t)
            a1=int(dist==1)
            a2=int(dist==2)
            lhs=sum(j in near[k] for k in near[i])
            rhs=3*(n-3)*int(i==j)+(n-2)*a1+4*a2
            assert lhs==rhs,(n,i,j,lhs,rhs)

if __name__=='__main__':
    for n in range(6,1001):
        check(n)
    for n in range(6,11):
        check_graph(n)
    print('VERIFY_OK 995 exact rational spectral/dual cases, 5 complete graph-square checks')
