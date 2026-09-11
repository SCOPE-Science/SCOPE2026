"""Recovery test: linear-phase reflection vs non-flat transversal metric.
Target class allows ANY fixed smooth g0. Try g0 = (1+0.3 r^2) I_2 (smooth conformal).
Linear phase Phi = x3 + i(a x1 + b x2), a^2+b^2=1. G=blockdiag(g0,1), G^{-1}=diag(e^{-2l},e^{-2l},1).
Eikonal residual E = G^{jk} d_jPhi d_kPhi = 1 - e^{-2l(x')}(a^2+b^2).
If E is O(1) (no tau decay possible), linear-phase CGO remainder cannot be o(1):
conjugated-operator zeroth-order error tau^2*E destroys the 1/tau remainder gain.
Also test mixed-term frequency scaling for the FLAT case (eta2 vertical part -> |m|~tau).
"""
import numpy as np

# 1) conformal factor
rng = np.random.default_rng(1)
N=200000
r = np.sqrt(rng.uniform(0,1,N))  # radius samples in disk
lam = 0.5*np.log(1+0.3*r*r)
E = 1.0 - np.exp(-2*lam)   # residual with a^2+b^2=1
print(f"conformal g0: eikonal residual range [{E.min():.4f},{E.max():.4f}], mean {E.mean():.4f}")
print(f"-> residual is O(1), x'-dependent; tau^2*E term in conjugated operator has NO tau decay.")
print(f"-> linear-phase CGO remainder bound O(1/tau) FAILS for non-flat g0. RECOVERY_TEST: NEGATIVE for linear route.")

# 2) flat-case mixed-term frequency growth (generic nonvertical xi)
tau_vals = np.array([20.,40.,80.,160.])
xi = np.array([2.0,1.0,3.0])
xip = xi[:2]; v=np.array([-xip[1],xip[0]]); v/=np.linalg.norm(v)
eta1=np.array([v[0],v[1],0.0])
a=xi/np.linalg.norm(xi)
e3=np.array([0.,0.,1.])
rvec=e3-(e3@a)*a-((e3@eta1))*eta1; rvec/=np.linalg.norm(rvec)
eta2=rvec
R=np.diag([1.,1.,-1.])
for tau in tau_vals:
    s=np.sqrt(tau**2-np.dot(xi,xi)/4)
    z1=tau*eta1+1j*(xi/2+s*eta2); z2=-tau*eta1+1j*(xi/2-s*eta2)
    m1=(R@z1)+z2
    print(f"tau={tau:6.1f} s={s:7.2f} |Im m1|={np.linalg.norm(m1.imag):9.2f} ( vertical part {m1.imag[2]:+.2f} ~ 2*s*eta2_3={2*s*eta2[2]:+.2f} )")
print("-> generic-xi mixed terms oscillate with frequency ~tau: Riemann-Lebesgue kills them. FLAT route viable.")
# 3) vertical xi: exact zero
xiv=np.array([0.,0.,4.])
print(f"vertical xi: mixed frequency exactly 0 (analytic) -> cone restriction needed; Paley-Wiener closes via collar compact support.")
