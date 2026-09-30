import numpy as np

# EXACT preset fallback audit.
# Objects: v0=(sin x3,0,0) => ||grad v0||_inf = 1 => c1 = 1e-2.
# Amplitude: a^2 = c_cap * M*^2 * lam^{-2/3} * r^{4/3}, M*=1; r = lam^{-alpha}.
# Claim: R(lam,al) := ||R_trans||_1/(||R_osc||_1 + lam^{-1}) >= c1 * lam^{(4al-3)/3}
#   for ALL dyadic lam>=2^12, ALL al in (3/4,1].
# Model (order-sharp, generous to claim):
#   ||R_trans||_1 = a * lam^{-1} * S,  S = (2/pi)*||d1 psi_n||_1 = 1.800633 (exact analytic, quadrature-verified)
#   ||R_osc||_1   = C_osc * a^2, C_osc = 2.0 (axial-oscillation model); also tested C_osc = 0 (pure transverse, floor only)
#   Both variants are tried; INFLATION x100 on R_trans also tried (still parametric decay).
S = (2/np.pi)*2.828109  # = 1.8006...
c1 = 1e-2
def audit(C_osc, c_cap, inflate=1.0, ks=range(12,25), alphas=(0.751,0.8,0.9,1.0)):
    fails = 0; total = 0; worst = None
    for al in alphas:
        e = (4*al-3)/3
        for k in ks:
            lam = 2.0**k; r = lam**(-al)
            a2 = c_cap * lam**(-2/3) * r**(4/3)
            a = np.sqrt(a2)
            Rtr = inflate * a * lam**(-1) * S
            Ros = C_osc * a2
            ratio = Rtr/(Ros + lam**(-1))
            bound = c1 * lam**e
            total += 1
            if ratio < bound:
                fails += 1
                if worst is None or ratio/bound < worst[0]:
                    worst = (ratio/bound, al, k)
    return fails, total, worst

for C_osc in [2.0, 0.0]:
    for c_cap in [0.1, 1.0, 10.0]:
        for inflate in [1.0, 100.0]:
            f, t, w = audit(C_osc, c_cap, inflate)
            print(f"C_osc={C_osc} c_cap={c_cap} inflate={inflate}: FAIL {f}/{t}  worst ratio/bound={w[0]:.2e} at al={w[1]},k={w[2]}")
# exponent algebra check
print("e(0.751)=%.4f e(0.8)=%.4f e(0.9)=%.4f e(1.0)=%.4f" % tuple((4*a-3)/3 for a in (0.751,0.8,0.9,1.0)))
# sample row
lam=2.0**12; al=1.0; r=lam**(-al); a=np.sqrt(1.0*lam**(-2/3)*r**(4/3))
print(f"sample lam=4096,al=1: a={a:.3e} Rtr={a/lam*S:.3e} Ros={2*a*a:.3e} floor={1/lam:.3e} ratio={a/lam*S/(2*a*a+1/lam):.3e} bound={c1*lam**(1/3):.3e}")
