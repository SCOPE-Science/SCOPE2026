#!/usr/bin/env python3
"""Exact certificate for one-step global-disagreement amplification on small graphs.
Only Python's standard library is required. No floating-point comparisons occur.
"""
from fractions import Fraction as F
from itertools import combinations, permutations

def add(p,q):
    r=[F(0)]*max(len(p),len(q))
    for i,a in enumerate(p):r[i]+=a
    for i,a in enumerate(q):r[i]+=a
    return r

def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r

def determinant_poly(m):
    n=len(m); out=[F(0)]*(n+1)
    for perm in permutations(range(n)):
        s=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=[F(s)]
        for i,j in enumerate(perm):term=mul(term,m[i][j])
        out=add(out,term)
    return tuple(out)

def connected(n,edges):
    seen={0}
    while True:
        new=seen|{v if u in seen else u for u,v in edges if u in seen or v in seen}
        if new==seen:return len(seen)==n
        seen=new

def signature(n, edges):
    es=set(edges);allpairs=list(combinations(range(n),2))
    return min(tuple(int(tuple(sorted((p[u],p[v]))) in es) for u,v in allpairs)
               for p in permutations(range(n)))

def spectral_polynomial(n,edges):
    A=[[F(0) for j in range(n)] for i in range(n)]
    for u,v in edges:A[u][v]=A[v][u]=F(1)
    d=[sum(row) for row in A]
    P=[[A[i][j]/d[i] for j in range(n)] for i in range(n)]
    # H projects onto differences from the last coordinate; rank n-1.
    H=[[F(int(i==j)-int(i==n-1)) for j in range(n-1)] for i in range(n)]
    # Both Gram matrices G=H^T H, K=H^T P^T B P H.
    PH=[[sum(P[i][k]*H[k][j] for k in range(n)) for j in range(n-1)] for i in range(n)]
    G=[[sum(H[i][j]*H[i][k] for i in range(n)) for k in range(n-1)] for j in range(n-1)]
    K=[[sum(PH[i][j]*PH[i][k] for i in range(n))-
        sum(PH[i][j] for i in range(n))*sum(PH[i][k] for i in range(n))/n
        for k in range(n-1)] for j in range(n-1)]
    mat=[[[K[i][j],-G[i][j]] for j in range(n-1)] for i in range(n-1)]
    return determinant_poly(mat)

# Each coefficient list is ascending in z, for det(K-zG).
examples={
 'K2':(2,[(0,1)]),
 'P3':(3,[(0,1),(1,2)]),
 'K3':(3,[(0,1),(0,2),(1,2)]),
 'P4':(4,[(0,1),(1,2),(2,3)]),
 'star':(4,[(0,1),(0,2),(0,3)]),
 'C4':(4,[(0,1),(1,2),(2,3),(0,3)]),
 'paw':(4,[(0,1),(1,2),(0,2),(2,3)]),
 'diamond':(4,[(0,1),(0,2),(0,3),(1,2),(1,3)]),
 'K4':(4,list(combinations(range(4),2)))
}
expected_counts={2:{'K2':1},3:{'P3':3,'K3':1},4:{'P4':12,'star':4,'C4':3,'paw':12,'diamond':6,'K4':1}}
expected_polynomials={
 'K2':(F(2),F(-2)),
 'P3':(F(0),F(-3),F(3)),
 'K3':(F(3,16),F(-3,2),F(3)),
 'P4':(F(1,4),F(-5,2),F(7),F(-4)),
 'star':(F(0),F(0),F(4),F(-4)),
 'C4':(F(0),F(0),F(4),F(-4)),
 'paw':(F(1,36),F(-59,72),F(23,6),F(-4)),
 'diamond':(F(0),F(-16,81),F(20,9),F(-4)),
 'K4':(F(4,729),F(-4,27),F(4,3),F(-4))
}
# Coefficients are independent expected exact determinant identities.
sigs={signature(n,e):(name,n) for name,(n,e) in examples.items()}
assert len(sigs)==len(examples),'Representative graphs overlap.'
check_count=0
for n in (2,3,4):
    counts={name:0 for name in expected_counts[n]}
    ep=list(combinations(range(n),2))
    for mask in range(1<<len(ep)):
        edges=[p for k,p in enumerate(ep) if mask>>k&1]
        if not connected(n,edges):continue
        key=signature(n,edges)
        assert key in sigs, ('unknown graph',n,edges)
        name,_=sigs[key]
        counts[name]+=1
        poly=spectral_polynomial(n,edges)
        assert poly==spectral_polynomial(*examples[name]), ('invariance',name,edges)
        check_count+=1
    assert counts==expected_counts[n], (n,counts)
    print('CONNECTED',n,'total',sum(counts.values()),'classes',counts)

for name,(n,edges) in examples.items():
    p=spectral_polynomial(n,edges)
    print('POLYNOMIAL',name,[str(c) for c in p])
    assert p==expected_polynomials[name], ('wrong polynomial',name,p,expected_polynomials[name])
# Witness P4: x=(1/2,1,0,1/2), P x=(1,1/4,3/4,0)
x=list(map(F,[F(1,2),1,0,F(1,2)]))
y=[F(1),F(1,4),F(3,4),F(0)]
P4_edges=examples['P4'][1]
d=[sum(int(i in edge) for edge in P4_edges) for i in range(4)]
assert [sum(x[j] for j in range(4) if tuple(sorted((i,j))) in P4_edges)/d[i] for i in range(4)]==y
def global_disagreement(x):
    return sum((x[i]-x[j])**2 for i,j in combinations(range(len(x)),2))
assert global_disagreement(x)==2
assert global_disagreement(y)==F(5,2)
assert global_disagreement(y)/global_disagreement(x)==F(5,4)
print('WITNESS',str(global_disagreement(x)),str(global_disagreement(y)),str(F(5,4)))
print('PASS:',check_count,'connected labeled graphs; 9 exact characteristic polynomials and rational witness.')
