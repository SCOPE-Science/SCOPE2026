"""Exact finite checks of a continuum tree boundary-trace theorem.

The universal inequality is established by the proof, not by enumeration.
Uses only the Python standard library.
"""
from fractions import Fraction as F
from itertools import product
from collections import deque


def prufer_tree(code):
    n = len(code) + 2
    deg = [1] * n
    for v in code:
        deg[v] += 1
    ed = []
    for v in code:
        u = min(i for i, d in enumerate(deg) if d == 1)
        ed.append((u, v))
        deg[u] -= 1
        deg[v] -= 1
    a, b = [i for i, d in enumerate(deg) if d == 1]
    ed.append((a, b))
    return ed


def cut_constant(n, edges):
    g = [[] for _ in range(n+1)]
    for u,v in edges:
        g[u].append(v); g[v].append(u)
    leaves={v for v in range(n+1) if len(g[v]) == 1}
    best=F(0)
    for u,v in edges:
        for start, blocked in ((u,v),(v,u)):
            seen={start}
            todo=[start]
            while todo:
                w=todo.pop()
                for z in g[w]:
                    if (w==start and z==blocked) or z in seen:
                        continue
                    seen.add(z); todo.append(z)
            s=len(seen)-1  # number of complete edges on this side
            r=len(seen&leaves)
            q=len(leaves)-r
            value=F(r*(n-s)**2+q*s*s,n*n)
            if value>best:best=value
    return best


def theoretical(n):
    if n<=4:return F(1)
    if n%2==0:return F(n-1,4)
    return F((n-1)*(n*n+1),4*n*n)


def double_star(r,q):
    # centers 0 and 1; all other vertices pendant to a center
    return [(0,1)]+[(0,2+i) for i in range(r)]+[(1,2+r+i) for i in range(q)]

checks=0
# All labeled trees through seven edges (8 vertices). No sampling here.
for n in range(1,8):
    target=theoretical(n)
    best=F(0)
    num_best=0
    for code in product(range(n+1),repeat=n-1):
        value=cut_constant(n,prufer_tree(code))
        assert value<=target,(n,code,value,target)
        checks+=1
        if value>best:
            best=value;num_best=1
        elif value==best:
            num_best+=1
    assert best==target,(n,best,target)
    checks+=1
    print('EXHAUSTIVE_LABELLED_TREES',n,(n+1)**(n-1),'best_squared',str(best))

# Distinct graph shapes and first transition, beyond exhaustive sizes.
for n in range(5,81):
    s=n//2; q=n-s-1
    assert s>=q>=1
    assert cut_constant(n,double_star(s,q)) == theoretical(n)
    checks+=1

# Universal upper bound is a purely rational one-variable inequality.
for n in range(2,301):
    t=theoretical(n)
    for s in range(1,n-1):
        phi=F(s*(n*n-(n+1)*s),n*n)
        assert phi<=t,(n,s,phi,t)
        checks+=1

# A ramp of length eps on the central bridge approaches the norm.
# Its endpoint trace mean is (r + eps/2)/n, variation exactly 1.
for n in range(5,81):
    r=n//2;q=n-r-1
    v=theoretical(n)
    for denominator in (10,100,1000,10000):
        eps=F(1,denominator)
        mean=(F(r)+eps/2)/n
        observed=r*(1-mean)**2+q*mean**2
        assert observed < v
        assert 0 < v-observed < F(4,denominator)
        checks+=1

print('ALL_EXACT_TREE_TRACE_TESTS_PASSED',checks)
