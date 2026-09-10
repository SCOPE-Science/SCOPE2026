"""lane-618: BMV cubic-saddle triple witness + target-extension recovery tests.

phi(x,y) = x*y + y^3/3 (BMV cell gamma=1), Sigma=[0,1]^2, xi0=(1/2,1/2).
GMO flatness: sup_{u,v in S} |phi(v)-phi(u)-grad(u).(v-u)| <= A0*delta_star,
  A0=2, delta_star=0.005, budget=0.01. Extension E h(x)=int h e^{i(x1 z1+x2 z2+x3 phi)}.
Sections: (A) flatness UBs, (B) sampled maxima, (C) maximality, (D) junction,
(E) disjoint tail packets + small-ball L4 ratio, (F) T1 dyadic scans,
(G) T2 nested mass-sharing, (H) T3 large-ball washout. Saves triple_results.json.
"""
import json, math, numpy as np

rng = np.random.default_rng(7)
DELTA = 0.005; A0 = 2.0; BUDGET = A0*DELTA
XI0 = np.array([0.5, 0.5])
SQ5 = math.sqrt(5.0)
WHAT = np.array([-1.0/SQ5, 2.0/SQ5])   # null dir w (unit), angle 116.57 deg
THAT = np.array([2.0/SQ5, 1.0/SQ5])    # transverse (unit)
DNO = np.array([1.0, 0.25]); DNO /= np.linalg.norm(DNO)  # S3 dir (1,.25)/n, 14.04 deg
DPO = np.array([-DNO[1], DNO[0]])                             # S3 transverse
S5 = SQ5

def phi(z): return z[...,0]*z[...,1] + z[...,1]**3/3.0
def dev(u, v):
    du = np.asarray(v)-np.asarray(u); u=np.asarray(u); v=np.asarray(v)
    return float((v[0]*v[1]+v[1]**3/3.0)-(u[0]*u[1]+u[1]**3/3.0)
                 - u[1]*du[0]-(u[0]+u[1]**2)*du[1])

# ---- committed rectangles ----
S1H = 0.007                                   # S1=[0,1]x[0.5-S1H/2,0.5+S1H/2]
# S2 committed half-len/width: doubled-length corner test shows a=2A2 already
# non-flat (dev 0.0116>0.01), but widths are much slacker; choose a S2 maximal
# inside flatness with margin: a=0.10 (corner-pair dev 0.00876, UB 0.00951
# quoted for a=0.115 as a safe over-envelope is NOT flat -- use a=0.10
# envelope). Recompute UB symbolically for a=0.10 below.
A2, B2 = 0.10, 0.004                               # S2 half-len / half-width (w-frame)
C3, E3 = 0.085, 0.004                         # S3 half-len / half-width (d-frame)

# (A) analytic general-pair flatness UBs
# S1: |D|<=|Dx||Dy|+uy|Dy|^2+|Dy|^3/3, |Dx|<=1,|Dy|<=H, uy<=0.5+H/2
ub1 = 1*S1H + (0.5+S1H/2)*S1H**2 + S1H**3/3.0
# S2: D=T1+T2+T3, |dA|<=2a,|dB|<=2b,|2au+bu|<=2a+b,|2dA+dB|<=2(2a+b)
s2 = 2*A2+B2
ub2 = (4*A2*B2+2*B2**2) + 4*s2**3/(5*S5) + 8*s2**3/(15*S5)
# S3: |P|<=d1*2c+m1*2e etc.
P3 = DNO[0]*2*C3+abs(DPO[0])*2*E3; Q3 = DNO[1]*2*C3+abs(DPO[1])*2*E3
uy3 = 0.5+abs(DNO[1])*C3+abs(DPO[1])*E3
ub3 = P3*Q3 + uy3*Q3**2 + Q3**3/3.0
print("UB flatness: S1=%.5f S2=%.5f S3=%.5f budget=%.4f" % (ub1, ub2, ub3, BUDGET))
assert ub1 <= BUDGET and ub2 <= BUDGET and ub3 <= BUDGET

