"""Supplementary numerical diagnostics for the Poisson single-visit allocation theorem.

No finite test is offered as proof of the global theorems. Run with Python 3.10+.
"""
import math
import random


def f(x):
    return x * math.exp(-x)


def fp(x):
    return (1.0-x) * math.exp(-x)


def objective(v):
    return sum(f(x) for x in v)


def two_flower_optimum(b):
    if b <= 4:
        return b/2, b/2
    lo, hi = 0.0, b/2
    for _ in range(90):
        t = (lo+hi)/2
        h = t / math.tanh(t) if t else 1.0
        if 2+2*h < b:
            lo = t
        else:
            hi = t
    t=(lo+hi)/2
    return b/2-t, b/2+t


def candidates(n,b):
    # All global maxima are either balanced or have one overloaded coordinate.
    candidates = [[b/n]*n]
    left = max(1.0, (b-b)/(n-1))
    right = min(2.0, (b-2)/(n-1), b/n)
    if right <= left:
        return candidates
    def g(y):
        return fp(b-(n-1)*y)-fp(y)
    steps=1200
    prev=left
    for i in range(1,steps+1):
        cur=left+(right-left)*i/steps
        if g(prev)*g(cur) < 0:
            a, c = prev, cur
            for _ in range(65):
                m=(a+c)/2
                if g(a)*g(m)<=0:
                    c=m
                else:
                    a=m
            y=(a+c)/2
            x=b-(n-1)*y
            if x>2 and 1<y<2:
                candidates.append([y]*(n-1)+[x])
        prev=cur
    return candidates


def check():
    checks=0
    for k in range(1,281):
        b=k*0.05
        lo,hi=two_flower_optimum(b)
        assert abs(lo+hi-b)<1e-12
        checks+=1
        best=f(lo)+f(hi)
        if b <=4:
            assert abs(lo-hi)<1e-12
        else:
            assert hi>lo and abs(fp(lo)-fp(hi))<1e-12
        checks+=1
        for j in range(101):
            x=b*j/100
            assert best >= f(x)+f(b-x)-2e-12, (b,x,best)
            checks+=1
    for n in (3,4,5,6,8):
        for b in [0.7*n,1.01*n,1.35*n,1.7*n,1.95*n,2*n,2.4*n,3*n,5*n]:
            cands=candidates(n,b)
            target=max(map(objective,cands))
            assert target >= objective([b/n]*n)-1e-12
            checks+=1
            for k in range(750):
                w=[-math.log(max(1e-15,random.random())) for _ in range(n)]
                total=sum(w)
                alloc=[b*x/total for x in w]
                assert objective(alloc) <= target+1e-8,(n,b,target,alloc,objective(alloc))
                checks+=1
    for n in range(3,13):
        b=2*n
        ep=1e-3
        v=[2-ep]*(n-1)+[2+(n-1)*ep]
        assert objective(v)> n*f(2)
        checks+=1
    print('PASS',checks,'supplementary assertions')


if __name__=='__main__':
    random.seed(1729)
    check()
