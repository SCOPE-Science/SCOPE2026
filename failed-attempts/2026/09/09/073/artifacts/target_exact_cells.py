"""Lane 471 TARGET, part 4 (EXACT, no sampling): line-vs-plane cell analysis + exact wall measure.
For each tube centerline L(t)=b+t e, each plane k: l_k(t)=a_k t + c_k (affine linear, EXACT coeffs).
Roots t_k*=-c_k/a_k (|a_k|>tiny else parallel: margin recorded). Sorted roots split [-1/2,1/2] into
intervals; each interval has a fixed sign vector => exact cell id. Tube's delta-neighborhood meets cell C
if centerline meets C OR passes within delta/sin(phi) of boundary... instead of angle bookkeeping we
certify two exact quantities:
 (E1) exact #cells met by CENTERLINE per tube (Bezout <=5), exact cell-load histogram, exact good cell;
 (E2) exact wall LENGTH fraction: |{t: min_k |l_k(t)|/||n_k|| <= d}| measured exactly as union of <=4
      interval preimages (each |a t+c|<=d||n|| is one interval, possibly empty/unbounded->clipped).
Covers H (stem), bush, sticky-S, plany families + canonical arrangement. No spine sampling anywhere.
"""
import json, math
import numpy as np

d = 2.0**-12
N = 2048
LO, HI = -0.5, 0.5

# canonical arrangement (UNNORMALIZED frames; dist divides by row norm):
# P1: x=0.13, P2: y=-0.07, P3: z=0.11, P4: x+y+1.3z=0.21 (matches target_cell_test.py)
NR = np.array([[1.,0,0],[0,1.,0],[0,0,1],[1.,1.,1.3]])
OF = np.array([0.13, 0.07, 0.11, 0.21])  # L2 = y+0.07 so that L2=0 <=> y=-0.07
nN = np.linalg.norm(NR,axis=1)
NRn = NR/nN[:,None]
OFn = OF/nN  # normalized-frame offsets; A=(NRn)e, C=(NRn)b-OFn; dist=|At+C| (rows unit)

def exact_family(bx,by,bz,ex,ey,ez,label):
    n = len(bx)
    a = ex*NR[:,0:1].T[0] if False else None
    # a_k(tube) = n_k . e ; c_k = n_k . b - o_k
    A = np.stack([ex,ey,ez],axis=1) @ NRn.T   # (n,4)
    C = np.stack([bx,by,bz],axis=1) @ NRn.T - OFn[None,:]  # (n,4)
    par = np.abs(A) < 1e-15
    npar = int(par.sum())
    # roots (inf where parallel)
    R = np.where(par, np.inf, -C/np.where(par,1.0,A))
    # per-tube: sorted interior roots, cell count, wall length
    cell_count = np.zeros(n,dtype=int)
    maxcells = 0
    pat_to_id = {}
    tubes_per_cell = {}
    wall_len = np.zeros(n)
    for i in range(n):
        rts = sorted(r for r in R[i,:] if np.isfinite(r) and LO < r < HI)
        # distinct (planes general position: distinct roots generic; merge ties)
        pts = [LO]+rts+[HI]
        # cells of open intervals
        seen = set()
        for s_idx in range(len(pts)-1):
            mid = 0.5*(pts[s_idx]+pts[s_idx+1])
            sv = tuple(1 if (A[i,k]*mid+C[i,k])>0 else -1 for k in range(4))
            # (midpoint exactly 0 impossible unless identically-zero form, excluded below)
            seen.add(sv)
            if sv not in pat_to_id: pat_to_id[sv]=len(pat_to_id)
            c = pat_to_id[sv]
            tubes_per_cell[c]=tubes_per_cell.get(c,0)+1  # counts tube-cell incidences (per-interval dupes merged below)
        # NOTE: tubes_per_cell above overcounts if same cell in 2 intervals (non-convex cells). Fix: use seen.
        cell_count[i]=len(seen)
        maxcells=max(maxcells,len(seen))
        # wall length: union of intervals {|A t+C|<=d} clipped to [LO,HI]
        ivs=[]
        for k in range(4):
            ak,ck = A[i,k],C[i,k]
            if abs(ak)<1e-15:
                if abs(ck)<=d: ivs.append((LO,HI))
            else:
                t1=(-d-ck)/ak; t2=(d-ck)/ak
                lo,hi=(min(t1,t2),max(t1,t2))
                lo,hi=max(lo,LO),min(hi,HI)
                if hi>lo and hi>LO and lo<HI: ivs.append((lo,hi))
        ivs.sort()
        tot=0.0; curo=None
        for lo,hi in ivs:
            if curo is None: curo=[lo,hi]
            elif lo<=curo[1]: curo[1]=max(curo[1],hi)
            else: tot+=curo[1]-curo[0]; curo=[lo,hi]
        if curo is not None: tot+=curo[1]-curo[0]
        wall_len[i]=tot
    # fix tubes_per_cell (recompute from seen-sets to avoid dupes)
    # redo cleanly:
    tpc = {}
    for i in range(n):
        rts = sorted(r for r in R[i,:] if np.isfinite(r) and LO < r < HI)
        pts=[LO]+rts+[HI]
        seen=set()
        for s_idx in range(len(pts)-1):
            mid=0.5*(pts[s_idx]+pts[s_idx+1])
            sv=tuple(1 if (A[i,k]*mid+C[i,k])>0 else -1 for k in range(4))
            seen.add(sv)
        for sv in seen:
            tpc[sv]=tpc.get(sv,0)+1
    loads=sorted(tpc.values(),reverse=True)
    return dict(label=label,n_tubes=n,n_cells=len(tpc),loads=loads,good=max(loads),
                avg=sum(loads)/max(len(loads),1),max_cells_per_tube=int(cell_count.max()),
                bezout_ok=bool((cell_count<=5).all()),n_parallel_entries=npar,
                wall_frac=float(wall_len.sum()/(n*1.0)),wall_lengths=wall_len)

