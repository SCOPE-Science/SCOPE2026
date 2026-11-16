"""Independent finite consistency tests for the coherent double-hat Gabor theorem.
Finite tests complement, but do not replace, the analytic arguments."""
import math
import cmath
import random
from scipy.optimize import minimize_scalar

random.seed(20260911)
checks = 0

def check(test, context):
    global checks
    checks += 1
    if not test:
        raise AssertionError(context)

def energy(d, c, x, theta):
    h_plus=(1-x)+x*cmath.exp(1j*theta)
    h_minus=(1-x)-x*cmath.exp(1j*theta)
    z=cmath.exp(-1j*d*theta)
    return abs((1+c*z)*h_plus)**2+abs((1+(-1)**d*c*z)*h_minus)**2

def energy_closed(d,c,x,theta):
    rho=abs(c)
    t=2*x*(1-x)
    if d%2==0:
        return 2*(1-t)*abs(1+c*cmath.exp(-1j*d*theta))**2
    return 2*(1+rho*rho)*(1-t)+4*t*math.cos(theta)*(c*cmath.exp(-1j*d*theta)).real

def m_odd(d, c):
    # Roots of the derivative can be found by bracketing all derivative sign changes
    # on a sufficiently fine grid for these finite tests only.
    if not c: return 0.
    phi=cmath.phase(c)
    def P(t):return math.cos(t)*math.cos(d*t-phi)
    def deriv(t):return -math.sin(t)*math.cos(d*t-phi)-d*math.cos(t)*math.sin(d*t-phi)
    N=800*d
    from scipy.optimize import brentq
    roots=[0., 2*math.pi]
    last_t=0;last_f=deriv(0)
    for i in range(1,N+1):
        t=2*math.pi*i/N; f=deriv(t)
        if last_f*f<0:
            roots.append(brentq(deriv,last_t,t,xtol=1e-14))
        if f==0:roots.append(t)
        last_t,last_f=t,f
    return min(P(t) for t in roots)

for d in range(1,12):
    for j in range(100):
        c=complex(random.uniform(-2,2),random.uniform(-2,2))
        x=random.random()
        theta=random.uniform(-math.pi,math.pi)
        check(abs(energy(d,c,x,theta)-energy_closed(d,c,x,theta))<1e-11,('energy identity',d,j))
        check(energy(d,c,x,theta)>=-1e-12,('positive',d,j))
        bound=2*(abs(c)+1)**2 if d%2==0 else 2*(1+abs(c)**2)
        check(energy(d,c,x,theta)<=bound+1e-11,('upper',d,j))

for d in (1,2,3,4,5,6,7,8):
    for c in (0,1,2,-1,-0.5,0.5+0.7j,-1+0.05j,1j,2j):
        rho=abs(c); D=1+rho**2
        if d%2==0:
            a=(rho-1)**2
            b=2*(rho+1)**2
        else:
            a=D+2*rho*m_odd(d,c)
            b=2*D
        check(a>=-1e-10 and a<=b,('bounds',d,c,a,b))
        # Numerical grid only verifies agreement, not exact global minimization.
        grid=[energy(d,c,x,t*2*math.pi/1600) for x in (0,.5,1) for t in range(1601)]
        check(abs(min(grid)-a)<0.001,('minimum',d,c,min(grid),a))
        check(abs(max(grid)-b)<0.001,('maximum',d,c,max(grid),b))
        if d==1:
            formula=1+rho**2+c.real-rho
            check(abs(a-formula)<1e-12,('adjacent',c,a,formula))

for d in (1,3,5,7):
    for eps in (0.003,0.001):
        c=-1+1j*eps
        exact=1+abs(c)**2+2*abs(c)*m_odd(d,c)
        approx=eps**2/(d*d+1)
        check(abs(exact-approx)<2e-8,('odd anisotropy',d,eps,exact,approx))
for eps in (0.003,0.001):
    even=(math.sqrt(1+eps*eps)-1)**2
    approx=eps**4/4
    check(abs(even-approx)<1e-10,('even quartic',eps,even,approx))
check(abs((1+1+2*m_odd(3,1))-7/8)<1e-12,('d3 value',m_odd(3,1)))
print('PASS:',checks,'finite algebraic/numerical assertions')
