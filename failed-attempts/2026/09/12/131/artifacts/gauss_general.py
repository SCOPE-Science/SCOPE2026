"""Exact general-Gaussian EOT under target normalization (derivation in WORKLOG).

C(A,B) = (TrA+TrB)/2 - sum_i [ m_i*sig_i + (eps/2)*log(1-m_i^2) ],
  sig_i = singular values of A^{1/2} B^{1/2} (= eigvals of (A^{1/2} B A^{1/2})^{1/2}),
  m_i   = (-eps+sqrt(eps^2+4 sig_i^2))/(2 sig_i).
OT(A,B) = (TrA+TrB)/2 - sum_i sig_i.
Self terms: sig_i = eigenvalues of A (resp. B).
Checks intensive ratio (1/n)|S-OT|/eps over class-admissible ensembles.
Class proxy: kappa=1 -> eig(A),eig(B) <= 1; M=1 -> tr/n <= 1; F=2 -> tr(inv)/n <= 2.
"""
import numpy as np

def C_gauss(A, B, eps):
    n = A.shape[0]
    sqA = np.linalg.cholesky(A)  # A = L L^T; A^{1/2}=L^T? use symmetric sqrt via eigh for safety
    # symmetric sqrt
    w, V = np.linalg.eigh(A); sq = (V*np.sqrt(w)) @ V.T
    M = sq @ B @ sq  # A^{1/2} B A^{1/2}
    ev = np.linalg.eigvalsh(M); ev = np.maximum(ev, 0)
    sig = np.sqrt(ev)
    # m*sig = (D-eps)/2 with D=sqrt(eps^2+4 sig^2)
    D = np.sqrt(eps**2 + 4*sig**2)
    t = (D - eps)/(2*np.maximum(sig,1e-300))
    t = np.minimum(t, 1-1e-15)
    val = (np.trace(A)+np.trace(B))/2 - np.sum((D-eps)/2 + (eps/2)*np.log1p(-t*t))
    ot = (np.trace(A)+np.trace(B))/2 - np.sum(sig)
    return val, ot

def S_ratio(A, B, eps):
    n = A.shape[0]
    C, OT = C_gauss(A, B, eps)
    Caa, _ = C_gauss(A, A, eps)
    Cbb, _ = C_gauss(B, B, eps)
    S = C - 0.5*(Caa+Cbb)
    return abs(S-OT)/n/eps, abs(S-OT)/n/eps**2, (S-OT)/n

def check(name, A, B):
    print(f"--- {name} --- eigA[{np.linalg.eigvalsh(A).min():.4f},{np.linalg.eigvalsh(A).max():.4f}] "
          f"trA/n={np.trace(A)/A.shape[0]:.4f} trinvA/n={np.trace(np.linalg.inv(A))/A.shape[0]:.4f}")
    for eps in [0.2, 0.1, 0.05, 0.02, 0.01, 0.005]:
        r1, r2, d = S_ratio(A, B, eps)
        print(f"  eps={eps:<6} (S-OT)/n={d:+.3e}  R1={r1:.5f}  R2={r2:.5f}")

rng = np.random.default_rng(1)
n = 16
# 1. spiked: one tiny eig 1/(nF)-ish, rest 1
for n in [4, 16, 64]:
    F = 2.0
    delta = 1.0/(n*(F-1)+1)
    A = np.eye(n); B = np.eye(n); B[0,0] = delta
    # scale so tr/n<=1: B tr/n = ((n-1)+delta)/n <=1 ok
    check(f"spiked n={n} delta={delta:.4f}", A, B)

# 2. equicorrelated at max allowed correlation
for n in [4, 16, 64]:
    sig2 = 1.0
    # largest eig sig2*(1+(n-1)rho)<=1 -> rho <= 0 -> take rho=0? use sig2=0.5 to allow rho
    sig2 = 0.5
    rho = (1/sig2 - 1)/(n-1) * 0.99  # just inside kappa bound
    A = sig2*((1-rho)*np.eye(n) + rho*np.ones((n,n)))
    B = 0.7*np.eye(n)
    print(f"equicorr n={n} rho={rho:.5f} trinvA/n={np.trace(np.linalg.inv(A))/n:.4f}")
    check(f"equicorr n={n}", A, B)

# 3. random rotation of spiked (delocalized small eigvec) + random B
for n in [8, 32]:
    F = 2.0
    delta = 1.0/(n*(F-1)+1)
    Q, _ = np.linalg.qr(rng.normal(size=(n,n)))
    A = Q @ np.diag(np.concatenate([[delta], np.ones(n-1)])) @ Q.T
    Q2, _ = np.linalg.qr(rng.normal(size=(n,n)))
    B = Q2 @ np.diag(rng.uniform(0.5, 1.0, n)) @ Q2.T
    check(f"random-rotated-spiked n={n}", A, B)

# 4. Wishart-ish random with clipping into class
for n in [8, 32]:
    Z = rng.normal(size=(n,n))
    A = Z @ Z.T / n * 0.5 + 0.3*np.eye(n)
    # clip eigenvalues to [0.4, 1.0]
    w, V = np.linalg.eigh(A)
    wc = np.clip(w, 0.4, 1.0)
    A = (V*wc) @ V.T
    Z = rng.normal(size=(n,n))
    B = Z @ Z.T / n * 0.5 + 0.3*np.eye(n)
    w, V = np.linalg.eigh(B)
    wc = np.clip(w, 0.4, 1.0)
    B = (V*wc) @ V.T
    check(f"wishart-clipped n={n}", A, B)
