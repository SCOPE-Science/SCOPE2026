#!/usr/bin/env python3
"""Independent finite checks for reversible neighbor-sum waves on a clique plus a leaf.
All operations are integer arithmetic modulo three, with no external libraries.
"""
import math


def adjacency(n):
    # Core vertices 0,...,n-1; private leaf n adjacent only to vertex 0.
    m=n+1
    a=[[0]*m for _ in range(m)]
    for i in range(n):
        for j in range(n):
            if i!=j:a[i][j]=1
    a[0][n]=a[n][0]=1
    return a


def update_matrix(n):
    a=adjacency(n);m=n+1
    t=[[0]*(2*m) for _ in range(2*m)]
    for i in range(m):
        for j in range(m):t[i][j]=a[i][j]
        t[i][m+i]=2;t[m+i][i]=1
    return t


def matmul(a,b):
    dim=len(a); b_cols=list(zip(*b))
    return [[sum(x*y for x,y in zip(row,col))%3 for col in b_cols] for row in a]


def identity(dim):return [[int(i==j) for j in range(dim)] for i in range(dim)]


def power(a,k):
    ret=identity(len(a))
    while k:
        if k&1:ret=matmul(ret,a)
        k//=2
        if k:a=matmul(a,a)
    return ret


def rank3(a):
    a=[row[:] for row in a];m=len(a);q=len(a[0]);r=0
    for col in range(q):
        pivot=next((i for i in range(r,m) if a[i][col]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        if a[r][col]==2:a[r]=[(2*x)%3 for x in a[r]]
        for i in range(r+1,m):
            factor=a[i][col]
            if factor:
                for j in range(col,q):a[i][j]=(a[i][j]-factor*a[r][j])%3
        r+=1
        if r==m:break
    return r


def nullity_power(n,k):
    t=update_matrix(n);p=power(t,k);m=len(p)
    for i in range(m):p[i][i]=(p[i][i]-1)%3
    return m-rank3(p)


def fixed_dim(n,k):
    assert n>=3 and k>=1
    if n%3==0:
        return (n-2)*(1+(k%3==0))+6*(k%28==0)
    if n%3==2:
        return (n-2)*(1+(k%3==0))+2*(k%4==0)+4*(k%8==0)
    s=1
    while k%3==0:
        s*=3;k//=3
    return min(s,6)+(n-3)*min(s,2)+(k%2==0)*min(s,2)


def predicted_order(n):return (84,18,24)[n%3]


def exhaustive_orbits(n):
    # Exhaustive state-space permutation enumeration, with a direct vertex update
    # unrelated to matrix multiplication/rank code.
    m=n+1;L=2*m; size=3**L;visited=bytearray(size);hist={}
    a=adjacency(n);neighbors=[[j for j in range(m) if a[i][j]] for i in range(m)]
    weights=[3**i for i in range(L)]
    def nxt(idx):
        digits=[];v=idx
        for _ in range(L):
            digits.append(v%3);v//=3
        total=0
        for i in range(m):
            new=(sum(digits[j] for j in neighbors[i])-digits[m+i])%3
            total+=weights[i]*new+weights[m+i]*digits[i]
        return total
    for start in range(size):
        if visited[start]:continue
        cur=start; length=0
        while not visited[cur]:
            visited[cur]=1;length+=1;cur=nxt(cur)
        if cur!=start:raise AssertionError('not a permutation')
        hist[length]=hist.get(length,0)+1
    assert sum(t*c for t,c in hist.items())==size
    order=predicted_order(n)
    assert all(order%t==0 for t in hist)
    assert math.lcm(*hist.keys())==order
    for k in range(1,order+1):
        actual=sum(t*c for t,c in hist.items() if k%t==0)
        expected=3**fixed_dim(n,k)
        assert actual==expected,(n,k,actual,expected)
    return hist


def main():
    for n in range(3,19):
        order=predicted_order(n);T=update_matrix(n)
        assert power(T,order)==identity(len(T)),('order bound',n)
        for p in (2,3,7):
            if order%p==0:
                assert power(T,order//p)!=identity(len(T)),('sharpness',n,p)
        for k in range(1,order+1):
            actual=nullity_power(n,k)
            expected=fixed_dim(n,k)
            assert actual==expected,(n,k,actual,expected)
        print('RANK_AND_ORDER_PASS n=%d period=%d fixed_dim_at_1=%d' % (n,order,fixed_dim(n,1)))
    for n in (3,4,5):
        hist=exhaustive_orbits(n)
        print('EXHAUSTIVE_PASS n=%d configurations=%d orbit_histogram=%s' % (n,3**(2*n+2),str(dict(sorted(hist.items())))))
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':main()
