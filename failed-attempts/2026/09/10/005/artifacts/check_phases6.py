"""Target step 5c: Morse phase with interior crit at z0 != 0 (keeps n=1 mode).

Real coeffs c_1..c_N, linear equality Phi'(z0)=0 at z0=0.35 (one linear
constraint, preserves fundamental). Inequalities: dn<=-m on Gamma_D,
dn>=+m on K_D (true scale). Projected subgradient with equality projection,
normalized rows, decaying lr. Verify Morse + N-pattern.
"""
import math, json, os
import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__))
A = math.pi/4
N = 32
MGN = 0.5
Z0 = 0.35

def arc_grids(clear=0.06, nG=300, nK=900):
    tG = np.linspace(-A+clear, A-clear, nG)
    tK = np.concatenate([np.linspace(A+clear, math.pi-A-clear, nK//2),
                         np.linspace(-(math.pi-A-clear), -(A+clear), nK//2)])
    return tG, tK

tG, tK = arc_grids()
DG = np.array([[n*math.cos(n*t) for n in range(1, N+1)] for t in tG])
DK = np.array([[n*math.cos(n*t) for n in range(1, N+1)] for t in tK])
DG = DG/np.sqrt((DG**2).sum(1, keepdims=True))
DK = DK/np.sqrt((DK**2).sum(1, keepdims=True))
eq = np.array([n*Z0**(n-1) for n in range(1, N+1)])
eq = eq/np.linalg.norm(eq)

w = np.zeros(N)
lr0 = 0.5
for it in range(30000):
    lr = lr0/math.sqrt(1+it/800)
    vG = DG @ w + MGN; vK = MGN - DK @ w
    g = 1e-4*w
    pos = vG > 0; g += (DG[pos].T @ vG[pos])/len(tG)
    pos2 = vK > 0; g -= (DK[pos2].T @ vK[pos2])/len(tK)
    w -= lr*g
    w -= (w @ eq)*eq  # project onto equality
    w = np.clip(w, -5, 5)
    if it % 7500 == 0:
        print("it=%d violG=%.4f violK=%.4f eq=%.2e |w|=%.3f" % (
            it, np.maximum(vG, 0).max(), np.maximum(vK, 0).max(),
            abs(w @ eq), abs(w).max()))

c = w
print("eq-residual:", c @ eq)
DGt = np.array([[n*math.cos(n*t) for n in range(1, N+1)] for t in tG])
DKt = np.array([[n*math.cos(n*t) for n in range(1, N+1)] for t in tK])
print("TRUE max dn Gamma_D = %.4f" % (DGt@c).max())
print("TRUE min dn K_D = %.4f" % (DKt@c).min())
cc = {n+1: float(c[n]) for n in range(N)}
def Phip(z): return sum((n+1)*cc[n+1]*z**n for n in range(N))
def Phipp(z): return sum((n+1)*n*cc[n+1]*z**(n-1) for n in range(1, N))
print("Phip(Z0) =", Phip(Z0))
poly = np.poly1d([(n+1)*cc[n+1] for n in range(N-1, -1, -1)])
roots = np.roots(poly.coef)
inside = np.array([r for r in roots if abs(r) < 1-1e-6])
print("N_CRIT =", len(inside), [(round(z.real,3), round(z.imag,3)) for z in inside])
simp = [abs(Phipp(z)) for z in inside]
print("MIN|Phi''| =", min(simp) if len(simp) else None)
cvals = [sum(cc[n]*z**n for n in range(1, N+1)) for z in inside]
mg = min([abs(cvals[i]-cvals[j]) for i in range(len(cvals)) for j in range(i+1, len(cvals))]) if len(cvals) > 1 else float('inf')
print("MIN_CVAL_GAP =", mg)
res = dict(max_GammaD=float((DGt@c).max()), min_KD=float((DKt@c).min()),
           eq_res=float(c@eq), Phip_Z0=float(abs(Phip(Z0))),
           n_crit=int(len(inside)),
           crit=[(float(z.real), float(z.imag)) for z in inside],
           min_Phipp=float(min(simp)) if len(simp) else None,
           min_cval_gap=float(mg), coeffs={str(n): cc[n] for n in range(1, N+1)})
with open(os.path.join(OUT, "phases6.json"), "w") as f:
    json.dump(res, f, indent=1)
feas = bool((DGt@c).max() < -0.05 and (DKt@c).min() > 0.05)
morse = bool(len(inside) >= 1 and all(s > 1e-3 for s in simp) and mg > 1e-3)
print("VERIFY_PHASES6_OK" if (feas and morse and abs(Phip(Z0)) < 1e-6) else "VERIFY_PHASES6_FAIL")
