#!/usr/bin/env python3
"""Direct finite-field checks of random evolution-algebra rigidity bound.
Works with prime fields for the tested finite examples. No third-party packages.
"""
from itertools import product, permutations
from math import comb, prod
from fractions import Fraction

def invertible(mat, q):
    n=len(mat); a=[list(row) for row in mat]; pivot=0
    for j in range(n):
        i=next((i for i in range(pivot,n) if a[i][j]),None)
        if i is None: continue
        a[i],a[pivot]=a[pivot],a[i]
        inverse=pow(a[pivot][j],-1,q)
        a[pivot]=[(z*inverse)%q for z in a[pivot]]
        for h in range(pivot+1,n):
            if a[h][j]:
                b=a[h][j]
                a[h]=[(a[h][k]-b*a[pivot][k])%q for k in range(n)]
        pivot+=1
    return pivot==n

def strongly_connected(mat):
    n=len(mat)
    for start in range(n):
        seen={start}; todo=[start]
        while todo:
            u=todo.pop()
            for v in range(n):
                if mat[u][v] and v not in seen:
                    seen.add(v);todo.append(v)
        if len(seen)!=n:return False
    return True

def graph_automorphisms(mat):
    n=len(mat)
    for perm in permutations(range(n)):
        if all(bool(mat[i][j])==bool(mat[perm[i]][perm[j]]) for i in range(n) for j in range(n)):
            yield perm

def monomial_aut_count(mat,q, graph_perms=None):
    n=len(mat)
    total=0
    for perm in graph_perms if graph_perms is not None else graph_automorphisms(mat):
        for lam in product(range(1,q),repeat=n):
            if all((mat[i][j]*lam[j]-lam[i]*lam[i]*mat[perm[i]][perm[j]])%q==0
                   for i in range(n) for j in range(n)):
                total+=1
    return total

def probability_bound(n,q):
    p=Fraction(q-1,q)
    alpha=p*p+(1-p)*(1-p)
    bad_sc=sum(comb(n,s)*Fraction(1,q**(s*(n-s))) for s in range(1,n))
    bad_sym=sum((n**k)*alpha**Fraction(2*n*k-k*k,2) for k in range(2,n+1))
    bad_loops=Fraction(1,q**n)
    gl_prob=prod((1-Fraction(1,q**j)) for j in range(1,n+1))
    return float((bad_sc+bad_sym+bad_loops)/gl_prob), float(gl_prob)

def test(n,q):
    tested=0;certified=0;actual_trivial=0;violations=0; hist={}
    nonsimple=0; singleton_bad=0
    for entries in product(range(q),repeat=n*n):
        mat=[entries[i*n:(i+1)*n] for i in range(n)]
        if not invertible(mat,q):continue
        tested+=1
        gp=list(graph_automorphisms(mat))
        sc=strongly_connected(mat)
        if not sc: nonsimple+=1
        single=(n>=2 and any(all(mat[i][j]==0 for j in range(n) if i!=j) or all(mat[j][i]==0 for j in range(n) if i!=j) for i in range(n)))
        if single: singleton_bad+=1
        assert not single or not sc
        certificate=(sc and any(mat[i][i] for i in range(n)) and len(gp)==1)
        if certificate: certified+=1
        count=monomial_aut_count(mat,q,gp)
        hist[count]=hist.get(count,0)+1
        if count==1:actual_trivial+=1
        if certificate and count!=1: violations+=1
    b, glp=probability_bound(n,q)
    print(f'CASE n={n} q={q} perfect={tested} certificate={certified} trivial={actual_trivial} violations={violations} bound={b:.8f} glprob={glp:.8f} notsimple={nonsimple} singleton={singleton_bad} counts={sorted(hist.items())}')
    assert nonsimple>=singleton_bad
    assert violations==0
    assert certified<=actual_trivial
    assert 1-certified/tested<=b+1.e-12
    return tested
if __name__=='__main__':
    total=sum(test(n,q) for n,q in [(1,2),(2,2),(3,2),(4,2),(1,3),(2,3),(3,3)])
    print(f'VERIFY_OK perfect_matrices={total} cases=7 certificate_no_false_positive=True')
