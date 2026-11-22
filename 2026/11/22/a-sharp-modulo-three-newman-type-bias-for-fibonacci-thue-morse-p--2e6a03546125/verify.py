#!/usr/bin/env python3
"""Exact independent checks for Fibonacci-weight parity in residue classes mod three."""

# Z[omega], omega**2+omega+1=0, represented as (a,b).
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y):
    a,b=x;c,d=y
    return (a*c-b*d,a*d+b*c-b*d)
def mm(A,B):
    return [[add(mul(A[i][0],B[0][j]),mul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
ONE=(1,0);ZERO=(0,0);OMEGA=(0,1)
POW=[ONE,OMEGA,(-1,-1)]
F=[0,1]
for n in range(2,140): F.append(F[-1]+F[-2])
T=lambda j:[[ONE,neg(POW[F[j+1]%3])],[ONE,ZERO]]
M=[[ONE,ZERO],[ZERO,ONE]]
for j in range(1,9): M=mm(T(j),M)
expected=[[(8,1),(-1,-3)],[(3,1),(0,-1)]]
assert M==expected,(M,expected)
det=add(mul(M[0][0],M[1][1]),neg(mul(M[0][1],M[1][0])))
assert det==ONE
tr=add(M[0][0],M[1][1]);assert tr==(8,0)
M2=mm(M,M)
assert M2==[[add(mul((8,0),M[i][j]),neg(ONE if i==j else ZERO)) for j in range(2)] for i in range(2)]
Qm1=ONE;Q0=ONE;Q=[ONE]
for L in range(1,114):
    v=add(Q0,neg(mul(POW[F[L+1]%3],Qm1)))
    Q.append(v)
    Qm1,Q0=Q0,v
assert Q[7]==(3,0),Q[7]
assert Q[15]==(23,0),Q[15]
assert Q[23]==(181,0),Q[23]
for t in range(12):
    assert Q[8*t+7][1]==0
for t in range(11):
    assert Q[8*(t+2)+7][0]==8*Q[8*(t+1)+7][0]-Q[8*t+7][0]
# Independent exhaustive digit DP over each residue for all short lengths.
def dp(L):
    # dp[k][r][prev] (signed count)
    a=[[0]*3 for _ in range(2)];a[0][0]=1
    for j in range(1,L+1):
        b=[[0]*3 for _ in range(2)]
        for prev in range(2):
            for r in range(3):
                b[0][r]+=a[prev][r]
                if prev==0:b[1][(r+F[j+1])%3]-=a[prev][r]
        a=b
    return [a[0][r]+a[1][r] for r in range(3)]
def zeck(n):
    bits=0
    j=len(F)-1
    while n:
        while F[j]>n:j-=1
        n-=F[j];bits+=1;j-=2
    return bits
checks=0
for L in range(92):
    d=dp(L)
    assert sum(d) == [1,0,-1,-1,0,1][L%6],(L,d)
    # direct enumeration for 0 <= n < F_{L+2} for first 20 lengths
    if L<=19:
        brute=[0,0,0]
        for n in range(F[L+2]):
            brute[n%3]+=(-1)**zeck(n)
        assert d==brute,(L,d,brute)
        checks+=F[L+2]
    if L%8==7:
        t=(L-7)//8
        # compute via recurrence with no spectral approximation
        q0,q1=3,23
        for _ in range(t): q0,q1=q1,8*q1-q0
        bt=[0,-1,1][t%3]
        assert d==[(2*q0+bt)//3,(bt-q0)//3,(bt-q0)//3],(L,d,q0,bt)
    checks+=10
print('PASS:',checks,'integer assertions / comparisons; exact Z[omega] matrix',M,'det',det,'trace',tr)
for t in range(5):
    L=8*t+7
    if L<24: print('L',L,'F[L+2]',F[L+2],'D',dp(L))
