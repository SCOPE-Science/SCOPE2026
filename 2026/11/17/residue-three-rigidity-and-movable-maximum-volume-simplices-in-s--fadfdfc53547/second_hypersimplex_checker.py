"""Exact finite corroboration of maximal-simplex configurations of hypersimplices.
No finite run is a substitute for the arbitrary-dimensional proof.
"""
from itertools import combinations
from collections import Counter
from math import factorial, comb

def det(A):
    """Fraction-free exact integer determinant (Bareiss)."""
    B=[list(row) for row in A]; n=len(B); sign=1; previous=1
    for j in range(n-1):
        if B[j][j]==0:
            i=next((i for i in range(j+1,n) if B[i][j]),None)
            if i is None:return 0
            B[i],B[j]=B[j],B[i];sign=-sign
        pivot=B[j][j]
        for i in range(j+1,n):
            for k in range(j+1,n):
                v=B[i][k]*pivot-B[i][j]*B[j][k]
                assert v%previous==0
                B[i][k]=v//previous
            B[i][j]=0
        previous=pivot
    return sign*B[n-1][n-1]

def component_count(n, edges):
    p=list(range(n));size=[1]*n
    def find(x):
        while p[x]!=x:x=p[x]
        return x
    for a,b in edges:
        a,b=find(a),find(b)
        if a!=b:p[a]=b;size[b]+=size[a]
    return len(set(find(x) for x in range(n)))

def max_count(n):
    k,r=divmod(n,3)
    if r==0: return factorial(n)//(6**k*factorial(k))
    if r==1:return factorial(n)//(2*6**(k-1)*factorial(k-1))
    first=factorial(n)*27//(20*6**(k-1)*factorial(k-1))
    second=factorial(n)//(8*6**(k-2)*factorial(k-2)) if k>=2 else 0
    return first+second

def check(n):
    edges=list(combinations(range(n),2)); values=Counter(); max_sets=[]
    for subset in combinations(range(len(edges)),n):
        E=[edges[i] for i in subset]
        A=[[int(i==a or i==b) for a,b in E] for i in range(n)]
        d=abs(det(A));values[d]+=1
        assert d==0 or d==2**component_count(n,E)
        if d==2**(n//3): max_sets.append(frozenset(subset))
    assert max(values)==2**(n//3)
    assert len(max_sets)==max_count(n),(n,len(max_sets),max_count(n))
    if n%3==0:
        for subset in max_sets:
            assert not any((len(subset&other)==n-1) for other in max_sets if subset!=other)
    print('n',n,'tested',sum(values.values()),'det_levels',dict(sorted(values.items())), 'maximizers',len(max_sets))

for n in range(3,8):check(n)
print('SECOND_HYPERSIMPLEX_EXACT_CHECK_PASS')
