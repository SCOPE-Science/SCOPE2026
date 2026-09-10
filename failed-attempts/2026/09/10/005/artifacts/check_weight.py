"""Target step 3: harmonic-difference Carleman weight proposal.

Weight varphi(z) = Re(Phi_D(z) - Phi_N(z)) = 2*sum_{odd n} c_n Re(z^n)
with c from phases3 (NTR=64). Verify on grid:
 (a) no interior critical point: |grad varphi| = |Phi_D'-Phi_N'| > 0 on D grid;
 (b) normal derivative d_n varphi = Re(z(Phi_D'(z)-Phi_N'(z))) > 0 on K_D cap K_N
     overlap (length pi: top+bottom arcs), < 0 on Gamma_D U Gamma_N (length pi);
 (c) index-style sign table on all four boundary quarter-blocks.
Writes weight.json. Prints VERIFY lines.
"""
import math, json, os
import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__))
A = math.pi/4
NTR = 64
exec(open(os.path.join(OUT, "check_phases3.py")).read().split("# strict-sign check")[0].split("c = a")[1].splitlines()[0] and "/dev/null" or "/dev/null") if False else None
# rebuild c quickly (same construction, no prints)
def smootherstep(v):
    v = min(1.0, max(0.0, v)); return 6*v**5-15*v**4+10*v**3
def h_raw(t):
    g = abs((t+math.pi) % (2*math.pi)-math.pi)
    return -3.0+4.0*smootherstep(((g-A)/0.12+1.0)/2.0)
KQ = 60000
tq = np.linspace(-math.pi, math.pi, KQ, endpoint=False)
hv = np.array([h_raw(t) for t in tq]); mu = float(np.mean(hv))
hh = hv-mu
a = np.zeros(NTR+1)
for n in range(NTR+1):
    f = 2.0 if n > 0 else 1.0
    a[n] = f*float(np.mean(hh*np.cos(n*tq)))
c = a/np.maximum(np.arange(NTR+1), 1); c[0] = 0.0

def Wp(z):  # d/dz varphi-complex = Phi_D'(z) - Phi_N'(z), Phi_N(z)=Phi_D(-z)
    dp = sum(n*c[n]*z**(n-1) for n in range(1, NTR+1))
    dn = sum(n*c[n]*(-z)**(n-1)*(-1) for n in range(1, NTR+1))
    return dp-dn

# (a) interior min |grad varphi| = |Wp| on fine interior grid
G = 321
mg, marg = 1e9, None
for i in range(G):
    for j in range(G):
        x = -1+2*i/(G-1); y = -1+2*j/(G-1)
        if x*x+y*y >= 0.999**2: continue
        v = abs(Wp(complex(x, y)))
        if v < mg: mg, marg = v, (round(x,3), round(y,3))
print("MIN_|grad varphi|_interior = %.4f at %s" % (mg, marg))

# (b,c) boundary sign table on four quarter-blocks
B = 7200
blocks = {"Gamma_D(t~0)": [], "top-gap(overlap)": [], "Gamma_N(t~pi)": [], "bottom-gap(overlap)": []}
for k in range(B):
    t = 2*math.pi*k/B - math.pi
    z = complex(math.cos(t), math.sin(t))
    dn = (z*Wp(z)).real
    at = abs(t)
    if at < A: blocks["Gamma_D(t~0)"].append(dn)
    elif abs(at-math.pi/2) < A or abs(at-math.pi/2) <= A: blocks["top-gap(overlap)"].append(dn) if t > 0 else blocks["bottom-gap(overlap)"].append(dn)
    else: blocks["Gamma_N(t~pi)"].append(dn)
for k, v in blocks.items():
    print("%s: min=%+.4f max=%+.4f n=%d" % (k, min(v), max(v), len(v)))
overlap_pos = min(min(blocks["top-gap(overlap)"]), min(blocks["bottom-gap(overlap)"]))
io_neg = max(max(blocks["Gamma_D(t~0)"]), max(blocks["Gamma_N(t~pi)"]))
print("OVERLAP_MIN(dn)=%.4f  IO_MAX(dn)=%.4f" % (overlap_pos, io_neg))
res = dict(min_grad_interior=float(mg), argmin=list(marg),
           overlap_min=float(overlap_pos), io_max=float(io_neg),
           block_stats={k: dict(min=float(min(v)), max=float(max(v))) for k, v in blocks.items()})
with open(os.path.join(OUT, "weight.json"), "w") as f:
    json.dump(res, f, indent=1)
print("VERIFY_WEIGHT_OK" if (mg > 0.05 and overlap_pos > 0 and io_neg < 0) else "VERIFY_WEIGHT_FAIL")
