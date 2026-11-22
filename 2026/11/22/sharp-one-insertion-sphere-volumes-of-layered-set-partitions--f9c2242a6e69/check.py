"""Standalone exact check of layered-partition insertion formula and extrema.
No external dependencies. Python 3.10+.
"""
from itertools import product
from math import comb
from collections import defaultdict

def normal(w):
    seen={}; output=[]
    for x in w:
        if x not in seen: seen[x]=len(seen)
        output.append(seen[x])
    return tuple(output)

def layered(a):
    return tuple(j for j,length in enumerate(a) for _ in range(length))

def compositions(n,k):
    if k==1:
        yield (n,)
        return
    for first in range(1,n-k+2):
        for tail in compositions(n-first,k-1):yield (first,)+tail

def insertion_outputs(a):
    w=layered(a); k=len(a)
    return {normal(w[:i]+(b,)+w[i:]) for i in range(len(w)+1) for b in range(k+1)}

def triangle_penalty(a):
    s=0; total=0
    for x in a+(2,):
        if x==1:s+=1
        else:
            total+=s*(s+1)//2
            s=0
    return total

def formula(a):
    n=sum(a);k=len(a)
    return (n+1)*(k+1)-n-triangle_penalty(a)

def expected_bounds(n,k):
    t=min(k,n-k)
    s=k-t; L=t+1
    a,b=divmod(s,L)
    tmin=(L-b)*a*(a+1)//2 + b*(a+1)*(a+2)//2
    tmax=k*(k+1)//2 if n==k else k*(k-1)//2
    base=(n+1)*(k+1)-n
    return base-tmax,base-tmin

def all_rgfs(n):
    if not n:
        yield ();return
    for w in all_rgfs(n-1):
        for x in range(max(w,default=-1)+2):
            if not w and x!=0:continue
            yield w+(x,)

def independent_outputs(n):
    by_target=defaultdict(set)
    for Q in all_rgfs(n+1):
        for i in range(n+1):
            P=normal(Q[:i]+Q[i+1:]);by_target[P].add(Q)
    return by_target

def check():
    comparisons=0; classes=0
    for n in range(1,11):
        for k in range(1,n+1):
            counts=[]; shapes=[]
            for a in compositions(n,k):
                actual=len(insertion_outputs(a))
                predicted=formula(a)
                assert actual==predicted,(n,k,a,actual,predicted)
                counts.append(actual);shapes.append(a)
                comparisons+=1
            lo,hi=expected_bounds(n,k)
            assert min(counts)==lo and max(counts)==hi,(n,k,lo,hi,min(counts),max(counts))
            t=min(k,n-k);s=k-t;L=t+1; q,r=divmod(s,L)
            max_count=1 if n==k else (comb(n-k-1,k-1) if n>=2*k else comb(L,r))
            min_count=1 if n==k or k==1 else 2
            assert counts.count(hi)==max_count,('max',n,k,counts.count(hi),max_count)
            assert counts.count(lo)==min_count,('min',n,k,counts.count(lo),min_count)
            classes+=1
    # Independent reverse test: enumerate all superpartitions Q and delete each element.
    independent=0
    for n in range(1,8):
        inv=independent_outputs(n)
        for k in range(1,n+1):
            for a in compositions(n,k):
                w=layered(a)
                assert len(inv[w])==formula(a),(n,k,a,len(inv[w]),formula(a))
                independent+=1
    print('VERIFY_OK', 'forward_layered_cases',comparisons,'extremal_strata',classes,
          'independent_reverse_cases',independent, 'max_n',10)
if __name__=='__main__':check()
