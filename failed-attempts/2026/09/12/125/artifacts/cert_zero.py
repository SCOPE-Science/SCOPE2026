import numpy as np
from fractions import Fraction
def B3(x):
    # exact rational evaluation at dyadic/11-grid points via Fractions
    from fractions import Fraction
    ax = abs(x)
    if ax < 1: return (Fraction(4)-6*x*x+3*ax**3)/6
    elif ax <= 2: return (Fraction(2)-ax)**3/6
    else: return Fraction(0)
a=Fraction(1,2)
def Za_exact(x,nu):
    # nu in {0, 1/2}? e^{2pi i k nu} = (-1)^k if nu=1/2; =1 if nu=0
    tot=Fraction(0)
    # returns possibly complex only for general nu; here real
    for k in range(-8,9):
        w = 1 if nu==0 else ((-1)**k)
        tot += B3(x-a*k)*w
    return tot
b=Fraction(11,6); p=11; q=12
# point x=0.24=6/25? use x grid: report said (0.24,0.0) on coarse grid step 0.02 -> x=6/25? Actually linspace(0,.5,25): x=0.24 yes =6/25. nu=0.
# Build exact 11x12 integer matrix with convention B: Z[r,s]=Za(x + s*a/q - r/b, 0)
x=Fraction(6,25); nu=0
Z=[[Fraction(0)]*q for _ in range(p)]
for r in range(p):
    for s in range(q):
        Z[r][s]=Za_exact(x + Fraction(s,1)*a/q - Fraction(r,1)/b, nu)
# print rank via float SVD + exact integer null vector attempt: find rational null vector of Z (12 unknowns, 11 eqns) -> guaranteed nonzero! That's trivial (more cols than rows).
# The frame criterion needs uniform lower bound of smallest singular value over (x,nu), not a single zero. Single-point near-zero SVD does not disprove frame; need zero on positive-measure set i.e. det of Gram = 0 on open set, or explicit l2 kernel sequence.
# So diagnose: compute min over grid of smin with finer grid to see if smin touches 0 only at isolated points (consistent with frame) or on curves.
import numpy as np
def B3f(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
def Zaf(x,nu):
    tot=0j
    for k in range(-8,9):
        tot+=B3f(np.array([x-0.5*k]))[0]*np.exp(2j*np.pi*k*nu)
    return tot
def smin(x,nu):
    Z=np.zeros((11,12),complex)
    for r in range(11):
        for s in range(12):
            Z[r,s]=Zaf(x+s*0.5/12-r/(11/6),nu)
    return np.linalg.svd(Z,compute_uv=False)[-1]
xs=np.linspace(0,0.5,101); nus=np.linspace(0,1,101)
M=np.zeros((101,101))
for i,x in enumerate(xs):
    for j,nu in enumerate(nus):
        M[i,j]=smin(x,nu)
print("global min",M.min(),"max",M.max(),"mean",M.mean())
print("frac<1e-3:",np.mean(M<1e-3),"frac<1e-2:",np.mean(M<1e-2),"frac<0.05:",np.mean(M<0.05))
i,j=np.unravel_index(np.argmin(M),M.shape); print("argmin",xs[i],nus[j])
# slice at nu=0
row=M[:,0]; print("nu=0 slice min/max:",row.min(),row.max())
