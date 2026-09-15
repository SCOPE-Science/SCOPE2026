"""Bounded probe: kappa=2 stratum plausibility + finite-volume signatures.
Model: golden-mean alpha, even v = 2*l1*cos(2pi th)+2*l2*cos(4pi th).
Tasks: (1) L(E,eps) slope proxy for kappa; (2) E-scan for S_3^+ candidates;
(3) finite-volume ED decay/IPR; (4) reflected-resonance distances.
Finite data CANNOT imply infinite-volume AL; purpose is plausibility + exposing gap.
"""
import numpy as np

alpha = (np.sqrt(5)-1)/2
l1, l2 = 2.0, 1.0   # v = 2*l1 cos + 2*l2 cos4pi  => amplitudes 4 and 2

def v(th, eps=0.0):
    # th real array; complexify th + i*eps
    z1 = 2*np.pi*(th + 1j*eps)
    z2 = 2*2*np.pi*(th + 1j*eps)
    return 2*l1*np.cos(z1) + 2*l2*np.cos(z2)

def LE(E, eps, n=4000, th0=0.12345, seed_transient=200):
    ths = (th0 + np.arange(n+seed_transient)*alpha) % 1.0
    ths = ths[seed_transient:]
    # product via QR-free norm accumulation with periodic renormalization
    M = np.eye(2, dtype=complex)
    logs = 0.0
    for i, th in enumerate(ths):
        vv = v(th, eps)
        A = np.array([[E - vv, -1.0],[1.0, 0.0]], dtype=complex)
        M = A @ M
        if (i+1) % 200 == 0:
            nr = np.linalg.norm(M)
            logs += np.log(nr)
            M = M / nr
    nr = np.linalg.norm(M)
    logs += np.log(nr)
    return logs / n

print("alpha golden mean:", alpha)
Es = np.arange(-8.0, 8.01, 0.5)
eps0, eps1 = 0.0, 0.02
print(f"{'E':>7} {'L0':>8} {'L1':>8} {'slope/2pi':>10}")
cands = []
for E in Es:
    L0 = LE(E, eps0, n=2000)
    L1 = LE(E, eps1, n=2000)
    kappa = (L1-L0)/eps1/(2*np.pi)
    print(f"{E:7.2f} {L0:8.4f} {L1:8.4f} {kappa:10.3f}")
    if L0 > 0.3 and kappa > 1.5:
        cands.append((float(E), float(L0), float(kappa)))
print("CANDIDATE kappa~2, L>0:", cands)

# Finite-volume ED at E near candidate
N = 401
th0 = 0.12345
ns = np.arange(N) - N//2
ths = (th0 + ns*alpha) % 1.0
pot = np.real(v(ths, 0.0))
H = np.diag(pot) + np.diag(np.ones(N-1), 1) + np.diag(np.ones(N-1), -1)
evals, evecs = np.linalg.eigh(H)
# pick state closest to candidate E (or middle)
Etarget = cands[0][0] if cands else 0.0
idx = int(np.argmin(np.abs(evals - Etarget)))
psi = np.abs(evecs[:, idx])**2
imax = int(np.argmax(psi))
x = np.abs(np.arange(N)-imax)
# exponential fit on tails (5..60 sites), log-linear
mask = (x>=5)&(x<=80)&(psi>1e-12)
xx, yy = x[mask], np.log(psi[mask])
A = np.vstack([xx, np.ones_like(xx)]).T
slope, intercept = np.linalg.lstsq(A, yy, rcond=None)[0]
IPR = float(np.sum(psi**2))
print(f"ED: Etarget~{Etarget:.2f} closest eval={evals[idx]:.4f} IPR={IPR:.4f} exp-slope={slope:.4f} (neg=localized-like)")

# reflected resonance stats: d(k)=||2th - k a|| for random thetas
rng = np.random.default_rng(0)
for th in [0.12345, 0.5, rng.random()]:
    ds = [abs(((2*th - k*alpha + 0.5) % 1.0) - 0.5) for k in range(-50, 51)]
    print(f"theta={th:.5f} min||2th-k a||(|k|<=50)={min(ds):.4f}")
print("NOTE: finite-volume decay/IPR are suggestive only; no LDT / double-resonance elimination; no infinite-volume AL implication.")