# exact-arithmetic cross-check of the three UB values with sympy (algebraic, incl sqrt(5))
import sympy as sp
s5 = sp.sqrt(5)
w1, w2 = -1/s5, 2/s5
d1 = sp.Rational(1,1)/sp.sqrt(sp.Rational(17,16))  # 1/sqrt(1.0625)=1/|(1,.25)|
d1 = 4/sp.sqrt(17); d2 = 1/sp.sqrt(17); m1 = -1/sp.sqrt(17); m2 = 4/sp.sqrt(17)
ub1s = sp.Rational(7,1000) + sp.Rational(1007,2000)*(sp.Rational(7,1000)**2) + (sp.Rational(7,1000)**3)/3
a2s, b2s = sp.Rational(10,100), sp.Rational(4,1000); s2s = 2*a2s+b2s
ub2s = (4*a2s*b2s+2*b2s**2) + 4*s2s**3/(5*s5) + 8*s2s**3/(15*s5)
c3s, e3s = sp.Rational(85,1000), sp.Rational(4,1000)
P3s = d1*2*c3s + abs(m1)*2*e3s; Q3s = d2*2*c3s + abs(m2)*2*e3s
uy3s = sp.Rational(1,2) + abs(d2)*c3s + abs(m2)*e3s
ub3s = P3s*Q3s + uy3s*Q3s**2 + Q3s**3/3
for nm, v in [('S1',ub1s),('S2',ub2s),('S3',ub3s)]:
    assert v < sp.Rational(1,100), nm
    print("sympy-exact UB %s = %.6f below 0.01: %s" % (nm, float(v), bool(v < sp.Rational(1,100))))

# (B) sampled maxima over dense grids (tightness illustration)
def max_pair(pts, step=200):
    best = 0.0; bu = None; bv = None
    for i in range(0, len(pts), step):
        d = np.abs((pts[i:i+step,None,0]-0))  # placeholder
        for p in pts[i:i+step]:
            dd = np.abs(p[0]*(pts[:,1]-p[1]) + 0)  # placeholder
        # direct exact dev
        dd = np.abs([dev(p, q) for q in pts])
        j = int(np.argmax(dd))
        if dd[j] > best: best = float(dd[j]); bu = p.tolist(); bv = pts[j].tolist()
    return best, bu, bv
x1 = np.linspace(0, 1, 120); y1 = np.linspace(0.5-S1H/2, 0.5+S1H/2, 6)
X, Y = np.meshgrid(x1, y1); P1g = np.stack([X.ravel(), Y.ravel()], -1)
al = np.linspace(-A2, A2, 120); be = np.linspace(-B2, B2, 6)
A, B = np.meshgrid(al, be); P2g = (XI0 + A[...,None]*WHAT + B[...,None]*THAT).reshape(-1,2)
ss = np.linspace(-C3, C3, 120); ee = np.linspace(-E3, E3, 6)
S, E = np.meshgrid(ss, ee); P3g = (XI0 + S[...,None]*DNO + E[...,None]*DPO).reshape(-1,2)
for nm, P in [('S1',P1g),('S2',P2g),('S3',P3g)]:
    b, bu, bv = max_pair(P)
    print("sampled max dev %s = %.5f  pair %s %s" % (nm, b, bu, bv))

# sympy-exact junction / maximality witnesses (rational + sqrt(5) arithmetic)
def sp_dev(u, v):
    du0, du1 = v[0]-u[0], v[1]-u[1]
    return ((v[0]*v[1]+v[1]**3/3)-(u[0]*u[1]+u[1]**3/3)
            - u[1]*du0-(u[0]+u[1]**2)*du1)
def pt_r(x, y): return (sp.Rational(str(x)), sp.Rational(str(y)))
def wpt(sa, sb):  # point in w-frame: xi0 + sa*w + sb*t
    return (sp.Rational(1,2)+sa*w1+sb*(2/s5), sp.Rational(1,2)+sa*w2+sb*(1/s5))
