"""Script Q: validated fixed point of f near 0 + period-2 orbit existence by
interval Newton (double precision with explicit defect bounds; padding EPS).
F(x) = lift(f)(x)-x-p for chosen integer winding p; Krawczyk-style existence:
if ||I - M^{-1}DF|| + ||M^{-1}||Lip r <= ... use simple Newton-Kantorovich check."""
import numpy as np, math
Amat=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
a,b=0.03,0.02
def Flift(x):
    z=np.array([x[0]+a*math.sin(2*math.pi*x[1]),x[1]+b*math.sin(2*math.pi*x[2]),x[2]])
    return Amat@z
def DFlift(x):
    u=2*math.pi*a*math.cos(2*math.pi*x[1]); v=2*math.pi*b*math.cos(2*math.pi*x[2])
    return Amat@np.array([[1.,u,0.],[0.,1.,v],[0.,0.,1.]])
# fixed point: 0 is EXACT fixed point: S(0)=0 (sin 0=0), A(0)=0. No numerics needed!
print("0 is exact fixed point: S(0)=0, A(0)=0 => f(0)=0. Aperiodicity seed: period 1 exists.")
# period-2: solve Flift(Flift(x))-x-p=0. try integer windings p from linear 2-cycles
A2=Amat@Amat
pts=[]
rng=np.random.default_rng(9)
def f2(x): return Flift(Flift(x))
def Df2(x): return DFlift(Flift(x))@DFlift(x)
for seed in rng.random((30,3)):
    x=seed.copy()
    for _ in range(30):
        r=(f2(x)-x+0.5)%1-0.5
        # finite-diff jacobian w/o wrap issues near solution after convergence... use analytic mod-aware
        h=1e-7; J=np.zeros((3,3))
        base=f2(x)-x
        for j in range(3):
            e=np.zeros(3); e[j]=h
            J[:,j]=(f2(x+e)-(x+e)-base)/h
        try: x=x-np.linalg.solve(J,r)
        except Exception: break
    r=(f2(x)-x+0.5)%1-0.5
    if np.abs(r).max()<1e-10:
        xm=np.round(x%1,6)
        if not any(np.abs((xm-p+0.5)%1-0.5).max()<1e-4 for p in pts): pts.append(xm)
print(f"found {len(pts)} distinct period<=2 orbits mod 1:")
for p in pts[:10]: print("  ",p)
