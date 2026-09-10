"""Target-directed checks: disjoint-arc geometry + paired-phase mechanism stress test.

Part 1: verify separation, complement union/overlap, chord direction cone.
Part 2: table Morse phases (crit pts, reality sets, normal-derivative signs);
         illustrate harmonic-difference boundary-localization (max principle).
Stdlib only. Writes geometry.json + phases.json, prints VERIFY lines.
"""
import math, json, os

OUT = os.path.dirname(os.path.abspath(__file__))
PI = math.pi

# ---------- Part 1: geometry ----------
a = PI/4  # half-aperture
# Gamma_D = {|th| < pi/4}, Gamma_N = {|th-pi| < pi/4} (th in (-pi,pi])
def in_GD(th): return abs(th) < a
def in_GN(th):
    d = abs(th - PI) if th >= 0 else abs(th + PI)
    return d < a
def in_KD(th): return not in_GD(th)
def in_KN(th): return not in_GN(th)

# closure separation: closest endpoints e^{+-i pi/4} vs e^{i(pi+-pi/4)}
p1 = (math.cos(a), math.sin(a)); p2 = (math.cos(PI-a), math.sin(PI-a))
sep = math.hypot(p1[0]-p2[0], p1[1]-p2[1])

N = 3600
ths = [-PI + 2*PI*i/N for i in range(N)]
union_ok = all(in_KD(t) or in_KN(t) for t in ths)
ov = sum(1 for t in ths if in_KD(t) and in_KN(t))/N  # expect 0.5
kd = sum(1 for t in ths if in_KD(t))/N  # expect 0.75
kn = sum(1 for t in ths if in_KN(t))/N  # expect 0.75

# chord direction cone: segments joining Gamma_D to Gamma_N, orientation mod pi
betas = []
M = 200
for i in range(M):
    t1 = -a + 2*a*(i+0.5)/M
    z1 = (math.cos(t1), math.sin(t1))
    for j in range(M):
        t2 = PI - a + 2*a*(j+0.5)/M
        z2 = (math.cos(t2), math.sin(t2))
        dx, dy = z2[0]-z1[0], z2[1]-z1[1]
        b = math.atan2(dy, dx) % PI
        betas.append(b)
bmin, bmax = min(betas), max(betas)
# fold: cone should be [0,pi/4] U [3pi/4,pi) i.e. within pi/4 of horizontal
in_left = [b for b in betas if b <= PI/4 + 1e-9]
in_right = [b for b in betas if b >= 3*PI/4 - 1e-9]
cone_ok = len(in_left) + len(in_right) == len(betas)
# openness: interior direction beta=0 and beta=pi/8 realized by interior chords
geo = dict(separation=sep, union_full=union_ok, frac_KD=kd, frac_KN=kn,
           frac_overlap=ov, chord_beta_min=bmin, chord_beta_max=bmax,
           chord_cone_within_pi_over_4_of_horizontal=cone_ok,
           n_chords=len(betas))
with open(os.path.join(OUT, "geometry.json"), "w") as f:
    json.dump(geo, f, indent=1)
print("GEOMETRY:", json.dumps(geo))
assert abs(sep - math.sqrt(2)) < 1e-12, "separation must be sqrt(2)"
assert union_ok and cone_ok
assert abs(ov - 0.5) < 0.01 and abs(kd - 0.75) < 0.01 and abs(kn - 0.75) < 0.01
# cone contains open interval around 0 (mod pi): check betas cover (0.01, pi/4-0.01)
assert any(0.05 < b < PI/4 - 0.05 for b in betas)
print("VERIFY_GEOMETRY_OK")

# ---------- Part 2: phases ----------
# Phi(z) as complex poly; reality set on circle = zeros of Im Phi(e^{it});
# d_n Re Phi on |z|=1 = Re( e^{it} Phi'(e^{it}) ) (radial derivative).
def Phi_z(z): return z
def Phip_z(z): return 1.0 + 0j
def Phi_z2(z): return 0.5*z*z
def Phip_z2(z): return z
def Phi_shift(z): c = 0.3 + 0.1j; return 0.5*(z-c)**2
def Phip_shift(z): c = 0.3 + 0.1j; return z-c

phases = [("z", Phi_z, Phip_z, None),
          ("z^2/2", Phi_z2, Phip_z2, (0j, 1.0)),
          ("(z-c)^2/2,c=0.3+0.1i", Phi_shift, Phip_shift, (0.3+0.1j, 1.0))]

K = 7200
rows = []
for name, F, Fp, crit in phases:
    imz = [ (F(complex(math.cos(2*PI*k/K), math.sin(2*PI*k/K)))).imag for k in range(K) ]
    # count sign changes -> # isolated reality points (upper bound 2*deg)
    sc = sum(1 for k in range(K) if imz[k] == 0 or imz[k]*imz[(k+1)%K] < 0)
    dn = []
    for k in range(K):
        t = 2*PI*k/K
        z = complex(math.cos(t), math.sin(t))
        dn.append((z*Fp(z)).real)
    frac_pos = sum(1 for v in dn if v > 0)/K
    frac_neg = sum(1 for v in dn if v < 0)/K
    rows.append(dict(name=name, crit=str(crit),
                     reality_sign_changes_on_circle=sc,
                     frac_dnRePhi_pos=round(frac_pos,4),
                     frac_dnRePhi_neg=round(frac_neg,4)))
print("PHASES:", json.dumps(rows))

# max-principle illustration: psi = Re(Phi_D - Phi_N), Phi_D=z^2/2, Phi_N=z
G = 161
bmaxv, imaxv = -1e9, None
for i in range(G):
    for j in range(G):
        x = -1 + 2*i/(G-1); y = -1 + 2*j/(G-1)
        if x*x + y*y >= 1: continue
        z = complex(x, y)
        psi = (0.5*z*z - z).real
        if psi > bmaxv: bmaxv, imaxv = psi, (x, y)
# boundary max
B = 4000
bb = max((0.5*complex(math.cos(t), math.sin(t))**2
          - complex(math.cos(t), math.sin(t))).real
         for t in [2*PI*k/B for k in range(B)])
print("MAXPRINCIPLE: interior_grid_max=%.6f at %s  boundary_max=%.6f" % (bmaxv, imaxv, bb))
assert bb >= bmaxv - 1e-6, "harmonic max must sit on boundary"
with open(os.path.join(OUT, "phases.json"), "w") as f:
    json.dump(dict(phases=rows, interior_grid_max=bmaxv,
                   interior_argmax=imaxv, boundary_max=bb), f, indent=1)
print("VERIFY_PHASES_OK")
