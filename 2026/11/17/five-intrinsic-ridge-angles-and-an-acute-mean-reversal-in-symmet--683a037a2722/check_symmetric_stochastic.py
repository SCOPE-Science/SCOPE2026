"""Exact independent finite checks for the symmetric stochastic polytope theorem.
Uses the off-diagonal tangent basis and exact rational arithmetic only.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def inv(A):
    n=len(A)
    aug=[[Q(x) for x in row]+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if aug[i][k])
        aug[k],aug[pivot]=aug[pivot],aug[k]
        z=aug[k][k]
        aug[k]=[x/z for x in aug[k]]
        for i in range(n):
            if i!=k:
                z=aug[i][k]
                if z:aug[i]=[x-z*y for x,y in zip(aug[i],aug[k])]
    return [row[n:] for row in aug]


def classification(n,e,f):
    if e[0]==e[1] and f[0]==f[1]:return 'LL'
    if (e[0]==e[1])!=(f[0]==f[1]):
        l,o=(e,f) if e[0]==e[1] else (f,e)
        return 'LE_inc' if l[0] in o else 'LE_non'
    return 'EE_inc' if len(set(e)&set(f)) else 'EE_non'


def witness(n,e,f):
    eps=Q(1,20*n)
    X=[[Q(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            X[i][j]=X[j][i]=eps if (i,j) not in (e,f) else Q(0)
    loops=[a[0] for a in (e,f) if a[0]==a[1]]
    if len(loops)==2:
        i,j=loops
        X[i][j]=X[j][i]=Q(3,4)
        for k in range(n):
            if k not in (i,j):
                X[i][k]=X[k][i]=Q(1,4*(n-2))
                X[j][k]=X[k][j]=Q(1,4*(n-2))
    elif len(loops)==1:
        i=loops[0]
        other = f if e==(i,i) else e
        if i in other:
            if n==3:return None
            j=next(k for k in other if k!=i)
            for k in range(n):
                if k!=i and k!=j:X[i][k]=X[k][i]=Q(1,n-2)
        else:
            for k in range(n):
                if k!=i:X[i][k]=X[k][i]=Q(1,n-1)
    for i in range(n):
        X[i][i]=1-sum(X[i][j] for j in range(n) if j!=i)
    return X


def one(n):
    edges=list(combinations(range(n),2))
    facets=[(i,i) for i in range(n)]+edges
    T=len(edges)
    G=[[Q(4 if i==j else (1 if set(edges[i])&set(edges[j]) else 0)) for j in range(T)] for i in range(T)]
    Ginv=inv(G)
    C={}
    for facet in facets:
        if facet[0]==facet[1]:
            i=facet[0]; C[facet]=[Q(-int(i in e)) for e in edges]
        else:
            C[facet]=[Q(int(e==facet)) for e in edges]
    norm={a:sum(C[a][i]*Ginv[i][j]*C[a][j] for i in range(T) for j in range(T)) for a in facets}
    D=n*n-2*n+2
    expected_norm={'L':Q((n-1)**2,n*n),'E':Q(D,2*n*n)}
    assert all(norm[a]==expected_norm['L' if a[0]==a[1] else 'E'] for a in facets)
    expected_gram={'LL':Q(1,n*n), 'LE_inc':Q(-(n-1),n*n), 'LE_non':Q(1,n*n),
                   'EE_inc':Q(-(n-2),2*n*n), 'EE_non':Q(1,n*n)}
    observed={k:0 for k in expected_gram}
    ridge=0
    for e,f in combinations(facets,2):
        k=classification(n,e,f)
        g=sum(C[e][i]*Ginv[i][j]*C[f][j] for i in range(T) for j in range(T))
        assert g==expected_gram[k],(n,e,f,k,g,expected_gram[k])
        X=witness(n,e,f)
        if n==3 and k=='LE_inc':
            assert X is None
            continue
        assert X is not None
        assert all(X[i][j]==X[j][i] for i in range(n) for j in range(n))
        assert all(sum(X[i])==1 for i in range(n))
        for a in facets:
            if a in (e,f):assert X[a[0]][a[1]]==0,(n,e,f,a,X)
            else:assert X[a[0]][a[1]]>0,(n,e,f,a,X)
        observed[k]+=1;ridge+=1
    expected_counts={'LL':comb(n,2),'LE_inc': n*(n-1) if n>=4 else 0,
                     'LE_non':comb(n,2)*(n-2),'EE_inc':n*comb(n-1,2),'EE_non':3*comb(n,4)}
    assert observed==expected_counts, (n,observed,expected_counts)
    assert ridge==(comb(n*(n+1)//2,2) if n>=4 else 9)
    print('PASS n=',n,'dimension=',T,'facets=',len(facets),'ridges=',ridge,'classes=',observed)

if __name__=='__main__':
    for n in range(3,8):one(n)
    print('SYMMETRIC_STOCHASTIC_RIDGE_EXACT_PASS')
