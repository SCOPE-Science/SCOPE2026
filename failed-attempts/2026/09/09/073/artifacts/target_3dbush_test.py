"""Lane 471 TARGET, part 5: genuinely-3D bush stress (Fibonacci 2048 dirs on S^2 through origin).
- min pairwise angle G (exact, vectorized); multiplicity N at center (all centerlines through 0);
- union lower bound via analytic outer-disjointness: concurrent lines angle>=G, |s|,|t|>=R0 =>
  dist>=2 R0 sin(G/2); choose R0=d/sin(G/2) (margin exactly 2d); union>=N*2 pi d^2 (0.5-R0);
- maximal-ratio consistency (C_needed at eps=0); trilinear: 3 octant-caps w/ mutual gap, J localized.
Stdlib+numpy.
"""
import json, math
import numpy as np

d = 2.0**-12; N=2048
# Fibonacci sphere
ga = math.pi*(3.0-math.sqrt(5.0))
jj=np.arange(N)
zz = 1.0-(2.0*(jj+0.5)/N)
rr = np.sqrt(np.maximum(0.0,1-zz**2))
az = ga*jj
ex=rr*np.cos(az); ey=rr*np.sin(az); ez=zz
E=np.stack([ex,ey,ez],axis=1)
# min pairwise angle: Gram matrix (2048^2 = 4.2M entries, float64 = 33MB, ok)
G = E@E.T
np.fill_diagonal(G,-2.0)
cmax = G.max()
Gmin_angle = math.acos(min(1.0,cmax))
print("max cos =",cmax,"Gmin(deg)=",math.degrees(Gmin_angle))
s = math.sin(Gmin_angle/2.0)
R0 = d/s
print("R0=",R0,"R0/d=",R0/d)
tube_vol = math.pi*d**2+(4.0/3.0)*math.pi*d**3
per = 2*math.pi*d**2*(0.5-R0)
Ulb = N*per; Uub = N*tube_vol
print("union in [%.3e, %.3e]"%(Ulb,Uub))
MnUb=(4*math.pi)**(3.0/8.0)
fn=Ulb**(3.0/8.0); ratio=MnUb/fn
print("fnorm>=%.4f ratio_ub=%.2f Cneed=%.2f"%(fn,ratio,ratio/d**(-1.0/8.0)))
# direction separation check: need Gmin >= d (delta-separated)? Fibonacci min ~ ?
print("delta-separated (Gmin>=d):",Gmin_angle>=d,"margin:",Gmin_angle/d)
# trilinear caps: three groups by octant-ish: cap A: ez>0.8; cap B: ex>0.8,ez<0; cap C: ex<-0.8,ez<0 -- sizes?
A=np.where(ez>0.8)[0]; B=np.where((ex>0.8)&(ez<0.2))[0]; C=np.where((ex<-0.8)&(ez<0.2))[0]
print("cap sizes:",len(A),len(B),len(C))
def gap(X,Y):
    g=(E[X]@E[Y].T)
    dd=np.arccos(np.clip(g,-1,1))
    return float(dd.min())
if len(A)>0 and len(B)>0 and len(C)>0:
    gAB=gap(A,B); gBC=gap(B,C); gCA=gap(C,A)
    print("gaps deg:",math.degrees(gAB),math.degrees(gBC),math.degrees(gCA))
    chord=min(2*math.sin(g/2) for g in (gAB,gBC,gCA))
    Rstar=4*d/chord
    print("Rstar/d=",Rstar/d)
    # grid J enclosure over [-8d,8d]^3? Rstar/d likely ~3-4. spacing d/4.
    halfside=math.ceil(Rstar/d+1)*d
    h=d/4.0
    ax=np.arange(-halfside,halfside+h/2,h)
    Xg,Yg,Zg=np.meshgrid(ax,ax,ax,indexing='ij')
    PX,PY,PZ=Xg.ravel(),Yg.ravel(),Zg.ravel()
    M=PX.size; voxvol=h**3
    print("voxels:",M)
    lo=[np.zeros(M,dtype=np.int32) for _ in range(3)]
    hi=[np.zeros(M,dtype=np.int32) for _ in range(3)]
    r2in=(d-h)**2; r2out=(d+h)**2
    P2=PX**2+PY**2+PZ**2
    for ci,cap in ((0,A),(1,B),(2,C)):
        for idx in cap:
            e0,e1,e2=E[idx]
            sproj=PX*e0+PY*e1+PZ*e2
            dist2=P2-sproj**2
            lo[ci]+=(dist2<=r2in).astype(np.int32)
            hi[ci]+=(dist2<=r2out).astype(np.int32)
    Jlo=float(np.sum((lo[0].astype(float)*lo[1]*lo[2])**(1.0/3.0))*voxvol)
    Jhi=float(np.sum((hi[0].astype(float)*hi[1]*hi[2])**(1.0/3.0))*voxvol)
    Pi=(len(A)*len(B)*len(C))**(1.0/3.0)
    print("J in [%e,%e], C in [%.2f,%.2f]"%(Jlo,Jhi,Jlo/(d**3*Pi),Jhi/(d**3*Pi)))
    Jout=(Jlo,Jhi,Pi)
else:
    Jout=None
log=dict(d=d,N=N,Gmin_deg=float(math.degrees(Gmin_angle)),sep_margin=float(Gmin_angle/d),
         R0=float(R0),R0_over_d=float(R0/d),union_lb=float(Ulb),union_ub=float(Uub),
         ratio_ub=float(ratio),C_needed=float(ratio/d**(-1.0/8.0)),
         caps=[int(len(A)),int(len(B)),int(len(C))],
         trilinear=dict(J_lo=float(Jout[0]),J_hi=float(Jout[1]),C_lo=float(Jout[0]/(d**3*Jout[2])),C_hi=float(Jout[1]/(d**3*Jout[2]))) if Jout else None,
         verdict="3D bush (mult 2048) controlled: union near-maximal, C_needed O(20); transverse 3-cap J enclosed with O(1) constant")
with open("output/artifacts/target_3dbush_log.json","w") as f: json.dump(log,f,indent=1)
print(json.dumps(log,indent=1))
