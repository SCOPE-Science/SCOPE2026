"""T1/T2/T3: quantitative ingredients for single-pair log-stability route (numpy only)."""
import numpy as np, json

out = {}

# ============ T1: Poisson extension of fixed quarter-arc bump ============
M = 65536
th = np.linspace(-np.pi, np.pi, M, endpoint=False)
t = 4*th/np.pi
psi = np.zeros_like(th)
m = np.abs(t) < 1
psi[m] = np.exp(1 - 1/(1 - t[m]**2))   # smooth bump, max 1 at th=0, supp |th|<pi/4
F = np.fft.rfft(psi)                    # F[n] = sum_j psi_j e^{-2pi i n j/M}
N = 400
narr = np.arange(N+1)
cpos = ((-1)**narr) * F[:N+1] / M       # c_n for n>=0
print("tail |c_N| =", abs(cpos[N]), " c0 =", cpos[0].real)

G = 401
xs = np.linspace(-1, 1, G)
XX, YY = np.meshgrid(xs, xs)
Z = XX + 1j*YY
R = np.abs(Z); TH = np.angle(Z)
admis = R <= 0.8                        # vertices >=0.2 from boundary

# u = c0 + sum_{n>=1} 2 Re(c_n z^n); f'(z) = sum 2 n c_n z^{n-1}
Fp = np.zeros_like(Z)
P = np.ones_like(Z)                     # z^{n-1}
for nn in range(1, N+1):
    Fp += 2*nn*cpos[nn]*P
    P *= Z
ux = Fp.real; uy = -Fp.imag
g = np.hypot(ux, uy)
ga = g[admis]
print("T1: min|grad| on r<=0.8 =", ga.min(), " max =", ga.max())
imin = np.argmax(admis.ravel() & (g.ravel() == ga.min()))
iy, ix = np.unravel_index(np.argmin(np.where(admis, g, np.inf)), g.shape)
print("T1: argmin at x,y =", xs[ix], xs[iy])
out["T1"] = {"min_grad": float(ga.min()), "max_grad": float(ga.max()),
             "argmin_xy": [float(xs[ix]), float(xs[iy])],
             "tail_cN": float(abs(cpos[N])), "c0": float(cpos[0].real)}

# winding of grad field around argmin (critical-point certificate attempt)
x0, y0 = xs[ix], xs[iy]
radii = [0.05, 0.1, 0.2]
for rr in radii:
    an = np.linspace(0, 2*np.pi, 361)
    zx = x0 + rr*np.cos(an); zy = y0 + rr*np.sin(an)
    zz = zx + 1j*zy
    inside = np.abs(zz) < 0.999
    fz = np.zeros_like(zz)
    pw = np.ones_like(zz)
    for nn in range(1, N+1):
        fz += 2*nn*cpos[nn]*pw
        pw *= zz
    vx, vy = fz.real, fz.imag * -1
    ang = np.unwrap(np.arctan2(vy, vx))
    print(f"T1 winding r={rr}: total change = {ang[-1]-ang[0]:.4f}, "
          f"min|g| on circle = {np.hypot(vx,vy)[inside].min():.3e}")

# values along symmetry axis y=0
xax = np.linspace(-0.8, 0.8, 9)
za = xax + 0j
fa = np.zeros_like(za, dtype=complex)
pw = np.ones_like(za, dtype=complex)
for nn in range(1, N+1):
    fa += 2*nn*cpos[nn]*pw
    pw *= za
print("T1 axis ux:", np.round(fa.real, 5))

# ============ T3: sensitivity dynamic range ============
g2 = g[admis]**2
print("T3: max|g|^2/min|g|^2 =", g2.max()/g2.min())
out["T3"] = {"sens_ratio": float(g2.max()/g2.min())}

# ============ T2: transmission singularity exponent, 90-deg corner ============
def first_exponent(k, Nn):
    h = 2*np.pi/Nn
    thg = (np.arange(Nn)+0.5)*h          # cell centers
    # inclusion sector |angle|<pi/4 (opening pi/2); map to [0,2pi)
    a = (thg + np.pi) % (2*np.pi) - np.pi
    sig = np.where(np.abs(a) < np.pi/4, k, 1.0)
    # edge values
    the = np.arange(Nn)*h
    ae = (the + np.pi) % (2*np.pi) - np.pi
    sige = np.where(np.abs(ae) < np.pi/4, k, 1.0)
    A = np.zeros((Nn, Nn))
    for i in range(Nn):
        A[i, i] = (sige[(i+1) % Nn] + sige[i])/h**2
        A[i, (i+1) % Nn] = -sige[(i+1) % Nn]/h**2
        A[i, (i-1) % Nn] = -sige[i]/h**2
    Minv = np.diag(1.0/sig)
    E = Minv @ A
    w = np.linalg.eigvals(E)
    w = np.sort(w.real)
    # smallest positive above tolerance
    pos = w[w > 1e-8]
    return float(np.sqrt(pos[0])), float(np.sqrt(pos[1]))

for k in [0.2, 0.5, 2.0, 3.0, 4.0, 10.0]:
    lams = [first_exponent(k, Nn) for Nn in (300, 600)]
    print(f"T2 k={k}: lam1 (N=300,600) = {lams[0][0]:.6f}, {lams[1][0]:.6f}  "
          f"lam2 = {lams[0][1]:.6f}, {lams[1][1]:.6f}")
    out[f"T2_k_{k}"] = {"lam1_N300": lams[0][0], "lam1_N600": lams[1][0]}

with open("t1t2t3_results.json", "w") as f:
    json.dump(out, f, indent=1)
print("saved t1t2t3_results.json")
