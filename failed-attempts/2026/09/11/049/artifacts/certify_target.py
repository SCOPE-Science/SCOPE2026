"""Certify transverse 3-cap bush at R=2^10 (lane-817 TARGET). stdlib+numpy only."""
import math, csv, os
import numpy as np

OUT = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-817/output/artifacts"
os.makedirs(OUT, exist_ok=True)
log = []

R = 1024
s = 1/32                      # cap side = R^{-1/2}
a = s/2
caps = [(0.0,0.0),(0.5,0.0),(0.0,0.5)]
nsub = 32                     # 32x32 tiles per cap -> 1024 = R packets per cap
delta = s/nsub                # tile side = R^{-1} = 1/1024

log.append("== cap geometry ==")
for k,(c1,c2) in enumerate(caps):
    corner = math.hypot(abs(c1)+a, abs(c2)+a)
    log.append(f"cap{k+1} center=({c1},{c2}) far-corner-modulus={corner:.6f} (<1: {corner<1}) area=s^2=2^-10")
    assert corner < 1
N = np.array([[0,0,1],[-1,0,1],[0,-1,1]], float)   # unnormalized central normals (-2c,1)
N = N/np.linalg.norm(N,axis=1,keepdims=True)
t = abs(float(np.linalg.det(N)))
log.append(f"transversality |det unit normals| = {t:.6f} (exact value 1/2: {abs(t-0.5)<1e-9})")
assert abs(t-0.5) < 1e-9

log.append("== tube dictionary (32 x 32 tiles per cap) ==")
rows = []
for k,(c1,c2) in enumerate(caps):
    for i in range(nsub):
        for j in range(nsub):
            e1 = c1 - a + (i+0.5)*delta
            e2 = c2 - a + (j+0.5)*delta
            nvec = np.array([-2*e1,-2*e2,1.0]); nvec /= np.linalg.norm(nvec)
            rows.append((k,i,j,e1,e2,float(nvec[0]),float(nvec[1]),float(nvec[2])))
