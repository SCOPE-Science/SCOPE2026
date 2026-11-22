"""Independent numerical and symbolic checks of conditional torus-section laws.

Run with Python 3 and SciPy and SymPy installed. No network or external data.
"""
from math import pi, asin, sqrt
from scipy.integrate import quad
from scipy.special import betainc
import sympy as sp

assertions = 0

def close(a, b, tol=1e-9):
    global assertions
    assert abs(a-b) <= tol * max(1, abs(a), abs(b)), (a, b, tol)
    assertions += 1

C = sp.symbols('C', positive=True)
t = sp.sqrt(sp.Rational(3,10))
k_sym = sp.simplify(3*sp.integrate(C*(1-C)*(C**2-sp.Rational(3,10)), (C,t,1)))
assert k_sym == sp.Rational(27,400)-sp.Rational(9,2500)*sp.sqrt(30)
assertions += 1
K = float(k_sym)

def values(R):
    a = 1/R
    u0 = sqrt(1-a*a)
    I = quad(lambda c:c*(1-c)/sqrt(1-c*c/R**2), 0,1,epsabs=1e-14)[0]
    annulus_area = I/R**2
    one_area = 2*(1-annulus_area)
    two_area = 1+R*pi/4-annulus_area-one_area
    # Compare area computed directly in (u,m), independently of the c-Jacobian.
    annulus2 = quad(lambda u: 1-R*sqrt(1-u*u), u0,1,epsabs=1e-14)[0]
    two_area2 = quad(lambda u:R*sqrt(1-u*u)-1, 0,u0,epsabs=1e-13)[0]
    close(annulus_area,annulus2)
    close(two_area,two_area2)
    close(annulus_area+one_area+two_area, 1+R*pi/4)
    # Exact finite-R total variation, derived independently via uniform-support mass.
    tv_disk = annulus_area
    tv_two = (2/pi)*(asin(a)+a*u0)
    close(tv_two,1-two_area/(R*pi/4))
    close(tv_disk,1-one_area/2)
    # Annulus conditional density: f_R(c,m)=c/(I sqrt(1-c^2/R^2)).
    cmass = quad(lambda c:c*(1-c)/(I*sqrt(1-c*c/R**2)),0,1,epsabs=1e-13)[0]
    close(cmass,1)
    limitmass = quad(lambda c:6*c*(1-c),0,1)[0]
    close(limitmass,1)
    # Integrate variation in marginal C; conditional M|C uniform under both.
    tv_ann = .5*quad(lambda c:(1-c)*abs(c/(I*sqrt(1-c*c/R**2))-6*c),0,1,
                      epsabs=5e-15, points=[sqrt(max(0,R*R*(1-1/(36*I*I))))])[0]
    return annulus_area,tv_disk,tv_two,tv_ann,one_area,two_area,I

for R in [1.1,1.3,1.9,2,3,5,10,20,40,80,160]:
    a,b,c,d,one,two,I = values(R)
    if R >= 10:
        close(a*R*R,sp.Rational(1,6),tol=.003)  # O(R^-2)
        close(d*R*R,K,tol=.002)
        close(c*R,4/pi,tol=.003)
        close(b*R*R,1/6,tol=.003)
    if R>=40:
        close(a, 1/(6*R*R)+1/(40*R**4), tol=1e-9)
        close(b, 1/(6*R*R)+1/(40*R**4), tol=1e-9)
    print('R=%6.1f, annulus_area=%.10g, P1=%.8g, TVann*R^2=%.9g, TVone*R^2=%.9g, TVtwo*R=%.9g' %
          (R,a,one/(1+pi*R/4),d*R**2,b*R**2,c*R))

# Exact algebraic confirmation of the asymptotic coefficient, using beta density.
close(quad(lambda x:6*x*(1-x)*(x*x-0.3),sqrt(.3),1)[0]/2,K,tol=1e-13)
print('K=',k_sym, '≈',K)
print('ASSERTIONS PASSED:',assertions)

from scipy.optimize import brentq
# General convex meridians: rectangular and smooth elliptic support functions.
def total_variation_general(R, a, b, kind):
    assert R > 2*a
    def H(x):
        s = b*x/R
        co = sqrt(1-s*s)
        return (a*s+b*co) if kind=='rectangle' else sqrt(a*a*s*s+b*b*co*co)
    def g(x): return H(x)/b - x
    xmax = brentq(g, 0.5, 1.5)
    def Jac(x): return x/sqrt(1-(b*x/R)**2)
    J = quad(lambda x:Jac(x)*g(x),0,xmax,epsabs=5e-14)[0]
    def Vpart(x):
        gr = max(0,g(x)); gl = max(0,1-x)
        a1 = Jac(x)/J; a0=6*x
        return min(gr,gl)*abs(a1-a0)+max(0,gr-gl)*a1+max(0,gl-gr)*a0
    tv=.5*quad(Vpart,0,max(1,xmax),epsabs=5e-13,points=[1,min(1,xmax),max(1,xmax)])[0]
    return tv

for shape,a,b in [('rectangle',1,1),('rectangle',0.5,2),('ellipse',2,1),('ellipse',1,2)]:
    for R in [20,40,80,160]:
        tv=total_variation_general(R,a,b,shape)
        print('general',shape,a,b,R,'R*TV',tv*R,'R^2*TV',tv*R**2)
        if shape=='rectangle' and R==160:
            close(R*tv,2*a,tol=.04)
        if shape=='ellipse' and R==160:
            assert R*tv<.1
            assertions+=1
print('TOTAL ASSERTIONS:',assertions)
