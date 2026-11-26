#!/usr/bin/env python3
"""Exact independent checks for Yule tree cherry-count / leaf-depth covariance.
No external modules required. Run with python3 verify_yule.py.
"""
from collections import defaultdict
from fractions import Fraction as F

def canon(a,b):
    return (a,b) if repr(a)<=repr(b) else (b,a)

def split_all(t):
    if t is None:
        yield (None,None)
    else:
        a,b=t
        for x in split_all(a):
            yield canon(x,b)
        for x in split_all(b):
            yield canon(a,x)

def stats(t):
    depths=[]
    cherrydepths=[]
    def rec(node,d):
        if node is None:
            depths.append(d)
            return
        a,b=node
        if a is None and b is None:
            cherrydepths.extend((d+1,d+1))
        rec(a,d+1)
        rec(b,d+1)
    rec(t,0)
    return len(cherrydepths)//2,sum(depths),sum(cherrydepths)

def theory(n):
    h=sum((F(1,k) for k in range(1,n+1)),F(0))
    return (F(n,3),2*n*(h-1),F(4*n,3)*(h-1)+F(2*n,9),-F((n-3)*(n+2),9*(n-1)))

def check():
    shapes={ (None,None):1 }
    n=2
    checks=0
    for n in range(2,13):
        denom=sum(shapes.values())
        assert denom==__import__('math').factorial(n-1), (n,denom)
        if n>=3:
            mean_c=F(sum(w*stats(t)[0] for t,w in shapes.items()),denom)
            mean_s=F(sum(w*stats(t)[1] for t,w in shapes.items()),denom)
            mean_q=F(sum(w*stats(t)[2] for t,w in shapes.items()),denom)
            mean_cs=F(sum(w*stats(t)[0]*stats(t)[1] for t,w in shapes.items()),denom)
            observed=(mean_c,mean_s,mean_q,mean_cs-mean_c*mean_s)
            assert observed==theory(n),(n,observed,theory(n))
            checks+=4
        if n<12:
            nxt=defaultdict(int)
            for t,w in shapes.items():
                for x in split_all(t):
                    nxt[x]+=w
            shapes=nxt
    # Completely separate exact-state recurrences, beyond enumeration:
    c,s,q,cs=F(1),F(2),F(2),F(2)
    for n in range(2,301):
        if n>=3:
            expected=theory(n)
            assert (c,s,q,cs-c*s)==expected,(n,c,s,q,cs,expected)
            checks+=4
        newcs=(1-F(1,n))*cs+(1+F(1,n))*s+(2-F(4,n))*c-F(1,n)*q+2
        newq=(1-F(2,n))*q+F(2,n)*s+2
        news=(1+F(1,n))*s+2
        newc=(1-F(2,n))*c+1
        c,s,q,cs=newc,news,newq,newcs
    print('PASS',checks,'exact comparisons; n<=12 dynamic shape enumeration, n<=300 independent recurrences')

if __name__=='__main__':
    check()
