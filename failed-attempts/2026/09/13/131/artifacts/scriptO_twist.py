"""Script O: twist (aperiodicity) certificate probe: gcd of periods of periodic points.
f_star homotopic to A_star (S homotopic to id) => Lefschetz numbers equal; fixed points
of f^n counted via degree. Probe: find period of a few orbits: linear cat map has
fixed point 0 only? det(A-I) = ? compute; for f, 0 is fixed (S(0)=0, A(0)=0).
Also 2-cycle probe via Newton from random seeds; report periods found with gcd 1."""
import numpy as np, math
Amat=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
print("det(A-I) =",round(float(np.linalg.det(Amat-np.eye(3))),6), " => # fixed pts of linear map =",abs(round(float(np.linalg.det(Amat-np.eye(3))))))
a,b=0.03,0.02
def f(x):
    z=np.stack([x[...,0]+a*np.sin(2*np.pi*x[...,1]),x[...,1]+b*np.sin(2*np.pi*x[...,2]),x[...,2]],axis=-1)%1
    return (z@Amat.T)%1
def dist(x,y): return np.abs((x-y+0.5)%1-0.5).max(axis=-1)
rng=np.random.default_rng(5)
X=rng.random((40,3))
for n in range(1,7):
    Xn=X.copy()
    for _ in range(n): Xn=f(Xn)
    d=dist(Xn,X)
    print(f"n={n}: min return dist={d.min():.4f} #close(<0.05)={(d<0.05).sum()}")
# Newton for period-1 (fixed) points near grid
def F(x): return (f(x)-x+0.5)%1-0.5
XF=rng.random((60,3))
for it in range(12):
    h=1e-6; J=np.zeros((60,3,3))
    for j in range(3):
        E=np.zeros((60,3)); E[:,j]=h
        J[:,:,j]=((F(XF+E)-F(XF))/h+0.5)%1-0.5
        # fix wrap in finite diff: use unwrapped f
    try: XF-=(np.linalg.solve(J,F(XF))%(1)+0.5)%1-0.5
    except Exception as e: print("newton fail",e); break
print("fixed-pt candidates (first 5):",np.round(XF[:5],4))
print("residuals:",np.abs(F(XF)).max(axis=1)[:8].round(4))
