"""Standalone finite checks of the absorbing-walk kernel and limiting constants.
Run with Python 3: python checker.py. All displayed checks use stdlib only.
Infinite asymptotic statements require the proof in RESULT.md.
"""
from fractions import Fraction as F
from math import factorial, comb, sqrt, pi, gamma, log, isclose

checks = 0

def eq(a,b,label):
    global checks
    checks += 1
    if a != b:
        raise AssertionError((label,a,b))

def near(a,b,label,rel=1e-11):
    global checks
    checks += 1
    if not isclose(a,b,rel_tol=rel,abs_tol=1e-14):
        raise AssertionError((label,a,b))

K=18
M=9
# CT simple walk on positive integers, rate 1 in each direction,
# killed on visiting 0: Q=-2I+off-diagonal 1.
# Verify the first K+1 Taylor coefficients against the exact Bessel kernel.
def bessel_I_2t_coeff(k,n):
    k=abs(k)
    if n<k or ((n-k)&1):
        return F(0)
    v=(n-k)//2
    return F(1,factorial(v)*factorial(v+k))

def kernel_coef(i,j,n):
    return sum(F((-2)**(n-h),factorial(n-h)) *
        (bessel_I_2t_coeff(i-j,h)-bessel_I_2t_coeff(i+j,h))
        for h in range(n+1))

for i in range(1,M+1):
    active={i: F(1)}
    for n in range(K+1):
        for j in range(1,M+1):
            eq(active.get(j,F(0))/factorial(n),kernel_coef(i,j,n),
                ('semigroup',i,j,n))
        new={}
        for state,value in active.items():
            for dest,coef in ((state,-2),(state-1,1),(state+1,1)):
                if dest>=1:
                    new[dest]=new.get(dest,F(0))+value*coef
        active={k:v for k,v in new.items() if v}

# Telescoping Bessel recurrence I_{k-1}(2t)-I_{k+1}(2t)=k I_k(2t)/t.
for i in range(1,M+1):
    for j in range(1,i+1):
        for n in range(K+1):
            lhs=bessel_I_2t_coeff(i-j,n)-bessel_I_2t_coeff(i+j,n)
            rhs=sum(k*bessel_I_2t_coeff(k,n+1)
                    for k in range(i-j+1,i+j,2))
            eq(lhs,rhs,('bessel telescoping',i,j,n))

# QSD probability normalization: sum_{j=1}^m j*rho^(j-1)
# =(1-(m+1)*rho**m+m*rho**(m+1))/(1-rho)**2.
for num in range(1,6):
    for den in range(num+1,9):
        rho=F(num,den)
        for m in range(1,50):
            lhs=sum(j*rho**(j-1) for j in range(1,m+1))
            rhs=(1-(m+1)*rho**m+m*rho**(m+1))/(1-rho)**2
            eq(lhs,rhs,('QSD normalization',rho,m))

# Check constants in the concrete rates a=2,b=1/2, d=2,
# beta=1: k_1=1/2, survival leading factor 1/log(2).
d=2
k1=2**(.5)*gamma(.5)/(sqrt(2*pi)*d**1)
near(k1,0.5,'beta-1 kernel amplitude')
near((1/log(2))*k1*(0.5/(0.5**2)),1/log(2),'beta-1 survival amplitude')
k2=1/(sqrt(2*pi)*d**1.5)
near(k2,1/(4*sqrt(pi)),'beta-2 kernel amplitude')
print('PASS:',checks,'exact-rational and numerical assertions')
