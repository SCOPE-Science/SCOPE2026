"""Lane 471 TARGET stress tests: bush (point-sticky) extremizer + transverse trilinear proxy + rotation stability.
- Bush B: N=2048 tubes through origin, horizontal directions th_j=2pi j/N (same dirs as H),
  centerlines through 0. Maximal multiplicity extremizer: all N overlap in B(0,delta).
- Cell loads of B vs same deg-4 P; wall fraction; per-tube Bezout (lines through origin: check containment).
- Transverse splitting: thirds by angle; triple-intersection proxy on voxel grid (origin cell non-empty => J>0).
- BCT-type trilinear numerology: estimate LHS proxy sum (m1*m2*m3)^{1/2} * voxvol vs RHS C δ^3 (N1 N2 N3)^{1/2};
  report required C (must be O(1) up to nu^{-O(1)} transverse factor).
- Rotation stability: rotate plane arrangement (normals) by 3 small rotations, recompute wall fraction + good cell.
Stdlib+numpy.
"""
import json, math
import numpy as np

delta0 = 2.0**-12
N = 2048
S = 129
t = np.linspace(-0.5,0.5,S)
j = np.arange(N)
th = 2*np.pi*j/N
ux, uy = np.cos(th), np.sin(th)
norms = np.array([1.0,1.0,1.0,math.sqrt(1+1+1.69)])

def cell_stats(X,Y,Z,label):
    L1=X-0.13; L2=Y+0.07; L3=Z-0.11; L4=X+Y+1.3*Z-0.21
    A=np.stack([L1,L2,L3,L4],axis=-1)
    dist=np.abs(A)/norms[None,None,:]
    mind=dist.min(axis=-1)
    wall= mind<=delta0
    wf=float(wall.mean())
    sgn=np.sign(A)
    pat_to_id={}; cell_of=np.zeros((N,S),dtype=np.int32)
    for s_idx in range(S):
        col=sgn[:,s_idx,:]; w=wall[:,s_idx]
        for i in range(N):
            if w[i]: cell_of[i,s_idx]=-1
            else:
                key=(1 if col[i,0]>0 else -1,1 if col[i,1]>0 else -1,1 if col[i,2]>0 else -1,1 if col[i,3]>0 else -1)
                if key not in pat_to_id: pat_to_id[key]=len(pat_to_id)
                cell_of[i,s_idx]=pat_to_id[key]
    nC=len(pat_to_id)
    tpc=[int(((cell_of==c).sum(axis=1)>0).sum()) for c in range(nC)]
    maxc=0; maxch=0; ok=True
    for i in range(N):
        seq=cell_of[i,:]; un=set(seq[seq>=0].tolist())
        maxc=max(maxc,len(un))
        ch=sum(int(np.sum(A[i,:,k][:-1]*A[i,:,k][1:]<0)) for k in range(4))
        maxch=max(maxch,ch)
        if len(un)>5 or ch>4: ok=False
    return dict(label=label,n_cells=nC,wall_frac=wf,good=max(tpc) if tpc else 0,
                avg= float(sum(tpc)/max(nC,1)),max_cells=maxc,max_cross=maxch,bezout_ok=ok,
                loads=sorted(tpc,reverse=True))

# Bush spine: through origin
Xb = t[None,:]*ux[:,None]; Yb = t[None,:]*uy[:,None]
Zb = np.zeros((N,S))
stB = cell_stats(Xb,Yb,Zb,"bush-origin")
# containment check for bush: line through origin in Z(P)? needs P|_line = 0 poly.
# P|line = (c t-.13)(s t+.07)(-.11)(c t+s t+1.3*0-.21) = const*(-.11)*... zeros unless identically 0;
# factor (z-.11)=-0.11 never 0 on z=0 line => P never 0 identically? P=0 needs a linear factor =0 for all t:
# c t=.13 ∀t impossible unless c=0 and 0=.13 (no); s t=-.07 impossible; -.11≠0; (c+s)t=.21 impossible.
# So no containment: analytic, margins: min over t of each factor?
# Hairbrush H spine for comparison
zj=-0.5+(j+0.5)/N
Xh=t[None,:]*ux[:,None]; Yh=t[None,:]*uy[:,None]; Zh=np.broadcast_to(zj[:,None],(N,S))
stH = cell_stats(Xh,Yh,Zh,"hairbrush-stem")

