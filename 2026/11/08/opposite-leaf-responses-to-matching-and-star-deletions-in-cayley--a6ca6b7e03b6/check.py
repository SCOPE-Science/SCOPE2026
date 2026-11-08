"""Independent exact checks for a pair of edge-deletion UST leaf laws.

Run: python check.py (Python 3, standard library only).
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def mat_tau(n, r):
    if r == 0:
        return n ** (n - 2)
    return n ** (n-r-2) * (n-2)**r


def star_tau(n, r):
    if r == 0:
        return n ** (n - 2)
    return n ** (n-r-2) * (n-1)**(r-1) * (n-r-1)


def predicted_leaves(n, r, shape):
    baseline = Fraction(n*(n-1)**(n-2), n**(n-2))
    if shape == 'matching':
        a = Fraction(n*(n-3), (n-1)*(n-2))
        return baseline*(1+Fraction(2*r, n*(n-3)))*a**r
    if shape == 'star':
        return baseline*(Fraction(1,n)*Fraction(n,n-1)**r +
                         Fraction(n-1,n)*Fraction(n*(n-2),(n-1)**2)**r)
    raise ValueError(shape)


def edge_set(n, r, shape):
    bad = {(2*i,2*i+1) for i in range(r)} if shape == 'matching' else {(0,i+1) for i in range(r)}
    return [(i,j) for i in range(n) for j in range(i+1,n) if (i,j) not in bad]


def exact_enumeration(n, r, shape):
    edges=edge_set(n,r,shape)
    total=0; leaves=0
    for es in combinations(edges,n-1):
        par=list(range(n)); deg=[0]*n
        def find(x):
            while par[x]!=x:
                x=par[x]
            return x
        good=True
        for x,y in es:
            a,b=find(x),find(y)
            if a==b:
                good=False;break
            par[a]=b
            deg[x]+=1;deg[y]+=1
        if good:
            total+=1;leaves+=deg.count(1)
    return total, Fraction(leaves,total)


def bareiss_det(a):
    n=len(a); m=[row[:] for row in a]; sign=1; last=1
    for k in range(n-1):
        if m[k][k]==0:
            p=next((i for i in range(k+1,n) if m[i][k]),None)
            if p is None:return 0
            m[p],m[k]=m[k],m[p];sign=-sign
        pivot=m[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                m[i][j]=(m[i][j]*pivot - m[i][k]*m[k][j])//last
        for i in range(k+1,n):m[i][k]=0
        last=pivot
    return sign*m[n-1][n-1]


def tau_from_matrix(n, edges):
    m=[[0]*(n-1) for _ in range(n-1)]
    for i,j in edges:
        if i<n-1:m[i][i]+=1
        if j<n-1:m[j][j]+=1
        if i<n-1 and j<n-1:m[i][j]-=1;m[j][i]-=1
    return bareiss_det(m)


def leaf_expected_from_minors(n, edges):
    t=tau_from_matrix(n,edges)
    out=Fraction()
    for u in range(n):
        reduced={v:i for i,v in enumerate([v for v in range(n) if v!=u])}
        er=[(reduced[a],reduced[b]) for a,b in edges if a!=u and b!=u]
        degree=sum(u in e for e in edges)
        out+=Fraction(degree*tau_from_matrix(n-1,er),t)
    return t,out


def run():
    assertions=0
    for n in range(4,12):
        base=predicted_leaves(n,0,'matching')
        for r in range(2,n//2+1):
            em=predicted_leaves(n,r,'matching')
            es=predicted_leaves(n,r,'star')
            assert em<base<es;assertions+=2
            for kind in ('matching','star'):
                edges=edge_set(n,r,kind)
                t, e=leaf_expected_from_minors(n,edges)
                want_t=mat_tau(n,r) if kind=='matching' else star_tau(n,r)
                assert t==want_t and e==predicted_leaves(n,r,kind), (n,r,kind,t,e,want_t)
                assertions+=2
                if n<=7:
                    brute_t,brute_e=exact_enumeration(n,r,kind)
                    assert t==brute_t and e==brute_e
                    assertions+=2
    for n in range(5,12):
        base=predicted_leaves(n,0,'matching')
        for r in range(n//2+1,n-1):
            es=predicted_leaves(n,r,'star')
            assert es>base; assertions+=1
            t,e=leaf_expected_from_minors(n,edge_set(n,r,'star'))
            assert t==star_tau(n,r) and e==es;assertions+=1
            if n<=7:
                bt,be=exact_enumeration(n,r,'star')
                assert (t,e)==(bt,be);assertions+=1
    assert predicted_leaves(10,1,'matching')==predicted_leaves(10,1,'star')==predicted_leaves(10,0,'matching')
    assertions+=1
    print(f'VERIFY_OK {assertions} exact assertions')

if __name__=='__main__':run()
