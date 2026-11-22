"""Reproducibility checks for inverse-square adaptive-reset excursion times.

Requires Python 3, SymPy, NumPy, SciPy. The mathematical proof uses
positivity of the Feynman--Kac Green kernel, not numerical experiments.
"""
import math
import sympy as sp
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
import numpy as np

h, b, D, y = sp.symbols('h b D y', positive=True)
q = D * h*(h+1)/y**2
A = D*(h+2)*(h-1)
M1 = (y**2 + 2*b**(h+2)*y**(-h)/h)/A
m1_at_b = b**2/(D*h*(h-1))
m2_at_b = 2*b**4*(2*h-3)/(D**2*h**2*(h-1)*(h-3)*(2*h-1))
cv2 = (2*h**2-3*h+3)/((h-3)*(2*h-1))

def equal(lhs,rhs):
    assert sp.simplify(lhs-rhs) == 0, sp.factor(lhs-rhs)

equal(D*sp.diff(M1,y,2)-q*M1,-1)
equal(sp.diff(M1,y).subs(y,b),0)
equal(M1.subs(y,b),m1_at_b)
# Green at the reflecting endpoint, for source f.
G = b**(h+1)*y**(-h)/(D*h)
m2_from_green = 2*b**(h+1)/(D*h)*(b**(3-h)/(h-3)+2*b**(h+2)/h*b**(1-2*h)/(2*h-1))/A
equal(m2_from_green,m2_at_b)
equal(m2_at_b/m1_at_b**2 - 1,cv2)
equal(cv2,1+4*h/((h-3)*(2*h-1)))
equal(sp.diff(cv2,h),-4*(2*h**2-3)/((h-3)**2*(2*h-1)**2))

# Independent truncated-domain elliptic finite-difference calculation:
# Reflecting at b; absorbing at y=L. The truncated moments are lower
# than the infinite-domain moments and increase with L.
def approx(hv, L=150.0, grid=12001):
    bb=1.0; dd=1.0
    dx=(L-bb)/(grid-1)
    yy=np.linspace(bb,L,grid)
    rate=hv*(hv+1)/yy[:-1]**2
    main=2*dd/dx**2 + rate
    low=np.full(grid-2,-dd/dx**2)
    up=np.full(grid-2,-dd/dx**2)
    up[0]=-2*dd/dx**2
    mat=diags([low,main,up],[-1,0,1],format='csr')
    one=spsolve(mat,np.ones(grid-1))
    two=spsolve(mat,2*one)
    return one[0],two[0]

for hv in (4.0,5.0,8.0):
    one,two=approx(hv)
    exact_one=float(m1_at_b.subs({h:hv,b:1,D:1}))
    exact_two=float(m2_at_b.subs({h:hv,b:1,D:1}))
    assert abs(one/exact_one-1)<0.02,(hv,one,exact_one)
    assert abs(two/exact_two-1)<0.04,(hv,two,exact_two)
    print(f'h={hv:g}: finite-domain E[R]={one:.9f} vs {exact_one:.9f}, '
          f'E[R²]={two:.9f} vs {exact_two:.9f}')
print('PASS: exact ODE/Green/variance identities and independent elliptic discretizations')
