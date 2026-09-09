"""Lane 471 TARGET cell test: deg-4 Ham-sandwich-type partition vs Wolff hairbrush at delta0=2^-12.
Checks: separation, disjointness/volume, sharpness constant, cell loads, wall fraction,
Bezout (<=4 hits/line), trilinear J=0 certificate, single-scale maximal ratio.
Stdlib + numpy only. Writes target_cell_log.json.
"""
import json, math
import numpy as np

delta0 = 2.0**-12
N = 2048
p0 = 8.0/3.0

# --- 1. direction separation (analytic cert + numeric) ---
# adjacent chord = 2 sin(pi/N); analytic lower bound via sin>=y-y^3/6, pi>3.14159265
y0 = 3.14159265 / N
low_chord = 2.0*(y0 - y0**3/6.0)
sep_ok = low_chord > delta0
ratio = (2*math.sin(math.pi/N))/delta0

# numeric directions
j = np.arange(N)
th = 2*np.pi*j/N
ux, uy = np.cos(th), np.sin(th)
zj = -0.5 + (j+0.5)/N  # base heights, spacing 1/N = 2*delta0
spacing = 1.0/N
disjoint_ok = spacing >= 2*delta0 - 1e-18  # line gap >= sum of radii

# union volume (exact cylinders + caps; tangencies null)
tube_vol = math.pi*delta0**2*1.0 + (4.0/3.0)*math.pi*delta0**3
union_vol = N*tube_vol

# --- 2. sharpness constant at p0 (analytic) ---
c_star = (4.0/3.0)*(3.0**(3.0/8.0))

# --- 3. degree-4 partition: 4 planes general position ---
# l1=x-0.13, l2=y+0.07, l3=z-0.11, l4=x+y+1.3z-0.21
offs = np.array([0.13, -0.07, 0.11, 0.21])
n4norm = math.sqrt(1+1+1.69)
norms = np.array([1.0,1.0,1.0,n4norm])

S = 129
t = np.linspace(-0.5,0.5,S)
# spine array (N,S,3): x = t*ux, y = t*uy, z = zj
X = t[None,:]*ux[:,None]
Y = t[None,:]*uy[:,None]
Z = np.broadcast_to(zj[:,None], (N,S))
L1 = X-0.13; L2 = Y+0.07; L3 = Z-0.11; L4 = X+Y+1.3*Z-0.21
A = np.stack([L1,L2,L3,L4],axis=-1)  # (N,S,4)
dist = np.abs(A)/norms[None,None,:]
mind = dist.min(axis=-1)  # (N,S)
wall_mask = mind <= delta0
wall_frac = float(wall_mask.mean())
n_wall_pts = int(wall_mask.sum())

# cell assignment for non-wall pts: sign vector
sgn = np.sign(A)  # -1,0,1
# encode nonzero patterns of non-wall pts
nonwall = ~wall_mask
pats = set()
cell_of = np.zeros((N,S),dtype=np.int32)
pat_to_id = {}
for s in range(S):
    col = sgn[:,s,:]
    w = wall_mask[:,s]
    for i in range(N):
        if w[i]:
            cell_of[i,s]=-1
        else:
            key = (1 if col[i,0]>0 else -1,1 if col[i,1]>0 else -1,1 if col[i,2]>0 else -1,1 if col[i,3]>0 else -1)
            pats.add(key)
            if key not in pat_to_id:
                pat_to_id[key]=len(pat_to_id)
            cell_of[i,s]=pat_to_id[key]
n_cells = len(pats)

# per-tube: #distinct cells visited, #wall hits, transitions (Bezout check: line meets Z<=4 -> cells<=5)
per_tube_cells = []
per_tube_trans = []
bezout_ok = True
for i in range(N):
    seq = cell_of[i,:]
    seqnw = seq[seq>=0]
    uniq = set(seqnw.tolist())
    per_tube_cells.append(len(uniq))
    # count sign changes of each linear form along spine (proxy for Z crossings)
    ch = 0
    for k in range(4):
        v = A[i,:,k]
        ch += int(np.sum(v[:-1]*v[1:]<0))
    per_tube_trans.append(ch)
    if len(uniq)>5 or ch>4:
        bezout_ok=False
max_cells_per_tube = max(per_tube_cells)
max_cross = max(per_tube_trans)

# per-cell loads: #tubes meeting cell, spine-mass pts per cell
nC = n_cells
tubes_per_cell = [0]*nC
pts_per_cell = [0]*nC
for c in range(nC):
    M = (cell_of==c)
    pts_per_cell[c]=int(M.sum())
    tubes_per_cell[c]=int((M.sum(axis=1)>0).sum())
total_incidences = sum(tubes_per_cell)
avg_load = total_incidences/max(nC,1)

# good cell: max tubes
good = max(tubes_per_cell) if tubes_per_cell else 0

# --- 4. trilinear J certificate ---
# Planary disjointness => any triple intersection empty => J=0 exactly (analytic).
# Numeric cross-check on coarse voxel grid: voxel size delta0, bbox [-1,1]^2 x [-0.6,0.6];
# paint tube centers? Use spine-point occupancy per third as proxy + report max triple overlap 0.
third = N//3
G1 = set(); G2=set(); G3=set()
def vox(x,y,z):
    return (round(x/delta0),round(y/delta0),round(z/delta0))
# subsample every 8th spine pt for speed
for i in range(0,third,1):
    for s in range(0,S,8):
        G1.add(vox(float(X[i,s]),float(Y[i,s]),float(Z[i,s])))
for i in range(third,2*third,1):
    for s in range(0,S,8):
        G2.add(vox(float(X[i,s]),float(Y[i,s]),float(Z[i,s])))
for i in range(2*third,N,1):
    for s in range(0,S,8):
        G3.add(vox(float(X[i,s]),float(Y[i,s]),float(Z[i,s])))
triple_proxy = len(G1&G2&G3)

log = dict(
  delta0=delta0, N=N, p0=p0, conj_exp=1/8,
  sep_analytic_low=float(low_chord), sep_ok=bool(sep_ok), sep_ratio=float(ratio),
  spacing=float(spacing), disjoint_ok=bool(disjoint_ok),
  tube_vol=float(tube_vol), union_vol=float(union_vol),
  sharp_const_cstar=float(c_star),
  degree=4, n_planes=4, n_cells=int(n_cells), expect_cells=15,
  wall_frac=float(wall_frac), n_wall_pts=int(n_wall_pts),
  total_spine_pts=int(N*S),
  max_cells_per_tube=int(max_cells_per_tube), max_crossings=int(max_cross),
  bezout_ok=bool(bezout_ok),
  total_incidences=int(total_incidences), avg_load=float(avg_load),
  good_cell_tubes=int(good),
  tubes_per_cell=sorted(tubes_per_cell,reverse=True),
  pts_per_cell=sorted(pts_per_cell,reverse=True),
  trilinear_J_exact=0, triple_voxel_proxy=int(triple_proxy),
  counts_note="line meets deg-4 Z in <=4 pts (no centerline contained: checked analytically), so <=5 cells/tube",
)
with open("output/artifacts/target_cell_log.json","w") as f:
    json.dump(log,f,indent=1)
print(json.dumps({k:v for k,v in log.items() if k not in ("tubes_per_cell","pts_per_cell")},indent=1))
print("tubes_per_cell desc:",log["tubes_per_cell"])
print("pts_per_cell desc:",log["pts_per_cell"])
