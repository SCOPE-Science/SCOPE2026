"""Finite verification of K-preconditional isomorphism spectra.
No third-party dependencies. Run: python verification/exhaustive.py.
"""
import itertools
from collections import Counter


def lattice(m):
    top=m+1
    def le(a,b):return a==0 or a==b or b==top
    def meet(a,b):
        if a==top:return b
        if b==top:return a
        return a if a==b else 0
    return le,meet

def good(a,m):
    top=m+1
    le,meet=lattice(m)
    N=m+2
    for p,q,r in itertools.product(range(N),repeat=3):
        if not le(a[top][p],p):return False
        if not le(meet(p,q),a[p][q]):return False
        if not le(a[p][q],a[p][meet(p,q)]):return False
        if not le(a[p][meet(q,r)],a[p][q]):return False
        z=meet(p,q)
        if not le(a[p][a[z][r]],a[z][r]):return False
    return True

def candidates(m):
    n=m+2;top=m+1;le,_=lattice(m)
    # P3/P4 reduce each atom row to two values. P2 allows v in {i, top}.
    choices=[]
    for i in range(1,top):
        choices.append([(u,v) for u in range(n) for v in (i,top) if le(u,v)])
    for w in range(n):
        for rows in itertools.product(*choices):
            table=[[w]*n]+[[v if j in (i,top) else u for j in range(n)] for i,(u,v) in enumerate(rows,1)]+[list(range(n))]
            if good(table,m):yield tuple(tuple(r) for r in table)

def canonical(table,m,perms):
    top=m+1;n=m+2
    forms=[]
    for p in perms:
        perm=(0,)+p+(top,)
        inv=[0]*n
        for i,j in enumerate(perm):inv[j]=i
        forms.append(tuple(perm[table[inv[i]][inv[j]]] for i in range(n) for j in range(n)))
    return min(forms)

def formula(m):
    from fractions import Fraction
    from math import factorial
    def parts(n,lower=1):
        if n==0:
            yield ()
        for a in range(lower,n+1):
            for sub in parts(n-a,a):yield (a,)+sub
    val=Fraction(0)
    for p in parts(m):
        c=Counter(p)
        z=1;prod=1
        for d,k in c.items():z*=d**k*factorial(k)
        for d,k in c.items():
            nfix=sum(e*r for e,r in c.items() if d%e==0)
            prod*=(3+nfix)**k
        val+=Fraction(prod,z)
    assert val.denominator==1
    return int(val)+(m+1)**2

for m in (2,3,4):
    perms=list(itertools.permutations(range(1,m+1)))
    num=0;classes=set()
    for t in candidates(m):
        num+=1;classes.add(canonical(t,m,perms))
    expected_labeled=(m+3)**m+2**m+2*m*3**(m-1)
    expected_classes=formula(m)
    assert num==expected_labeled,(m,num,expected_labeled)
    assert len(classes)==expected_classes,(m,len(classes),expected_classes)
    print('m=',m,'labeled=',num,'isomorphism_classes=',len(classes),'OK')
for m in range(5,11):
    print('m=',m,'orbit_formula=',formula(m),'OK')
print('VERIFY_OK')