j=np.arange(N); th=2*np.pi*j/N; ux=np.cos(th); uy=np.sin(th); uz=np.zeros(N)
zj=-0.5+(j+0.5)/N
out={}
# H
r=exact_family(np.zeros(N),np.zeros(N),zj,ux,uy,uz,"H"); out["H"]={k:(v if k!="wall_lengths" else "array") for k,v in r.items()}; out["H"]["loads"]=r["loads"]
print("H:",{k:v for k,v in out["H"].items() if k!="loads"},"loads:",r["loads"][:6],"wallmax:",float(r["wall_lengths"].max()))
# Bush
r2=exact_family(np.zeros(N),np.zeros(N),np.zeros(N),ux,uy,uz,"bush"); out["bush"]={k:(v if k!="wall_lengths" else "array") for k,v in r2.items()}; out["bush"]["loads"]=r2["loads"]
print("bush:",{k:v for k,v in out["bush"].items() if k!="loads"},"loads:",r2["loads"][:8])
# Sticky S
bx=-0.5+(j+0.5)/N
r3=exact_family(bx,np.zeros(N),np.full(N,0.11),ux,uy,uz,"sticky"); out["sticky"]={k:(v if k!="wall_lengths" else "array") for k,v in r3.items()}; out["sticky"]["loads"]=r3["loads"]
print("sticky:",{k:v for k,v in out["sticky"].items() if k!="loads"},"loads:",r3["loads"][:8])
# Plany
w=2.0**-6
az=2*np.pi*j/N; pol=np.pi/2+w*(2*((j*7919)%256)/255.0-1.0)
ex=np.sin(pol)*np.cos(az); ey=np.sin(pol)*np.sin(az); ez=np.cos(pol)
bxx=-0.5+(j+0.5)/N
r4=exact_family(bxx,np.zeros(N),np.zeros(N),ex,ey,ez,"plany"); out["plany"]={k:(v if k!="wall_lengths" else "array") for k,v in r4.items()}; out["plany"]["loads"]=r4["loads"]
print("plany:",{k:v for k,v in out["plany"].items() if k!="loads"},"loads:",r4["loads"][:8])
with open("output/artifacts/target_exact_cells.json","w") as f:
    json.dump(out,f,indent=1)
print("WALL fracs exact: H=%.6f bush=%.6f sticky=%.6f plany=%.6f"%(
  float(r["wall_lengths"].sum()/N),float(r2["wall_lengths"].sum()/N),float(r3["wall_lengths"].sum()/N),float(r4["wall_lengths"].sum()/N)))
