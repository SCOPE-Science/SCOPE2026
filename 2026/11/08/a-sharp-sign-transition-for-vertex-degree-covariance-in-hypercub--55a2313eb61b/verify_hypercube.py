"""Exact checks for uniform-spanning-tree vertex-degree covariance on hypercubes.
Python 3, standard library only; no network or external data required.
"""
from itertools import combinations
from fractions import Fraction
from math import comb

def h(d,j):
    assert 0 <= j < d
    n=1<<d
    return Fraction(n-sum(comb(d,q) for q in range(j+1)), n*comb(d,j)*(d-j))

def special(d,t):
    assert 1 <= t <= d
    n=1<<d
    hh={j:h(d,j) for j in range(d)}
    q=Fraction(0)
    def add(mult,left,right=None):
        nonlocal q
        if mult:
            q+=mult*(hh[left] if right is None else hh[left]-hh[right])**2
    add(4*t,t-1)
    if d-t: add(4*(d-t),t)
    if t>=2: add(t*(t-1),t-2,t-1)
    if t<d: add(2*t*(d-t),t,t-1)
    if d-t>=2: add((d-t)*(d-t-1),t,t+1)
    return (2*h(d,0) if t==1 else Fraction(0))-q

def formula(d,t):
    if d==1: return Fraction(0)
    if d==2 and t==1: return Fraction(0)
    if d>=3 and t==1:
        n=1<<d
        return Fraction((n-2*d)*(n*(d-4)+2*d+4), n*n*d*(d-1)*(d-2))
    return special(d,t)

def laplace_green(d,x):
    n=1<<d
    return sum((Fraction(1 if (x&s).bit_count()%2==0 else -1,2*s.bit_count()) for s in range(1,n)),Fraction(0))/n

def matrix_sum(d,t):
    x=(1<<t)-1
    p=2*h(d,0)
    ans=Fraction(0)
    for i in range(d):
        for j in range(d):
            a=(1<<i);b=(1<<j)
            k=(laplace_green(d,x)-laplace_green(d,x^a)-laplace_green(d,x^b)+laplace_green(d,x^a^b))
            ans-=k*k
    if t==1: ans+=p
    return ans

def edges(d):
    n=1<<d
    return [(x,x^(1<<i)) for x in range(n) for i in range(d) if x<(x^(1<<i))]

def connected_tree(n,ees):
    par=list(range(n))
    def root(x):
        while par[x]!=x:
            x=par[x]
        return x
    for x,y in ees:
        a,b=root(x),root(y)
        if a==b:return False
        par[a]=b
    return len({root(i) for i in range(n)})==1

def exhaustive(d):
    n=1<<d; e=edges(d); m=n-1
    totals={t:[0,0,0] for t in range(1,d+1)}
    count=0
    for inds in combinations(range(len(e)),m):
        ee=[e[i] for i in inds]
        if not connected_tree(n,ee):continue
        count+=1
        deg=[0]*n
        for x,y in ee:deg[x]+=1;deg[y]+=1
        for t in totals:
            a=deg[0];b=deg[(1<<t)-1]
            totals[t][0]+=a;totals[t][1]+=b;totals[t][2]+=a*b
    assert count>0
    for t,(a,b,c) in totals.items():
        observed=Fraction(c,count)-Fraction(a*b,count**2)
        assert observed==formula(d,t),(d,t,observed,formula(d,t))
    return count

def main():
    assert exhaustive(1)==1
    assert exhaustive(2)==4
    assert exhaustive(3)==384
    checks=0
    for d in range(2,9):
        for t in range(1,d+1):
            assert special(d,t)==matrix_sum(d,t)==formula(d,t),(d,t)
            assert (formula(d,t)>0) == (d>=3 and t==1),(d,t,formula(d,t))
            assert (formula(d,t)==0) == (d==2 and t==1),(d,t,formula(d,t))
            checks+=3
    print('PASS: exhaustive n=2,4,8; 384 spanning trees at Q3; 105 exact spectral/formula/sign assertions:',checks)
    for d in range(2,7):print('d=',d,'cov by distance=',[str(formula(d,t)) for t in range(1,d+1)])

if __name__=='__main__':main()
