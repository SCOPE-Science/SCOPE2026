"""Self-contained checks for the sharp variation gain of the bilateral quadratic-difference smoother.
The exact rational part certifies nonmonotonicity without floating-point assumptions.
"""
from fractions import Fraction
from math import cos, exp, pi, sin, sqrt
import cmath
import random

def solve(a, b):
    """Exact rational Gaussian elimination, partial pivoting unnecessary here (SPD)."""
    n = len(b)
    a = [list(row)+[bi] for row,bi in zip(a,b)]
    for k in range(n):
        pivot = a[k][k]
        assert pivot != 0
        for i in range(k+1,n):
            v = a[i][k]
            if not v:continue
            f=v/pivot
            for j in range(k+1,n+1):a[i][j]-=f*a[k][j]
            a[i][k]=0
    x=[Fraction(0) for _ in range(n)]
    for i in range(n-1,-1,-1):
        x[i]=(a[i][n]-sum(a[i][j]*x[j] for j in range(i+1,n)))/a[i][i]
    return x

def rational_norm_interval(lam, m=7):
    n=2*m+1
    aa={-2:lam,-1:-4*lam,0:1+6*lam,1:-4*lam,2:lam}
    a=[[aa.get(i-j,Fraction(0)) for j in range(n)] for i in range(n)]
    b=[Fraction(int(i==m)) for i in range(n)]
    h=solve(a,b)
    hv={j-m:h[j] for j in range(n)}
    err={i: Fraction(int(i==0))-sum(aa[k]*hv.get(i-k,Fraction(0)) for k in range(-2,3))
         for i in range(-m-2,m+3)}
    e=sum(map(abs,err.values()),Fraction(0))
    nh=sum(map(abs,h),Fraction(0))
    assert 0<e<1
    return nh/(1+e),nh/(1-e),nh,e

one16 = rational_norm_interval(Fraction(1,16))
one9  = rational_norm_interval(Fraction(1,9))
assert one16[0] > Fraction(136,125) # 1.088
assert one9[1] < Fraction(1081,1000) # 1.081
assert one16[0] > one9[1]
print('CERTIFIED_NONMONOTONE_GAIN_PASS', [str(float(v)) for v in one16[:2]], [str(float(v)) for v in one9[:2]])

def q_from_lambda(lam):
    aa=2-1j/sqrt(lam)
    q=(aa-cmath.sqrt(aa*aa-4))/2
    if abs(q)>1:q=(aa+cmath.sqrt(aa*aa-4))/2
    assert abs(q)<1 and q.imag>0
    return q

def kernel(lam,j):
    q=q_from_lambda(lam)
    return (q**(abs(j)+1)/(1-q*q)).imag/sqrt(lam)

def kernel_norm(lam):
    q=q_from_lambda(lam)
    M=max(40,int(50/(-__import__('math').log(abs(q)))))
    return abs(kernel(lam,0))+2*sum(abs(kernel(lam,j)) for j in range(1,M+1))

for lam in (Fraction(1,16),Fraction(1,9)):
    l,u,*_=rational_norm_interval(lam)
    kn=kernel_norm(float(lam))
    assert float(l)<kn<float(u)

for lam in (.001,.01,.1,.6,1,4,100,1600):
    # Exact finite recurrence is satisfied by the independently derived kernel formula.
    aa=[float(lam),-4*float(lam),1+6*float(lam),-4*float(lam),float(lam)]
    for j in range(-14,15):
        z=sum(aa[k+2]*kernel(lam,j-k) for k in range(-2,3))
        assert abs(z-(j==0))<3e-11
    q=q_from_lambda(lam)
    nmax=max(40,int(50/(-__import__('math').log(abs(q)))))
    assert abs(sum(kernel(lam,j) for j in range(-nmax,nmax+1))-1)<3e-11
print('RESOLVENT_KERNEL_AND_MASS_PASS')

random.seed(22403)
for lam in (.02,.2,2,200):
    nmax=max(60,int(50/(-__import__('math').log(abs(q_from_lambda(lam))))))
    kk={j:kernel(lam,j) for j in range(-nmax,nmax+1)}
    K=sum(map(abs,kk.values()))
    for _ in range(24):
        d={j:random.uniform(-1,1) for j in range(-8,9)}
        out={j:sum(kk.get(j-k,0)*v for k,v in d.items()) for j in range(-nmax-10,nmax+11)}
        assert sum(map(abs,out.values())) <= (K+1e-9)*sum(map(abs,d.values()))
print('RANDOM_BV_DIFFERENCE_TESTS_PASS')
lim=1+sqrt(2)*exp(-3*pi/4)/(1-exp(-pi))
assert abs(lim-1.1400934670509761)<1e-12
for lam in (1e4,1e6,1e8):
    assert abs(kernel_norm(lam)-lim)<.012*lam**(-.25)
print('CONTINUUM_GAIN_LIMIT_TESTS_PASS',format(lim,'.15f'))
print('ALL_VARIATION_GAIN_CHECKS_PASS')
