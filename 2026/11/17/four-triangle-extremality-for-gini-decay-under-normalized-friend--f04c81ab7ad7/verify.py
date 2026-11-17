"""Exact-rational diagnostics for normalized heat and Gini variation on friendship graphs.

Run: python verify.py
The finite tests corroborate, but do not replace, the all-size proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def gini(x):
    return sum(abs(x[i]-x[j]) for i in range(len(x)) for j in range(i+1, len(x)))


def projections(m):
    n = 2*m+1
    P = [[F(0) for _ in range(n)] for _ in range(n)]
    C = [[F(0) for _ in range(n)] for _ in range(n)]
    Q = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        C[i][0]=F(1,3)
        for l in range(1,n): C[i][l]=F(1,3*m)
    for j in range(m):
        for v in [2*j+1,2*j+2]:
            for u in [2*j+1,2*j+2]: P[v][u]+=F(1,2)
            for u in range(1,n): P[v][u]-=F(1,2*m)
    for u in range(1,n): Q[0][u]=F(1,2*m)
    Q[0][0]=-1
    for j in range(m):
        u,v=2*j+1,2*j+2
        for l,w in [(u,v),(v,u)]:
            Q[l][l]=-1; Q[l][0]=F(1,2); Q[l][w]=F(1,2)
    I=[[F(i==j) for j in range(n)] for i in range(n)]
    R=[[I[i][j]-P[i][j]-C[i][j] for j in range(n)] for i in range(n)]
    return P,C,Q,R


def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def apply(A,x):
    return [sum(a*y for a,y in zip(row,x)) for row in A]


def target(m):
    return F(2*(m*m-1),m*(2*m-1))


def count_cut_ratio(m,r,b):
    c=m-r-b
    s=2*r+b
    if s==0 or s==2*m+1: return F(0),F(0)
    S=F(s,2*m)
    p_g=2*r*b+4*r*c+2*b*c+2*r*(1-S)+2*b*abs(F(1,2)-S)+2*c*S
    x_g=s*(2*m+1-s)
    return p_g,F(x_g)


for m in range(1,9):
    P,C,Q,R=projections(m)
    n=2*m+1
    assert matmul(P,P)==P
    assert matmul(C,C)==C
    assert matmul(P,C)==[[F(0)]*n for _ in range(n)]
    assert matmul(Q,P)==[[-v/2 for v in row] for row in P]
    assert matmul(Q,R)==[[-F(3,2)*v for v in row] for row in R]
    assert matmul(Q,C)==[[F(0)]*n for _ in range(n)]
    # Every orbit of binary cuts; all possible mixtures of complete, split and empty pairs.
    for r in range(m+1):
        for b in range(m-r+1):
            num,den=count_cut_ratio(m,r,b)
            if den:
                assert num<=target(m)*den,(m,r,b,num,den)
    if m>=2:
        num,den=count_cut_ratio(m,1,0)
        assert num==target(m)*den
    # Exact independent matrix check using rational eigenmode multipliers.
    a=F(3,4); bb=a**3
    H=[[C[i][j]+a*P[i][j]+bb*R[i][j] for j in range(n)] for i in range(n)]
    assert all(sum(row)==1 for row in H)
    assert all(v>=0 for row in H for v in row)
    L=bb+(a-bb)*target(m)
    for j in range(n):
        x=[F(0)]*n; x[j]=1
        if gini(x): assert gini(apply(H,x))<=L*gini(x)
    if m>=2:
        x=[F(0)]*n; x[1]=1; x[2]=1
        assert gini(apply(H,x))==L*gini(x)
    if m==1:
        x=[F(0)]*n; x[1]=1
        assert gini(apply(H,x))==L*gini(x)
    for step in range(240):
        x=[F(((j*11+step*7+j*j*step)%17)-8,7) for j in range(n)]
        assert gini(apply(H,x))<=L*gini(x)
print('EXACT_EIGENPROJECTION_AND_NORMALIZED_GENERATOR_IDENTITIES_PASSED 8')
print('EXHAUSTIVE_PAIR_ORBIT_BINARY_CUT_BOUNDS_PASSED 8')
print('EXACT_FULL_PAIR_SHARPNESS_AND_SIGNED_SIGNAL_CHECKS_PASSED 1920')
for m in range(3,40):
    assert (target(m)-1)<=F(1,14)
assert (target(4)-1)==F(1,14)
print('UNIQUE_FOUR_TRIANGLE_GLOBAL_COEFFICIENT_BOUND_PASSED')
print('ALL_FRIENDSHIP_NORMALIZED_GINI_CHECKS_PASSED')
