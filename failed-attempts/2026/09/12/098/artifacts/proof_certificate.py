"""Proof certificate numerics for lane-1320 (midpoint-retraction Dirac integrator).
Uses only numpy. Produces output/artifacts/results.json with certified numbers.

Scheme D_h (midpoint-retraction Dirac = RATTLE-mid), M=I:
  (P) q+ = q + h p - (h^2/2) F + h G0^T L,   g(q+) = 0,   G0 = Gforce(q)
  (V) p+ = (q+-q)/h - (h/2) F + G1^T M2,     G1 p+ = 0,   G1 = Gforce(q+)
Constraint rows stay g(q+)=0 with exact Jacobian G(q+) in Newton; only the
force/projection matrices G0,G1 are rescaled (G -> T G). This is exactly what
"replacing the constraint Jacobian" means; invariance follows from
range((TG)^T) = range(G^T).
"""
import numpy as np, json, math

G_GRAV = 9.81
F = np.array([0., G_GRAV, 0., G_GRAV])

def Gmat(q):
    x1, y1, x2, y2 = q
    dx, dy = x2 - x1, y2 - y1
    return np.array([[2*x1, 2*y1, 0., 0.],
                     [-2*dx, -2*dy, 2*dx, 2*dy]])

def gvec(q):
    x1, y1, x2, y2 = q
    return np.array([x1*x1 + y1*y1 - 1., (x2-x1)**2 + (y2-y1)**2 - 1.])

def lam_cont(q, p):
    G = Gmat(q)
    A = G @ G.T
    w = np.array([2*np.dot(p[:2], p[:2]), 2*np.dot(p[2:]-p[:2], p[2:]-p[:2])])
    return np.linalg.solve(A, G @ F - w)

def angles_to_state(th1, ph, w1, w2):
    q1 = np.array([math.sin(th1), -math.cos(th1)])
    d = np.array([math.sin(ph), -math.cos(ph)])
    q2 = q1 + d
    t1 = np.array([math.cos(th1), math.sin(th1)])
    t2 = np.array([math.cos(ph), math.sin(ph)])
    p1 = w1 * t1
    p2 = p1 + w2 * t2
    return np.concatenate([q1, q2]), np.concatenate([p1, p2])

def energy(q, p):
    return 0.5*np.dot(p, p) + G_GRAV*(q[1]+q[3])

def Dstep(q, p, h, Gforce=None, tol=1e-14, maxit=25):
    Gf = Gforce if Gforce is not None else Gmat
    G0 = Gf(q)
    qp = q + h*p
    Lam = np.zeros(2)
    for it in range(maxit):
        r1 = qp - q - h*p + 0.5*h*h*F - h*(G0.T @ Lam)
        r2 = gvec(qp)
        if max(np.linalg.norm(r1), np.linalg.norm(r2)) < tol:
            break
        J = np.zeros((6, 6)); J[:4, :4] = np.eye(4); J[:4, 4:] = -h*G0.T; J[4:, :4] = Gmat(qp)
        d = np.linalg.solve(J, -np.concatenate([r1, r2]))
        qp = qp + d[:4]; Lam = Lam + d[4:]
    else:
        return None
    if max(np.linalg.norm(qp-q-h*p+0.5*h*h*F-h*(G0.T@Lam)), np.linalg.norm(gvec(qp))) > 1e-11:
        return None
    v = (qp - q)/h
    G1 = Gf(qp)
    Lam2 = np.linalg.solve(G1 @ G1.T, -(G1 @ (v - 0.5*h*F)))
    return qp, v - 0.5*h*F + G1.T @ Lam2, it

# ---------------- 0. datum ----------------
th1 = ph = math.pi/3; w1 = w2 = 1.5
q0, p0 = angles_to_state(th1, ph, w1, w2)
H0 = energy(q0, p0)
eta0 = lam_cont(q0, p0)
print("datum H =", H0, " eta =", eta0)
assert -12 <= H0 <= -8 and abs(w1) <= 2 and abs(w2) <= 2
assert np.linalg.norm(gvec(q0)) < 1e-15 and np.linalg.norm(Gmat(q0)@p0) < 1e-15

# ---------------- 1. uniform linear-algebra + contraction bounds ----------------
rng = np.random.default_rng(0)
worst_det = 1e9; worst_smin = 1e9
for _ in range(4000):
    a = rng.uniform(0, 2*math.pi); b = rng.uniform(0, 2*math.pi)
    q, _ = angles_to_state(a, b, 0., 0.)
    A = Gmat(q) @ Gmat(q).T
    ev = np.linalg.eigvalsh(A)
    worst_det = min(worst_det, np.linalg.det(A)); worst_smin = min(worst_smin, ev[0])
