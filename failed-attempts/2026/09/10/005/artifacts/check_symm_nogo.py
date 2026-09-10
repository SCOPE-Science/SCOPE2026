"""Target step 4: verify symmetric-pairing obstructions S1 + chord endpoint restriction.

S1: rotation-symmetric pair Phi_N(z)=Phi_D(-z), real coeffs (from check_phases3):
    dn(psi_-) at gap midpoints +-i must vanish EXACTLY (parity argument);
    dn(psi_+) on Gamma_N must be strictly POSITIVE (wrong sign for IO pattern).
Chords: horizontal chords hitting both quarter-arcs have |c|<=1/sqrt(2);
    endpoint arcs for tilted chords.
Writes symm_nogo.json. Prints VERIFY lines.
"""
import math, json, os
import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__))
A = math.pi/4
NTR = 64
def smootherstep(v):
    v = min(1.0, max(0.0, v)); return 6*v**5-15*v**4+10*v**3
def h_raw(t):
    g = abs((t+math.pi) % (2*math.pi)-math.pi)
    return -3.0+4.0*smootherstep(((g-A)/0.12+1.0)/2.0)
KQ = 60000
tq = np.linspace(-math.pi, math.pi, KQ, endpoint=False)
hv = np.array([h_raw(t) for t in tq]); mu = float(np.mean(hv)); hh = hv-mu
a = np.zeros(NTR+1)
for n in range(NTR+1):
    f = 2.0 if n > 0 else 1.0
    a[n] = f*float(np.mean(hh*np.cos(n*tq)))
c = a/np.maximum(np.arange(NTR+1), 1); c[0] = 0.0
assert max(abs(x.imag) for x in c) == 0

def PhiD(z): return sum(c[n]*z**n for n in range(1, NTR+1))
def PhiN(z): return PhiD(-z)

# S1a: dn(psi_-) at +-i, psi_- = Re(PhiD - PhiN)
for t, lbl in [(math.pi/2, "+i"), (-math.pi/2, "-i")]:
    z = complex(math.cos(t), math.sin(t))
    Wp = sum(n*c[n]*z**(n-1) for n in range(1, NTR+1)) - \
         sum(n*c[n]*(-z)**(n-1)*(-1) for n in range(1, NTR+1))
    print("dn(psi_-)(%s) = %.3e (predict 0 by parity)" % (lbl, (z*Wp).real))
# S1b: dn(psi_+) range on Gamma_N (predict strictly >0)
Bp = np.linspace(math.pi-A, math.pi+A, 2001)
vals = []
for t in Bp:
    z = complex(math.cos(t), math.sin(t))
    Wp = sum(n*c[n]*z**(n-1) for n in range(1, NTR+1)) + \
         sum(n*c[n]*(-z)**(n-1)*(-1) for n in range(1, NTR+1))
    vals.append((z*Wp).real)
print("psi_+ on Gamma_N: min=%+.4f max=%+.4f (predict min>0)" % (min(vals), max(vals)))
# S1c: psi_+ dn range on each overlap gap (predicts sign change: min<0<max)
for blo, bhi, lbl in [(A, math.pi-A, "top-gap"), (-(math.pi-A), -A, "bottom-gap")]:
    Bg = np.linspace(blo, bhi, 2001)
    v = []
    for t in Bg:
        z = complex(math.cos(t), math.sin(t))
        Wp = sum(n*c[n]*z**(n-1) for n in range(1, NTR+1)) + \
             sum(n*c[n]*(-z)**(n-1)*(-1) for n in range(1, NTR+1))
        v.append((z*Wp).real)
    print("psi_+ %s: min=%+.4f max=%+.4f zero_cross=%s" % (lbl, min(v), max(v), min(v) < 0 < max(v)))

# Chords: horizontal y=c endpoints in arcs?
ok_bd = 1/math.sqrt(2)
for cc in [0.0, 0.5, 0.7071, 0.8]:
    x = math.sqrt(max(0, 1-cc*cc))
    ang = math.degrees(math.atan2(cc, x))
    print("y=%.4f right-endpoint angle=%.2f deg inGammaD=%s" % (cc, ang, abs(math.atan2(cc, x)) < A))
print("THRESHOLD 1/sqrt(2)=%.6f" % ok_bd)

res = dict(s1a_dn_psi_minus_at_ipi_over_2=float(
        (complex(0,1)* (sum(n*c[n]*complex(0,1)**(n-1) for n in range(1,NTR+1)) -
         sum(n*c[n]*complex(0,-1)**(n-1)*(-1) for n in range(1,NTR+1)))).real),
    psi_plus_GammaN_min=float(min(vals)), psi_plus_GammaN_max=float(max(vals)),
    chord_threshold=float(ok_bd))
with open(os.path.join(OUT, "symm_nogo.json"), "w") as f:
    json.dump(res, f, indent=1)
s1a = abs(res["s1a_dn_psi_minus_at_ipi_over_2"]) < 1e-9
print("VERIFY_SYMM_NOGO_OK" if (s1a and min(vals) > 0.5) else "VERIFY_SYMM_NOGO_FAIL")
