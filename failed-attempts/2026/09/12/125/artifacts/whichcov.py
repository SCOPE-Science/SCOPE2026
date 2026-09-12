import numpy as np
# Resolve covering: Walnut fiber size.
# Standard: for rational ab=p/q, fiber matrices are q x q (Zeebe? "p"?). Here p=11,q=12.
# Walnut rep: S f = b^{-1} sum_k G_k T_{k/b} f. Periodize with step delta = a/q? Let's derive.
# T_{k/b}: fiber index over the 1/b-lattice cosets inside [0,a)? 
# Note 1/b = 6/11 = 12 delta with delta=1/22. a = 1/2 = 11 delta. So the joint grid has step delta, period a=11 delta.
# Fiber at y in [0,delta): the orbit {y + j delta : j=0..10} (11 points = a/delta). Good -> 11x11 fiber. So fiber2/Mmat 11x11 is the correct Walnut fiber.
# ZZ toy 11x12: different object (analysis/synthesis), but Gram should be 11x11 too: G=(1/b)ZZ*. So toy formula G was wrong: it used B=11 rows but q=12 cols with wrong Zak sampling; its min eig ~1 is meaningless.
# Also trace check: tr M(y,theta) = b^{-1} sum_s G0(y+s delta) = (6/11)*sum. mean G0~0.9587*11*6/11=5.75 ✓.
# So fiber floor ~0. Now: is essinf exactly 0? Need: inf_{y,th} lambda_min = 0 with attainment or limit? If 0 attained at isolated points only, still NO frame (need uniform A>0: inf must be >0). Our samples show eigmin ~1e-8..1e-6 ~numerical zero at several points.
# Let's scan fiber min eig on grid fast.
def B3f(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
a=0.5; b=11/6; beta=6/11; delta=1/22; binv=6/11
an=np.arange(-8,9)
GKV={}
xs_pre=np.linspace(-3,3,1321)  # step ~0.0045; Gk smooth; use interpolation
BV=B3f(xs_pre)
def Gk_fast(k, y):
    # direct small sum (only ~9 terms matter)
    tot=0.0
    for n in range(-8,9):
        tot+=float(np.interp(y-n*a, xs_pre, BV))*float(np.interp(y-n*a-k*beta, xs_pre, BV))
    return tot
def min_eig(y, th):
    M=np.zeros((11,11),complex)
    for s in range(11):
        ys=y+s*delta
        for sp in range(11):
            tot=0j
            for k in [s-sp, s-sp-11, s-sp+11]:
                if abs(k)>7: continue
                v=int(round((s-sp-12*k)/11))
                tot+=Gk_fast(k,ys)*np.exp(2j*np.pi*v*th)
            M[s,sp]=binv*tot
    return np.linalg.eigvalsh(M)[0]
import time
t0=time.time()
Ny=22; Nt=24
ys=np.linspace(0,delta,Ny,endpoint=False); ths=np.linspace(0,1,Nt,endpoint=False)
mn=1e9; arg=None
for y in ys:
    for th in ths:
        v=min_eig(y,th)
        if v<mn: mn=v; arg=(y,th)
print(f"scan {Ny}x{Nt}: min={mn:.3e} at {arg}  ({time.time()-t0:.1f}s)")
