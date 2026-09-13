"""Attempt rigorous upper bound: interval DP (positive ops => clean rel-error bounds)
then exact-Fraction PSD certificate of A=4I-J via scaled integer LDL? First quick test:
float Cholesky of A=4I-J (scaled) — does it even succeed with margin?"""
import numpy as np
I=np.load("output/artifacts/I_mat.npy"); J=np.load("output/artifacts/J_mat.npy")
s0=I[0,0]
A=(4*I-J)/s0
print("A diag range:", np.diag(A).min(), np.diag(A).max())
print("A offdiag max abs:", np.abs(A-np.diag(np.diag(A))).max())
w=np.linalg.eigvalsh((A+A.T)/2)
print("eig(A) min/max:", w.min(), w.max())
print("eig(A) smallest 8:", w[:8])
try:
    L=np.linalg.cholesky((A+A.T)/2)
    print("Cholesky OK; min diag(L):", np.diag(L).min())
except Exception as e:
    print("Cholesky FAIL:", e)
# Also A2 = 3.8I-J and 3.7I-J margins
for lam in [3.6,3.7,3.8,3.9]:
    B=(lam*I-J)/s0
    wb=np.linalg.eigvalsh((B+B.T)/2)
    print("lam=%.1f mineig=%.6f" % (lam, wb.min()))
