"""Exact rational finite sanity checks for the stated harvesting allocation theorem.

The proof in RESULT.md is the infinite-dimensional/parameter argument; these
checks only detect arithmetic and normalization mistakes in finite cases.
"""
from fractions import Fraction as F
from itertools import product


def H(x):
    p=F(1)
    v=F(0)
    for a in x:
        v += a/p
        p *= 1+a
    return v


def pairs(x):
    return sum((x[i]*x[j] for i in range(len(x)) for j in range(i+1,len(x))),F(0))


def cost(x,c):
    return c*sum((a*a for a in x),F(0))/2-H(x)


def compositions(N,S):
    if N==1:
        yield (S,)
        return
    for a in range(S+1):
        for rest in compositions(N-1,S-a):
            yield (a,)+rest


def run():
    tests=0
    strict=0
    for N in range(2,8):
        for Sint in range(1,7):
            S=F(Sint,3)
            threshold=1/(1+S)
            vertex=(S,)+(F(0),)*(N-1)
            for nums in compositions(N,Sint):
                x=tuple(F(a,3) for a in nums)
                P=pairs(x)
                B=S-H(x)
                assert B>=P/(1+S), (N,S,x,B,P)
                if P>0:
                    assert B>P/(1+S)
                    strict+=1
                for c in (F(0),threshold/2,threshold):
                    assert cost(x,c)>=cost(vertex,c)
                    if P>0: assert cost(x,c)>cost(vertex,c)
                    tests+=1
                # Directly compare the pure old-state harvest before and after
                # swapping any two consecutive positive entries.
                for i in range(N-1):
                    if x[i]>0 and x[i+1]>0:
                        xp=list(x); xp[i],xp[i+1]=xp[i+1],xp[i]
                        diff=H(x)-H(xp)
                        prefix=F(1)
                        for j in range(i):prefix*=1+x[j]
                        exp=x[i]*x[i+1]*(x[i]-x[i+1])/(prefix*(1+x[i])*(1+x[i+1]))
                        assert diff==exp,(x,diff,exp)
                        tests+=1
            for eps in (S/F(10),S/F(1000)):
                c=threshold+(F(1,1)/(1+S-eps)-threshold)+F(1,1000)
                # c is larger than the exact local split threshold
                split=(S-eps,eps)+(F(0),)*(N-2)
                assert cost(split,c)<cost(vertex,c)
                tests+=1
    print('VERIFY_OK',tests,'rational checks,',strict,'strict-split cases')


if __name__=='__main__':
    run()
