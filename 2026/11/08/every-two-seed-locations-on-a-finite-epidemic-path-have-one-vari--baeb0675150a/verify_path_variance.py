#!/usr/bin/env python3
"""Exact checks for a finite-path source-variance theorem (standard library)."""
from math import comb
from fractions import Fraction


def add(left, right, scalar=1):
    n=max(len(left),len(right)); out=[0]*n
    for i,v in enumerate(left): out[i]+=v
    for i,v in enumerate(right): out[i]+=scalar*v
    return trim(out)

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def mul(a,b):
    ans=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):ans[i+j]+=x*y
    return trim(ans)

def variance_poly(t):
    # number of consecutive open edges until first failed one, capped at t
    out=[0]*(2*t+1)
    for k in range(1,t+1):out[k]+=k
    for k in range(t+1,2*t+1):out[k]-=2*t+1-k
    return trim(out)

def source_variance(m,a):
    return add(variance_poly(a),variance_poly(m-a))

def exact_edge_moments(m,a):
    first=[0]*(m+1);second=[0]*(m+1)
    # A configuration with k transmitting edges has weight p^k(1-p)^(m-k).
    for mask in range(1<<m):
        k=mask.bit_count(); sz=1
        j=a-1
        while j>=0 and (mask>>j)&1:sz+=1;j-=1
        j=a
        while j<m and (mask>>j)&1:sz+=1;j+=1
        for t in range(m-k+1):
            coefficient=comb(m-k,t)*((-1)**t);power=k+t
            first[power]+=sz*coefficient
            second[power]+=sz*sz*coefficient
    return trim(first),trim(second)

def evaluate(a,p):
    return sum(Fraction(c)*p**i for i,c in enumerate(a))

def qcoeff(d):
    # d divisible by (1-p), quotient coefficients are cumulative sums.
    out=[];running=0
    for x in d:
        running+=x;out.append(running)
    assert running==0, 'p=1 boundary failed'
    return trim(out[:-1])

def difference_poly(m,a,c):
    return add(source_variance(m,a),source_variance(m,c),-1)

def signs(a):
    return [1 if x>0 else -1 for x in a if x!=0]

def main():
    state_pairs=0;polynomial_checks=0
    for m in range(2,12):
        for a in range(m+1):
            e,e2=exact_edge_moments(m,a)
            true=add(e2,mul(e,e),-1)
            expected=source_variance(m,a)
            assert true==expected,(m,a,true,expected)
            state_pairs+=1<<m;polynomial_checks+=1
    comparisons=0
    for m in range(2,41):
        for a in range(m//2):
            for c in range(a+1,m//2+1):
                d=difference_poly(m,a,c)
                q=qcoeff(d)
                sg=signs(q)
                assert sg and sg[0]==-1 and sg[-1]==1
                assert sum(sg[i]!=sg[i-1] for i in range(1,len(sg)))==1
                assert d[a+1]<0
                assert d[-1]==-1
                comparisons+=1
    # Concrete six-vertex path: terminal seed versus a middle source.
    f0=source_variance(5,0);f2=source_variance(5,2)
    assert evaluate(f0,Fraction(1,2))-evaluate(f2,Fraction(1,2))==Fraction(-145,1024)
    assert evaluate(f0,Fraction(9,10))-evaluate(f2,Fraction(9,10))==Fraction(18663573519,10000000000)
    print('PASS: %d independent configurations across %d exact source-moment polynomials' % (state_pairs,polynomial_checks))
    print('PASS: %d distinct location comparisons through 41 vertices have one coefficient sign change' % comparisons)
    print('PASS: exact P6 rational contrasts at p=1/2 and p=9/10')
    print('NOTE: infinite-length uniqueness follows from the analytic proof, not these finite checks')

if __name__=='__main__':main()
