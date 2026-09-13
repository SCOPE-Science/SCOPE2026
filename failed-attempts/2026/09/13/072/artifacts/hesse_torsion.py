"""Find exact-order-7 point on Hesse cubic E_lam: x^3+y^3+z^3-3 lam xyz=0.
Chord-tangent arithmetic with O=(1:-1:0); Newton solve 7P=O in local coords.
Goal: candidate (a:b:c) with (a:b:c) 7-torsion -> order-7 Sklyanin params
(under sigma = translation by (a:b:c); to be confirmed against literature).
"""
import numpy as np
lam = 0.0  # Fermat
def onE(P):
    x,y,z = P
    return x**3+y**3+z**3-3*lam*x*y*z
O = np.array([1.0,-1.0,0.0])
def third(P, Q):
    # third intersection of line PQ with E (affine lift, dehomogenize by max coord)
    d = P - Q
    # parametrize Q + t d; find t roots of cubic; known roots t=0 (Q), t=1 (P) if both on E
    f = lambda t: onE(Q + t*d)
    # recover cubic coeffs by interpolation at 4 points
    ts = np.array([0.0,1.0,2.0,3.0]); vs = np.array([f(t) for t in ts])
    V = np.vander(ts, 4, increasing=True)
    c = np.linalg.solve(V, vs)  # c0 + c1 t + c2 t^2 + c3 t^3
    r = np.roots([c[3],c[2],c[1],c[0]])
    # identify roots near 0 and 1, return the third
    rs = sorted(r, key=lambda z: (abs(z-0)+abs(z-1)))
    return Q + rs[2]*d
def add(P, Q):
    R = third(P, Q)
    S = third(O, R)
    return S / np.max(np.abs(S))
def mul(n, P):
    R = O.copy()
    Q = P.copy(); k = n
    while k:
        if k & 1: R = add(R, Q)
        Q = add(Q, Q); k >>= 1
    return R
def norm_aff(P):
    # affine chart z=1 if possible else x=1; distance to O irrelevant; use inhomogeneous
    if abs(P[2])>1e-6: return P/P[2]
    return P/P[0]
# random point on E: intersect with random line through O? line through O meets E at 2 other pts
rng = np.random.default_rng(0)
sols=[]
for trial in range(200):
    D = rng.normal(size=3); D = D/np.linalg.norm(D)
    # line O + t D
    f = lambda t: onE(O + t*D)
    ts = np.array([0.0,1.0,2.0,0.5]); vs=np.array([f(t) for t in ts])
    V=np.vander(ts,4,increasing=True); c=np.linalg.solve(V,vs)
    r=np.roots([c[3],c[2],c[1],c[0]])
    r=[z.real for z in r if abs(z.imag)<1e-8 and abs(z)>1e-6]
    if len(r)>=1:
        P = O + r[0]*D
        if abs(onE(P))<1e-8:
            P7 = mul(7,P)
            # check order: is 7P=O? (projective equality)
            M=np.column_stack([P7,O]); _,s_,_=np.linalg.svd(M)
            if s_[-1]<1e-6:
                sols.append(P); break
print("random-order-7 found:", len(sols))
# Newton: solve 7P=O starting from random P, local coords (x/z, y/z) near point with z!=0
def to_aff(P):
    if abs(P[2])>0.2: return np.array([P[0]/P[2], P[1]/P[2]])
    return np.array([P[1]/P[0], P[2]/P[0]])
def F(uv):
    x,y=uv; P=np.array([x,y,1.0]); Q=mul(7,P); Q=Q/Q[2]
    # residual in tangent: Q - O has no meaning (O at infinity z=0); use j-invariant-free residual:
    # 7P=O iff 7P equals O projectively: cross product zero
    cr = np.cross(Q, O)
    return np.array([cr[0],cr[1]])  # two eqs, overdetermined; use least squares Newton
P = np.array([1.0, 2.0, 1.0])
# project onto E first: fix x, solve for y? E: y^3 -3 lam x z y + (x^3+z^3)=0 -> cubic in y
x,z=1.0,1.0
cc=np.roots([1.0,0.0,-3*lam*x*z,x**3+z**3])
print("cube roots for y:",cc)
