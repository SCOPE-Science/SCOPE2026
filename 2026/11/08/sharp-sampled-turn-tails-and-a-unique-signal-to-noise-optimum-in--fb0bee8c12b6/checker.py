"""Independent algebra, geometry, Gaussian-transition and optimization diagnostics.

Run: python3 checker.py
Requires numpy, scipy and sympy. Finite samples diagnose but do not prove limits.
"""
from math import pi, sin, cos, sqrt, log
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm, solve_continuous_lyapunov
from scipy.optimize import minimize_scalar
import sympy as sp

checks = 0

def check(test, label):
    global checks
    if not test:
        raise AssertionError(label)
    checks += 1

Tx, Ty, u = 1.0, 5.0, 0.5
S = Tx + Ty
Delta = Tx - Ty
A, B = 4*Tx*Ty, Delta**2
M = np.array([[-1., u], [u, -1.]])
D = np.diag([Tx, Ty])
Sigma = solve_continuous_lyapunov(-M, 2*D)
C = np.array([[0., -1.], [1., 0.]])
det = (A+B*u*u)/(4*(1-u*u))
rho0 = 1/(2*pi*sqrt(det))
mean_rate = u*Delta/(2*sqrt(det))
variance_coef = S/(2*sqrt(det))
check(np.allclose(M@Sigma+Sigma@M+2*D, 0., atol=1e-12), 'Lyapunov covariance')
check(np.all(np.linalg.eigvalsh(Sigma)>0), 'positive stationary covariance')
check(abs(np.linalg.det(Sigma)-det)<1e-12, 'covariance determinant')
check(np.allclose(M@Sigma+D, u*Delta/2*C, atol=1e-12), 'stationary current')
check(abs(mean_rate + 1/sqrt(8)) < 1e-12, 'example mean rate')
check(abs(variance_coef - 3/sqrt(8)) < 1e-12, 'example variance coefficient')

v = sp.symbols('v', positive=True)
Hsymbol = (sp.pi-v+sp.sin(v)*sp.cos(v))/(2*sp.sin(v)**2)
gsymbol = ((sp.pi-v)*sp.cos(v)+sp.sin(v))/sp.sin(v)**3
check(sp.simplify(sp.diff(Hsymbol,v)+gsymbol)==0, 'H derivative equals -g')
check(sp.simplify(Hsymbol.subs(v,sp.pi/2)-sp.pi/4)==0, 'half turn tail profile')
check(sp.limit(v**2*Hsymbol,v,0)==sp.pi/2, 'small-angle singular coefficient')

def H(alpha):
    return (pi-alpha+sin(alpha)*cos(alpha))/(2*sin(alpha)**2)

def g(alpha):
    return ((pi-alpha)*cos(alpha)+sin(alpha))/sin(alpha)**3

for alpha in [0.4, 0.8, pi/2, 2.1, 2.8]:
    # independent physical area: integrate horizontal widths of the disk segment
    R = 1/(2*sin(alpha))
    center_y = 0.5*cos(alpha)/sin(alpha)
    integral, _ = quad(lambda y: 2*sqrt(max(0.,R*R-(y-center_y)**2)),
                       max(0.,center_y-R), center_y+R, epsabs=1e-10)
    check(abs(integral-H(alpha)/2)<1e-8, 'independent chord-segment area')
    check(g(alpha)>0., 'positive macroscopic-turn profile')

for p in [2.25, 2.5, 3.0, 4.0, 5.0]:
    val, err = quad(lambda alpha:alpha**p*g(alpha),0,pi,epsabs=1e-7)
    check(val>0 and err<1e-5, 'finite high-order moment integral')

ys = sp.symbols('ys', real=True)
P=2*A+(B-3*A)*ys-2*B*ys*ys
yopt=(B-3*A+sqrt((B-3*A)**2+16*A*B))/(4*B)
check(abs(yopt-0.625)<1e-12, 'exact signal-to-noise optimizer')
check(abs(float(P.subs(ys, yopt)))<1e-12, 'optimal polynomial root')
check(float(P.subs(ys,0.5))>0 and float(P.subs(ys,2/3))<0, 'sharp optimizer bracket')
objective=lambda y: y*sqrt(1-y)/sqrt(A+B*y)
res=minimize_scalar(lambda y:-objective(y),bounds=(0,1),method='bounded',options={'xatol':1e-12})
check(res.success and abs(res.x-yopt)<1e-5, 'independent numerical global search')
for yy in np.linspace(0,1,501):
    check(objective(yy)<=objective(yopt)+1e-12,'dense independent optimizer scan')

# The random sample uses the exact two-time stationary OU Gaussian law, not
# the rare-turn asymptotic construction.
rng = np.random.default_rng(20261101)
L = np.linalg.cholesky(Sigma)
n = 1_200_000
for h in (0.012, 0.003):
    F=expm(M*h)
    innovation = Sigma-F@Sigma@F.T
    Li=np.linalg.cholesky(innovation)
    total_plus=0
    total_cubic=0.0
    total_signed=0.0
    total_quadratic=0.0
    for _ in range(6):
        k=n//6
        start=rng.standard_normal((k,2))@L.T
        end=start@F.T + rng.standard_normal((k,2))@Li.T
        theta=np.arctan2(start[:,0]*end[:,1]-start[:,1]*end[:,0],
                         np.einsum('ij,ij->i',start,end))
        total_plus += np.count_nonzero(theta>pi/2)
        total_cubic += float((abs(theta)**3).sum())
        total_signed += float(theta.sum())
        total_quadratic += float((theta**2).sum())
    predicted_plus = rho0*S*H(pi/2)
    observed_plus = total_plus/(n*h)
    predicted_cube=(S/(pi*sqrt(det)))*quad(lambda t:t**3*g(t),0,pi)[0]
    observed_cube=total_cubic/(n*h)
    observed_mean=total_signed/(n*h)
    observed_quad=total_quadratic/(n*h*log(1/h))
    print(f'h={h}: plus-tail/h={observed_plus:.6f}, limit={predicted_plus:.6f}; '
          f'cubic/h={observed_cube:.6f}, limit={predicted_cube:.6f}; '
          f'mean/h={observed_mean:.6f}, limit={mean_rate:.6f}; '
          f'second/(h log1/h)={observed_quad:.6f}, limit={variance_coef:.6f}')
    check(abs(observed_plus/predicted_plus-1)<0.16, 'Gaussian sampled-turn tail')
    check(abs(observed_cube/predicted_cube-1)<0.18, 'Gaussian sampled-turn cubic')
    check(abs(observed_mean-mean_rate)<0.13, 'Gaussian signed mean')
    check(variance_coef<observed_quad<1.8*variance_coef, 'finite-h log variance trend')
print(f'PASSED {checks} independent algebra/geometry/finite-Gaussian diagnostics')
