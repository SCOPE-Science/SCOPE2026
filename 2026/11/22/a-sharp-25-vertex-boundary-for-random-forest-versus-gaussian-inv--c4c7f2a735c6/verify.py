"""Exact arithmetic checks for the forest/Gaussian variance extremal theorem.

No external packages and no Monte Carlo. The general theorem is analytic.
"""
from fractions import Fraction as Q
from math import comb

checks = 0

def eq(x, y):
    global checks
    assert x == y, (x, y)
    checks += 1

def vf(spectrum, q):
    return sum((q * lam / (lam + q)**2 for lam in spectrum), Q(0))

def vg(spectrum, q):
    return 2 * sum((q*q / (lam+q)**2 for lam in spectrum), Q(0))

def cert(spectrum, q):
    n = len(spectrum)
    assert spectrum[0] == 0
    return Q(25-n, 12) + sum((((lam-5*q)/(lam+q))**2 / 12 for lam in spectrum[1:]), Q(0))

# Scalar certificate, with varied rational eigenvalues and regularization.
for lam in (Q(0), Q(1,3), Q(1), Q(2), Q(5), Q(20), Q(120)):
    for q in (Q(1,7), Q(1), Q(3), Q(17,2)):
        eq(q*(2*q-lam)/(lam+q)**2,
           (lam-5*q)**2/(12*(lam+q)**2)-Q(1,12))

# Equality and sharp dimensional boundary, exact fractions.
for n in range(2, 75):
    for q in (Q(1,2), Q(1), Q(7,3)):
        eig = [Q(0)] + [5*q]*(n-1)
        eq(vg(eig, q)-vf(eig, q), cert(eig, q))
        eq(vf(eig, q)-vg(eig, q), Q(n-25,12))

# The first strict reversal, n=26, q=1 and edge weight w=5/26.
E26 = [Q(0)]+[Q(5)]*25
eq(vf(E26, Q(1)), Q(125,36))
eq(vg(E26, Q(1)), Q(122,36))
eq(vf(E26, Q(1))-vg(E26, Q(1)), Q(1,12))

# Fixed n: strict inequality at x=5 exactly for n>=26.
for n in range(2, 80):
    e=[Q(0)]+[Q(5)]*(n-1)
    eq((vf(e,Q(1))>vg(e,Q(1))), n>=26)

# Confirm the complete-graph quadratic and its roots for n=26.
for x in (Q(1),Q(4),Q(5),Q(13,2),Q(7),Q(20)):
    q=Q(1); spec=[Q(0)]+[x]*25
    eq(vf(spec,q)-vg(spec,q),(-2*x*x+21*x-52)/(x+1)**2)
for x in (Q(4),Q(13,2)):
    eq((-2*x*x+21*x-52),Q(0))

# Direct independent forest root distribution on complete graph:
# Z(q)=q(q+nw)^(n-1); root count =1+Binomial(n-1,q/(q+nw)).
for n in range(2,9):
    q=Q(2,3); w=Q(5,2*n); lam=n*w
    p=q/(q+lam)
    probabilities=[Q(comb(n-1,k))*p**k*(1-p)**(n-1-k) for k in range(n)]
    eq(sum(probabilities),Q(1))
    avg=sum((Q(k+1)*probabilities[k] for k in range(n)),Q(0))
    vr=sum(((Q(k+1)-avg)**2*probabilities[k] for k in range(n)),Q(0))
    eq(avg,Q(1)+(n-1)*p)
    eq(vr,vf([Q(0)]+[lam]*(n-1),q))

# Non-flat spectra have a strictly positive certificate residual.
for spec in ([Q(0),Q(3),Q(5)],
             [Q(0),Q(1),Q(7),Q(14)],
             [Q(0),Q(1,2),Q(2),Q(5),Q(11)]):
    for q in (Q(1),Q(3)):
        eq(vg(spec,q)-vf(spec,q),cert(spec,q))
        assert cert(spec,q)>Q(25-len(spec),12)
        checks+=1

print(f"PASS: {checks} exact rational checks")

# Independent small-graph check: enumerate every rooted forest on a weighted
# tree and compute Gaussian moments from an exact inverse matrix.
from itertools import combinations

def mat_inverse(A):
    n=len(A)
    C=[list(row)+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if C[i][j])
        C[j],C[pivot]=C[pivot],C[j]
        fac=C[j][j]
        C[j]=[v/fac for v in C[j]]
        for i in range(n):
            if i!=j:
                fac=C[i][j]
                C[i]=[u-fac*v for u,v in zip(C[i],C[j])]
    return [row[n:] for row in C]

def exact_tree_check(n, edges, q):
    # Explicit forest enumeration, including root multiplicities.
    z=Q(0);r1=Q(0);r2=Q(0)
    for mask in range(1<<len(edges)):
        par=list(range(n))
        def root(i):
            while par[i]!=i:i=par[i]
            return i
        weight=Q(1)
        for j,(a,b,w) in enumerate(edges):
            if mask & (1<<j):
                A,B=root(a),root(b)
                assert A!=B
                par[A]=B;weight*=w
        sizes={}
        for i in range(n):
            v=root(i);sizes[v]=sizes.get(v,0)+1
        for size in sizes.values():weight*=size
        r=len(sizes);term=weight*q**r
        z+=term;r1+=r*term;r2+=r*r*term
    forestvar=r2/z-(r1/z)**2
    L=[[Q(0) for _ in range(n)] for _ in range(n)]
    for a,b,w in edges:
        L[a][a]+=w;L[b][b]+=w;L[a][b]-=w;L[b][a]-=w
    A=[[L[i][j]+(q if i==j else 0) for j in range(n)] for i in range(n)]
    P=mat_inverse(A)
    P=[[q*x for x in row] for row in P]
    tr=lambda M:sum(M[i][i] for i in range(n))
    P2=[[sum(P[i][k]*P[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    eq(r1/z,tr(P))
    eq(forestvar,tr(P)-tr(P2))
    eq(2*tr(P2),2*sum(P[i][j]*P[i][j] for i in range(n) for j in range(n)))

for n,edges in [
    (2,[(0,1,Q(2))]),
    (3,[(0,1,Q(1)),(1,2,Q(3,2))]),
    (4,[(0,1,Q(2)),(0,2,Q(1,3)),(2,3,Q(4))]),
    (5,[(0,1,Q(1)),(0,2,Q(2)),(0,3,Q(1,2)),(3,4,Q(3))]),
]:
    for q in (Q(1),Q(5,3)):
        exact_tree_check(n,edges,q)
print(f"PASS: {checks} total exact rational checks (including forest enumeration)")