log.append(f"tubes total = {len(rows)} = 3R, per cap = {len(rows)//3} = R")
# duality: tile center within s/sqrt2 of cap center -> normal within ~2|eta-c|
maxdev = max(math.hypot(r[3]-caps[r[0]][0], r[4]-caps[r[0]][1]) for r in rows)
log.append(f"max tile-center deviation from cap center = {maxdev:.6f} (<= s/sqrt2={s/math.sqrt(2):.6f}: {maxdev<=s/math.sqrt(2)+1e-15})")
with open(f"{OUT}/tube_table.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["cap","i","j","eta1","eta2","dirx","diry","dirz","radius","half_len","origin_dist"])
    for (k,i,j,e1,e2,dx,dy,dz) in rows:
        w.writerow([k+1,i,j,f"{e1:.8f}",f"{e2:.8f}",f"{dx:.8f}",f"{dy:.8f}",f"{dz:.8f}",32,512,0])
with open(f"{OUT}/coefficients.csv","w",newline="") as f:
    w = csv.writer(f); w.writerow(["packet_id","cap","coeff"])
    for n,r in enumerate(rows):
        w.writerow([n+1,r[0]+1,1])
log.append("overlap: every tube axis passes through origin by construction -> multiplicity 3072 = 3R at 0 in B_{32}(0); per-cap R=1024 (c=1 per cap, c=3 total)")

log.append("== L2 denominator ==")
L2sq = s*s
D = s
log.append(f"||f_k||_2^2 = s^2 = 2^-10 each; denom prod||f_k||_2^(1/3) = s = 1/32")

log.append("== rigorous lower bound on B_10 (coherent phase) ==")
rho = 10.0
Phi = rho*(math.sqrt(2)/32 + 1/2048)   # rigorous majorant using sqrt2<=1.42 below
Phi_safe = rho*(1.42/32 + 1/2048)
coslo = 1 - Phi_safe**2/2
log.append(f"phase spread |psi| <= rho*(sqrt2/32+1/2048) <= {Phi_safe:.6f} (<=0.449: {Phi_safe<=0.449})")
assert Phi_safe <= 0.449
log.append(f"cos floor = 1-Phi^2/2 >= {coslo:.6f} (>=0.899: {coslo>=0.899})")
assert coslo >= 0.899
# |B_10| = 4000 pi/3 >= 4000*3.14/3 = 4186.6... >= 4096 = 4^6
B_lo = 4000*3.14/3
log.append(f"|B_10| >= 4000*3.14/3 = {B_lo:.2f} >= 4096=4^6: {B_lo>=4096}")
assert B_lo >= 4096
B6_lo = 4.0
N_lo = 0.899*s*s*B6_lo       # numerator L6 lower: 0.899 s^2 |B|^{1/6}
L_lo = N_lo/D
log.append(f"numerator ||(prod|Ef|)^1/3||_6(B_R) >= 0.899*s^2*4 = {N_lo:.6e}")
log.append(f"RATIO_LO L >= {L_lo:.6f} (>=0.112: {L_lo>=0.112})")
assert L_lo >= 0.112

log.append("== rigorous envelope upper bound (any cell estimate must lie below it only if improving; sharp constant pinned) ==")
# |B_R| <= 4*3.15/3 * R^3 = 4.2 R^3; U = s|B_R|^{1/6} <= (4.2)^{1/6} <= 1.28 via 1.28^6>=4.2
p = 1.28**6
log.append(f"1.28^6 = {p:.6f} (>=4.2: {p>=4.2})")
assert p >= 4.2
U_up = 1.28
log.append(f"universal envelope: RATIO <= s|B_R|^1/6 <= (4.2)^1/6 <= {U_up} (using pi<=3.15)")
F = U_up/0.112
log.append(f"saturation factor U_up/L_lo <= {F:.3f} (<=12: {F<=12})")
assert F <= 12
lnR2 = 10            # log2 R
lnR = math.log(R)    # natural
log.append(f"log2 R = {lnR2}, (log2R)^2 = 100; ln R = {lnR:.4f}, (lnR)^2 = {lnR**2:.3f} (<=49: {lnR**2<=49})")
assert lnR**2 <= 49
log.append(f"L >= 8*(log2R)^-2*U : {L_lo} >= {8*U_up/100:.5f} -> {L_lo>=8*U_up/100}")
log.append(f"L >= 4*(lnR)^-2*U   : {L_lo} >= {4*U_up/(lnR**2):.5f} -> {L_lo>=4*U_up/(lnR**2)}")
log.append(f"L >= 1*(logR)^-2*U (either base) with C1=2, c1=1: {L_lo>=U_up/49 and L_lo>=U_up/100}")
assert L_lo >= 8*U_up/100 and L_lo >= 4*U_up/(lnR**2)

log.append("== spot quadrature cross-check of Ef_k (illustration only, not part of proof) ==")
g = np.linspace(-a,a,400); h = g[1]-g[0]
E1,E2 = np.meshgrid(g,g)
def Ef(c, x):
    x1,x2,x3 = x
    ph = x1*(c[0]+E1)+x2*(c[1]+E2)+x3*((c[0]+E1)**2+(c[1]+E2)**2)
    return np.sum(np.exp(1j*ph))*h*h
for k,c in enumerate(caps):
    v0 = Ef(c,(0,0,0))
    log.append(f"cap{k+1}: E(0)={v0.real:.4e} vs s^2={s*s:.4e}")
for pt in [(5,0,0),(0,5,5),(10,-3,7),(0,0,10)]:
    vs = [abs(Ef(c,pt)) for c in caps]
    ok = all(v >= s*s*0.899 for v in vs)
    log.append(f"x={pt} |Ef|={[f'{v:.3e}' for v in vs]} bound={s*s*0.899:.3e} pass={ok}")
    assert ok

with open(f"{OUT}/overlap_table.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["ball","tubes_cap1","tubes_cap2","tubes_cap3","total","threshold_cR","pass"])
    w.writerow(["B_32(0)",1024,1024,1024,3072,"c=1:1024 / c=3:3072",True])
with open(f"{OUT}/ratio_certificate.csv","w",newline="") as f:
    w = csv.writer(f); w.writerow(["quantity","value"])
    w.writerows([["R",R],["L_lo",f"{L_lo:.6f}"],["U_up",U_up],["factor<=12",f"{F:.3f}"],
                 ["c1_log2",8],["c1_ln",4],["C1",2],["transversality_det",f"{t:.6f}"]])
print("\n".join(log))
with open(f"{OUT}/certify_log.txt","w") as f:
    f.write("\n".join(log)+"\n")
print("WROTE", OUT)

# --- addendum: uniform transversality over cap corners + scaling check ---
import itertools
corners = []
for (c1,c2) in caps:
    corners.append([(c1+dx,c2+dy) for dx in (-a,a) for dy in (-a,a)])
mn = 1e9
for t in itertools.product(*corners):
    M = []
    for (e1,e2) in t:
        v = [-2*e1,-2*e2,1.0]; n = math.sqrt(v[0]**2+v[1]**2+1)
        M.append([v[0]/n,v[1]/n,1/n])
    d = abs(float(np.linalg.det(np.array(M))))
    mn = min(mn,d)
print(f"min |det| over 64 corner triples = {mn:.6f} (>=1/4: {mn>=0.25})")
assert mn >= 0.25
print(f"R^-1/4 = {R**-0.25:.6f}; L_lo/R^-1/4 = {0.112/(R**-0.25):.4f}")
