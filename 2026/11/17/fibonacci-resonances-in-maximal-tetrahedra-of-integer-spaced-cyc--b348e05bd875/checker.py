"""Exact checks for four-point Vandermonde maxima on integer intervals.

Run: python checker.py
The analytic theorem in RESULT.md covers all orders; finite checks are corroborative.
"""
from itertools import combinations
from math import isqrt

def score(t):
    p=1
    for a,b in combinations(t,2): p*=b-a
    return p

def candidates(N):
    if N<3: raise ValueError('requires N>=3')
    q=isqrt(N*N//5)
    def F(y):
        s=N-y
        e=s%2
        return N*y*(s*s-e)*((N+y)**2-e)//16
    ys=[y for y in (q,q+1) if 1<=y<=N-2]
    M=max(F(y) for y in ys)
    result=[]
    for y in ys:
        if F(y)!=M: continue
        s=N-y
        for x in sorted({s//2,(s+1)//2}):
            z=s-x
            result.append((0,x,x+y,N))
    return M,sorted(set(result))

def brute(N):
    best=0; opts=[]
    for three in combinations(range(1,N),2):
        a,b=three
        val=score((0,a,b,N))
        if val>best: best=val; opts=[(0,a,b,N)]
        elif val==best: opts.append((0,a,b,N))
    return best,opts

def direct_det(t):
    a,b,c,d=t
    ps=[(u,u*u,u*u*u) for u in t]
    x,y,z=[tuple(ps[i][j]-ps[0][j] for j in range(3)) for i in (1,2,3)]
    return abs(x[0]*(y[1]*z[2]-y[2]*z[1])-x[1]*(y[0]*z[2]-y[2]*z[0])+x[2]*(y[0]*z[1]-y[1]*z[0]))

def fib_odd(limit):
    a,b=0,1; idx=1
    while b<=limit:
        if idx>=5 and idx%2==1:yield b
        a,b=b,a+b;idx+=1

# Complete enumeration of all vertex-supported tetrahedra for 4<=n<=60.
# Endpoints must occur at all maxima; explicitly audit that as well.
quadruples=0
for n in range(4,61):
    N=n-1
    M,optimizers=candidates(N)
    B,Bopt=brute(N)
    assert (B,Bopt)==(M,optimizers), (n,B,Bopt,M,optimizers)
    global_M=0;global_ops=[]
    for t in combinations(range(n),4):
        val=score(t);quadruples+=1
        if val>global_M:global_M=val;global_ops=[t]
        elif val==global_M:global_ops.append(t)
    assert global_M==M and global_ops==optimizers, (n,global_M,M)
    for t in optimizers:
        assert direct_det(t)==score(t)

# Independent one-variable exhaustive checks, and Pell/Fibonacci resonance census.
fibs=set(fib_odd(10000));ties=[]
for N in range(3,10001):
    M, opts=candidates(N)
    q=isqrt(N*N//5)
    # A separate integral one-dimensional maximization (not the two-candidate formula).
    def f(y):
        x=(N-y)//2; z=(N-y)-x
        return N*x*y*z*(x+y)*(y+z)
    best=max(f(y) for y in range(1,N-1)) if N<=500 else max(f(y) for y in range(max(1,q-4),min(N-1,q+6)))
    assert best==M,(N,best,M)
    is_tie=len(opts)==3
    assert is_tie==(N in fibs),(N,is_tie,N in fibs)
    if is_tie:ties.append(N)
print('CYCLIC_FEKETE_PASS', 'full_n=4..60',f'full_quadruples={quadruples}', '1d_N=3..10000', 'ties='+','.join(map(str,ties)), 'exact_determinants=PASS')
