import numpy as np, itertools, cmath
from engine import principal_series_mats, Q, WORDS, mat_of_word, MAT2IDX, LENS
np.set_printoptions(precision=3, suppress=True, linewidth=200)

def W0_mats_on_exps():
    # matrices S1,S2 as 2x2 on column (c1,c2): S1=[[-1,1],[0,1]], S2=[[1,0],[3,-1]]
    A1=np.array([[-1,1],[0,1]]); A2=np.array([[1,0],[3,-1]])
    return A1,A2
A1,A2=W0_mats_on_exps()

def orbit_reps_on_T_sample():
    """Enumerate W0 orbit types on (t1,t2) in (C*)^2: classify stabilizer + pole locus."""
    # We'll sample a grid of roots-of-unity-ish + generic points
    pts={}
    cand=[1,-1,1j,-1j,2,3,0.5]
    for a in cand:
        for b in cand:
            pts[(complex(a),complex(b))]=(complex(a),complex(b))
    # extra: exp points
    import cmath
    for k in range(8):
        z=cmath.exp(2j*cmath.pi*k/8)
        pts[(z,1)]=(z,1); pts[(1,z)]=(1,z); pts[(z,z)]=(z,z)
    return list(pts.values())

def w0_orbit(t):
    A1,A2=W0_mats_on_exps()
    # action on T: (w.t)_i = t1^{M11}... careful: th_x(wt) = t^{w^{-1}x}? Convention: (w t)(x) = t(w^{-1} x).
    # Build orbit by applying generators with inverse action.
    # Since s_i^{-1}=s_i, (s.t)(e_j) = t(s e_j).
    def s_act(s,t):
        t1,t2=t
        if s==1:
            # s1 e1=-e1+e2? wait s1 acts on exps: s1(1,0)=(-1,0)? compute: s1_act((1,0)) = (-1+0,0)=(-1,0). s1(0,1)=(1,1).
            # (s.t)_1 = t(s e_1)= t1^{-1}; (s.t)_2 = t(s e_2)= t1*t2.
            return (1/t1, t1*t2)
        else:
            # s2(1,0)=(1,3), s2(0,1)=(0,-1): (s.t)_1=t1*t2^3, (s.t)_2=1/t2
            return (t1*t2**3, 1/t2)
    seen=set(); orb=[]
    stack=[t]
    def key(z): return (round(z[0].real,9),round(z[0].imag,9),round(z[1].real,9),round(z[1].imag,9))
    while stack:
        u=stack.pop()
        k=key(u)
        if k in seen: continue
        seen.add(k); orb.append(u)
        for s in [1,2]:
            stack.append(s_act(s,u))
    return orb

def pole_signature(t):
    """which positive roots take value 1 or -1 at t (resonance locus)."""
    # positive roots of G2: a1,a2,a1+a2,2a1+a2? Let's list: short: a1, a1+a2, 2a1+a2? long: a2,3a1+a2? hmm standard:
    # Positive roots: alpha1, alpha2, alpha1+alpha2, 2alpha1+alpha2, 3alpha1+alpha2, 3alpha1+2alpha2.
    proots=[(1,0),(0,1),(1,1),(2,1),(3,1),(3,2)]
    def ev(e): return t[0]**e[0]*t[1]**e[1]
    return {e:ev(e) for e in proots}

# generic irreducibility: Schur test via commutant dimension
def commutant_dim(M):
    # solve [C,T1]=[C,T2]=[C,X1]=0 (X2 then follows if X1 gen? include both)
    import numpy as np
    n=12
    def comm_mat(A):
        return np.kron(np.eye(n),A)-np.kron(A.T,np.eye(n))
    K=np.vstack([comm_mat(M["T1"]),comm_mat(M["T2"]),comm_mat(M["X1"]),comm_mat(M["X2"])])
    s=np.linalg.svd(K,compute_uv=False)
    tol=1e-6
    rank=np.sum(s>tol)
    return n*n-rank, s

for t in [(2.0+0j,3.0+0j),(1.5,2.5),(0.7+0.3j,1.1-0.2j)]:
    M=principal_series_mats(t)
    d,s=commutant_dim(M)
    print("t=",t,"commutant dim=",d, "min sv tail", s[-3:])

# central character: W0-invariant Laurent polynomials act by scalars; check orbit-sums of (1,0),(0,1) etc.
def center_acts_scalar(M,t):
    # z1 = sum_{w} th_{w(1,0)} etc. Build matrices for a few orbit sums, check scalar.
    from engine import theta_times_Tw, eval_poly
    import numpy as np
    n=12
    # orbit of (1,0) under W0
    A1m=np.array([[-1,1],[0,1]]); A2m=np.array([[1,0],[3,-1]])
    def apply(w,e):
        v=np.array(e)
        # w is word; apply letters left-to-right? mat = product: apply in order
        for s in w:
            v=(A1m if s==1 else A2m)@v
        return tuple(int(x) for x in v)
    for base in [(1,0),(0,1),(1,1)]:
        orb=set(apply(w,base) for w in WORDS)
        Z=np.zeros((n,n),dtype=complex)
        for e in orb:
            for w in range(n):
                r=theta_times_Tw(e,w)
                for u in range(n):
                    Z[u,w]+=eval_poly(r[u],t)
        # check scalar
        d=np.diag(Z)
        off=np.linalg.norm(Z-np.diag(d))
        print(f"base={base} orbit-size={len(orb)} diagmean={np.mean(d):.4f} maxdev={np.max(np.abs(d-np.mean(d))):.2e} off={off:.2e}")
    return

print("--- center ---")
center_acts_scalar(principal_series_mats((2.0,3.0)),(2.0,3.0))
center_acts_scalar(principal_series_mats((1j,1.0)),(1j,1.0))
