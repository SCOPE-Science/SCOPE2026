"""mpmath high-precision generalized EVP (dps=60) on longdouble I,J + threshold analysis."""
import pickle, numpy as np
from mpmath import mp
mp.dps = 60
d = pickle.load(open("output/artifacts/IJ_ld.pkl","rb"))
I=d["I"]; J=d["J"]
B=I.shape[0]
Im=mp.matrix(B,B); Jm=mp.matrix(B,B)
for i in range(B):
    for j in range(B):
        Im[i,j]=mp.mpf(str(float(I[i,j])))
        Jm[i,j]=mp.mpf(str(float(J[i,j])))
print("matrices loaded", flush=True)
# scale
s0=Im[0,0]
for i in range(B):
    for j in range(B):
        Im[i,j]/=s0; Jm[i,j]*=(mp.mpf(50)/s0)/mp.mpf(50)  # careful: J already has factor 50
print("const M =", float(Jm[0,0]/Im[0,0]), flush=True)
# whiten via eigh in mpmath? mp.eigsy? Use: solve generalized via Cholesky-free:
# eig of inv(I)*J by mp.eig? Use power iteration for top generalized eig + inverse iteration for min eig of (4I-J,I)?
# Simplest: mp.eig() on Mmat = I^{-1} J via LU solve.
Mmat = mp.lu_solve(Im, Jm.tolist()) if False else mp.inverse(Im)*Jm
print("lu_solve done", flush=True)
ER, EV = mp.eig(Mmat, left=False, right=True)
evals=[complex(ER[i]) for i in range(B)]
re=sorted([z.real for z in evals])
print("top 8 generalized eigs (mpmath):", re[-8:], flush=True)
print("max M (mpmath) =", re[-1], flush=True)
# min eig of Is to assess conditioning
sI = mp.eigsy(Im)  # symmetric eig
print("min eig Im:", min(float(x) for x in sI[0]), flush=True)
