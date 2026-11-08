#!/usr/bin/env python3
"""Exact checks of position-resolved Ewens fixed-point–inversion covariances.
No third-party packages required.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def inversion_count(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def number_cycles(p):
    n=len(p); seen=set(); c=0
    for i in range(n):
        if i not in seen:
            c+=1; v=i
            while v not in seen:
                seen.add(v);v=p[v]-1
    return c

def expectation_inversions(n,t):
    return (Fraction(n*n*(n-1)**2,4)+(t-1)*Fraction(n*(n-1)*(2*n-1),6))/((t+n-1)*(t+n-2))

def covariance(n,i,t):
    z = Fraction(n+1,2)
    core = Fraction((n-1),6)*(1-t)*(2*n*n + 3*n*t -7*n-3*t+3)/((n+t-3)*(n+t-2)*(n+t-1))
    return t/(t+n-1)*(core-2*(i-z)**2/(n+t-2))

def total_covariance(n,t):
    b=n*(n-2)*(n-3)+(4*n*(n-3)+2)*t+(4*n-2)*t*t
    return -n*t*(n-1)*b/(6*(n+t-3)*(n+t-2)*(n+t-1)**2)

def brute(n,t):
    den=Fraction(0); s_inv=Fraction(0)
    s_fix=[Fraction(0)]*n; s_cross=[Fraction(0)]*n
    for p in permutations(range(1,n+1)):
        w=t**number_cycles(p); x=inversion_count(p); den+=w;s_inv+=w*x
        for i in range(n):
            if p[i]==i+1: s_fix[i]+=w;s_cross[i]+=w*x
    mean=s_inv/den
    return mean,[s_cross[i]/den-s_fix[i]/den*mean for i in range(n)]

def pair_inversion(n, gap, t):
    return (Fraction(n*(n-1),2)+(t-1)*(n-gap))/((n+t-1)*(n+t-2))

def pair_covariance(n,k,a,b,t):
    assert 1 <= a < b <= n and 1 <= k <= n
    if k == a:
        conditional = Fraction(a-1,1)/(n+t-2)
    elif k == b:
        conditional = Fraction(n-b,1)/(n+t-2)
    else:
        conditional = pair_inversion(n-1,b-a-(a<k<b),t)
    return t/(n+t-1)*(conditional-pair_inversion(n,b-a,t))

def triple_brute(n,t):
    den=Fraction(0)
    pair={(a,b):Fraction(0) for a in range(1,n) for b in range(a+1,n+1)}
    fix={k:Fraction(0) for k in range(1,n+1)}
    joint={(k,a,b):Fraction(0) for k in fix for a,b in pair}
    for p in permutations(range(1,n+1)):
        w=t**number_cycles(p); den+=w
        fps=[k for k in fix if p[k-1]==k]
        inv=[(a,b) for a,b in pair if p[a-1]>p[b-1]]
        for k in fps:fix[k]+=w
        for a,b in inv:pair[a,b]+=w
        for k in fps:
            for a,b in inv:joint[k,a,b]+=w
    return {(k,a,b): joint[k,a,b]/den-fix[k]*pair[a,b]/den**2 for k,a,b in joint}

def main():
    checks=0
    for n in range(3,8):
        for t in (Fraction(1,3),Fraction(1,2),Fraction(1),Fraction(2),Fraction(5,2),Fraction(4)):
            em,cv=brute(n,t)
            assert em==expectation_inversions(n,t),(n,t,'mean',em)
            checks+=1
            assert sum(cv)==total_covariance(n,t),(n,t,'aggregate',cv)
            checks+=1
            for i,x in enumerate(cv,1):
                assert x==covariance(n,i,t),(n,i,t,'position',x,covariance(n,i,t))
                checks+=1
                assert x==cv[-i],(n,i,t,'symmetry')
                checks+=1
                if t>=1:
                    assert x<=0,(n,i,t,'nonpositive')
                    checks+=1
                    assert (x==0)==(t==1 and n%2==1 and i==(n+1)//2),(n,i,t,'equality')
                    checks+=1
    for n in range(3,7):
        for t in (Fraction(1,3), Fraction(1), Fraction(5,3), Fraction(3)):
            data=triple_brute(n,t)
            for (k,a,b),x in data.items():
                assert x==pair_covariance(n,k,a,b,t),(n,t,k,a,b,x,pair_covariance(n,k,a,b,t))
                checks+=1
                if k!=a and k!=b:
                    if t==1:assert x==0
                    elif k<a or k>b:assert x*(t-1)<0
                    else:assert (x==0)==(2*(b-a)==n+1)
                    checks+=1
    print('VERIFY_OK',checks,'exact assertions')
if __name__=='__main__':main()
