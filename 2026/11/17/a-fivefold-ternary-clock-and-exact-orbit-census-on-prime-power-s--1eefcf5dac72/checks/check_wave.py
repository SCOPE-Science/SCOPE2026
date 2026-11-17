#!/usr/bin/env python3
"""Pure-Python modular rank and exact-period checks for ternary sunlet waves."""

def multiply(a,b):
    n=len(a)
    result=[[0]*n for _ in range(n)]
    for i,row in enumerate(a):
        out=result[i]
        for k,x in enumerate(row):
            if x:
                bk=b[k]
                for j,y in enumerate(bk):
                    out[j]+=x*y
        for j in range(n):out[j]%=3
    return result

def power(a,k):
    n=len(a)
    r=[[int(i==j) for j in range(n)] for i in range(n)]
    while k:
        if k&1:r=multiply(r,a)
        k//=2
        if k:a=multiply(a,a)
    return r

def rank_mod3(a):
    a=[row[:] for row in a]
    m=len(a);n=len(a[0]);r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if a[i][c]%3),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=1 if a[r][c]==1 else 2
        if inv==2:a[r]=[(2*x)%3 for x in a[r]]
        for i in range(r+1,m):
            if a[i][c]:
                k=a[i][c]
                a[i]=[(u-k*v)%3 for u,v in zip(a[i],a[r])]
        r+=1
        if r==m:break
    return r

def operator(n):
    v=2*n;d=2*v
    a=[[0]*d for _ in range(d)]
    for i in range(n):
        for j in ((i-1)%n,(i+1)%n,n+i):
            a[i][j]=1
            a[j][i]=1
    for i in range(v):
        a[i][v+i]=2
        a[v+i][i]=1
    return a

def is_identity(a):
    return all(x%3==int(i==j) for i,row in enumerate(a) for j,x in enumerate(row))

def nullity_tk_minus_i(m,k):
    a=power(m,k)
    for i in range(len(a)):a[i][i]=(a[i][i]-1)%3
    return len(a)-rank_mod3(a)

def main():
    for n in (3,9,27):
        m=operator(n);r=0;s=n
        while s>1:
            assert s%3==0
            r+=1;s//=3
        assert is_identity(power(m,5*n))
        assert not is_identity(power(m,n))
        assert not is_identity(power(m,5*n//3))
        observed=[]
        for j in range(r+1):
            k=5*3**j
            actual=nullity_tk_minus_i(m,k)
            expected=4*min(n,2*3**j)
            assert actual==expected,(n,k,actual,expected)
            observed.append((k,actual))
        for k in (1,2,3,4,6,7,8,9,11,12):
            assert nullity_tk_minus_i(m,k)==0
        print('n=%d dimension=%d exact_order=%d fixed_space_dimensions=%s'%(n,4*n,5*n,observed))
if __name__=='__main__':main()