print("min det(GG^T) =", worst_det, " min eig =", worst_smin)
assert worst_det >= 16 - 1e-9
nG, nF, P, CQ, Ainv = 3.465, 13.874, 4.473, 2.237, 0.75
hmax, R = 0.005, 100.0
dmax = hmax*P + hmax*hmax*(nG*R + nF/2)
inner = P + hmax*(nG*R + nF/2)
selfmap = Ainv*(0.5*nG*nF + CQ*inner*inner)
Lip = Ainv*CQ*2*dmax*nG
print("R=%g dmax=%.6f selfmap=%.4f Lip=%.4f" % (R, dmax, selfmap, Lip))
assert selfmap <= R and Lip < 1
Pp = 3.5
wmax = math.sqrt(2*(2*Pp*Pp)**2)
lammax = Ainv*(nG*nF + wmax)
B2 = nF + nG*lammax
print("wmax=%.3f lammax=%.3f B2=%.3f drift=%.4f" % (wmax, lammax, B2, hmax*B2))
assert hmax*B2 <= 1.5
nGd = 6.929
Adot = 2*nGd*nG
wdot = math.sqrt((4*Pp*B2)**2 + (4*Pp*2*B2)**2)
lamdot = Ainv*(Adot*lammax + nGd*nF + wdot)
B3 = nGd*lammax + nG*lamdot
Cq = B3/6.0
print("lamdot=%.1f B3=%.1f Cq=%.1f" % (lamdot, B3, Cq))

# ---------------- 2. well-definedness sweep ----------------
grid = []
for a in np.linspace(0.3, 2.6, 6):
    for b in np.linspace(0.3, 2.6, 6):
        for o1 in (-1.8, -0.7, 0.7, 1.8):
            for o2 in (-1.8, -0.7, 0.7, 1.8):
                q, p = angles_to_state(a, b, o1, o2)
                H = energy(q, p)
                if -12 <= H <= -8:
                    grid.append((q, p))
print("sweep data count =", len(grid))
sweep_ok = True; maxit_seen = 0
for h in (0.005, 0.0025, 0.001, 1e-4):
    for (q, p) in grid:
        r = Dstep(q, p, h)
        if r is None: sweep_ok = False; print("FAIL", h); break
        maxit_seen = max(maxit_seen, r[2])
    else: continue
    break
print("sweep ok =", sweep_ok, " max Newton iters =", maxit_seen)
assert sweep_ok

# ---------------- 3. exact preservation (long run) ----------------
q, p = q0.copy(), p0.copy(); h = 0.005
maxg = maxv = 0.0; E0 = energy(q, p); maxE = 0.0
for _ in range(2000):
    q, p, _ = Dstep(q, p, h)
    maxg = max(maxg, np.linalg.norm(gvec(q)))
    maxv = max(maxv, np.linalg.norm(Gmat(q) @ p))
    maxE = max(maxE, abs(energy(q, p)-E0))
print("2000 steps: max|g|=%.2e max|Gp|=%.2e max|dE|=%.3e" % (maxg, maxv, maxE))
assert maxg < 1e-12 and maxv < 1e-12

# ---------------- 4. representation independence ----------------
Tconst = np.diag([2.0, 1.0])
def Gtilde1(q): return Tconst @ Gmat(q)
def T2mat(q):
    x1, y1, x2, y2 = q
    return np.array([[1+0.3*math.sin(x1), 0.2], [0.0, 1+0.3*math.cos(y2)]])
def Gtilde2(q): return T2mat(q) @ Gmat(q)
inv_res = {}
for Gf, nm in ((Gtilde1, "diag(2,1)"), (Gtilde2, "q-dep")):
    qa, pa = q0.copy(), p0.copy(); qb, pb = q0.copy(), p0.copy()
    md = 0.0
    for _ in range(200):
        qa, pa, _ = Dstep(qa, pa, 0.002)
        r = Dstep(qb, pb, 0.002, Gforce=Gf)
        assert r is not None, nm
        qb, pb, _ = r
        md = max(md, np.linalg.norm(qa-qb), np.linalg.norm(pa-pb))
    print("invariance max diff [%s] = %.2e" % (nm, md))
    assert md < 1e-9
    inv_res[nm] = md

# ---------------- 5. naive scheme representation dependence ----------------
def Nstep(q, p, h, Tmat, eta):
    Gt = Tmat @ Gmat(q)
    return q + h*p - 0.5*h*h*F + 0.5*h*h*(Gt.T @ eta)
h = 0.005
pred = 0.5*h*h*(Gmat(q0).T @ ((Tconst.T - np.eye(2)) @ eta0))
num = Nstep(q0, p0, h, Tconst, eta0) - Nstep(q0, p0, h, np.eye(2), eta0)
print("naive predicted diff =", np.linalg.norm(pred), " numeric =", np.linalg.norm(num))
assert np.linalg.norm(pred) > 1e-4 and abs(np.linalg.norm(num)-np.linalg.norm(pred)) < 1e-12
def state_of(z):
    return angles_to_state(z[0], z[1], z[2], z[3])
z0 = np.array([th1, ph, w1, w2])
eps = 1e-6; Leta = 0.0
e0 = lam_cont(*state_of(z0))[0]
for i in range(4):
    dz = np.zeros(4); dz[i] = eps
    e1 = lam_cont(*state_of(z0+dz))[0]
    Leta = max(Leta, abs(e1-e0)/eps)
