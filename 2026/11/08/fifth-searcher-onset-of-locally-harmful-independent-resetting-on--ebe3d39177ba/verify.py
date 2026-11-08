#!/usr/bin/env python3
"""Exact rational verification of a finite-state independent-reset first-detection theorem.
Run: python verify.py. Requires only Python's standard library.
"""
from fractions import Fraction as F
from itertools import product

# Transient labels are (2,1,3,4), with vertex 0 absorbing.
# Each walk has total jump rate 1; death occurs on a 1 -> 0 jump.
EDGES = {
    0: ((1, F(1, 2)), (2, F(1, 2))),
    1: ((0, F(1, 2)),),
    2: ((0, F(1, 2)), (3, F(1, 2))),
    3: ((2, F(1)),),
}
EXPECTED = (
    (F(12), F(-10)),
    (F(1555,272), F(-44679,18496)),
    (F(629176456,168587283),F(-5826055874237962,9473890663107363)),
    (F(98335794451053,35264790234112), F(-98437587236766524607457,4857833711937191749095424)),
    (F(779533184020835725901911436,347041368750556008691694017),
     F(117715636350470400400957554016380716796973103498302122,
       602188558121296962986525429886983883962244425767981445)),
)

def rational_solve(A, rhs):
    """Elementary rational Gaussian elimination; rhs can have multiple columns."""
    n=len(A); k=len(rhs[0]); v=[[F(x) for x in A[i]]+[F(x) for x in rhs[i]] for i in range(n)]
    for j in range(n):
        pivot=next((p for p in range(j,n) if v[p][j]), None)
        assert pivot is not None, 'singular transient generator'
        v[j],v[pivot]=v[pivot],v[j]
        for i in range(j+1,n):
            if v[i][j] == 0: continue
            factor=v[i][j]/v[j][j]
            v[i][j]=F(0)
            for q in range(j+1,n+k):
                v[i][q]-=factor*v[j][q]
    sol=[[F(0) for _ in range(k)]for _ in range(n)]
    for i in range(n-1,-1,-1):
        for h in range(k):
            sol[i][h]=(v[i][n+h]-sum((v[i][j]*sol[j][h] for j in range(i+1,n)), F(0)))/v[i][i]
    return sol

def solve_counts(N):
    states=[(a,b,c,N-a-b-c) for a in range(N+1) for b in range(N-a+1)
            for c in range(N-a-b+1)]
    idx={s:i for i,s in enumerate(states)}; d=len(states)
    A=[[F(0) for _ in range(d)] for _ in range(d)]
    for x,c in enumerate(states):
        A[x][x]=F(N)
        for i in range(4):
            if c[i]==0: continue
            for j,rate in EDGES[i]:
                cc=list(c);cc[i]-=1;cc[j]+=1
                A[x][idx[tuple(cc)]]-=c[i]*rate
    start=idx[(N,0,0,0)]
    u=[x[0] for x in rational_solve(A,[[F(1)] for _ in states])]
    b=[]
    for x,c in enumerate(states):
        val=F(0)
        for i in (1,2,3):
            if not c[i]:continue
            cc=list(c);cc[i]-=1;cc[0]+=1
            val+=c[i]*(u[idx[tuple(cc)]]-u[x])
        b.append(val)
    v=[x[0] for x in rational_solve(A,[[z] for z in b])]
    # Exact certificates: both linear systems hold at every state.
    for i in range(d):
        assert sum((A[i][j]*u[j] for j in range(d)), F(0)) == 1
        assert sum((A[i][j]*v[j] for j in range(d)), F(0)) == b[i]
    return u[start],v[start],d

def solve_labeled(N):
    """Independent, uncompressed construction for small N (full 4**N states)."""
    states=list(product(range(4),repeat=N))
    idx={s:i for i,s in enumerate(states)}; d=len(states)
    A=[[F(0) for _ in range(d)] for _ in range(d)]
    for k,config in enumerate(states):
        A[k][k]=F(N)
        for i,pos in enumerate(config):
            for nxt,rate in EDGES[pos]:
                other=list(config);other[i]=nxt
                A[k][idx[tuple(other)]]-=rate
    u=[z[0] for z in rational_solve(A,[[1] for _ in states])]
    b=[]
    for k,config in enumerate(states):
        val=F(0)
        for i,pos in enumerate(config):
            if pos:
                other=list(config);other[i]=0
                val+=u[idx[tuple(other)]]-u[k]
        b.append(val)
    v=[z[0] for z in rational_solve(A,[[z] for z in b])]
    return u[idx[(0,)*N]],v[idx[(0,)*N]]


def main():
    for n in range(1,6):
        mean,der,states=solve_counts(n)
        assert (mean,der)==EXPECTED[n-1], f'mismatch at {n}'
        assert (der<0 if n<=4 else der>0)
        if n<=3:
            assert (mean,der)==solve_labeled(n), f'labeled mismatch at {n}'
        print(f'N={n}: states={states}, M(0)={mean}, M\'(0+)={der}, sign={"negative" if der<0 else "positive"}')
    print('VERIFY_OK: five exact independent-reset signs, 3 labeled cross-checks, and all rational residuals')

if __name__=='__main__': main()