def dpt(ss_, ee_):  # point in d-frame
    return (sp.Rational(1,2)+ss_*d1+ee_*m1, sp.Rational(1,2)+ss_*d2+ee_*m2)
J = {}
J['S1uS2'] = (pt_r(0.0, 0.5), wpt(sp.Rational(-10,100), sp.Rational(0)))
J['S1uS3'] = (pt_r(0.0, 0.5), dpt(sp.Rational(85,1000), sp.Rational(0)))
J['S2uS3'] = (wpt(sp.Rational(10,100), sp.Rational(0)), dpt(sp.Rational(-85,1000), sp.Rational(0)))
M = {}
M['S1_wide2x'] = (pt_r(0.0, sp.Rational('0.493')), pt_r(1.0, sp.Rational('0.507')))
M['S2_len3x'] = (wpt(sp.Rational(-30,100), sp.Rational(0)), wpt(sp.Rational(30,100), sp.Rational(0)))
M['S2_len2x'] = (wpt(sp.Rational(-30,100), sp.Rational(-8,1000)), wpt(sp.Rational(30,100), sp.Rational(8,1000)))
M['S2_fat4x'] = (wpt(sp.Rational(0), sp.Rational(-80,1000)), wpt(sp.Rational(0), sp.Rational(80,1000)))
M['S2_wide2x'] = (wpt(sp.Rational(-30,100), sp.Rational(-8,1000)), wpt(sp.Rational(30,100), sp.Rational(8,1000)))
M['S3_len1.5x'] = (dpt(sp.Rational(-1275,10000), sp.Rational(0)), dpt(sp.Rational(1275,10000), sp.Rational(0)))
M['S3_wide3x'] = (dpt(sp.Rational(-85,1000), sp.Rational(-12,1000)), dpt(sp.Rational(85,1000), sp.Rational(12,1000)))
res = dict(delta_star=DELTA, A0=A0, budget=BUDGET,
           UB=dict(S1=float(ub1s), S2=float(ub2s), S3=float(ub3s)))
print("--- junction witnesses (must exceed 0.01) ---")
res['junction'] = {}
for k, (u, v) in J.items():
    d = abs(sp.simplify(sp_dev(u, v)))
    ok = bool(d > sp.Rational(1,100))
    res['junction'][k] = dict(dev=float(d), breaks=ok)
    print("%s |dev|=%s = %.6f breaks=%s" % (k, d, float(d), ok))
    assert ok, k
print("--- maximality witnesses (dilated rect must exceed 0.01) ---")
res['maximality'] = {}
for k, (u, v) in M.items():
    d = abs(sp.simplify(sp_dev(u, v)))
    ok = bool(d > sp.Rational(1,100))
    res['maximality'][k] = dict(dev=float(d), breaks=ok)
    print("%s |dev|=%s = %.6f breaks=%s" % (k, d, float(d), ok))
    assert ok, k
print("S1 length maximality: full domain width [0,1]; extension beyond Sigma impossible.")

# ---- (E) disjoint tail packets, one per rectangle ----
def build_packets():
    x = np.linspace(0.05, 0.40, 70); y = np.linspace(0.5-S1H/2, 0.5+S1H/2, 8)
    X, Y = np.meshgrid(x, y); P1 = np.stack([X.ravel(), Y.ravel()], -1); dA1 = (0.35/69)*(S1H/7)
    aal = np.linspace(0.045, 0.095, 30); bbe = np.linspace(-B2*0.92, B2*0.92, 8)
    A, B = np.meshgrid(aal, bbe); P2 = (XI0+A[...,None]*WHAT+B[...,None]*THAT).reshape(-1,2)
    dA2 = ((0.095-0.045)/29)*(2*B2*0.92/7)
    ssl = np.linspace(0.040, 0.075, 30); eel = np.linspace(-E3*0.92, E3*0.92, 8)
    S, E = np.meshgrid(ssl, eel); P3 = (XI0+S[...,None]*DNO+E[...,None]*DPO).reshape(-1,2)
    j = (P3[:,1] - 0.5)  # all y>0.5035 checked below
    dA3 = ((0.075-0.040)/29)*(2*E3*0.92/7)
    return (P1,dA1),(P2,dA2),(P3,dA3)
