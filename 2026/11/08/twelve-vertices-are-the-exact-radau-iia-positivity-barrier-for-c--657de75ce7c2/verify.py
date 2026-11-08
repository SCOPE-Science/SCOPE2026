"""Exact-rational finite regression checks for a graph-heat spectral theorem.

No numerical approximation is used; the proof for all graph sizes is in RESULT.md.
Run: python3 verify.py
"""
from fractions import Fraction as F
from itertools import accumulate


def r(x):
    x=F(x)
    return 2*(3-x)/(x*x+4*x+6)


def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def inv(a):
    n=len(a)
    aug=[[F(a[i][j]) for j in range(n)] + [F(i==j) for j in range(n)]
         for i in range(n)]
    for j in range(n):
        k=next(k for k in range(j,n) if aug[k][j])
        aug[k],aug[j]=aug[j],aug[k]
        z=aug[j][j]; aug[j]=[v/z for v in aug[j]]
        for i in range(n):
            if i==j: continue
            z=aug[i][j]
            if z: aug[i]=[u-z*v for u,v in zip(aug[i],aug[j])]
    return [row[n:] for row in aug]


def graph_laplacian(parts):
    n=sum(parts)
    labels=[v for i,p in enumerate(parts) for v in [i]*p]
    return [[F(n-parts[labels[i]]) if i==j else
             F(-1) if labels[i]!=labels[j] else F(0)
             for j in range(n)] for i in range(n)],labels


def transition(parts,h):
    n=sum(parts);L,labels=graph_laplacian(parts)
    L2=mm(L,L)
    den=[[F(i==j)+F(2,3)*h*L[i][j]+h*h*L2[i][j]/6
          for j in range(n)] for i in range(n)]
    num=[[F(i==j)-h*L[i][j]/3 for j in range(n)] for i in range(n)]
    return mm(num,inv(den)),labels


def expected_entry(parts,h,i,j):
    n=sum(parts)
    labels=[v for k,p in enumerate(parts) for v in [k]*p]
    if labels[i]!=labels[j]:return (1-r(n*h))/n
    p=parts[labels[i]]; q=n-p
    if i==j:
        return F(1,n)+(1-F(1,p))*r(q*h)+(F(1,p)-F(1,n))*r(n*h)
    return F(1,n)-r(q*h)/p+(F(1,p)-F(1,n))*r(n*h)


def witness_formula(n,p):
    t=F(p,n)
    return -(n*(255-110*t+15*t*t)-2848+1056*t)/(51*n*(51-22*t+3*t*t))


def verify():
    tests=0; entries=0; rows=0
    cases=[(1,1),(1,2),(2,2),(1,5),(2,4),(3,3),(1,10),(2,9),(3,8),
           (5,6),(1,11),(2,10),(3,9),(4,8),(5,7),(6,6),(1,12),
           (2,11),(4,9),(2,2,2,2,2,2),(3,4,5),(1,1,1,1,1,1,1,1,1,1,1,1),
           (2,3,4),(1,2,3,4),(4,4,4),(3,3,3,3),(1,1,1,1,1,1,1,1,1,1,1),
           (2,2,2,2,2),(1,2,2,2,2),(1,1,2,3,4)]
    for parts in cases:
        n=sum(parts)
        for h in (F(0),F(1,9),F(1,2),F(5,3),F(20,1)):
            T,labels=transition(parts,h)
            assert all(sum(row,F(0))==1 for row in T)
            rows+=n
            for i in range(n):
                for j in range(n):
                    v=expected_entry(parts,h,i,j)
                    assert T[i][j]==v,(parts,h,i,j,T[i][j],v)
                    if i!=j and h>0:assert v>0
                    if n<=11:assert v>=0
                    entries+=1
            tests+=1
        if n>=12:
            for part_idx,p in enumerate(parts):
                h=F(8,n-p)
                T,labels=transition(parts,h)
                i=labels.index(part_idx)
                assert T[i][i]==witness_formula(n,p)
                assert T[i][i]<0
                tests+=1
    for n in range(12,51):
        for p in range(1,n):
            assert witness_formula(n,p)<0
    print(f'PASS {tests} exact matrix/witness cases, {entries} exact entries, {rows} row sums;')
    print('PASS witness expression negative for 741 integer pairs of orders 12..50;')
    print('NOTE finite tests are not a proof for unbounded graph order or all timesteps.')

if __name__=='__main__':verify()
