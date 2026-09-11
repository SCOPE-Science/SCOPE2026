"""Ellipticity / Lipschitz / collar check for model CTA pair on Omega=B(0,1)x(0,2).
g0 = I_2 (Euclidean transversal), sigma_j = mu_j * I_3.
mu1 = 1; mu2 = 1 + compact interior bump with TRUE zero in collar of Gamma_acc.
Collar C = {r>0.85} U {x3>1.7}. Bump support: {s<1}, s=sqrt((r/0.35)^2+((x3-0.55)/0.45)^2)
-> r<0.35, x3 in (0.10,1.00): disjoint from collar. Exact zero (incl. gradient) on collar.
"""
import numpy as np

def bump(x, y, z, A=0.2):
    r = np.sqrt(x*x+y*y)
    s2 = (r/0.35)**2 + ((z-0.55)/0.45)**2
    out = np.zeros_like(s2)
    m = s2 < 1.0
    # standard compact bump exp(-1/(1-s^2)), normalized to max 1 at s=0 (value e^-1 -> scale by e)
    out[m] = np.exp(-1.0/(1.0-s2[m]))*np.e
    return A*out

rng = np.random.default_rng(0)
N=400000
xs = rng.uniform(-1,1,N); ys=rng.uniform(-1,1,N); zs=rng.uniform(0,2,N)
mask = xs*xs+ys*ys<1.0
xs,ys,zs = xs[mask],ys[mask],zs[mask]
b = bump(xs,ys,zs)
mu2 = 1.0+b
print(f"samples: {len(b)}")
print(f"mu2 range: [{mu2.min():.6f},{mu2.max():.6f}]")
ok_ell = bool((mu2.min()>=0.5)&(mu2.max()<=2.0))
print(f"ellipticity 0.5<=mu<=2 holds: {ok_ell}")
# Lipschitz: analytic gradient bound of compact bump: |grad| <= A*e*max|d/ds e^{-1/(1-s^2)}|*|grad s|
# d/ds[e^{-1/(1-s^2)}] = e^{-1/(1-s^2)} * (-2s/(1-s^2)^2); max of 2s*e^{-1/(1-s^2)}/(1-s^2)^2 on [0,1)
ss = np.linspace(0,1,1000001)
f = 2*ss*np.exp(-1/(1-ss**2+1e-300))/(1-ss**2+1e-300)**2
f[~np.isfinite(f)] = 0
print(f"max radial profile derivative factor ~ {np.nanmax(f):.4f} (x e x A -> Lipschitz const)")
r = np.sqrt(xs*xs+ys*ys)
collar = (r>0.85)|(zs>1.7)
print(f"max|mu2-mu1| in collar: {np.abs(b[collar]).max():.3e} (must be exactly 0)")
# gradient in collar must be exactly 0: check via finite diff on grid
g = np.linspace(-1,1,401); zz = np.linspace(0,2,401)
X,Z = np.meshgrid(g,zz)
B = bump(X, 0*X, Z)
dBdx = np.gradient(B, g, axis=1); dBdz = np.gradient(B, zz, axis=0)
RR = np.abs(X)
col = (RR>0.85)|(Z>1.7)
print(f"max|grad bump| in collar (grid): {np.maximum(np.abs(dBdx[col]).max(), np.abs(dBdz[col]).max()):.3e}")
print(f"max|grad bump| global (grid): {np.maximum(np.abs(dBdx).max(), np.abs(dBdz).max()):.4f}")
print(f"Linf(mu2-mu1) global: {np.abs(b).max():.4f} (distinctness)")
ok = ok_ell and (np.abs(b[collar]).max()==0.0)
print("NONVACUITY_AND_COLLAR_OK" if ok else "CHECK_FAILED")
