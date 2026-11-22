"""Independent numerical and algebraic sanity checks for the polynomial flow.
Requires Python >=3.10, SciPy and SymPy. Not an infinite-time proof.
"""
from math import pi, sin, sqrt, exp, isfinite
import sympy as sp
from scipy.integrate import solve_ivp

x,y = sp.symbols('x y', real=True)
R=x*x+y*y
for k in (1,2,3,4):
    a,b,c=sp.Integer(3),sp.Integer(5),sp.Integer(7)
    fx=-a*R**k*x-(b*y*y+c*R**2)*y
    fy=-a*R**k*y+(b*y*y+c*R**2)*x
    assert sp.expand(x*fx+y*fy+a*R**(k+1))==0
    assert sp.expand(x*fy-y*fx-R*(b*y*y+c*R**2))==0
print('Four exact polynomial polar-identity checks passed.')

# The first 30 full turns are a finite-data check of U_n/n, not a proof.
for k,a,b,c,tol in [(2,1.,1.,1.,.015), (3,1.,1.,1.,.04),
                       (2,2.,.5,3.,.02), (4,.8,2.,1.5,.075)]:
    p=2*k-3
    def du_dtheta(theta,U):
        r=U[0]**(-1./p)
        return [p*a*r/(b*sin(theta)**2+c*r*r)]
    sol=solve_ivp(du_dtheta,(0.,60*pi),[1.],method='DOP853',rtol=2e-10,
                  atol=2e-10,max_step=.018)
    assert sol.success
    target=2*pi*p*a/sqrt(b*c)
    relative=abs(sol.y[0,-1]/30/target-1.)
    assert relative<tol, (k,a,b,c,relative)
    print(f'k={k}, a={a}, b={b}, c={c}: 30-turn U_n/n relative error {relative:.5f}')

# The k=1 angle remains trapped below a finite multiple of pi.
for a,b,c in [(1.,1.,1.),(2.,.5,3.)]:
    A=b/(2*a); B=c/(2*a)
    def rhs(s,theta):return [A*sin(theta[0])**2+B*exp(-s)]
    for theta0 in (0.,.3,2.9,4.1):
        sol=solve_ivp(rhs,(0.,140.),[theta0],rtol=1e-11,atol=1e-11,
                       max_step=.2)
        assert sol.success
        angle=sol.y[0,-1]
        multiple=round(angle/pi)
        assert multiple*pi-angle>0 and multiple*pi-angle<.1,(angle,multiple)
print('Eight k=1 finite-time angular trapping checks passed.')
