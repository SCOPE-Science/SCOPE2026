"""Finite checks of the characteristic-two idempotent distribution theorem.
All computations use exact binary and quartic-field arithmetic.
"""
from itertools import product
from collections import Counter
from fractions import Fraction
from math import prod

def multiplication_table(q):
    if q == 2:
        return [[a & b for b in range(q)] for a in range(q)]
    if q == 4:
        # alpha^2 = alpha+1; encode a+b*alpha as a+2*b.
        def mul(a,b):
            x,y=a&1,a>>1; u,v=b&1,b>>1
            return ((x*u+y*v)&1) | (((x*v+y*u+y*v)&1)<<1)
        return [[mul(a,b) for b in range(4)] for a in range(4)]
    raise ValueError(q)

def binary_rank(rows):
    pivots={}
    for z in rows:
        while z:
            i=z.bit_length()-1
            if i in pivots:z ^=pivots[i]
            else:
                pivots[i]=z
                break
    return len(pivots)

def determinant(M,mul):
    n=len(M)
    if n == 2:
        return mul[M[0][0]][M[1][1]] ^ mul[M[0][1]][M[1][0]]
    if n == 3:
        a,b,c=M[0];d,e,f=M[1];g,h,i=M[2]
        return (mul[a][mul[e][i]] ^ mul[a][mul[f][h]] ^
                mul[b][mul[d][i]] ^ mul[b][mul[f][g]] ^
                mul[c][mul[d][h]] ^ mul[c][mul[e][g]])
    raise ValueError(n)

def nullity_fixed(M,mul,q):
    n=len(M); m=1 if q==2 else 2
    cols=[]
    for j in range(n):
        for t in range(m):
            z=1<<t
            sq=mul[z][z]
            col=0
            for i in range(n):
                a=mul[M[i][j]][sq]
                col ^= a << (m*i)
            col ^= 1 << (m*j+t)
            cols.append(col)
    return m*n - binary_rank(cols)

def expected_counts(n,group_order):
    # By the GL_n(F2) fixed-space distribution, computed independently.
    m=2**(n*n)
    mult=multiplication_table(2)
    dist=Counter()
    for vec in product(range(2),repeat=n*n):
        M=[vec[i*n:(i+1)*n] for i in range(n)]
        if not determinant(M,mult):continue
        dist[nullity_fixed(M,mult,2)]+=1
    size=sum(dist.values())
    return {k:group_order*v//size for k,v in dist.items()}

for q,n in [(2,2),(4,2),(2,3),(4,3)]:
    mul=multiplication_table(q)
    counts=Counter()
    for entries in product(range(q),repeat=n*n):
        M=[entries[i*n:(i+1)*n] for i in range(n)]
        if determinant(M,mul):
            d=nullity_fixed(M,mul,q)
            counts[d]+=1
    size=sum(counts.values())
    expected_order=prod(q**n-q**i for i in range(n))
    assert size==expected_order
    ex=expected_counts(n,size)
    assert dict(counts)==ex,(q,n,dict(counts),ex)
    moment=sum((2**d-1)*v for d,v in counts.items())
    assert moment==size
    print(f'q={q} n={n} |GL|={size}: fixed F2-dimension {dict(sorted(counts.items()))}; matches GL_{n}(2) law')
print('VERIFY_OK')
