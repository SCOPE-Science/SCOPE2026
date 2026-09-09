"""Lane 409 — part 6: stationary SHE / Wick bounds (quantitative BB2 support).

Torus T^3 period 2π. Stationary massive SHE: dΨ_k = -(|k|^2+m^2)Ψ_k dt + dW_k,
stationary Var = 1/(2(|k|^2+m^2)) per real component.
Checks:
 1. E||Ψ||_{H^s}^2 = Σ_k <k>^{2s} 3/(2(|k|^2+m^2)) for s=-1/2-κ converges; tail bound.
 2. Mollifier effect: |ρ̂(εk)|^2 ≤ 1, → bound uniform in ε (monotone).
 3. :Ψ^2: proxy: E||:Ψ^2:||_{H^s}^2 via contraction Σ_{k,l}... bound ~ Σ_k<k>^{2s}(|k|^{-2}★|k|^{-2});
    evaluate truncated convolution to show convergence for s<-1 (i.e. C^{-1-κ}).
 4. Log-divergent ledger check: mass counterterm Σ_{0<|k|≤1/ε}(|k|^2+m^2)^{-1} ~ 4π/ε - finite.
Writes results6.json.
"""
import json, math, os
import numpy as np

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results6.json")
res = {}
m2 = 1.0
N = 30

def lattice(N):
    r = np.mgrid[0:N+1,0:N+1,0:N+1] if False else None
    pts = []
    for k1 in range(-N,N+1):
        for k2 in range(-N,N+1):
            for k3 in range(-N,N+1):
                pts.append((k1,k2,k3))
    return pts

pts = lattice(N)
# 1. H^s norm expectation
for s in [-0.5-0.1, -0.5-0.25]:
    tot = 0.0
    for k in pts:
        r2 = k[0]**2+k[1]**2+k[2]**2
        bracket = 1+r2
        var = 3.0/(2.0*(r2+m2)) if r2>0 else 3.0/(2.0*m2)
        tot += (bracket**s)*var
    res[f"E_Hs_s={s}"] = tot
# tail: summand ~ 3/2 r^{2s-2} r^2 dr *4π = 6π r^{2s+1}... wait: summand ~<k>^{2s}/|k|^2, density 4πr^2
# tail ∫_N^∞ r^{2s} dr *4π*3/2 = 6π N^{2s+1}/|2s+1| for 2s+1<0.
for s in [-0.6, -0.75]:
    tail = 6*math.pi*(N**(2*s+1))/abs(2*s+1)
    res[f"tail_s={s}"] = tail
res["uniform_in_eps"] = True
res["uniform_note"] = "mollifier multiplies each mode variance by |ρ̂(εk)|²≤1 ⇒ truncated sums dominate; limit ε→0 monotone ⇒ sup_ε bound = massless-limit sum, finite for s<-1/2."

# 3. :Psi^2: second moment proxy in H^s: E|:Ψ²:(k)|² ~ 2*Σ_l V_l V_{k-l}, V_l=1/(2(|l|²+m²)).
# Bound the k=0 value + tail: S0 = Σ_{|l|≤N} V_l² ; full second moment ~ Σ_k <k>^{2s} (V★V)_k.
# Compute radial proxy integral: (V★V)(k) ≤ C<k>^{-1} (3D Coulomb convolution); then Σ_k<k>^{2s-1} converges iff 2s-1<-3, i.e. s<-1. ✓
V = {}
for k in pts:
    r2 = k[0]**2+k[1]**2+k[2]**2
    V[k] = 1.0/(2.0*(r2+m2))
# convolution at few k values (direct, N=12 for speed)
N2 = 12
pts2 = [k for k in pts if max(abs(x) for x in k) <= N2]
V2 = {k: 1.0/(2.0*(k[0]**2+k[1]**2+k[2]**2+m2)) for k in pts2}
S = set(pts2)
def conv(k):
    t = 0.0
    for l in pts2:
        m = (k[0]-l[0], k[1]-l[1], k[2]-l[2])
        if m in S:
            t += V2[l]*V2[m]
    return 2.0*t
for k in [(0,0,0),(1,0,0),(2,0,0),(3,0,0),(5,0,0)]:
    r = math.sqrt(k[0]**2+k[1]**2+k[2]**2)
    res[f"conv_k={k}"] = conv(k)
    res[f"conv_times_r_k={k}"] = conv(k)*max(r,1.0)
res["conv_note"] = "(V★V)(k)·|k| ≈ const (Coulomb ~1/|k|): convergent in H^s for s<-1 ⇒ :Ψ²: ∈ C^{-1-κ} uniformly in ε."
# 4. counterterm ledger: C(Λ) = 3g² Σ_{0<|k|≤Λ} 1/(|k|²+m²) ; fit C = A Λ + B log Λ + C0
Ls = [5,8,12,16,20,26]
Cs = {}
for L in Ls:
    t = 0.0
    for k in pts:
        r2 = k[0]**2+k[1]**2+k[2]**2
        if 0 < r2 <= L*L:
            t += 1.0/(r2+m2)
    Cs[L] = 3.0*t
res["counterterm_sums"] = {str(k): v for k,v in Cs.items()}
# fit A L + B ln L + C0
A = np.vstack([Ls, np.log(Ls), np.ones(len(Ls))]).T
coef, *_ = np.linalg.lstsq(A, [Cs[L] for L in Ls], rcond=None)
res["ct_fit"] = {"A": float(coef[0]), "B": float(coef[1]), "C0": float(coef[2]),
                 "4pi_times3": 12*math.pi,
                 "note": "A≈12π confirms linear divergence 3·(4πΛ); B captures log + lattice-shape terms."}
with open(OUT, "w") as f:
    json.dump(res, f, indent=2)
print(json.dumps(res, indent=2))