print("eta1(z0) =", e0, " Leta ~", Leta)
rbox = abs(e0)/(2*Leta)
hw = 0.02; n = 3
mn = 1e9; Hlo = 1e9; Hhi = -1e9
pts = [np.linspace(z0[i]-hw, z0[i]+hw, n) for i in range(4)]
mesh = math.sqrt(sum(((2*hw/(n-1)))**2 for _ in range(4)))
for a in pts[0]:
    for b in pts[1]:
        for o1 in pts[2]:
            for o2 in pts[3]:
                q, p = angles_to_state(a, b, o1, o2)
                H = energy(q, p)
                Hlo = min(Hlo, H); Hhi = max(Hhi, H)
                if not (-12 <= H <= -8): continue
                mn = min(mn, abs(lam_cont(q, p)[0]))
mn_cert = mn - Leta*mesh
print("box halfwidth=%.4f mesh=%.4f min|eta1|=%.4f certified=%.4f Hrange=[%.3f,%.3f]"
      % (hw, mesh, mn, mn_cert, Hlo, Hhi))
assert mn_cert > 0 and Hlo >= -12 and Hhi <= -8
# |G^T e1| = 2|q1| = 2, diff = (h^2/2)|eta1|*2 = h^2|eta1|
naive_gap = h*h*mn_cert
print("certified naive one-step gap at h=0.005: %.3e" % naive_gap)
assert naive_gap > 0

# ---------------- 6. order tests (independent projected-RK4 reference) ----------------
def rk4_proj(q, p, H):
    def acc(qq, pp): return -F + Gmat(qq).T @ lam_cont(qq, pp)
    k1q = p; k1p = acc(q, p)
    k2q = p+0.5*H*k1p; k2p = acc(q+0.5*H*k1q, p+0.5*H*k1p)
    k3q = p+0.5*H*k2p; k3p = acc(q+0.5*H*k2q, p+0.5*H*k2p)
    k4q = p+H*k3p; k4p = acc(q+H*k3q, p+H*k3p)
    qn = q + H/6*(k1q+2*k2q+2*k3q+k4q); pn = p + H/6*(k1p+2*k2p+2*k3p+k4p)
    for _ in range(3):
        G = Gmat(qn); d = np.linalg.solve(G@G.T, -gvec(qn)); qn = qn + G.T @ d
    G = Gmat(qn); d = np.linalg.solve(G@G.T, -(G@pn)); pn = pn + G.T @ d
    return qn, pn
def ref_flow(q, p, T, H=1e-4):
    n = int(round(T/H))
    for _ in range(n): q, p = rk4_proj(q, p, H)
    return q, p
qr, pr = ref_flow(q0, p0, 0.5)
print("ref constraint: %.1e %.1e" % (np.linalg.norm(gvec(qr)), np.linalg.norm(Gmat(qr)@pr)))
hs = [0.005, 0.0025, 0.00125, 0.000625]
errs = []
for h in hs:
    q, p = q0.copy(), p0.copy(); n = int(round(0.5/h))
    for _ in range(n):
        q, p, _ = Dstep(q, p, h)
    errs.append(max(np.linalg.norm(q-qr), np.linalg.norm(p-pr)))
print("global errs:", errs)
slopes = [math.log(errs[i]/errs[i+1])/math.log(hs[i]/hs[i+1]) for i in range(3)]
print("global slopes:", slopes)
assert all(1.8 < s < 2.2 for s in slopes)
loc = []
for h in (0.005, 0.0025, 0.00125):
    q1, p1, _ = Dstep(q0, p0, h)
    qe, pe = ref_flow(q0, p0, h, H=h/400)
    loc.append(max(np.linalg.norm(q1-qe), np.linalg.norm(p1-pe)))
print("local errs:", loc)
lslope = [math.log(loc[i]/loc[i+1])/math.log(2) for i in range(2)]
print("local slopes:", lslope)
assert all(2.7 < s < 3.3 for s in lslope)

res = dict(
    H0=H0, eta1=float(e0), min_det=float(worst_det), min_eig=float(worst_smin),
    R=R, selfmap=selfmap, Lip=Lip, lammax=lammax, B2=B2, B3=B3, Cq=Cq,
    sweep_ok=sweep_ok, max_newton=int(maxit_seen),
    maxg=maxg, maxv=maxv, maxE=maxE,
    invariance={k: float(v) for k, v in inv_res.items()},
    global_errs=errs, global_slopes=slopes, local_errs=loc, local_slopes=lslope,
    box_halfwidth=hw, min_eta1=float(mn), certified_eta1=float(mn_cert),
    Hbox=[Hlo, Hhi], naive_gap=float(naive_gap), Leta=float(Leta),
)
with open("output/artifacts/results.json", "w") as f:
    json.dump(res, f, indent=1)
print("WROTE output/artifacts/results.json")
