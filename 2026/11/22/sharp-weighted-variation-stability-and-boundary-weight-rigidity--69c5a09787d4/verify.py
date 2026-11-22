#!/usr/bin/env python3
"""Reproducible finite rational checks for the midrange stability theorem."""
from fractions import Fraction as F
from itertools import permutations
from random import Random


def midrange(x):
    n=len(x)
    return [(min(x[max(0,i-1):min(n,i+2)]) + max(x[max(0,i-1):min(n,i+2)]))/2 for i in range(n)]


def step_response_twice(perm,j):
    n=len(perm)
    v=[]
    for i in range(n):
        win=range(max(0,i-1),min(n,i+2))
        indices=[k for k in win]
        lo=min(indices,key=lambda k:perm[k]); hi=max(indices,key=lambda k:perm[k])
        v.append(int(lo>=j)+int(hi>=j))
    return tuple(abs(v[i+1]-v[i]) for i in range(n-1))


def variation(x,w):
    return sum(w[i]*abs(x[i+1]-x[i]) for i in range(len(w)))


def predicted(n,w):
    if n==2: return F(0)
    if n==3: return max(F(w[1],2*w[0]),F(w[0],2*w[1]))
    ratios=[F(max(w[0],w[1]),2*w[0]),F(max(w[-2],w[-1]),2*w[-1])]
    for j in range(1,n-2):
        p,q,r=w[j-1],w[j],w[j+1]
        ratios.extend([F(1),F(p+q,2*q),F(q+r,2*q),F(p+r,2*q)])
    return max(ratios)


def enumerate_chambers():
    total=0
    for n in range(2,9):
        feasible=[set() for _ in range(n-1)]
        permutations_checked=0
        for perm in permutations(range(n)):
            permutations_checked+=1
            for j in range(1,n):
                feasible[j-1].add(step_response_twice(perm,j))
        total+=permutations_checked
        # Check all *attainable* rank-two step-profile branches, including boundary.
        if n==2:
            assert feasible==[{(0,)}]
        elif n==3:
            assert feasible==[{(0,1),(1,0)},{(0,1),(1,0)}]
        else:
            first={(0,1)+(0,)*(n-3),(1,0)+(0,)*(n-3)}
            last={(0,)*(n-3)+(1,0),(0,)*(n-3)+(0,1)}
            assert feasible[0]==first, (n,feasible[0])
            assert feasible[-1]==last,(n,feasible[-1])
            for j in range(1,n-2):
                # Three affected edges in twice-normalized units:
                # (a,b)=(0,1/2)->(0,1,1); (0,1)->(0,2,0)
                # (1/2,1/2)->(1,0,1); (1/2,1)->(1,1,0)
                allowed=set()
                for a,b,c in [(0,1,1),(0,2,0),(1,0,1),(1,1,0)]:
                    v=[0]*(n-1)
                    v[j-1]=a; v[j]=b; v[j+1]=c
                    allowed.add(tuple(v))
                assert feasible[j]==allowed,(n,j,feasible[j],allowed)
        weights=[[1]*(n-1),[1+((i*i+3*i)%7) for i in range(n-1)],
                 [1+(i%2)*5 for i in range(n-1)],
                 list(range(1,n)),list(range(n-1,0,-1))]
        for w in weights:
            observed=max(F(sum(w[i]*z[i] for i in range(n-1)),2*w[j])
                          for j in range(n-1) for z in feasible[j])
            assert observed==predicted(n,w),(n,w,observed,predicted(n,w))
        if n>=4:
            taper=[1]*(n-1)
            taper[0]=taper[-1]=F(1,2)
            assert predicted(n,taper)==1
            for edge in [0,n-2]:
                under=taper[:];under[edge]=F(49,100)
                assert predicted(n,under)>1
                over=taper[:];over[edge]=F(101,100)
                assert predicted(n,over)>1
        print('EXACT_ORDER_CHAMBERS_AND_WEIGHTED_OPERATOR_NORMS_PASS',n,permutations_checked)
    return total


def random_input_checks():
    rng=Random(20261117)
    for n in range(2,13):
        for _ in range(450):
            w=[F(rng.randrange(1,12),rng.randrange(1,8)) for j in range(n-1)]
            x=[F(rng.randrange(-100,101),rng.randrange(1,13)) for i in range(n)]
            y=[F(rng.randrange(-100,101),rng.randrange(1,13)) for i in range(n)]
            v=variation([a-b for a,b in zip(x,y)],w)
            if v>0:
                out=variation([a-b for a,b in zip(midrange(x),midrange(y))],w)
                assert out <=predicted(n,w)*v,(n,x,y,w,out,v)
            z=midrange(x)
            assert variation(z,[1]*(n-1))<=variation(x,[1]*(n-1))
    print('EXACT_RATIONAL_TWO_INPUT_AND_ONE_INPUT_CHECKS_PASS',4950)


if __name__=='__main__':
    q=enumerate_chambers()
    random_input_checks()
    print('ALL_MIDRANGE_WEIGHTED_VARIATION_TESTS_PASS',q)
