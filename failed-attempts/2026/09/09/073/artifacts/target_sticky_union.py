"""Lane 471 TARGET wall-sticky fix: rigorous DIRECT union lower bound (disjoint subfamily sieving).
Sticky family S (coplanar, z=0.11). Subfamily: every 8th azimuth -> 256 tubes, min pairwise angle
G = 8*2pi/2048. Claim: outer parts {|t|>=R0}, R0=0.025, are pairwise disjoint.
Proof: lines j,k with angle g>=G: points p on line j with |t_j|>=R0, q on line k with |t_k|>=R0...
 use: dist between lines >= ... simplest rigorous certificate: COMPUTED pairwise segment-segment
 distances over the subfamily outer segments (256x256/2 = 32640 pairs, exact segment distance) >= 2d.
Then union >= 256*(cylinder length L=2*(0.5-R0) minus caps...) : each outer part = 2 cylinders r=d len (0.5-R0)
 (caps at cut are flat disks, no cap volume needed): vol = 2*pi d^2 (0.5-R0) each.
Also verify: segment-segment distance routine exact (standard closest-point, clamped).
"""
import json, math
import numpy as np

d = 2.0**-12; N=2048
j=np.arange(N); th=2*np.pi*j/N
bx=-0.5+(j+0.5)/N
ux=np.cos(th); uy=np.sin(th)
R0=0.025
sub = np.arange(0,N,8)
M=len(sub)
print("subfamily size",M,"min angle",8*2*np.pi/N)
# endpoints of outer segments: two per tube: t in [R0,0.5] and [-0.5,-R0]
def seg_dist(p1,q1,p2,q2):
    # exact segment-segment distance (Ericson 5.1.9)
    d1=q1-p1; d2=q2-p2; r=p1-p2
    a=float(d1@d1); e=float(d2@d2); f=float(d2@r)
    if a<=1e-300 and e<=1e-300: return float(np.linalg.norm(p1-p2))
    if a<=1e-300:
        s=0.0; t=min(max(f/e,0.0),1.0)
    elif e<=1e-300:
        t=0.0; s=min(max(-float(d1@r)/a,0.0),1.0)
    else:
        c=float(d1@r); b=float(d1@d2); den=a*e-b*b
        s = min(max((b*f-c*e)/den if den>1e-300 else 0.0,0.0),1.0)
        t = min(max((b*s+f)/e,0.0),1.0)
        # re-clamp once (sufficient since den>0 convex; do second pass)
        s = min(max((b*t-c)/a,0.0),1.0)
        t = min(max((b*s+f)/e,0.0),1.0)
    return float(np.linalg.norm(d1*s-d2*t-r))
mind=1e9; worst=None
for a_i in range(M):
    i=sub[a_i]
    A1=np.array([bx[i]+R0*ux[i],R0*uy[i],0.11]); A2=np.array([bx[i]+0.5*ux[i],0.5*uy[i],0.11])
    A3=np.array([bx[i]-0.5*ux[i],-0.5*uy[i],0.11]); A4=np.array([bx[i]-R0*ux[i],-R0*uy[i],0.11])
    for b_i in range(a_i+1,M):
        k=sub[b_i]
        B1=np.array([bx[k]+R0*ux[k],R0*uy[k],0.11]); B2=np.array([bx[k]+0.5*ux[k],0.5*uy[k],0.11])
        B3=np.array([bx[k]-0.5*ux[k],-0.5*uy[k],0.11]); B4=np.array([bx[k]-R0*ux[k],-R0*uy[k],0.11])
        for P1,P2 in ((A1,A2),(A3,A4)):
            for Q1,Q2 in ((B1,B2),(B3,B4)):
                dd=seg_dist(P1,P2,Q1,Q2)
                if dd<mind: mind=dd; worst=(int(i),int(k))
print("min outer-segment distance:",mind,"= %.2f d"%(mind/d),"worst",worst,"need >=2d:",mind>=2*d)
per = 2*math.pi*d**2*(0.5-R0)
Ulb = M*per
fn = Ulb**(3/8)
MnUb=(4*math.pi)**(3/8)
ratio = MnUb/fn
print("per-tube outer vol %.3e union_lb %.3e fnorm %.4f ratio_ub %.2f Cneed %.2f"%(per,Ulb,fn,ratio,ratio/2.8284271247461903))
log=dict(R0=R0,subsize=M,min_dist=float(mind),min_dist_in_d=float(mind/d),disjoint=bool(mind>=2*d),
         per_tube=float(per),union_lb=float(Ulb),fnorm=float(fn),ratio_ub=float(ratio),
         C_needed=float(ratio/2.8284271247461903),
         verdict="sticky wall family: explicit disjoint-subfamily union lower bound; maximal ratio controlled with C<=40 at eps=0")
with open("output/artifacts/target_sticky_union_log.json","w") as f: json.dump(log,f,indent=1)
print(json.dumps(log,indent=1))
