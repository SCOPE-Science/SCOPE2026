"""Script K: RIGOROUS cone certificates via affine corner bounds + padding.
Mb(c2,c3) = C + c2*E2 + c3*E3 exactly (Df affine in (c2,c3)), |c2|,|c3|<=1.
Unstable cone Ku(kappa): |s| <= kappa*|y|, y=(w,u), under M=[m11,r';c,B]:
  |s'| <= (|m11|*kappa+|r|)|y|, |y'| >= (sigmin(B)-kappa*|c|)|y|.
Bound each scalar by center+radius: |.| <= |C_.|+|E2_.|+|E3_.| (entrywise ell1/ell2),
sigmin(B) >= sigmin(B_C) - ||E2_B||_2 - ||E3_B||_2 (Weyl).
Stable cone Ks(kappa): |y| <= kappa*|s| under N=Df^{-1}=DS^{-1}A^{-1},
DS^{-1}=[[1,-u,u*v],[0,1,-v],[0,0,1]] polynomial in (u,v)= degree<=2 terms;
bound N = N0 + (explicit polynomial remainder with |u|<=alp,|v|<=bet) similarly.
Double-precision rounding padded by EPS=1e-9 (far below margins).
"""
import math
import numpy as np

EPS = 1e-9
A = np.array([[2., 1., 0.], [1., 2., 1.], [0., 1., 1.]])
w, P = np.linalg.eigh(A)
assert abs(P.T @ P - np.eye(3)).max() < 1e-14, "P orthogonality"
alp, bet = 2*math.pi*0.03, 2*math.pi*0.02
# Df(u,v) = A @ [[1,u,0],[0,1,v],[0,0,1]], u=alp*c2, v=bet*c3
DS0 = np.eye(3)
dDS2 = np.array([[0., 1., 0.], [0., 0., 0.], [0., 0., 0.]])   # d/du
dDS3 = np.array([[0., 0., 0.], [0., 0., 1.], [0., 0., 0.]])   # d/dv
C = P.T @ (A @ DS0) @ P
E2 = P.T @ (A @ dDS2) @ P * alp
E3 = P.T @ (A @ dDS3) @ P * bet

def split(M):
    return M[0, 0], M[0, 1:], M[1:, 0], M[1:, :]

c11, cr, cc, B = split(C)
e11, er, ec, eB = split(E2)
f11, fr, fc, fB = split(E3)
m11 = abs(c11) + abs(e11) + abs(f11) + EPS
rn = np.linalg.norm(cr) + np.linalg.norm(er) + np.linalg.norm(fr) + EPS
cn = np.linalg.norm(cc) + np.linalg.norm(ec) + np.linalg.norm(fc) + EPS
sB = min(np.linalg.svd(B, compute_uv=False)) - np.linalg.norm(E2[1:, 1:], 2) - np.linalg.norm(E3[1:, 1:], 2) - EPS
print(f"unstable-block bounds: |m11|<={m11:.4f} |r|<={rn:.4f} |c|<={cn:.4f} sigmin(B)>={sB:.4f}")
for kap in [0.3, 0.5, 0.8]:
    num = m11*kap + rn
    den = sB - kap*cn
    print(f"  kappa={kap}: image ratio <= {num/den:.4f} (need <{kap}: {num/den<kap}) "
          f"expansion >= {den:.4f} (>1: {den>1})")

# ---- stable cone under N = DS^{-1} A^{-1}: N(x) = Q0 + Q1*u + Q2*v + Q3*u*v ----
Ainv = np.linalg.inv(A)
Q0 = P.T @ (np.eye(3) @ Ainv) @ P
Q1 = P.T @ (np.array([[0., -1., 0.], [0., 0., 0.], [0., 0., 0.]]) @ Ainv) @ P
Q2 = P.T @ (np.array([[0., 0., 0.], [0., 0., -1.], [0., 0., 0.]]) @ Ainv) @ P
Q3 = P.T @ (np.array([[0., 0., 1.], [0., 0., 0.], [0., 0., 0.]]) @ Ainv) @ P
# stable cone Ks(kap): |y|<=kap|s|; write N=[n11,r';c,Bn]; s'=n11 s + r'.y, y'=c s + Bn y
n11 = abs(Q0[0, 0]) - (abs(Q1[0, 0])*alp + abs(Q2[0, 0])*bet + abs(Q3[0, 0])*alp*bet) - EPS
rn2 = np.linalg.norm(Q0[0, 1:]) + np.linalg.norm(Q1[0, 1:])*alp + np.linalg.norm(Q2[0, 1:])*bet + np.linalg.norm(Q3[0, 1:])*alp*bet + EPS
cn2 = np.linalg.norm(Q0[1:, 0]) + np.linalg.norm(Q1[1:, 0])*alp + np.linalg.norm(Q2[1:, 0])*bet + np.linalg.norm(Q3[1:, 0])*alp*bet + EPS
bN = np.linalg.norm(Q0[1:, 1:], 2) + np.linalg.norm(Q1[1:, 1:], 2)*alp + np.linalg.norm(Q2[1:, 1:], 2)*bet + np.linalg.norm(Q3[1:, 1:], 2)*alp*bet + EPS
print(f"stable-block bounds: n11>={n11:.4f} |r|<={rn2:.4f} |c|<={cn2:.4f} ||Bn||<={bN:.4f}")
for kap in [0.3, 0.5, 0.8, 1.0]:
    num = cn2 + bN*kap
    den = n11 - rn2*kap
    print(f"  kappa={kap}: image ratio <= {num/den:.4f} (need <{kap}: {num/den<kap}) "
          f"stable expansion >= {den:.4f} (>1: {den>1})")
print(f"implied contraction Lambda_s <= {1/(n11-rn2*0.5):.4f} (kappa=0.5 cone)")
