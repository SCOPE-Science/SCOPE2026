"""Exact joint-ellipsoid BGK test (S-lemma, no budget split) for lane-1018.
Variables: M in R^5 (macro coeffs), m micro with ||m||^2+|M|^2=1.
z = (q[1..4], r[0..4]) with q_a=<u_a,m>, r_a=<w_a,m>,
u_a=(I-Pi)(V phi_a) (a=1..4; u_0=0), w_a=(I-Pi)(V^2 phi_a).
Constraint: z' J^{-1} z <= ||m||^2, J = joint Gram (9x9, exact moments).
G(M,m) = D-kH >= (1-k)m^2 - k|M|^2-ish + eps[...] - k*eps-corrections.
Decision proxy: PSD of 14x14 Gmat in (M,y), z=J^{1/2}y, with normalization
|M|^2+|y|^2<=1 implies m^2>=|y|^2 ... we minimize
G = (1-k)|y|^2 + eps[M'Qmm M + 2M'Xq q + 2M'Xr r + q'Qpp q] - k|M|^2 - k*eps*eq
where eq bounds |2Re<AM,M+m>| <= |M|^2+|M||m| (||A||<=1/2): worst -k*eps*(1.5|M|^2+0.5m^2).
Sufficient: Gmat PSD. This is still sufficient (uses worst-case eq) but joint in (q,r).
"""
import numpy as np
exec(open('scratch/lmi15.py').read().split("eps = ")[0])  # F,S,B,P polys...
B = np.linalg.inv(np.eye(5) + S)
def picoeffs(p):
    return np.array([pexpect(pmul(polys[c], p)) for c in range(5)])
V1 = {(1,0,0):1.0}; V1SQ = {(2,0,0):1.0}
ua = [pmul(V1, polys[a]) for a in [1,2,3,4]]
wa = [pmul(V1SQ, polys[a]) for a in range(5)]
# micro parts: subtract Pi projection
Ca = np.array([picoeffs(p) for p in ua])
Cb = np.array([picoeffs(p) for p in wa])
def mgram(pa, pb, Ca_, Cb_):
    return pexpect(pmul(pa, pb)) - Ca_ @ Cb_
Ju = np.zeros((4,4)); Jw = np.zeros((5,5)); Juw = np.zeros((4,5))
for i in range(4):
    for j in range(4):
        Ju[i,j] = mgram(ua[i], ua[j], Ca[i], Ca[j])
for i in range(5):
    for j in range(5):
        Jw[i,j] = mgram(wa[i], wa[j], Cb[i], Cb[j])
for i in range(4):
    for j in range(5):
        Juw[i,j] = mgram(ua[i], wa[j], Ca[i], Cb[j])
J = np.block([[Ju, Juw],[Juw.T, Jw]])
evJ = np.linalg.eigvalsh(J)
print("joint J eigs:", evJ)
Jreg = J + 1e-12*np.eye(9)
wJ, VJ = np.linalg.eigh(Jreg)
Jh = VJ @ np.diag(np.sqrt(np.maximum(wJ,0))) @ VJ.T  # J^{1/2}
eps=1/8; kap=1/120
BS=B@S; FBF=F@B@F
Qmm=((BS+BS.T)/2-((FBF+FBF.T)/2))
Xq=B-2*F@B   # M'Xq q, q idx [1..4] -> cols 1..4 of Xq
Xr=B         # M'Xr r
Qpp=-(B+B.T)/2  # q'Qpp q on idx 1..4
# order y: [q1..q4, r0..r4]; maps: q_full = Eq y_q, Eq: 5x4 embedding rows1..4
Eq=np.zeros((5,4)); Eq[1,0]=1; Eq[2,1]=1; Eq[3,2]=1; Eq[4,3]=1
X = np.hstack([Xq@Eq, Xr])  # 5x9 cross M'X z
Qz = np.zeros((9,9)); Qz[:4,:4] = Eq.T@Qpp@Eq  # z-block (r-block 0)
# Gmat in (M(5), y(9)): G = M'(epsQmm - kap I -1.5kap eps I)M + 2eps M'X Jh y
#   + y'[(1-kap)I + eps Jh'QzJh - 0.5kap eps I]y
A11 = eps*Qmm - kap*np.eye(5) - 1.5*kap*eps*np.eye(5)
A12 = eps*X@Jh
A22 = ((1-kap) - 0.5*kap*eps)*np.eye(9) + eps*(Jh.T@Qz@Jh)
Gmat = np.block([[A11, A12/1.0],[np.zeros((9,5)), np.zeros((9,9))]])
Gmat = np.block([[A11, A12],[A12.T, A22]])
ev = np.linalg.eigvalsh(Gmat)
print("BGK joint Gmat min eig =", ev[0])
print("eigs:", np.round(ev,4))
print("BGK JOINT:", "CLOSE" if ev[0]>=0 else "OPEN")
# BM hard-sphere gap number
import math
Sbm = math.pi*((1/8)**0.5)*math.exp(-0.5)/24
print("Baranger-Mouhot HS lower bound lam_m >=", Sbm)
