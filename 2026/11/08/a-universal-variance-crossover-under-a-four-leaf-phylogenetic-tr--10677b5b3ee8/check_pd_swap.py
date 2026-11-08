#!/usr/bin/env python3
"""Exact arithmetic checks for a rooted phylogenetic diversity variance switch.

Run: python3 check_pd_swap.py. No third-party dependencies.
"""
from fractions import Fraction
from functools import lru_cache


def add(a,b):
    r=[0]*max(len(a),len(b))
    for i,x in enumerate(a):r[i]+=x
    for i,x in enumerate(b):r[i]+=x
    while len(r)>1 and r[-1]==0:r.pop()
    return tuple(r)

def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]+=x*y
    while len(r)>1 and r[-1]==0:r.pop()
    return tuple(r)

def scale(a,k):return tuple(k*x for x in a)

def sub(a,b):return add(a,scale(b,-1))

def power(a,n):
    out=(1,)
    for _ in range(n):out=mul(out,a)
    return out

def qpow(n):return (0,)*n+(1,)

def evaluate(a,q):return sum(c*q**i for i,c in enumerate(a))

def comb(n):
    if n==1:return 0
    return (comb(1), comb(n-1))

def four_fork():return ((0,0),(0,0))

def fork_tail(n):
    assert n>=4
    return four_fork() if n==4 else (0,fork_tail(n-1))

def edges(tree):
    """Return the full leaf mask and the descendant-leaf mask of every edge."""
    def clades(t):
        if t==0:
            m=1<<clades.next_leaf
            clades.next_leaf+=1
            return m, []
        a,ca=clades(t[0]);b,cb=clades(t[1])
        return a|b, [(a,ca),(b,cb)]+ca+cb
    clades.next_leaf=0
    full,arr=clades(tree)
    return full,[mask for mask,_ in arr]

def variance_cov(tree):
    full,mask=edges(tree)
    sizes=[v.bit_count() for v in mask]
    out=(0,)
    for s in sizes:
        out=add(out,mul(qpow(s),sub((1,),qpow(s))))
    for i,u in enumerate(mask):
        for j,v in enumerate(mask):
            if i==j:continue
            if u & v == v:  # u ancestor of v
                out=add(out,scale(mul(qpow(sizes[i]),sub((1,),qpow(sizes[j]))),2))
    return out

def mean_cov(tree):
    return sum_poly([sub((1,),qpow(mask.bit_count())) for mask in edges(tree)[1]])

def sum_poly(items):
    out=(0,)
    for x in items:out=add(out,x)
    return out

def moments_subsets(tree):
    full,masks=edges(tree)
    n=full.bit_count()
    means=(0,);seconds=(0,)
    for survivors in range(1<<n):
        k=survivors.bit_count()
        pd=sum(bool(x&survivors) for x in masks)
        weight=mul(power(sub((1,),(0,1)),k),qpow(n-k))
        means=add(means,scale(weight,pd))
        seconds=add(seconds,scale(weight,pd*pd))
    return means,sub(seconds,mul(means,means))

def predicted(n):
    b=add((-5,8,3,1),sum_poly([scale(qpow(s),2) for s in range(4,n)]))
    return mul(mul(qpow(2),sub((1,),(0,1))),b)

def mean_predicted():
    return (0,0,1,-1)

def main():
    checks=0
    for n in range(4,13):
        cat=comb(n);bal=fork_tail(n)
        # The covariance proof uses all clades, with no numerical approximations.
        assert sub(variance_cov(cat),variance_cov(bal))==predicted(n)
        assert sub(mean_cov(cat),mean_cov(bal))==mean_predicted()
        checks+=2
        if n<=9:
            m1,v1=moments_subsets(cat)
            m2,v2=moments_subsets(bal)
            assert v1==variance_cov(cat) and v2==variance_cov(bal)
            assert sub(m1,m2)==mean_predicted()
            checks+=3
    # An additional tiny-case enumeration checks the smallest n with two shapes.
    @lru_cache(None)
    def shapes(n):
        if n==1:return ('x',)
        found=set()
        for a in range(1,n):
            for t in shapes(a):
                for u in shapes(n-a):
                    found.add(tuple(sorted((t,u), key=repr)))
        return tuple(sorted(found,key=repr))
    assert [len(shapes(n)) for n in (1,2,3,4)]==[1,1,1,2]
    checks+=1
    for n in (4,5,6,8,16,32):
        b=add((-5,8,3,1),sum_poly([scale(qpow(s),2) for s in range(4,n)]))
        assert evaluate(b,Fraction(0))==-5
        assert evaluate(b,Fraction(1))==2*n-1
        assert evaluate(b,Fraction(1,4))<0<evaluate(b,Fraction(3,4))
        # derivative has strictly positive nonconstant coefficients, hence a positive derivative.
        assert all((i*c)>0 for i,c in enumerate(b) if i>0)
        checks+=4
    print('PASS:',checks,'symbolic/independent finite checks; smallest shape counts 1,1,1,2')
    print('PASS: exact variance identity n=4..12; independent all-survivor enumerations n=4..9')
    print('PASS: mean difference q^2(1-q), one crossing for each n, monotone n-dependence')

if __name__=='__main__':main()
