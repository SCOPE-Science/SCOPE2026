"""Independent finite-field checks for differential derivations of square-zero evolution algebras.

Run with Python 3.11+: python checker.py. All enumeration is finite and illustrative.
"""
from collections import Counter
from itertools import product
from math import prod


def add(a,b): return a^b

def mul(a,b,q):
    if q==2:return a&b
    assert q==4
    res=0
    while b:
        if b&1:res^=a
        b>>=1;a<<=1
        if a&4:a^=7  # x^2+x+1
    return res

def powf(a,n,q):
    z=1
    for _ in range(n):z=mul(z,a,q)
    return z

def rank(a,q):
    mat=[list(row) for row in a]
    n=len(mat);m=len(mat[0]) if n else 0;r=0
    for j in range(m):
        pivot=next((i for i in range(r,n) if mat[i][j]),None)
        if pivot is None:continue
        mat[pivot],mat[r]=mat[r],mat[pivot]
        inv=powf(mat[r][j],q-2,q)
        mat[r]=[mul(x,inv,q) for x in mat[r]]
        for i in range(n):
            if i==r:continue
            z=mat[i][j]
            if z:mat[i]=[add(b,mul(z,c,q)) for b,c in zip(mat[i],mat[r])]
        r+=1
        if r==n:break
    return r

def mm(A,B,q):
    return [[__import__('functools').reduce(add,(mul(A[i][k],B[k][j],q) for k in range(len(B))),0)
             for j in range(len(B[0]))]for i in range(len(A))]

def T_from_upper(v,r):
    M=[[0]*r for _ in range(r)];it=iter(v)
    for i in range(r):
        for j in range(i,r):M[i][j]=M[j][i]=next(it)
    return M

def direct(q,r):
    counts=Counter(); tcounts=Counter()
    for vals in product(range(q),repeat=r*(r+1)//2):
        T=T_from_upper(vals,r)
        if any(any(row) for row in mm(T,T,q)):continue
        s=rank(T,q);tcounts[s]+=1
        for f in product(range(q),repeat=r):
            if any(__import__('functools').reduce(add,(mul(f[k],T[k][j],q) for k in range(r)),0)
                   for j in range(r)):continue
            D=[T[i]+[0] for i in range(r)]+[list(f)+[0]]
            counts[rank(D,q)]+=1
            assert not any(any(row) for row in mm(D,D,q))
    return counts,tcounts

def gauss(n,k,q):
    if k<0 or k>n:return 0
    a=b=1
    for j in range(k):a*=q**(n-j)-1;b*=q**(k-j)-1
    return a//b

def gl(n,q):return prod(q**n-q**j for j in range(n))
def sp(a,q):return q**(a*a)*prod(q**(2*j)-1 for j in range(1,a+1))
def si(a,s,q):
    if s<0 or s>a:return 0
    return gauss(a,s,q)*prod(q**(a-j)+1 for j in range(s))
def iso(r,s,q):
    if r%2:return si((r-1)//2,s,q)
    return q**s*si(r//2-1,s,q)+si(r//2-1,s-1,q)
def sym(s,q):
    if not s:return 1
    if s%2:return gl(s,q)//sp((s-1)//2,q)
    a=s//2
    return gl(s,q)//(q**(s-1)*sp(a-1,q))+gl(s,q)//sp(a,q)
def predicted(r,q):
    counts=Counter();tcounts=Counter()
    for s in range(r//2+1):
        tcounts[s]=iso(r,s,q)*sym(s,q)
        counts[s]+=tcounts[s]*q**s
        counts[s+1]+=tcounts[s]*(q**(r-s)-q**s)
    return +counts,+tcounts

def derivation(M,r,q):
    # E has basis e_0,...,e_{r-1},z, and products e_i^2=z.
    # For each basis pair, D(xy)=D(x)y+xD(y).
    for i in range(r+1):
        for j in range(r+1):
            lhs=[0]*(r+1)
            if i==j and i<r:lhs=[M[k][r] for k in range(r+1)]
            rhs=[0]*r+[0]
            if j<r:rhs[-1]=add(rhs[-1],M[j][i])
            if i<r:rhs[-1]=add(rhs[-1],M[i][j])
            if lhs!=rhs:return False
    return True

def brute_all(r,q):
    counts=Counter(); n=r+1
    for tup in product(range(q),repeat=n*n):
        M=[list(tup[i*n:(i+1)*n]) for i in range(n)]
        if not derivation(M,r,q):continue
        if any(any(row) for row in mm(M,M,q)):continue
        counts[rank(M,q)]+=1
    return counts

for r,q in ((2,2),(3,2),(4,2),(2,4),(3,4)):
    got,tt=direct(q,r)
    want,wt=predicted(r,q)
    assert got==want and tt==wt,(r,q,got,want,tt,wt)
    print('SYM_PARAM_PASS',f'r={r}',f'q={q}', 'D-ranks='+str(dict(sorted(got.items()))), 'T-ranks='+str(dict(sorted(tt.items()))))
for r,q in ((2,2),(3,2)):
    got=brute_all(r,q);want,_=predicted(r,q)
    assert got==want,(r,q,got,want)
    print('ORIGINAL_DERIVATION_PASS',f'r={r}',f'q={q}','ranks='+str(dict(sorted(got.items()))))
print('EVOLUTION_SQUAREZERO_RANK_CENSUS_PASS')
