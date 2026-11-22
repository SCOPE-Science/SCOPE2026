"""Algebraic and numerical checks of two-boundary MFPT reconstruction."""
import math
import numpy as np
from scipy.integrate import quad, cumulative_trapezoid
from scipy.integrate import solve_bvp
import sympy as sp

x=sp.symbols('x', real=True)
S=sp.Function('S')(x); q=sp.Function('q')(x)
a=S*q; b=S*(1-q)
D=-1/(S*sp.diff(q,x))
mu=-D*sp.diff(S,x)/S
assert sp.simplify(D*sp.diff(a,x)+mu*a+1)==0
assert sp.simplify(D*sp.diff(b,x)+mu*b-1)==0
assert sp.simplify((D*(-sp.diff(q,x))).diff(x)-mu*(-sp.diff(q,x)))==0

# Exact nonconstant spatial diffusivity, zero drift.
x=sp.symbols('x',real=True,positive=True)
aa=sp.log(2/(1+x)); bb=sp.log(1+x)
SS=sp.simplify(aa+bb); qq=aa/SS
DD=sp.simplify(-1/(SS*sp.diff(qq,x)))
MM=sp.simplify(-DD*sp.diff(SS,x)/SS)
assert sp.simplify(DD-(1+x))==0 and MM==0
assert sp.simplify(-sp.diff(qq,x)-1/((1+x)*sp.log(2)))==0

# Exact nonidentifiability: every smooth g with sufficiently small eps.
g=sp.Function('g')(x); eps=sp.symbols('eps',real=True)
u=x-x*x/2
D1=1+eps*(1-x)*g
mu1=eps*g
assert sp.simplify(D1*sp.diff(u,x,2)+mu1*sp.diff(u,x)+1)==0

# Instability despite uniform convergence of both MFPT curves and first derivatives.
for n in [2,5,10,20,50,100]:
    c=.35
    grid=np.linspace(0,1,2001)
    qn=1-grid+c*np.sin(n*np.pi*grid)/(n*np.pi)
    Sn=np.ones_like(grid)
    Dn=1/(1-c*np.cos(n*np.pi*grid))
    assert (np.diff(qn)<0).all()
    un=cumulative_trapezoid(qn, grid,initial=0)
    vn=cumulative_trapezoid(1-qn,grid,initial=0)
    vn=vn[-1]-vn
    u0=grid-grid*grid/2
    v0=(1-grid*grid)/2
    assert max(abs(un-u0).max(),abs(vn-v0).max()) < c/(n*np.pi)+2e-6
    assert abs(Dn[0]-1)>=c/(1-c)-1e-12

# Compare reconstructed coefficients against BVPs for two nontrivial variable drift and diffusion models.
for amp in [.3,.8]:
    mesh=np.linspace(0,1,1500)
    dd=lambda z: 1+.4*z
    drift=lambda z: amp*(1+.4*z)
    # scale density is exp(-amp*x), and normalization C is fixed by q(0)=1,q(1)=0
    C=quad(lambda z: np.exp(amp*z)/dd(z),0,1,epsabs=1e-12)[0]
    scale=lambda z: C*np.exp(-amp*z)
    cdf=np.array([quad(lambda z: np.exp(amp*z)/dd(z),0,xx,epsabs=1e-11)[0]/C for xx in mesh])
    qq=1-cdf
    aa=scale(mesh)*qq; bb=scale(mesh)*(1-qq)
    # Reference MFPTs obtained from integrated slopes in each direction.
    left=cumulative_trapezoid(aa,mesh,initial=0)
    right=cumulative_trapezoid(bb,mesh,initial=0)
    right=right[-1]-right
    # Solve independent two-point boundary value problems for the same generator.
    for side,target,reference in [('left',left,left),('right',right,right)]:
        if side=='left':
            bc=lambda ya,yb:np.array([ya[0],yb[1]])
            guess=np.vstack((left,aa))
        else:
            bc=lambda ya,yb:np.array([ya[1],yb[0]])
            guess=np.vstack((right,-bb))
        def eq(z,y): return np.vstack((y[1],(-1-drift(z)*y[1])/dd(z)))
        sol=solve_bvp(eq,bc,mesh,guess,tol=2e-7,max_nodes=20000)
        assert sol.success,sol.message
        err=np.max(abs(sol.sol(mesh)[0]-reference))
        assert err<3e-5,(side,err)
    assert np.max(abs(1/(scale(mesh)*np.exp(amp*mesh)/dd(mesh)/C)-dd(mesh)))<1e-12
print('PASS: exact symbolic identities, two analytic model families, 6 instability witnesses, 4 independent BVPs')