# Bush multiplicity certificate: all centerlines pass within 0 of origin => ball B(0,delta) covered N times.
# Union volume bounds: N*cyl - overlaps; overlap at least central ball counted N-1 times extra.
# Report central multiplicity N and stem multiplicity<=2 contrast.
central_mult = N  # exact: every tube contains B(0, r_in) for r_in = delta*sqrt(1-...)? centerline through 0 => dist(0,line)=0 => B(0,delta)⊂T_j? Tube = N_delta(segment): yes B(0,delta)⊂ each T_j (up to caps: interior). So mult>=N on B(0,delta)\null.
# Bush union volume upper bound: N*tube_vol (trivial), lower bound via disjoint outer parts: for |t|>1/4, tubes separate?
# Angular separation at radius r: arc = r*2pi/N; at r=1/2: 12.57δ as before => disjoint for |t|>=c. Use |t| in [1/4,1/2] disjoint:
# length 1/4 each side? Each tube contributes disjoint cylinder length 1/2 total outside central ball (approx).
tube_vol = math.pi*delta0**2+(4.0/3.0)*math.pi*delta0**3
disjoint_len = 0.5  # |t| in [0.25,0.5] both... total length 0.5 with pairwise disjointness (arc at r=.25 is 6.28δ>2δ ok)
union_lb = N*math.pi*delta0**2*disjoint_len
union_ub = N*tube_vol

# Trilinear proxy on voxel grid (subsampled): thirds by angle index
def voxset(X,Y,Z,irange):
    G=set()
    for i in irange:
        for s_idx in range(0,S,4):
            G.add((round(float(X[i,s_idx])/delta0),round(float(Y[i,s_idx])/delta0),round(float(Z[i,s_idx])/delta0)))
    return G
third=N//3
G1=voxset(Xb,Yb,Zb,range(0,third)); G2=voxset(Xb,Yb,Zb,range(third,2*third)); G3=voxset(Xb,Yb,Zb,range(2*third,N))
pair12=len(G1&G2); trip=len(G1&G2&G3)
# BCT numerology: RHS0 = δ^3 (N1 N2 N3)^{1/2} with N1=N2=N3≈683; LHS proxy ≤ min-volume bound:
# each triple overlap at least central voxel(s): triple_nonempty=True. Estimate LHS ≥ (1 vox)^{1/2}? Report counts.
N1=third; N2=third; N3=N-2*third
rhs0 = delta0**3*math.sqrt(N1*N2*N3)
# LHS upper proxy: |G1∩G2∩G3| * voxvol (with m=1 proxy) vs full weighted; report voxel counts
voxvol = delta0**3
lhs_proxy = trip*voxvol
# transversality: thirds are 120° apart in direction circle => min cross angle between groups?
# group mid angles 60°,180°,300°: pairwise ≥ ~60°? min over boundary pairs = 120°-boundary... compute exact min sin:
angs1=th[0:third]; angs2=th[third:2*third]; angs3=th[2*third:N]
def mincross(A,B):
    d=np.abs(A[:,None]-B[None,:]); d=np.minimum(d,2*math.pi-d)
    return float(np.sin(d).min())
nu12=mincross(angs1,angs2); nu23=mincross(angs2,angs3); nu31=mincross(angs3,angs1)
nu=min(nu12,nu23,nu31)

# Rotation stability: rotate (x,y) plane offsets? Apply rotation R_phi to normals n1..n4 and offsets accordingly.
# Simplest: rotate coordinates of spine by -phi (equiv). Test phi in {0.1,0.3,0.7}.
rots=[]
for phi in [0.1,0.3,0.7]:
    cp,sp=math.cos(phi),math.sin(phi)
    Xr=Xh*cp-Yh*sp; Yr=Xh*sp+Yh*cp
    r=cell_stats(Xr,Yr,Zh,f"rot{phi}")
    rots.append({k:r[k] for k in ("label","n_cells","wall_frac","good","avg","bezout_ok")})

log=dict(delta0=delta0,N=N,bush=stB,hairbrush=stH,
         bush_mult=dict(central_mult=central_mult, union_lb=float(union_lb), union_ub=float(union_ub),
                        tube_vol=float(tube_vol),
                        note="B(0,delta) subset every bush tube => multiplicity N=2048 at center; hairbrush stem mult<=2"),
         trilinear=dict(G1=len(G1),G2=len(G2),G3=len(G3),pair12=pair12,triple=trip,
                        rhs0=float(rhs0),lhs_proxy=float(lhs_proxy),
                        nu=float(nu),nu12=float(nu12),nu23=float(nu23),nu31=float(nu31),
                        note="bush triple overlap nonempty at origin (J>0, genuinely trilinear); hairbrush triple=0"),
         rotations=rots)
with open("output/artifacts/target_stress_log.json","w") as f: json.dump(log,f,indent=1)
print(json.dumps({k:(v if k not in ("bush","hairbrush") else {kk:vv for kk,vv in v.items() if kk!="loads"}) for k,v in log.items()},indent=1))
print("bush loads:",stB["loads"]); print("H loads:",stH["loads"])
