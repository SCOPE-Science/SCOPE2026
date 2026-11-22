"""Reproducibility checks for geodesic Matern mixture repair on the circle.
Finite diagnostics supplement the exact coefficient proof in RESULT.md.
Requires Python 3, mpmath, sympy.
"""
import math
import mpmath as mp
import sympy as sp

mp.mp.dps=60
COUNT=0

def check(cond, label):
    global COUNT
    if not cond: raise AssertionError(label)
    COUNT += 1

def constants(a):
    Q=mp.expm1(mp.pi*a)
    L=a*mp.pi*(1+a*mp.pi)/(3*Q)
    c=4*mp.pi*a**3/(3*Q)
    d=8*a**4/3
    return L,c,d

def threshold(a, max_m=10000):
    L,c,d=constants(a)
    xstar=c/(2*d)
    # max is within the two indices straddling xstar
    root=max(mp.mpf('0'),(1/xstar-a*a))/4
    m0=max(1,int(mp.floor(mp.sqrt(root))))
    opts={max(1,m0-1),m0,m0+1,m0+2}
    return max((L+c/(a*a+4*m*m)-d/(a*a+4*m*m)**2,m) for m in opts)

def Fourier_ratio(a,n):
    E=mp.exp(-mp.pi*a)
    s=(-1)**n
    A=1-s*E
    B=s*mp.pi*E
    C=-s*mp.pi**2*E
    D=a*a+n*n
    return (-B*a/3+C*a*a/3)/A - 4*B*a**3/(3*A*D)+8*a**4/(3*D**2)

def integral_ratio(a,n):
    D=a*a+n*n
    E=mp.exp(-mp.pi*a)
    I=a*(1-(-1)**n*E)/D
    J=mp.quad(lambda th:mp.exp(-a*th)*(1+a*th+(a*th)**2/3)*mp.cos(n*th),[0,mp.pi])
    return J/I

# Symbolic differentiation identity in rational A, A', A'' form.
a,x,A,B,C=sp.symbols('a x A B C')
I=a*A*x
T=lambda f:sp.diff(f,a)+sp.diff(f,x)*(-2*a*x**2)+sp.diff(f,A)*B+sp.diff(f,B)*C
actual=sp.expand((I-a*T(I)+a*a*T(T(I))/3)/I)
expected=8*a**4*x**2/3-4*B*a**3*x/(3*A)-B*a/(3*A)+C*a*a/(3*A)
check(sp.simplify(actual-expected)==0,'symbolic coefficient identity')

for av in ['0.04','0.1','0.2','0.5','0.8','1','2','3']:
    z=mp.mpf(av)
    b,active=threshold(z)
    L,c,d=constants(z)
    check(b>L,'strict finite spectral notch '+av)
    check(active>=1,'valid active degree '+av)
    xstar=c/(2*d)
    n=2*active
    check(abs(b-(L+c/(z*z+n*n)-d/(z*z+n*n)**2))<mp.mpf('1e-48'),'active exact '+av)
    # Include finite modes surrounding active, and the zeroth and odd modes.
    for k in set([0,1,2,3,4,5,6,7,8,max(2,n-2),n,n+2,max(2,n+20)]):
        j=Fourier_ratio(z,k)
        chk=b+j
        check(chk>=-mp.mpf('1e-48'),'positive modes '+av+':'+str(k))
        if k%2==1:check(j>0,'odd mode '+av+':'+str(k))
    for k in [0,1,2,4]:
        check(abs(integral_ratio(z,k)-Fourier_ratio(z,k))<mp.mpf('1e-40'),'quadrature '+av+':'+str(k))
    # At a lower weight, the active mode violates PSD.
    check(b-mp.mpf('1e-5')+Fourier_ratio(z,n)<0,'sharp failure '+av)

# All tested neighboring switches unique, in increasing order.
def crossing(m):
    fn=lambda z:2*mp.pi/(4*z*mp.expm1(mp.pi*z)) - 1/(z*z+4*m*m)-1/(z*z+4*(m+1)*(m+1))
    lo=mp.mpf('1e-6');hi=mp.mpf(1)
    while fn(hi)>0:hi*=2
    for _ in range(130):
        md=(lo+hi)/2
        if fn(md)>0:lo=md
        else:hi=md
    return (lo+hi)/2
last=mp.mpf('0')
for m in range(1,40):
    z=crossing(m)
    check(z>last,'switch ordering '+str(m))
    L,c,d=constants(z)
    f=lambda j:L+c/(z*z+4*j*j)-d/(z*z+4*j*j)**2
    check(abs(f(m)-f(m+1))<mp.mpf('1e-30'),'switch equality '+str(m))
    for j in set([max(1,m-2),max(1,m-1),m,m+1,m+2,m+3]):
        check(f(j)<=f(m)+mp.mpf('1e-30'),'switch dominance '+str(m)+':'+str(j))
    last=z

# Continuous limiting optimum and the exponentially growing active degree.
for av in ['1','2','3','4']:
    z=mp.mpf(av)
    b,m=threshold(z)
    L,c,d=constants(z)
    cont=L+c*c/(4*d)
    check(0<=cont-b<10*z*mp.exp(-3*mp.pi*z),'asympt discretization '+av)
    approx=mp.sqrt(z/mp.pi)*mp.exp(mp.pi*z/2)
    check(abs(m/approx-1)<mp.mpf('0.20'),'active index asympt '+av)

print('PASSED',COUNT,'finite analytic/numerical diagnostics')
for av in ['0.1','0.2','0.5','1','2','3']:
    z=mp.mpf(av);b,m=threshold(z)
    print('a=',av,'b_crit=',mp.nstr(b,19),'active even n=',2*m)
for m in [1,2,3,5,10,20]:print('switch m=',m,'a=',mp.nstr(crossing(m),16))