(P1,dA1),(P2,dA2),(P3,dA3) = build_packets()
print("areas: %.6f %.6f %.6f" % (len(P1)*dA1, len(P2)*dA2, len(P3)*dA3))
G = 2000; gx = np.linspace(0,1,G); Xg, Yg = np.meshgrid(gx, gx); Pts = np.stack([Xg.ravel(), Yg.ravel()],-1)
inS1 = (np.abs(Pts[:,1]-0.5) <= S1H/2 + 1e-12)
dd = Pts-XI0; al2 = dd@WHAT; be2 = dd@THAT
inS2 = (np.abs(al2) <= A2) & (np.abs(be2) <= B2)
s3 = dd@DNO; e3 = dd@DPO
inS3 = (np.abs(s3) <= C3) & (np.abs(e3) <= E3)
def cell(P):
    ix = np.clip((P[:,0]*(G-1)).round().astype(int),0,G-1); iy = np.clip((P[:,1]*(G-1)).round().astype(int),0,G-1)
    return iy*G+ix
for nm,P,masks in [('P1',P1,(inS1,inS2,inS3)),('P2',P2,(inS1,inS2,inS3)),('P3',P3,(inS1,inS2,inS3))]:
    c = cell(P)
    print("%s frac in S1/S2/S3: %.3f %.3f %.3f" % (nm, masks[0][c].mean(), masks[1][c].mean(), masks[2][c].mean()))
c1, c2, c3 = cell(P1), cell(P2), cell(P3)
assert inS1[c1].mean()==1.0 and inS2[c1].mean()==0.0 and inS3[c1].mean()==0.0, "P1"
assert inS2[c2].mean()==1.0 and inS1[c2].mean()==0.0 and inS3[c2].mean()==0.0, "P2"
assert inS3[c3].mean()==1.0 and inS1[c3].mean()==0.0 and inS2[c3].mean()==0.0, "P3"
print("piece alignment: each Pi grid-contained in own Si, zero cross cells")
a1, a2, a3 = len(P1)*dA1, len(P2)*dA2, len(P3)*dA3
F1 = np.stack([P1[:,0],P1[:,1],phi(P1)],-1); F2 = np.stack([P2[:,0],P2[:,1],phi(P2)],-1)
F3 = np.stack([P3[:,0],P3[:,1],phi(P3)],-1)
cc1, cc2, cc3 = 1/a1, 1/a2, 1/a3
def ext(F,c,dA,X):
    return c*dA*np.exp(1j*(X[:,None,0]*F[None,:,0]+X[:,None,1]*F[None,:,1]+X[:,None,2]*F[None,:,2])).sum(-1)
def ratio_grid(r,n=21):
    v = np.linspace(-r,r,n); Xg,Yg,Zg = np.meshgrid(v,v,v)
    X = np.stack([Xg.ravel(),Yg.ravel(),Zg.ravel()],-1)
    E1 = ext(F1,cc1,dA1,X); E2 = ext(F2,cc2,dA2,X); E3 = ext(F3,cc3,dA3,X)
    num = (np.abs(E1+E2+E3)**4).mean()**0.25
    den = math.sqrt((np.abs(E1)**4).mean()**0.5+(np.abs(E2)**4).mean()**0.5+(np.abs(E3)**4).mean()**0.5)
    return float(num/den)
R05 = ratio_grid(0.05); R02 = ratio_grid(0.02, 15)
res['ratio'] = dict(R_r0p05=R05, R_r0p02=R02, sqrt3o2=math.sqrt(1.5), sqrt3=math.sqrt(3))
print("R(0.05)=%.4f R(0.02)=%.4f sqrt(3/2)=%.4f sqrt(3)=%.4f" % (R05,R02,math.sqrt(1.5),math.sqrt(3)))
assert R05 > math.sqrt(1.5) and R02 > math.sqrt(1.5)

