"""Numerical verification for lane-1249 parity obstruction.
Checks (with Fourier H^3 norm ||f||^2 = sum_k (1+k^2)^3 |c_k|^2):
 1. psi_{f,eps} = (phi0 + eps*eta)/sqrt(1+eps^2) is L2-normalized, smooth,
    H^3-close to phi0 for small eps.
 2. Its odd-component L2 norm = eps/sqrt(1+eps^2) > 0, lower-bounding L2
    distance to ANY even function (hence to any reachable state).
 3. On a truncated Fourier basis, parity P (k -> -k) commutes with the free
    propagator diag(exp(-i t k^2)) and with B = mult. by cos (shift k->k+-1 /2).
"""
import numpy as np

K = 8  # truncation |k| <= K
ks = np.arange(-K, K + 1)
dim = len(ks)
idx = {k: i for i, k in enumerate(ks)}

# Parity matrix P: (Pf)_k = f_{-k}
P = np.zeros((dim, dim))
for k in ks:
    P[idx[-k], idx[k]] = 1.0

# Free propagator at arbitrary t
t = 0.37
U = np.diag(np.exp(-1j * t * ks**2))

# B = multiplication by cos in Fourier basis: B_{j,k} = 1/2 if j=k+1 or k-1
B = np.zeros((dim, dim))
for k in ks:
    for j in (k - 1, k + 1):
        if j in idx:
            B[idx[j], idx[k]] += 0.5

comm_U = np.linalg.norm(P @ U - U @ P)
comm_B = np.linalg.norm(P @ B - B @ P)
print(f"||[P,U]||_F = {comm_U:.3e}")
print(f"||[P,B]||_F = {comm_B:.3e}")
assert comm_U < 1e-12 and comm_B < 1e-12

# Coefficients: phi0 = delta_{k,0}; eta = pi^{-1/2} sin = (e^{i th}-e^{-i th})/(2 i sqrt(pi))
# In basis e_k = (2pi)^{-1/2} e^{ik th}: eta = (sqrt(2)/(2i))(e_1 - e_{-1})
c_phi0 = np.zeros(dim, dtype=complex); c_phi0[idx[0]] = 1.0
c_eta = np.zeros(dim, dtype=complex)
c_eta[idx[1]] = np.sqrt(2) / (2j); c_eta[idx[-1]] = -np.sqrt(2) / (2j)
w = (1 + ks**2)**3  # H^3 weights
n_eta_H3 = np.sqrt(np.sum(w * np.abs(c_eta)**2))
print(f"||eta||_L2 = {np.linalg.norm(c_eta):.6f}, ||eta||_H3 = {n_eta_H3:.6f} (expect 2^1.5={2**1.5:.6f})")
assert abs(np.linalg.norm(c_eta) - 1.0) < 1e-12
assert abs(n_eta_H3 - 2**1.5) < 1e-12

for eps in [0.2, 0.1, 0.05, 0.01]:
    N = np.sqrt(1 + eps**2)
    c = (c_phi0 + eps * c_eta) / N
    dH3 = np.sqrt(np.sum(w * np.abs(c - c_phi0)**2))
    odd = (c - P @ c) / 2
    oddL2 = np.linalg.norm(odd)
    expect = eps / N
    print(f"eps={eps:.2f}: ||psi-phi0||_H3={dH3:.6f}, odd-part L2={oddL2:.6f} (expect {expect:.6f})")
    assert abs(oddL2 - expect) < 1e-12
    assert dH3 < 4 * eps  # O(eps) closeness

print("ALL CHECKS PASSED")
