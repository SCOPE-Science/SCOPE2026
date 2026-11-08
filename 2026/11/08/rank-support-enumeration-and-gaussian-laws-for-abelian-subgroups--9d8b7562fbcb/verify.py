"""Exact finite checks for path-graph isotropic-subspace support polynomials.

Run: python3 verify.py (Python >= 3.9; no external dependencies).
The proof, not finite tests, establishes the universal formulas.
"""
from collections import Counter
from itertools import combinations, product
from math import prod


def gb(n,k,q):
    if k<0 or k>n: return 0
    if k==0: return 1
    a=prod(q**(n-i)-1 for i in range(k))
    b=prod(q**(k-i)-1 for i in range(k))
    assert a%b==0
    return a//b


def gl(n,q):
    return prod(q**n-q**j for j in range(n))


def add(a,b,q):
    if q==4:return a^b
    return (a+b)%q


def mul(a,b,q):
    if q!=4:return a*b%q
    z=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&(b>>j)&1:z^=1<<(i+j)
    if z&8:z^=(1<<3)|(1<<2)|(1<<1)
    if z&4:z^=(1<<2)|(1<<1)|1
    return z


def detzero(a,b,c,d,q):
    if q==4:return mul(a,d,q)==mul(b,c,q)
    return (a*d-b*c)%q==0


def path_isotropic(rows,q):
    if not rows:return True
    n=len(rows[0])
    for j in range(n-1):
        for i in range(len(rows)):
            for k in range(i+1,len(rows)):
                if not detzero(rows[i][j],rows[i][j+1],rows[k][j],rows[k][j+1],q):
                    return False
    return True


def rref_matrices(n,r,q):
    for pivots in combinations(range(n),r):
        free=[(i,j) for i in range(r) for j in range(pivots[i]+1,n) if j not in pivots]
        for vals in product(range(q), repeat=len(free)):
            m=[[0]*n for _ in range(r)]
            for i,j in enumerate(pivots):m[i][j]=1
            for (i,j),x in zip(free,vals):m[i][j]=x
            yield m


def weighted_transfer(n,d,q):
    # polynomial lists for zero-ending and nonzero-ending sequences.
    # The second count is per projective direction, aggregated over its q-1 nonzero vectors.
    # For d=0 only the all-zero sequence exists.
    if d==0:return [1]
    m=(q**d-1)//(q-1); t=q-1
    z=[1]; x=[0,t]
    if n==0:return [1]
    for _ in range(1,n):
        length=max(len(z),len(x))
        zn=[(z[k] if k<len(z) else 0)+m*(x[k] if k<len(x) else 0) for k in range(length)]
        xn=[0]*(length+1)
        for k in range(length):
            xn[k+1]=t*((z[k] if k<len(z) else 0)+(x[k] if k<len(x) else 0))
        z,x=zn,xn
    return [(z[k] if k<len(z) else 0)+m*(x[k] if k<len(x) else 0) for k in range(max(len(z),len(x)))]


def predicted(n,r,q):
    polys=[weighted_transfer(n,d,q) for d in range(r+1)]
    out=[0]*(n+1)
    for d in range(r+1):
        coef=(-1)**(r-d)*q**((r-d)*(r-d-1)//2)*gb(r,d,q)
        for k,v in enumerate(polys[d]):out[k]+=coef*v
    D=gl(r,q)
    assert all(x%D==0 for x in out)
    return tuple(v//D for v in out)


def brute(n,r,q):
    out=Counter()
    if r==0:return (1,)+(0,)*n
    for matrix in rref_matrices(n,r,q):
        if path_isotropic(matrix,q):
            support=sum(any(row[j]!=0 for row in matrix) for j in range(n))
            out[support]+=1
    return tuple(out[k] for k in range(n+1))


def check():
    cases=0
    for q,max_n in ((2,7),(3,6),(4,5),(5,4)):
        for n in range(1,max_n+1):
            for r in range(0,min(n,4)+1):
                a=predicted(n,r,q)
                b=brute(n,r,q)
                assert a==b,('subspace-vs-transfer',q,n,r,a,b)
                cases+=1
    # Explicit rank-two rational generating function:
    # z^3/((1-z)(1-qz)(1-qz-(q^2-q)z^2))
    for q in (2,3,4,5,7):
        h=[0]*14
        h[3]=1
        # multiply power series by 1/(1-z), then 1/(1-qz), then final quadratic factor
        def convolve_recurrence(a,kind):
            b=[0]*len(a)
            for n in range(len(a)):
                if kind==0:b[n]=a[n]+(b[n-1] if n>=1 else 0)
                if kind==1:b[n]=a[n]+q*(b[n-1] if n>=1 else 0)
                if kind==2:b[n]=a[n]+q*(b[n-1] if n>=1 else 0)+q*(q-1)*(b[n-2] if n>=2 else 0)
            return b
        for kind in range(3):h=convolve_recurrence(h,kind)
        for n in range(len(h)):
            assert h[n]==sum(predicted(n,2,q)),('r2-rational',q,n,h[n],sum(predicted(n,2,q)))
    print('VERIFY_OK:',cases,'independent reduced-echelon support enumerations plus rank-two rational-series checks')

if __name__=='__main__':check()
