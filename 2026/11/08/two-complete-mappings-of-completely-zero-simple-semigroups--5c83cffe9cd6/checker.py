"""Exact finite checks for 2-complete mappings of Rees zero-matrix semigroups.

Uses only the Python standard library. No assumption of commutativity of the group.
"""
from itertools import permutations
from math import factorial

Z=('zero',)

def finite_group(degree):
    elements=list(permutations(range(degree)))
    def mul(a,b): return tuple(a[b[j]] for j in range(degree))
    def inverse(a):
        b=[0]*degree
        for j,k in enumerate(a):b[k]=j
        return tuple(b)
    return elements,mul,inverse

def verify_rees(degree,pattern,name):
    G,mul,inv=finite_group(degree)
    rows=len(pattern); cols=len(pattern[0])
    assert rows>0 and cols>0 and all(len(row)==cols for row in pattern)
    assert all(any(p is not None for p in row) for row in pattern)
    assert all(any(row[j] is not None for row in pattern) for j in range(cols))
    P=[[None if idx is None else G[idx] for idx in row] for row in pattern]
    nonzero=[(i,g,j) for i in range(cols) for g in G for j in range(rows)]
    X=[Z]+nonzero
    def times(a,b):
        if a==Z or b==Z:return Z
        i,g,l=a; j,h,m=b
        p=P[l][j]
        return Z if p is None else (i,mul(mul(g,p),h),m)
    def power(a,k):
        v=a
        for _ in range(k-1):v=times(v,a)
        return v
    full=all(p is not None for row in P for p in row)
    squares_zero=sum(power(x,2)==Z for x in nonzero)
    assert squares_zero==len(G)*sum(p is None for row in P for p in row)
    if full:
        # Invert each nonzero element in its own maximal subgroup.
        alpha={Z:Z}
        for i,g,j in nonzero:
            p=P[j][i]
            alpha[(i,g,j)]=(i,mul(mul(inv(p),inv(g)),inv(p)),j)
        assert set(alpha)==set(X) and set(alpha.values())==set(X)
        assert all(alpha[alpha[x]]==x for x in X)
        assert all(times(x,power(alpha[x],2))==alpha[x] for x in X)
    else:
        # Any bijection alpha must have alpha(0)=0, and hit every nonzero square-zero y.
        # Its inverse image x of y would satisfy x alpha(x)^2 = 0, colliding with theta(0).
        assert squares_zero>0
    return (name,len(X),len(G),rows,cols,full,squares_zero)

def count_complete(degree,pattern,k):
    G,mul,inv=finite_group(degree)
    R=len(pattern);C=len(pattern[0]);P=[[None if t is None else G[t] for t in row] for row in pattern]
    X=[Z]+[(i,g,j) for i in range(C) for g in G for j in range(R)]
    def times(a,b):
        if a==Z or b==Z:return Z
        i,g,j=a;u,h,v=b
        return Z if P[j][u] is None else (i,mul(mul(g,P[j][u]),h),v)
    def power(a):
        b=a
        for _ in range(k-1):b=times(b,a)
        return b
    count=0
    # A complete mapping fixes the zero; every other permutation is tested exactly.
    for perm in permutations(X[1:]):
        alpha={Z:Z,**dict(zip(X[1:],perm))}
        images={times(x,power(alpha[x])) for x in X}
        if len(images)==len(X):count+=1
    return count

cases=[
 (1,[[0]],'trivial 1x1'),
 (2,[[0]],'C2 1x1'),
 (3,[[0]],'S3 1x1'),
 (1,[[0,0]],'rectangular band 1x2'),
 (2,[[0,1]],'C2 1x2 full'),
 (3,[[0,1],[2,3]],'S3 2x2 full'),
 (1,[[0,0],[0,0]],'rectangular band 2x2'),
 (2,[[0,1],[1,0]],'C2 full nontrivial labels'),
 (3,[[0,None],[None,2]],'S3 sparse diagonal'),
 (1,[[0,None],[None,0]],'B2'),
 (1,[[0,0,None],[None,0,0],[0,None,0]],'3x3 sparse'),
 (2,[[0,None],[1,0]],'C2 sparse'),
 (3,[[0,1,None],[None,2,0]],'S3 rectangular sparse'),
]
if __name__=='__main__':
    for case in cases:
        name,size,order,rows,cols,full,squarezero=verify_rees(*case)
        print(f'{name}: size={size} group={order} shape={rows}x{cols} all_nonzero={full} squarezero_nonzero={squarezero} 2_complete={full}')
    c1=count_complete(1,[[0,None],[None,0]],1)
    c2=count_complete(1,[[0,None],[None,0]],2)
    a1=count_complete(1,[[0,0],[0,0]],1)
    a2=count_complete(1,[[0,0],[0,0]],2)
    assert (c1,c2)==(2,0)
    assert a1>=1 and a2>=1
    print(f'EXHAUSTIVE order5 Brandt B2: one_complete={c1} two_complete={c2}')
    print(f'EXHAUSTIVE order5 all-one Rees: one_complete={a1} two_complete={a2}')
    print('VERIFY_OK configurations=%d order5_exhaustive=4 all_tests_passed' % len(cases))
