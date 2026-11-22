"""Standalone bounded checks of characteristic-two affine order-four counts.

Run: python check_affine4.py. No external dependencies.
"""
from itertools import product
from math import prod
from functools import lru_cache

@lru_cache(None)
def gl_order(q,n):
    return prod(q**n-q**j for j in range(n))

@lru_cache(None)
def cen_order(q,cols):
    gaps=[cols[j]-cols[j+1] for j in range(len(cols)-1)]+[cols[-1]]
    exponent=sum(j*j for j in cols)-sum(j*(j+1)//2 for j in gaps)
    return q**exponent*prod(prod(q**j-1 for j in range(1,g+1)) for g in gaps)

def column_partitions(n, width):
    def walk(rem, mx, left, curr):
        if left==0:
            if rem==0: yield tuple(curr)
            return
        for t in range(min(mx,rem),-1,-1):
            yield from walk(rem-t,t,left-1,curr+[t])
    yield from walk(n,n,width,[])

def counts_formula(q,n,width):
    total=free=0
    for c in column_partitions(n,width):
        z=cen_order(q,c)
        assert gl_order(q,n)%z==0
        multiplier=gl_order(q,n)//z
        total+=multiplier*q**(n-c[-1])
        free+=multiplier*(q**(n-c[-1])-q**(n-c[0]))
    return total,free

def exact_four(q,n):
    a,b=counts_formula(q,n,4)
    c,d=counts_formula(q,n,2)
    return a-c,b-d

def mul2(a,b,n):
    out=[]
    for row in a:
        y=0
        for j in range(n):
            if row>>j&1:y^=b[j]
        out.append(y)
    return tuple(out)

def rank2(a,n):
    bas=[0]*n;r=0
    for row in a:
        v=row
        while v:
            i=v.bit_length()-1
            if bas[i]:v^=bas[i]
            else:bas[i]=v;r+=1;break
    return r

def brute_binary(n):
    total4=free4=total2=free2=0
    for bits in range(1 << (n*n)):
        N=tuple((bits>>(i*n))&((1<<n)-1) for i in range(n))
        N2=mul2(N,N,n)
        N4=mul2(N2,N2,n)
        if any(N4): continue
        N3=mul2(N2,N,n)
        r3=rank2(N3,n)
        r=rank2(N,n)
        total4+=2**(n-r3)
        free4+=2**(n-r3)-2**r
        if not any(N2):
            total2+=2**(n-r)
            free2+=2**(n-r)-2**r
    return total4-total2,free4-free2

# GF4, irreducible polynomial z^2+z+1; addition is xor.
def mult4(a,b):
    x=0
    for i in range(2):
        if (b>>i)&1: x^=a<<i
    for i in (2,):
        if (x>>i)&1:x^=0b111<<(i-2)
    return x

def rank4(rows,n):
    a=[list(r) for r in rows]
    k=0
    for j in range(n):
        s=next((r for r in range(k,n) if a[r][j]),None)
        if s is None:continue
        a[k],a[s]=a[s],a[k]
        inv=next(t for t in (1,2,3) if mult4(a[k][j],t)==1)
        a[k]=[mult4(z,inv) for z in a[k]]
        for r in range(n):
            if r!=k and a[r][j]:
                t=a[r][j]
                a[r]=[u^mult4(t,v) for u,v in zip(a[r],a[k])]
        k+=1
    return k

def mul4(A,B):
    n=len(A)
    return tuple(tuple(__import__('functools').reduce(lambda a,b:a^b,(mult4(A[i][k],B[k][j]) for k in range(n)),0) for j in range(n)) for i in range(n))

def brute_four(n):
    total4=free4=total2=free2=0
    for v in product(range(4),repeat=n*n):
        N=tuple(tuple(v[i*n+j] for j in range(n)) for i in range(n))
        N2=mul4(N,N);N4=mul4(N2,N2)
        if any(any(r) for r in N4):continue
        N3=mul4(N2,N)
        r3=rank4(N3,n);r=rank4(N,n)
        total4+=4**(n-r3);free4+=4**(n-r3)-4**r
        if not any(any(row) for row in N2):
            total2+=4**(n-r);free2+=4**(n-r)-4**r
    return total4-total2,free4-free2

if __name__=='__main__':
    for n in (1,2,3,4):
        got=brute_binary(n);want=exact_four(2,n)
        assert got==want,(2,n,got,want)
        print('PASS q=2 n=',n,'order-4 total,derangements',got)
    for n in (1,2):
        got=brute_four(n);want=exact_four(4,n)
        assert got==want,(4,n,got,want)
        print('PASS q=4 n=',n,'order-4 total,derangements',got)
    print('PASS six field/dimension exhaustive configurations')
