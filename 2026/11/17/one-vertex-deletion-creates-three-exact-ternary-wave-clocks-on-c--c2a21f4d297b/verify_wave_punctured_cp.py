"""Exact finite-field checks for reversible waves on a vertex-deleted cocktail-party graph.

Execute: python verify_wave_punctured_cp.py
No external libraries required.
"""
from itertools import product

def matmul(A, B):
    h=len(A); p=len(B); w=len(B[0]); C=[[0]*w for _ in range(h)]
    for i in range(h):
        for k in range(p):
            a=A[i][k]%3
            if a:
                for j in range(w): C[i][j]=(C[i][j]+a*B[k][j])%3
    return C

def rank(A):
    a=[row[:] for row in A]; m=len(a); n=len(a[0]); row=0
    for col in range(n):
        pivot=next((i for i in range(row,m) if a[i][col]),None)
        if pivot is None: continue
        a[row],a[pivot]=a[pivot],a[row]
        if a[row][col]==2: a[row]=[(2*v)%3 for v in a[row]]
        for i in range(row+1,m):
            f=a[i][col]
            if f: a[i]=[(a[i][j]-f*a[row][j])%3 for j in range(n)]
        row+=1
        if row==m:break
    return row

def identity(n):return [[int(i==j) for j in range(n)] for i in range(n)]

def power(A,n):
    out=identity(len(A))
    while n:
        if n&1:out=matmul(out,A)
        A=matmul(A,A);n//=2
    return out

def build(r):
    n=2*r+1; A=[[int(i!=j and not (i<2*r and j==i^1)) for j in range(n)] for i in range(n)]
    T=[[0]*(2*n) for _ in range(2*n)]
    for i in range(n):
        T[i][:n]=A[i]
        T[i][n+i]=2
        T[n+i][i]=1
    return A,T

def build_intact(m):
    n=2*m
    A=[[int(i!=j and j!=(i^1)) for j in range(n)] for i in range(n)]
    T=[[0]*(2*n) for _ in range(2*n)]
    for i in range(n):
        T[i][:n]=A[i];T[i][n+i]=2;T[n+i][i]=1
    return T

def predicted(r,k):
    v=k
    while v%3==0:v//=3
    b=2 if v!=k else 1
    c=min(4,k//v) # min(4, 3**val3(k))
    e=int(k%2==0)
    j=int(k%4==0)
    if r%3==0:return 2*(r+1)*j+(r-2)*e*b+e*c
    if r%3==1:return 2*r*j+(r-1)*e*b+4*int(k%8==0)
    return 2*r*j+(r-1)*e*b+4*int(k%5==0)

def clock(r):
    if r%3==0:return 36
    if r%3==2:return 60
    return 8 if r==1 else 24

def mobius(n):
    p=0;d=2
    while d*d<=n:
        if n%d==0:
            n//=d; p+=1
            if n%d==0:return 0
        d+=1
    if n>1:p+=1
    return -1 if p%2 else 1

def divisors(n):return [d for d in range(1,n+1) if n%d==0]

def full_fraction_numer(r,q=3):
    if r%3==0:return (q**(2*r+2)-1)*(q-1)*q**(2*r-1)
    if r%3==1:return (q**4-1)*(q**(r-1)-1)*q**(3*r-1) if r>=4 else (q**4-1)*q**2
    return (q**(2*r)-1)*(q**4-1)*(q**(r-1)-1)*q**(r-1)

def check():
    cases=0
    for r in range(1,10):
        A,T=build(r);n=len(T);L=clock(r)
        assert power(T,L)==identity(n),(r,'not global period',L)
        for prime in [2,3,5]:
            if L%prime==0: assert power(T,L//prime)!=identity(n),(r,'short order',L//prime)
        for k in range(1,121):
            Q=power(T,k)
            nullity=n-rank([[(Q[i][j]-int(i==j))%3 for j in range(n)] for i in range(n)])
            assert nullity==predicted(r,k),(r,k,nullity,predicted(r,k))
            cases+=1
        for q in (3,9):
            pop={d:sum(mobius(d//e)*q**predicted(r,e) for e in divisors(d)) for d in divisors(L)}
            assert sum(pop.values())==q**(4*r+2)
            assert all(pop[d]>=0 and pop[d]%d==0 for d in pop)
            assert pop[L]==full_fraction_numer(r,q),(r,q,pop[L],full_fraction_numer(r,q))
        print(f'r={r}: period {L}, {120} rank tests and primitive populations PASS')
    for m in range(2,11):
        S=build_intact(m);L=36 if m%3==0 else 12
        assert power(S,L)==identity(len(S)),(m,L,'intact not periodic')
        for p in (2,3):
            if L%p==0:assert power(S,L//p)!=identity(len(S)),(m,L,'intact shorter period')
    print('intact comparison: m=2..10 exact clocks PASS')
    # independent orbit enumeration on 3-vertex punctured graph
    r=1; _,T=build(r); N=len(T);L=clock(r)
    counts={}
    for x in product(range(3),repeat=N):
        y=x;period=0
        for k in range(1,L+1):
            y=tuple(sum(T[i][j]*y[j] for j in range(N))%3 for i in range(N))
            if y==x:period=k;break
        assert period>0
        counts[period]=counts.get(period,0)+1
    for d,pop in counts.items():
        assert pop% d==0
    assert sum(counts.values())==3**N
    print('r=1 exhaustive 729 states:', dict(sorted(counts.items())))
    print('TOTAL',cases,'modular rank checks PASS')
if __name__=='__main__':check()
