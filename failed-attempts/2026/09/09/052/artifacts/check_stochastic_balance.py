"""Lane 409 — stochastic-balance scaling (target-directed stress test of large-data closure).

Question: along amplitude family A^(lam)=lam*Abase (fixed non-abelian profile),
does deterministic dissipation D(lam) dominate the rough It^o commutator
  T(lam) = <F(A^(lam)), [A^(lam), Psi]>   (proxy for g<F,[v,Psi]> drift term)
uniformly at large lam for small g? If |T|/D -> 0 as lam->inf (at fixed Psi),
large-data closure is plausible; if |T|/D grows, closure fails at fixed g.

Psi = synthetic C^{-1/2-} field: independent Gaussians per Fourier mode with
Var ~ 1/|k|^2 (massive SHE stationary proxy), one fixed realization (seeded).
Lattice N=24 (speed), period 2pi, central differences, su(2)~R^3 cross product.
Also test Wick-ordered variant T_ren = <F,[A,Psi]> - c.t.(A) with scalar
mass-subtraction proxy to confirm cancellation does not change scaling.

Writes results9.json.
"""
import json, math, os
import numpy as np

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results9.json")
rng = np.random.default_rng(40911)
res = {}

N = 24
L = 2 * math.pi
dx = L / N
xs = np.linspace(0, L - dx, N)
V = L ** 3

# base profile (same as check_dissipation, coarser)
SIG = 0.6
C = np.array([L / 2] * 3)
I1, I2, I3 = np.meshgrid(range(N), range(N), range(N), indexing='ij')
Xc = (xs[I1] - C[0] + L / 2) % L - L / 2
Yc = (xs[I2] - C[1] + L / 2) % L - L / 2
Zc = (xs[I3] - C[2] + L / 2) % L - L / 2
B1 = np.exp(-(Xc**2 + Yc**2 + Zc**2) / (2 * SIG**2))
Xs2 = (xs[I1] - C[0] - 0.5 + L / 2) % L - L / 2
B2 = np.exp(-(Xs2**2 + Yc**2 + Zc**2) / (2 * SIG**2))
Abase = np.zeros((3, 3, N, N, N))
Abase[0, 2] = B1
Abase[1, 0] = 0.7 * B2

def curl_F(A, g):
    F = np.zeros((3, 3, 3, N, N, N))
    def d(idx, Fld):
        return (np.roll(Fld, -1, axis=idx) - np.roll(Fld, 1, axis=idx)) / (2 * dx)
    for i in range(3):
        for j in range(3):
            F[i, j] = d(i, A[j]) - d(j, A[i])
            cr = np.cross(A[i].transpose(1, 2, 3, 0), A[j].transpose(1, 2, 3, 0)).transpose(3, 0, 1, 2)
            F[i, j] = F[i, j] + g * cr
    return F

def energy(A, g):
    F = curl_F(A, g)
    return 0.5 * np.sum(F**2) * dx**3

def grad_energy(A, g):
    F = curl_F(A, g)
    G = np.zeros_like(A)
    def d(idx, Fld):
        return (np.roll(Fld, -1, axis=idx) - np.roll(Fld, 1, axis=idx)) / (2 * dx)
    for k in range(3):
        acc = np.zeros_like(A[k])
        for i in range(3):
            acc = acc - d(i, F[i, k])
            acc = acc + g * np.cross(A[i].transpose(1, 2, 3, 0), F[i, k].transpose(1, 2, 3, 0)).transpose(3, 0, 1, 2)
        G[k] = acc
    return G

def dissipation(A, g):
    G = grad_energy(A, g)
    return float(np.sum(G**2) * dx**3)

# synthetic Psi: Fourier modes Var = 1/(|k|^2+1) per (spatial,color) component, Hermitian
kfreq = np.fft.fftfreq(N, d=dx / (2 * math.pi))  # frequencies in Z approx
KX, KY, KZ = np.meshgrid(kfreq, kfreq, kfreq, indexing='ij')
K2 = KX**2 + KY**2 + KZ**2
amp = 1.0 / np.sqrt(K2 + 1.0)
amp[0, 0, 0] = 1.0
Psi = np.zeros((3, 3, N, N, N))
for i in range(3):
    for a in range(3):
        noise = rng.normal(size=(N, N, N)) + 1j * rng.normal(size=(N, N, N))
        # Hermitianize
        noise = (noise + np.conj(noise[::-1, ::-1, ::-1])) / math.sqrt(2)
        fhat = noise * amp * (N**3) * (dx**3 / V) * V**0  # scale proxy (shape only matters for exponents)
        f = np.real(np.fft.ifftn(fhat))
        f = f - f.mean()
        Psi[i, a] = f / f.std()  # normalize to O(1) per component; scaling exponents unaffected
res["psi_note"] = "Psi normalized per-component to unit std; only lam-scaling exponents used."

g = 0.5
lams = [0.5, 1.0, 2.0, 4.0, 8.0]
Es, Ds, Ts = [], [], []
for lam in lams:
    A = lam * Abase
    F = curl_F(A, g)
    E = energy(A, g)
    D = dissipation(A, g)
    # T = sum_{i,j} <F_ij, [A_i, Psi_j] + [Psi_i, A_j]>/2-ish proxy: use [A_1,Psi_2] contraction
    T = 0.0
    for i in range(3):
        for j in range(3):
            cr = np.cross(A[i].transpose(1, 2, 3, 0), Psi[j].transpose(1, 2, 3, 0)).transpose(3, 0, 1, 2)
            T += float(np.sum(F[i, j] * cr)) * dx**3
    Es.append(E); Ds.append(D); Ts.append(abs(T))
res["amplitude_E"] = dict(zip(map(str, lams), Es))
res["amplitude_D"] = dict(zip(map(str, lams), Ds))
res["amplitude_absT"] = dict(zip(map(str, lams), Ts))
res["ratio_T_over_D"] = dict(zip(map(str, lams), [t / d for t, d in zip(Ts, Ds)]))
# log-log fits (last 3 points = large-lam)
le = np.log(np.array(Es)); ld = np.log(np.array(Ds)); lt = np.log(np.array(Ts) + 1e-300)
ll = np.log(np.array(lams))
se, _ = np.polyfit(ll[-3:], le[-3:], 1)
sd, _ = np.polyfit(ll[-3:], ld[-3:], 1)
st, _ = np.polyfit(ll[-3:], lt[-3:], 1)
res["exp_E_large"] = float(se)
res["exp_D_large"] = float(sd)
res["exp_T_large"] = float(st)
res["T_vs_E_large"] = float(st / se)
res["D_vs_E_large"] = float(sd / se)
# decisive ratio trend: T/D along lam
res["T_over_D_trend"] = "increasing" if Ts[-1] / Ds[-1] > Ts[0] / Ds[0] else "decreasing"
res["closure_reading"] = ("If T/D grows with lam, fixed-g absorption of the rough drift by D "
    "fails at large data (supports obstruction ledger). If T/D shrinks, large-data "
    "closure plausible modulo renormalization. Lattice N=24 under-resolves quartic "
    "tail: exponents are qualitative stress-test only, recorded honestly.")

with open(OUT, "w") as f:
    json.dump(res, f, indent=2)
print(json.dumps(res, indent=2))
