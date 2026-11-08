"""Exact tests for the marked-distance law in complete bipartite uniform spanning trees.

Uses direct edge-subset enumeration, not the path-contraction formula. Run with
    python verify.py
"""
from itertools import combinations
from collections import Counter, deque
from fractions import Fraction
from math import factorial


def fall(m, k):
    if k < 0:
        raise ValueError('negative order')
    v = 1
    for j in range(k):
        v *= m-j
    return v


def tails(a, b, case, k):
    assert a >= 1 and b >= 1 and k >= 0
    if case == 'AA':
        assert a >= 2
        return Fraction(fall(a-2, k) * fall(b-1, k), (a*b)**k)
    if case == 'BB':
        return tails(b, a, 'AA', k)
    if case == 'AB':
        return Fraction(fall(a-1, k+1) * fall(b-1, k+1), (a*b)**(k+1))
    raise ValueError(case)


def distance_counts(a, b, u, v):
    n = a+b
    edges = [(i,j) for i in range(a) for j in range(a,n)]
    histogram = Counter()
    total = 0
    for subset in combinations(edges,n-1):
        graph = [[] for _ in range(n)]
        for x,y in subset:
            graph[x].append(y)
            graph[y].append(x)
        queue = deque([u])
        ds={u:0}
        while queue:
            x=queue.popleft()
            for y in graph[x]:
                if y not in ds:
                    ds[y]=ds[x]+1
                    queue.append(y)
        if len(ds)!=n:
            continue
        total+=1
        histogram[ds[v]]+=1
    return total,histogram


def determinant_integer(matrix):
    # Bareiss fraction-free determinant; independent matrix-tree verification.
    m=[list(map(int,row)) for row in matrix]
    n=len(m)
    if n==0:return 1
    if n==1:return m[0][0]
    sign=1
    prev=1
    for k in range(n-1):
        if not m[k][k]:
            for i in range(k+1,n):
                if m[i][k]:
                    m[i],m[k]=m[k],m[i]
                    sign=-sign
                    break
            else:return 0
        pivot=m[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                x=m[i][j]*pivot-m[i][k]*m[k][j]
                assert x%prev==0
                m[i][j]=x//prev
        for i in range(k+1,n):m[i][k]=0
        prev=pivot
    return sign*m[-1][-1]


def weighted_contraction_tree_count(a,b,r_a,r_b):
    # Matrix-Tree cofactor on the vertices outside the contracted path.
    left=a-r_a
    right=b-r_b
    M=[[0]*(left+right) for _ in range(left+right)]
    for i in range(left):
        M[i][i]=b
        for j in range(left,left+right):M[i][j]=M[j][i]=-1
    for j in range(left,left+right):M[j][j]=a
    return determinant_integer(M)


def check():
    tests=0
    for a in range(1,5):
        for b in range(1,5):
            if a+b>7:continue
            cases=[('AB',0,a)]
            if a>=2: cases.append(('AA',0,1))
            if b>=2: cases.append(('BB',a,a+1))
            for case,u,v in cases:
                total,hist=distance_counts(a,b,u,v)
                assert total==a**(b-1)*b**(a-1),(a,b,total)
                tests+=1
                assert sum(hist.values())==total
                tests+=1
                for k in range(0,a+b+2):
                    cut=2*k+(1 if case=='AB' else 0)
                    actual=Fraction(sum(c for d,c in hist.items() if d>cut),total)
                    expect=tails(a,b,case,k)
                    assert actual==expect,(a,b,case,k,actual,expect)
                    tests+=1
    for a in range(1,9):
        for b in range(1,9):
            for ra in range(1,a+1):
                for rb in range(1,b+1):
                    actual=weighted_contraction_tree_count(a,b,ra,rb)
                    # Written without negative exponents, as an integer count.
                    left=a-ra;right=b-rb
                    expected=(a**right)*(b**left)*(a*b-left*right)//(a*b)
                    assert actual==expected,(a,b,ra,rb,actual,expected)
                    tests+=1
    for a in range(1,30):
        for b in range(1,30):
            for case in ['AB']+(['AA'] if a>=2 else [])+(['BB'] if b>=2 else []):
                T0=1
                for k in range(0,a+b+2):
                    T=tails(a,b,case,k)
                    assert 0<=T<=T0,(a,b,case,k,T0,T)
                    T0=T
                    tests+=1
                assert T0==0
                tests+=1
    print('PASS',tests,'exact assertions')


if __name__=='__main__':check()
