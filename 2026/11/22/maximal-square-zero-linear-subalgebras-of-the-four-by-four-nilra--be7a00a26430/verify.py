#!/usr/bin/env python3
"""Exhaustive finite-field tests for square-zero spaces in a 4x4 nilradical.
Runs with the Python standard library. F_2 and F_3 are checked independently.
"""
from itertools import combinations, product
from collections import Counter

N=6

def rref_spaces(q,k):
    """Enumerate each k-plane exactly once by unique reduced-row-echelon basis."""
    for pivots in combinations(range(N),k):
        spots=[(i,j) for i,p in enumerate(pivots) for j in range(p+1,N) if j not in pivots]
        for values in product(range(q),repeat=len(spots)):
            B=[[int(j==p) for j in range(N)] for p in pivots]
            for (i,j),v in zip(spots,values): B[i][j]=v
            yield tuple(tuple(x) for x in B)

def Q(x,q):
    a,b,c,d,e,f=x
    return ((a*d)%q,(d*f)%q,(a*e+b*f)%q)

def good(B,q):
    for x in B:
        if Q(x,q)!=(0,0,0):return False
    for x,y in combinations(B,2):
        z=tuple((a+b)%q for a,b in zip(x,y))
        if Q(z,q)!=(0,0,0):return False
    return True

def rref_rank(M,q):
    A=[list(row) for row in M]
    if not A:return 0
    row=0
    for col in range(N):
        pos=next((i for i in range(row,len(A)) if A[i][col]%q),None)
        if pos is None:continue
        A[row],A[pos]=A[pos],A[row]
        inv=pow(A[row][col]%q,-1,q)
        A[row]=[(x*inv)%q for x in A[row]]
        for i in range(len(A)):
            if i!=row and A[i][col]%q:
                z=A[i][col]%q
                A[i]=[(a-z*b)%q for a,b in zip(A[i],A[row])]
        row+=1
        if row==len(A):break
    return row

def intersection_dim(B,C,q):
    return len(B)+len(C)-rref_rank(B+C,q)

def squarezero_spaces(q):
    tab={}
    for k in [3,4,5,6]:
        tab[k]=[B for B in rref_spaces(q,k) if good(B,q)]
    return tab

def multiplication(x,y,q):
    a,b,c,d,e,f=x; A,B,C,D,E,F=y
    # E13,E14,E24 coordinates of product
    return ((a*D)%q,(a*E+b*F)%q,(d*F)%q)

def zero_product(B,q):
    return all(multiplication(x,y,q)==(0,0,0) and multiplication(y,x,q)==(0,0,0) for x,y in combinations(B,2))

def enumerate_vectors(B,q):
    return {tuple(sum(coeff*x[j] for coeff,x in zip(cs,B))%q for j in range(N)) for cs in product(range(q),repeat=len(B))}

def check(q):
    spaces=squarezero_spaces(q)
    assert len(spaces[4])==1 and not spaces[5] and not spaces[6]
    assert len(spaces[3])==q**3+q**2+q+1+2*q+1
    E=spaces[4][0]
    assert all(row[0]==row[5]==0 for row in E)
    maxs=[E]+[B for B in spaces[3] if intersection_dim(B,E,q)<3]
    assert len(maxs)==2*(q+1)
    assert Counter(map(len,maxs))=={4:1,3:2*q+1}
    assert sum(not zero_product(B,q) for B in maxs)==q-1
    assert sum(any(multiplication(x,y,q)!=multiplication(y,x,q) for x,y in combinations(B,2)) for B in maxs)==(q-1 if q!=2 else 0)
    edges=[(i,j) for i,j in combinations(range(len(maxs)),2) if intersection_dim(maxs[i],maxs[j],q)==2]
    assert len(edges)==(q+1)**2
    assert all(sum(i in pair for pair in edges)==q+1 for i in range(len(maxs)))
    # A connected (q+1)-regular graph on 2(q+1) vertices is K_(q+1,q+1)
    # only after explicitly checking the adjacency bipartition.
    adj={i:set() for i in range(len(maxs))}
    for i,j in edges:adj[i].add(j);adj[j].add(i)
    side=set(adj[0]); other=set(range(len(maxs)))-side
    assert len(side)==len(other)==q+1
    assert all(adj[i]==side for i in other)
    assert all(adj[j]==other for j in side)
    counts=Counter()
    for x in product(range(q),repeat=N):
        if Q(x,q)!=(0,0,0):continue
        containers=sum(x in enumerate_vectors(B,q) for B in maxs)
        if x==(0,0,0,0,0,0):expected=2*(q+1)
        elif x[0]==x[1]==x[3]==x[4]==x[5]==0:expected=2*(q+1)
        elif x[3]!=0:expected=1
        else:expected=2
        assert containers==expected,(q,x,containers,expected)
        counts[containers]+=1
    assert sum(counts.values())==2*q**4-q**2
    print('q=%d: valid_3spaces=%d valid_4spaces=1 maximal=%d nonzero_product=%d edge_count=%d incidence=%s PASS'%(
        q,len(spaces[3]),len(maxs),q-1,len(edges),dict(sorted(counts.items()))))

if __name__=='__main__':
    for q in [2,3]:check(q)
    print('ALL CHECKS PASSED')
