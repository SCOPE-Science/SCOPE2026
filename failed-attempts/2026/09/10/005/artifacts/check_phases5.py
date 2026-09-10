"""Target step 5b: Morse phases WITH interior critical point, stable ridge solve.

LP in Chebyshev basis: minimize max|c|-style via IRLS-free approach:
feasibility of dn<= -m (Gamma_D), >= +m (K_D) as linear program solved by
scipy-free subgradient with NORMALIZED rows + clipping + decaying lr.
c_1 = 0 enforced by projection (drop column 1). Degree N=24 keeps conditioning OK.
"""
import math, json, os
import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__))
A = math.pi/4
N = 24
MGN = 0.5

def arc_grids(clear=0.06, nG=300, nK=900):
    tG = np.linspace(-A+clear, A-clear, nG)
    tK = np.concatenate([np.linspace(A+clear, math.pi-A-clear, nK//2),
                         np.linspace(-(math.pi-A-clear), -(A+clear), nK//2)])
    return tG, tK

tG, tK = arc_grids()
DG = np.array([[n*math.cos(n*t) for n in range(1, N+1)] for t in tG])
DK = np.array([[n*math.cos(n*t) for n in range(1, N+1)] for t in tK])
# normalize rows
DG = DG/np.sqrt((DG**2).sum(1, keepdims=True))
DK = DK/np.sqrt((DK**2).sum(1, keepdims=True))
# drop c_1 column (index 0) to enforce critical point at 0
DG2 = DG[:, 1:]; DK2 = DK[:, 1:]

w = np.zeros(N-1)
lr0 = 0.3
for it in range(20000):
    lr = lr0/math.sqrt(1+it/500)
    vG = DG2 @ w + MGN   # want <= 0
    vK = MGN - DK2 @ w   # want <= 0
    g = 1e-4*w
    pos = vG > 0; g += (DG2[pos].T @ vG[pos])/len(tG)
    pos2 = vK > 0; g -= (DK2[pos2].T @ vK[pos2])/len(tK)
    w -= lr*g
    w = np.clip(w, -3, 3)
    if it % 5000 == 0:
        print("it=%d violG=%.4f violK=%.4f |w|=%.3f" % (
            it, np.maximum(vG, 0).max(), np.maximum(vK, 0).max(), abs(w).max()))

c = np.zeros(N); c[1:] = w  # c_1 = 0
cc = {n+1: float(c[n]) for n in range(N)}
def Phip(z): return sum((n+1)*cc[n+1]*z**n for n in range(N))
def Phipp(z): return sum((n+1)*n*cc[n+1]*z**(n-1) for n in range(1, N))
# true (unnormalized) margins
DGt = np.array([[n*math.cos(n*t) for n in range(1, N+1)] for t in tG])
DKt = np.array([[n*math.cos(n*t) for n in range(1, N+1)] for t in tK])
print("TRUE max dn Gamma_D = %.4f (want<0)" % (DGt@c).max())
print("TRUE min dn K_D = %.4f (want>0)" % (DKt@c).min())
poly = np.poly1d([(n+1)*cc[n+1] for n in range(N-1, -1, -1)])
roots = np.roots(poly.coef)
inside = np.array([r for r in roots if abs(r) < 1-1e-6])
print("N_CRIT =", len(inside), [(round(z.real,3), round(z.imag,3)) for z in inside])
simp = [abs(Phipp(z)) for z in inside]
print("MIN|Phi''| =", min(simp) if len(simp) else None)
cvals = [sum(cc[n]*z**n for n in range(1, N+1)) for z in inside]
mg = min([abs(cvals[i]-cvals[j]) for i in range(len(cvals)) for j in range(i+1, len(cvals))]) if len(cvals) > 1 else float('inf')
print("MIN_CVAL_GAP =", mg)
print("Phi''(0) = 2c_2 =", 2*c[1])
res = dict(max_GammaD=float((DGt@c).max()), min_KD=float((DKt@c).min()),
           n_crit=int(len(inside)), min_Phipp=float(min(simp)) if len(simp) else None,
           min_cval_gap=float(mg), Phi2_0=float(2*c[1]),
           coeffs={str(n): cc[n] for n in range(1, N+1)})
with open(os.path.join(OUT, "phases5.json"), "w") as f:
    json.dump(res, f, indent=1)
feas = bool((DGt@c).max() < -0.05 and (DKt@c).min() > 0.05)
morse = bool(len(inside) >= 1 and all(s > 1e-3 for s in simp) and mg > 1e-3 and abs(2*c[1]) > 1e-3)
print("VERIFY_PHASES5_OK" if (feas and morse) else "VERIFY_PHASES5_FAIL")
