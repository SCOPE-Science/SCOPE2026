import numpy as np

def k1_of_lengths(L, kmax=16.0, nscan=8000):
    """L = array length 6 (a1..a3,b1..b3), total normalized 1 (not required).
    Returns smallest k>0 eigenvalue via entire 9x9 system sigma_min scan + refine.
    """
    a = np.asarray(L[:3]); b = np.asarray(L[3:])
    def Z(k):
        # unknowns order: phiA,phiB,phiC, c1..c3, d1..d3  (9)
        M = np.zeros((9,9))
        # rows 0..2: a-edges continuity: phiA*cos + c_i*sin - phiB =0
        for i in range(3):
            M[i,0] = np.cos(k*a[i])
            M[i,1] = -1.0
            M[i,3+i] = np.sin(k*a[i])
        # rows 3..5: b-edges: phiB*cos + d_j*sin - phiC=0
        for j in range(3):
            M[3+j,1] = np.cos(k*b[j])
            M[3+j,2] = -1.0
            M[3+j,6+j] = np.sin(k*b[j])
        # row 6: Kirchhoff A: sum c =0
        M[6,3:6] = 1.0
        # row 7: Kirchhoff C: sum phiB*sin(kb) - d_j*cos(kb)=0
        for j in range(3):
            M[7,1] += 0  # accumulate below
        # careful: single phiB coefficient = sum sin
        M[7,1] = np.sum(np.sin(k*b))
        for j in range(3):
            M[7,6+j] = -np.cos(k*b[j])
        # row 8: Kirchhoff B: phiA*sum sin(ka) + sum -c_i cos(ka) + sum d_j =0
        M[8,0] = np.sum(np.sin(k*a))
        for i in range(3):
            M[8,3+i] = -np.cos(k*a[i])
        M[8,6:9] = 1.0
        return M
    ks = np.linspace(0, kmax, nscan+1)
    # sigma min
    sig = np.empty_like(ks)
    for idx,k in enumerate(ks):
        if k==0:
            sig[idx]=0.0
            continue
        s = np.linalg.svd(Z(k), compute_uv=False)
        sig[idx]=s[-1]
    # find first dip below threshold after 0. Use local minima of sig with small value.
    # threshold adaptive: minima < 0.05? Since Z scaling O(1), true zeros give ~0.
    # scan for local minima
    cands=[]
    for i in range(1,nscan):
        if sig[i] < sig[i-1] and sig[i] <= sig[i+1] and sig[i] < 1e-2:
            # refine with golden/parabolic around ks[i]
            cands.append(i)
            break  # first eigenvalue only
    if not cands:
        return None, ks, sig
    i = cands[0]
    # refine: minimize sig in [ks[i-1],ks[i+1]] via ternary-like (sig is V-shaped, use fine scan)
    lo, hi = ks[i-1], ks[i+1]
    for _ in range(40):
        grid = np.linspace(lo,hi,41)
        ss = [np.linalg.svd(Z(k),compute_uv=False)[-1] for k in grid]
        j = int(np.argmin(ss))
        if j==0: lo,hi = grid[0],grid[1]
        elif j==len(grid)-1: lo,hi=grid[-2],grid[-1]
        else: lo,hi=grid[j-1],grid[j+1]
    k1=(lo+hi)/2
    return k1, ks, sig

if __name__=="__main__":
    # symmetric point
    L=np.ones(6)/6
    k1,_,_=k1_of_lengths(L)
    print("symmetric k1/pi =",k1/np.pi)
    # flower: contract a1->0? Actually flower needs 2 zeros: a1=0,b1=0, rest 1/4 each
    Lf=np.array([0,0.25,0.25,0,0.25,0.25])
    k1f,_,_=k1_of_lengths(Lf)
    print("flower k1/pi =",k1f/np.pi)
