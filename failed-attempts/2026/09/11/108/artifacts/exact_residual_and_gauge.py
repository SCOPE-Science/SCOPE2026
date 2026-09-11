"""Exact eikonal residual for conformal transversal g0 + gauge-rigidity sanity.
1) g0(x')=(1+0.3 r^2)I_2, Phi=x3+i(a x1+b x2), a^2+b^2=1:
   G^{-1}=diag(e^{-2l},e^{-2l},1), l=0.5*log(1+0.3r^2).
   E = G^{jk}d_jPhi d_kPhi = 1 - (a^2+b^2)e^{-2l} = 1-1/(1+0.3r^2) = 0.3r^2/(1+0.3r^2). EXACT.
2) Gauge: F(x',x3)=(x',x3+phi), phi compact interior bump; pushforward of sigma=mu I:
   F_*sigma = (DF sigma DF^T/det DF)∘F^{-1}; DF=I+e3⊗grad phi... off-diagonal (F_*sigma)_{i3} propto d_i phi.
   Nonzero unless phi const -> leaves CTA class (blockdiag with fixed g0). Confirms no cheap gauge collision.
"""
import numpy as np
import sympy as sp

# --- 1) exact residual ---
r = sp.symbols('r', real=True, nonnegative=True)
E = sp.Rational(3,10)*r**2/(1+sp.Rational(3,10)*r**2)
print("E(r) =", E)
print("E(0) =", E.subs(r,0), " E(1) =", E.subs(r,1), "=", float(E.subs(r,1)))
print("dE/dr(1) =", sp.diff(E,r).subs(r,1))
print("sup over disk = 3/13 ~=", float(sp.Rational(3,13)))
# conjugated-operator scaling: tau^2*E vs Carleman gain O(tau) -> remainder O(tau), BLOWS UP.
print("scaling: ||tau^2 E||_inf = tau^2*3/13 -> unbounded; O(1/tau) remainder IMPOSSIBLE. LINEAR ROUTE DEAD for this g0.")

# --- 2) gauge sanity (numeric) ---
def phi(x,y,z):
    s2=(x/0.3)**2+(y/0.3)**2+((z-1.0)/0.5)**2
    return 0.1*np.exp(-s2/(1-np.minimum(s2,0.999)))
rng=np.random.default_rng(2)
N=60000
xs=rng.uniform(-0.9,0.9,N); ys=rng.uniform(-0.9,0.9,N); zs=rng.uniform(0.2,1.8,N)
h=1e-6
def gradphi(x,y,z):
    gx=(phi(x+h,y,z)-phi(x-h,y,z))/(2*h); gy=(phi(x,y+h,z)-phi(x,y-h,z))/(2*h); gz=(phi(x,y,z+h)-phi(x,y,z-h))/(2*h)
    return gx,gy,gz
gx,gy,gz=gradphi(xs,ys,zs)
# DF = [[1,0,px],[0,1,py],[0,0,1+pz]] with p=grad phi; det=1+pz; F_*I = DF DF^T/det -> (1,3) entry = px(1+pz)/det
det=1+gz
off13=gx*(1+gz)/det  # = gx
print(f"max|off-diag (1,3)| = {np.abs(gx).max():.4f} (nonzero -> pushforward NOT block-diagonal CTA)")
print("GAUGE_SANITY_OK: interior compact diffeos exit class A_cyl; no cheap gauge disproof.")