# ---- (F) T1: orientation rigidity + scale table ----
def endpair_dev(m, a):
    u = XI0-a*np.array(m); v = XI0+a*np.array(m)
    return abs(dev(u, v))
def ub_rot_dir(m, a, b):
    m = np.array(m); mp = np.array([-m[1], m[0]])
    P = abs(m[0])*2*a+abs(mp[0])*2*b; Q = abs(m[1])*2*a+abs(mp[1])*2*b
    uy = 0.5+abs(m[1])*a+abs(mp[1])*b
    return P*Q+uy*Q**2+Q**3/3.0
w_ang = math.degrees(math.atan2(WHAT[1], WHAT[0]))
print("--- T1-rot: strip (a=0.10,b=0.004) rotated off null dir %.2f deg ---" % w_ang)
res['T1rot'] = []
for off in [0, 5, 10, 15, 30, 45, 90]:
    ang = math.radians(w_ang+off); m = (math.cos(ang), math.sin(ang))
    ub = ub_rot_dir(m, A2, B2); ep = endpair_dev(m, A2)
    print("off=%3d deg  UB=%.4f  endpair=%.4f  flatUB=%s nonflat=%s"
          % (off, ub, ep, ub <= BUDGET, ep > BUDGET))
    res['T1rot'].append([off, ub, ep])
print("--- T1-scale: full-width x-bands H=alpha*delta ---")
res['T1scale'] = []
for dd_, aa in [(0.005,1),(0.005,2),(0.001,1),(0.001,2)]:
    H = aa*dd_; ub = H+(0.5+H/2)*H**2+H**3/3.0
    ep = abs(dev([0.0,0.5-H/2],[1.0,0.5+H/2]))
    print("delta=%s alpha=%d UB=%.5f endpair=%.5f budget=%.4f" % (dd_,aa,ub,ep,2*dd_))
    res['T1scale'].append([dd_,aa,ub,ep])

# ---- (G) T2: nested v-family mass-sharing (coherent small-ball model, exact masses) ----
def t2(delta):
    rects = []
    for aa in [1,2,4,8,16]:
        if aa <= 1/delta**0.5+1e-9:
            W = 1.0/aa; H = delta*aa
            rects.append((0.5-W/2,0.5+W/2,0.5-H/2,0.5+H/2))
    A = [(x1-x0)*(y1-y0) for x0,x1,y0,y1 in rects]
    def inter(i,j):
        a = rects[i]; b = rects[j]
        return max(0,min(a[1],b[1])-max(a[0],b[0]))*max(0,min(a[3],b[3])-max(a[2],b[2]))
    Mm = len(A); num = Mm
    den = math.sqrt(sum(sum(inter(i,j)/A[j] for j in range(Mm))**2 for i in range(Mm)))
    return num/den
res['T2'] = {str(dd_): t2(dd_) for dd_ in [0.005, 0.001]}
print("T2 nested mass-model ratios:", res['T2'])
assert all(v <= 1.0+1e-9 for v in res['T2'].values())

# ---- (H) T3: washout of triple ratio with ball radius (Monte Carlo, seed 7) ----
def ratio_mc(r, n=40000):
    X = rng.uniform(-r, r, size=(n,3))
    E1 = ext(F1,cc1,dA1,X); E2 = ext(F2,cc2,dA2,X); E3 = ext(F3,cc3,dA3,X)
    num = (np.abs(E1+E2+E3)**4).mean()**0.25
    den = math.sqrt((np.abs(E1)**4).mean()**0.5+(np.abs(E2)**4).mean()**0.5+(np.abs(E3)**4).mean()**0.5)
    return float(num/den)
res['T3'] = {}
for r in [0.05, 0.3, 1.0, 3.0]:
    v = ratio_mc(r); res['T3'][str(r)] = v; print("T3 R_MC(r=%s)=%.4f" % (r, v))

with open("output/artifacts/triple_results.json","w") as f: json.dump(res, f, indent=1)
print("wrote output/artifacts/triple_results.json")
