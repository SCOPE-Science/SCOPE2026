"""Exact-rational replay tests for one-column heat-kernel Nyström on unit stars.

Run: python3 CHECK.py
Standard library only. Finite tests supplement, but do not replace, the proof.
"""
from fractions import Fraction as Q
from math import exp, log

checks = 0

def require(condition, msg):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(msg)

def matmul(A, B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)),Q(0))
             for j in range(n)] for i in range(n)]

def exact_kernel(m, a):
    """Combinatorial star heat kernel for a=e^{-t}, exactly in Q."""
    n=m+1
    b=a**n
    u=[m]+[-1]*m
    return [[Q(1,n)+a*(Q(i==j)-Q(1,n)-Q(u[i]*u[j],m*n))
             +b*Q(u[i]*u[j],m*n) for j in range(n)] for i in range(n)]

def formulas(m,a):
    b=a**(m+1)
    H=Q(1+m*b,m+1)
    D=(m+b+(m*m-1)*a)/(m*(m+1))
    H2=Q(1+m*b*b,m+1)
    D2=(m+b*b+(m*m-1)*a*a)/(m*(m+1))
    GH=H2/H
    GL=D2/D
    F=m*a*b+a+b-1
    difference=-Q(m*m-1)*(a-b)*F/((1+m*b)*(m+b+(m*m-1)*a))
    return H,D,H2,D2,GH,GL,F,difference

for m in range(2,15):
    for a in [Q(1,9), Q(1,4), Q(2,5), Q(1,2), Q(3,4), Q(9,10)]:
        K=exact_kernel(m,a)
        K2=exact_kernel(m,a*a)
        KK=matmul(K,K)
        H,D,H2,D2,GH,GL,F,diff=formulas(m,a)
        require(all(sum(row,Q(0))==1 for row in K),'row sums')
        for i in range(m+1):
            for j in range(m+1):
                require(KK[i][j]==K2[i][j], 'semigroup exact test')
                require(K[i][j]==K[j][i], 'symmetric heat kernel')
        require(K[0][0]==H,'hub diagonal')
        require(all(K[j][j]==D for j in range(1,m+1)),'leaf diagonal')
        require(K2[0][0]==H2 and K2[1][1]==D2,'second time diagonals')
        require(D>H,'max diagonal always a leaf')
        require(GH-GL==diff,'factor exact identity')
        require((GH>GL)==(F<0),'sign threshold')
        require((GL>GH)==(F>0),'sign threshold reverse')


def f(m,t):
    return m*exp(-(m+2)*t)+exp(-(m+1)*t)+exp(-t)-1

def root(m):
    low,high=0.,1.
    while f(m,high)>0: high*=2
    for _ in range(120):
        mid=(low+high)/2
        if f(m,mid)>0:low=mid
        else:high=mid
    return (low+high)/2

for m in [2,3,4,7,10,20,50,100,500,1000]:
    z=root(m)
    require(f(m,z/2)>0 and f(m,2*z)<0,'opposite sides')
    if m>=50:
        # A soft numerical spot-check, not an asymptotic proof.
        require(abs(m*z-log(m*m))<20,'root scale bound')

print('PASS:',checks,'exact-rational and numerical assertions')
print('Sample thresholds:',[(m,round(root(m),12)) for m in (2,3,10,100)])
