#!/usr/bin/env python3
"""Standalone integer verifier for Abelian antipower census in two-run periods.
Usage: python3 verify.py
"""
from random import Random

def zpref(x, a, b):
    p=a+b
    n,t=divmod(x,p)
    return n*a+min(a,t)

def direct(a,b,k,q):
    p=a+b
    return sum(len({zpref(s+(j+1)*k,a,b)-zpref(s+j*k,a,b)
                    for j in range(q)})==q for s in range(p))

def fast(a,b,k,q):
    assert a>=1 and b>=1 and k>=1 and q>=2
    p=a+b
    r=k%p
    if r==0 or q>min(a,b,r,p-r)+1:
        return 0
    # Every g_j(s) is affine between these transition points.
    cuts=sorted({0,p}|{(u-j*r)%p
                            for j in range(q+1) for u in (0,a)})
    total=0
    for L,R in zip(cuts,cuts[1:]):
        v=[zpref(L+(j+1)*r,a,b)-zpref(L+j*r,a,b) for j in range(q)]
        slopes=[(zpref(L+1+(j+1)*r,a,b)-zpref(L+1+j*r,a,b))-v[j]
                for j in range(q)] if R-L>=2 else [0]*q
        roots=set(); impossible=False
        for j in range(q):
            for i in range(j):
                d=slopes[i]-slopes[j]
                # v_i-v_j + d*(s-L)=0.
                c=v[j]-v[i]
                if d==0:
                    if c==0:
                        impossible=True
                        break
                elif c%d==0:
                    s=L+c//d
                    if L<=s<R: roots.add(s)
            if impossible: break
        if not impossible:
            total+=(R-L)-len(roots)
    return total

def onset_formula(a,b):
    s,t=sorted((a,b))
    if s==1 or s==2 and t in (2,4): return None,0
    if s>=3: return 2,2+2*(a==3)+2*(b==3)
    p=s+t
    return p//3+1,2

def check():
    count=0
    # Every q/r pair, includes q>p, k>p, and extremal run asymmetries.
    for a in range(1,15):
        for b in range(1,15):
            p=a+b
            for q in range(2, min(7,p+3)):
                for k in range(1,p+3):
                    x,y=fast(a,b,k,q),direct(a,b,k,q)
                    assert x==y,(a,b,k,q,x,y)
                    count+=1
    print('phase-count fast/direct agreements:',count)
    # Onset threshold and multiplicities, including infinite nonexistence cases
    c2=0
    for a in range(1,51):
        for b in range(1,51):
            p=a+b
            k,n=onset_formula(a,b)
            if k is None:
                assert all(fast(a,b,r,3)==0 for r in range(1,p))
            else:
                assert fast(a,b,k,3)==n,(a,b,k,n,fast(a,b,k,3))
                assert all(fast(a,b,r,3)==0 for r in range(1,k)),(a,b,k)
            c2+=1
    print('onset + exact phase multiplicity agreements:',c2)
    rng=Random(16481)
    for _ in range(1000):
        a=rng.randrange(1,3000)
        b=rng.randrange(1,3000)
        k=rng.randrange(1,10**12)
        q=rng.randrange(2,20)
        p=a+b
        if p>5000: continue
        assert fast(a,b,k,q)==direct(a,b,k,q),(a,b,k,q)
    print('random large-period/large-length agreements: passed')

if __name__=='__main__':check()
