"""Robust chord-tangent arithmetic on Hesse E_lam over C; find order-7 point."""
import numpy as np
lam = 2.0  # E: x^3+y^3+z^3-3 lam xyz=0 (contains (1:2:3))
def F(P):
    x,y,z=P; return x**3+y**3+z**3-3*lam*x*y*z
def grad(P):
    x,y,z=P
    return np.array([3*x**2-3*lam*y*z, 3*y**2-3*lam*x*z, 3*z**2-3*lam*x*y],dtype=complex)
O=np.array([1.0,-1.0,0.0],dtype=complex)
assert abs(F(O))<1e-12
def third(P,Q):
    P=np.array(P,dtype=complex); Q=np.array(Q,dtype=complex)
    if np.linalg.norm(np.cross(P,Q))<1e-12:  # same projective point -> tangent
        dline=grad(P)
    else:
        dline=np.cross(P,Q)  # line coeffs
    # parametrize line: find two distinct points? Use basis of nullspace of dline
    u,s,vh=np.linalg.svd(dline.reshape(1,3)); base=vh[1:,:]  # 2x3 rows span line
    A,B=base[0],base[1]
    # restrict cubic to line: A s + B t; solve cubic in (s:t) -> set t=1, solve in u=s/t (plus check t=0)
    import numpy.polynomial.polynomial as Ppoly
    def f(u): return F(A*u+B)
    ts=np.array([0,1,2,3],dtype=complex); vs=np.array([f(t) for t in ts])
    V=np.vander(ts,4,increasing=True); c=np.linalg.solve(V,vs)
    r=np.roots([c[3],c[2],c[1],c[0]])
    # identify which roots correspond to P and Q (projective), return third
    def proj(u): return A*u+B
    # match: known params: solve for u_P: P ~ A u + B -> least squares
    def param(R):
        M=np.column_stack([A,B]); # R = M [u,1]^T up to scale: solve cross zero
        # brute: try t=1 line: u from first nonzero coord ratio
        for i in range(3):
            if abs(B[i])>1e-9 or abs(A[i])>1e-9:
                pass
        # least squares on affine chart: normalize R and candidates by max coord
        return None
    # simpler: match by projective distance
    def pdist(u,R):
        C=proj(u); M=np.column_stack([C,R]); _,s_,_=np.linalg.svd(M); return s_[-1]
    # find u for P and Q by Newton from seeds? Instead: find all 3 roots, match greedily
    used=[False]*3
    import itertools
    # locate P: pick root minimizing pdist to P; same for Q
    dsP=[pdist(u,P) for u in r]; dsQ=[pdist(u,Q) for u in r]
    iP=int(np.argmin(dsP)); iQ=int(np.argmin(dsQ))
    assert dsP[iP]<1e-6, (dsP,r)
    # if P==Q (doubling), the tangent root is double: both iP,iQ may coincide; the "known" multiplicity is 2
    if iP==iQ:
        # double root at iP; third is the remaining root with largest... the one not iP (if double root, two entries equal)
        # identify duplicate: sort roots, find pair
        order=sorted(range(3),key=lambda i: abs(r[i]-r[iP]))
        third_idx=[i for i in range(3) if i not in order[:2]][0] if abs(r[order[1]]-r[iP])<1e-4 else [i for i in range(3) if i!=iP]
        # fallback: remaining index
        cands=[i for i in range(3) if i!=iP]
        # choose candidate farthest from r[iP]
        third_idx=max(cands,key=lambda i: abs(r[i]-r[iP]))
    else:
        third_idx=3-iP-iQ if len({iP,iQ})==2 else None
        third_idx=6-iP-iQ-sum([i for i in range(3)])  # nonsense guard
        third_idx=3-iP-iQ if (iP!=iQ and 0<=3-iP-iQ<=2) else None
        # correct: indices 0,1,2 sum=3
        third_idx=3-iP-iQ
    return proj(r[third_idx])/np.max(np.abs(proj(r[third_idx])))
def add(P,Q):
    R=third(P,Q); S=third(O,R); return S/np.max(np.abs(S))
def mul(n,P):
    R=O.copy(); Q=P.copy(); k=n
    while k:
        if k&1: R=add(R,Q)
        Q=add(Q,Q); k>>=1
    return R
def peq(P,Q):
    M=np.column_stack([P,Q]); _,s_,_=np.linalg.svd(M); return s_[-1]
# test group law basics
import numpy.random as rnd
rng=np.random.default_rng(1)
P=np.array([1.0,2.0,3.0],dtype=complex); print("F(P)=",F(P))
print("P+O==P?",peq(add(P,O),P))
print("P+(-P)==O?",peq(add(P,add(O,add(P,P))*0+third(P,third(O,P))),O))
# doubling test: 2P via tangent
P2=add(P,P); print("2P=",P2,"F=",F(P2))
print("7P==O?",peq(mul(7,P),O), " |2P| etc")
# Newton search for 7-torsion: parametrize E via x=1 line? E|_{x=1}: 1+y^3+z^3-3 lam y z=0. unknowns (y,z).
def lift(y,z): return np.array([1.0,y,z],dtype=complex)
def order7_res(yz):
    y,z=yz[0]+1j*yz[1],yz[2]+1j*yz[3]
    P=lift(y,z)
    return np.array([F(P).real,F(P).imag,0,0])  # placeholder
# use random complex starts + fsolve-like Newton on (y,z) in C^2: equations: F(P)=0 (1 cplx eq) + cross(mul(7,P),O)=0 (need 1 cplx eq: projective equality = rank 1; use 2x2 minor ratios)
def res_vec(v):
    y=v[0]+1j*v[1]; z=v[2]+1j*v[3]; P=np.array([1.0,y,z])
    if abs(F(P))>1e6: return np.array([1e6]*4)
    Q=mul(7,P)
    # equality Q==O: cross(Q,O) should be 0 vector; but O=(1,-1,0): cross = (Q1*0-Q2*(-1), Q2*1-Q0*0, Q0*(-1)-Q1*1) = (Q2, Q2? recompute) -> use two components normalized
    cr=np.cross(Q,O); n=np.max(np.abs(Q))
    return np.array([F(P).real,F(P).imag,(cr[0]/n).real,(cr[0]/n).imag])
from scipy.optimize import fsolve
