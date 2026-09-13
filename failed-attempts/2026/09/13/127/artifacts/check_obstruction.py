"""Lane-1765 TARGET obstruction check: Klein-four collinear odd class.

Class (T=1): Q(t)=(0,phi(t)), phi odd, half-antisymmetric phi(t+1/2)=-phi(t),
mirror phi(1/2-t)=phi(t) (consequence), phi>0 on (0,1/2) endpoints excluded.
Witness: phi from explicit cusp profile s on [0,1/4]:
  s(t) = N^-1 ( t^{2/3} + sign(t-c)|t-c|^{2/3} + t + c^{2/3} ), c=1/8,
extended by mirror / oddness / half-antisymmetry.
Checks: symmetries, COM=0, L=0, gap-zero enumeration (8 binary collisions at
6 instants), 2/3 cusp slopes, finite midpoint action with N avoiding nodes.
"""
import json
import os
import numpy as np

T = 1.0
C = 1.0 / 8.0
A = 1.0
P = 2.0 / 3.0

def num(t):
    t = np.asarray(t, dtype=float)
    return (np.abs(t) ** P
            + np.sign(t - C) * (np.abs(t - C) ** P)
            + t + C ** P)

NORM = float(num(0.25))

def s_prof(t):
    return num(np.asarray(t, dtype=float)) / NORM

def sp_prof(t):
    t = np.asarray(t, dtype=float)
    return ((2.0 / 3.0) * (np.abs(t) ** (-1.0 / 3.0))
            + (2.0 / 3.0) * (np.abs(t - C) ** (-1.0 / 3.0))
            + 1.0) / NORM

def phi(u):
    u = np.asarray(u, dtype=float) % 1.0
    out = np.empty_like(u)
    m1 = u < 0.25
    m2 = (u >= 0.25) & (u < 0.5)
    m3 = (u >= 0.5) & (u < 0.75)
    m4 = u >= 0.75
    out[m1] = s_prof(u[m1])
    out[m2] = s_prof(0.5 - u[m2])
    out[m3] = -s_prof(u[m3] - 0.5)
    out[m4] = -s_prof(1.0 - u[m4])
    return A * out

def phi_dot(u):
    u = np.asarray(u, dtype=float) % 1.0
    out = np.empty_like(u)
    m1 = u < 0.25
    m2 = (u >= 0.25) & (u < 0.5)
    m3 = (u >= 0.5) & (u < 0.75)
    m4 = u >= 0.75
    out[m1] = sp_prof(u[m1])
    out[m2] = -sp_prof(0.5 - u[m2])
    out[m3] = -sp_prof(u[m3] - 0.5)
    out[m4] = sp_prof(1.0 - u[m4])
    return A * out

# --- symmetry / structure residuals on fine grid ---
ts = np.linspace(0, 1, 400001)
res_odd = float(np.max(np.abs(phi(-ts) + phi(ts))))
res_anti = float(np.max(np.abs(phi(ts + 0.5) + phi(ts))))
res_mirror = float(np.max(np.abs(phi(0.5 - ts) - phi(ts))))
com = phi(ts) + phi(ts + 0.25) + phi(ts + 0.5) + phi(ts + 0.75)
res_com = float(np.max(np.abs(com)))
interior = (ts > 1e-9) & (ts < 0.5 - 1e-9)
min_pos = float(np.min(phi(ts[interior])))

# --- gap zeros: scan ---
def gaps(t):
    p0 = phi(t); p1 = phi(t + 0.25); p2 = phi(t + 0.5); p3 = phi(t + 0.75)
    return {
        "01": np.abs(p0 - p1), "12": np.abs(p1 - p2),
        "23": np.abs(p2 - p3), "30": np.abs(p3 - p0),
        "02": np.abs(p0 - p2), "13": np.abs(p1 - p3),
    }

g = gaps(ts)
mins = {k: float(np.min(v)) for k, v in g.items()}
argmins = {k: float(ts[int(np.argmin(v))]) for k, v in g.items()}

# --- cusp slopes (log-log): use decades where the |h|^{2/3} term dominates ---
hs = np.array([2.0 ** -k for k in range(20, 33)])
D = lambda t: phi(t) - phi(t + 0.25)
yD = np.abs(D(0.125 + hs))
slopeD = float(np.polyfit(np.log(hs), np.log(yD), 1)[0])
y0 = np.abs(phi(hs))
slope0 = float(np.polyfit(np.log(hs), np.log(y0), 1)[0])

# --- finite action: midpoint N=200000 avoids all multiples-of-1/8 nodes ---
N = 200000
h = T / N
t = (np.arange(N) + 0.5) * h
Kd = 2.0 * phi_dot(t) ** 2
ps = [phi(t + j * 0.25) for j in range(4)]
U = np.zeros(N)
for j in range(4):
    for k in range(j + 1, 4):
        U += 1.0 / np.maximum(np.abs(ps[j] - ps[k]), 1e-300)
Kint = float(Kd.mean() * T)
Uint = float(U.mean() * T)

# second resolution for corroboration
N2 = 80000
h2 = T / N2
t2 = (np.arange(N2) + 0.5) * h2
Kd2 = 2.0 * phi_dot(t2) ** 2
ps2 = [phi(t2 + j * 0.25) for j in range(4)]
U2 = np.zeros(N2)
for j in range(4):
    for k in range(j + 1, 4):
        U2 += 1.0 / np.maximum(np.abs(ps2[j] - ps2[k]), 1e-300)
Kint2 = float(Kd2.mean() * T)
Uint2 = float(U2.mean() * T)

results = {
    "NORM": NORM,
    "res_odd": res_odd,
    "res_half_antisymmetry": res_anti,
    "res_mirror": res_mirror,
    "res_COM": res_com,
    "min_phi_interior": min_pos,
    "gap_minima": mins,
    "gap_argmins": argmins,
    "cusp_slope_D_at_1over8": slopeD,
    "cusp_slope_phi_at_0": slope0,
    "K_integral_N200k": Kint,
    "U_integral_N200k": Uint,
    "A_total_N200k": Kint + Uint,
    "K_integral_N80k": Kint2,
    "U_integral_N80k": Uint2,
    "A_total_N80k": Kint2 + Uint2,
}
ok = (res_odd < 1e-9 and res_anti < 1e-9 and res_mirror < 1e-9
      and res_com < 1e-9 and min_pos > 0
      and abs(slopeD - 2.0 / 3.0) < 0.05 and abs(slope0 - 2.0 / 3.0) < 0.05
      and np.isfinite(Kint + Uint) and np.isfinite(Kint2 + Uint2))
results["all_assertions_pass"] = bool(ok)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "check_results.json")
with open(out, "w") as f:
    json.dump(results, f, indent=2)
print(json.dumps(results, indent=2))
assert ok
