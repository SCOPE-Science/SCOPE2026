#!/usr/bin/env python3
"""Exact checks of signed tree/Walsh boundary claims; Python standard library only."""
from itertools import combinations, product
from collections import Counter
from heapq import heapify, heappop, heappush


def bareiss_det(A):
    A = [row[:] for row in A]
    n = len(A)
    if n == 0:
        return 1
    sign, prev = 1, 1
    for i in range(n-1):
        if A[i][i] == 0:
            j = next((j for j in range(i+1,n) if A[j][i]), None)
            if j is None:
                return 0
            A[i], A[j] = A[j], A[i]
            sign = -sign
        pivot = A[i][i]
        for j in range(i+1,n):
            for k in range(i+1,n):
                numerator = A[j][k]*pivot - A[j][i]*A[i][k]
                assert numerator % prev == 0
                A[j][k] = numerator // prev
            A[j][i] = 0
        prev = pivot
    return sign*A[-1][-1]


def signed_tree_det(n, S):
    # Delete the final vertex from the Laplacian of K_n with sign -1 on S.
    S = {tuple(sorted(e)) for e in S}
    L = [[0]*(n-1) for _ in range(n-1)]
    for i in range(n-1):
        L[i][i] = n-1-2*sum(tuple(sorted((i,j))) in S for j in range(n) if j != i)
        for j in range(n-1):
            if i != j:
                L[i][j] = -1+2*(tuple(sorted((i,j))) in S)
    return bareiss_det(L)


def is_star(E):
    return bool(E) and any(all(v in e for e in E) for v in {x for e in E for x in e})


def check_boundary(n):
    E = list(combinations(range(n),2))
    m = n//2
    zero_at_first = 0
    for k in range(m):
        for S in combinations(E,k):
            w = signed_tree_det(n,S)
            if k < m-1:
                assert w > 0, (n,k,S,w)
            else:
                assert w >= 0, (n,k,S,w)
                if w == 0:
                    assert is_star(S), (n,S)
                    zero_at_first += 1
                else:
                    assert not is_star(S), (n,S)
    from math import comb
    expected = comb(n,2) if m==2 else n*comb(n-1,m-1)
    assert zero_at_first == expected, (n,zero_at_first,expected)
    witness = [(0,i) for i in range(1,m+1)]
    assert signed_tree_det(n,witness)<0, (n,witness)
    print('exact determinant boundary PASS', n, 'first zeros',zero_at_first,
          'negative star',signed_tree_det(n,witness))


def prufer_edges(word,n):
    degree=[1]*n
    for x in word:degree[x]+=1
    leaves=[x for x in range(n) if degree[x]==1]
    heapify(leaves)
    out=[]
    for x in word:
        y=heappop(leaves)
        out.append(tuple(sorted((x,y))))
        degree[x]-=1; degree[y]-=1
        if degree[x]==1:heappush(leaves,x)
    out.append(tuple(sorted((heappop(leaves),heappop(leaves)))))
    return out


def check_prufer(n):
    E=list(combinations(range(n),2)); edge_index={e:i for i,e in enumerate(E)}
    N=1<<len(E)
    a=[0]*N
    for w in product(range(n), repeat=n-2):
        mask=sum(1<<edge_index[e] for e in prufer_edges(w,n))
        a[mask]+=1
    assert sum(a)==n**(n-2) and max(a)==1
    for bit in range(len(E)):
        h=1<<bit
        for base in range(0,N,2*h):
            for i in range(h):
                x,y=a[base+i],a[base+i+h]
                a[base+i],a[base+i+h]=x+y,x-y
    assert a[0]==n**(n-2)
    for mask,val in enumerate(a):
        if n%2:assert val % 2 == 1 and val!=0
        S=[e for i,e in enumerate(E) if mask&(1<<i)]
        if len(S) <= 3:
            assert val==signed_tree_det(n,S), (n,mask,val)
    if n%2==0:
        m=n//2
        z=[mask for mask,x in enumerate(a) if x==0 and mask.bit_count()==m-1]
        from math import comb
        expected=comb(n,2) if m==2 else n*comb(n-1,m-1)
        assert len(z)==expected
    print('independent Pruefer/FWHT PASS',n,'tree count',a[0],
          'zero total',sum(x==0 for x in a))

if __name__=='__main__':
    for n in range(3,7): check_prufer(n)
    for n in (4,6,8): check_boundary(n)
