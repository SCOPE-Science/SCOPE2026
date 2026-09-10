"""Target step 2b: single-weight strict-sign phases via smoothed-step Neumann data.

h_D: -3 on Gamma_D interior, +1 on K_D interior, C^2 smootherstep transitions
(width delta) at junctions, zero-mean adjusted. Phi_D(z)=sum (a_n/n) z^n.
Checks: strict signs w/ margins at interior sample points, Morse
(simple critical points in D, distinct critical values), rotation
Phi_N(z)=Phi_D(-z) gives N-pattern, blow-up quantity for Delta=phi_D-phi_N.
Stdlib + numpy. Writes phases3.json. Prints VERIFY lines.
"""
import math, json, os
import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__))
A = math.pi/4
DELTA = 0.12
NTR = 64

def smootherstep(v):
    v = min(1.0, max(0.0, v))
    return 6*v**5 - 15*v**4 + 10*v**3

def h_raw(t):
    g = abs((t + math.pi) % (2*math.pi) - math.pi)
    u = (g - A)/DELTA
    return -3.0 + 4.0*smootherstep((u+1.0)/2.0)

KQ = 200000
tq = np.linspace(-math.pi, math.pi, KQ, endpoint=False)
hv = np.array([h_raw(t) for t in tq])
mu = float(np.mean(hv))
print("MEAN_RAW =", mu)

def h(t):
    return h_raw(t) - mu

a = np.zeros(NTR+1)
for n in range(NTR+1):
    w = 1.0 if n == 0 else 2.0
    a[n] = float(np.mean(np.array([h(t) for t in tq])*np.cos(n*tq))*w/math.pi*math.pi)
# NOTE: mean over [-pi,pi) with weight: a_n = (1/pi) int h cos(nt); discrete mean*2pi/pi=2*mean
# recompute cleanly:
a = np.zeros(NTR+1)
hh = np.array([h(t) for t in tq])
for n in range(NTR+1):
    f = 2.0 if n > 0 else 1.0
    a[n] = f*float(np.mean(hh*np.cos(n*tq)))
print("a0 (should be ~0) =", a[0])
assert abs(a[0]) < 1e-9

c = a/np.maximum(np.arange(NTR+1), 1); c[0] = 0.0  # Phi_D coeffs

def Phip_D(z):
    return sum(n*c[n]*z**(n-1) for n in range(1, NTR+1))

def dn_phiD(t):
    z = complex(math.cos(t), math.sin(t))
    return (z*Phip_D(z)).real

# strict-sign check: interior points with clearance eps from junctions
EPS = 0.25
MG = 7200
tg = np.linspace(-math.pi, math.pi, MG, endpoint=False)
def clearance(t):
    g = abs(t)
    return min(abs(g-A), abs(g-(math.pi-A)), abs(abs(t)-math.pi+1e9))
ok = True; m_in = 1e9; m_out = 1e9
for t in tg:
    g = abs(t)
    dj = min(abs(g-A), abs(math.pi-g-A))  # distance to nearest junction set {|t|=A or |t-pi|=A}
    if dj < EPS:
        continue
    v = dn_phiD(t)
    if g < A:
        if not v < 0: ok = False; break
        m_in = min(m_in, -v)
    else:
        if not v > 0: ok = False; break
        m_out = min(m_out, v)
print("SIGN_STRICT(clearance %.2f):" % EPS, ok, " margin_GD=%.3f margin_KD=%.3f" % (m_in, m_out))

# Morse: roots of Phi_D' in D
poly = np.poly1d([n*c[n] for n in range(NTR, 0, -1)])
roots = np.roots(poly.coef)
inside = np.array([r for r in roots if abs(r) < 1-1e-6])
print("N_CRIT_IN_DISK =", len(inside))
def Phipp_D(z):
    return sum(n*(n-1)*c[n]*z**(n-2) for n in range(2, NTR+1))
simp = [abs(Phipp_D(z)) for z in inside]
nondeg = all(s > 1e-4 for s in simp)
print("MIN_|Phi''|_at_crit =", min(simp) if len(simp) else None, " NONDEG=", nondeg)
cvals = [sum(c[n]*z**n for n in range(1, NTR+1)) for z in inside]
mind = min([abs(cvals[i]-cvals[j]) for i in range(len(cvals)) for j in range(i+1, len(cvals))]) if len(cvals) > 1 else float('inf')
print("MIN_CVAL_GAP =", mind)
morse = bool(nondeg and (mind > 1e-4))

# rotation: Phi_N(z) = Phi_D(-z); check N-pattern at sample points
def dn_phiN(t):
    z = complex(math.cos(t), math.sin(t))
    return ((-z)*Phip_D(-z)).real  # d/dr Phi_D(-r e^{it}) at r=1 = Re(-z Phi_D'(-z))
def in_GN(t):
    return abs(abs(t)-math.pi) < A if False else (math.pi-abs(t)) < A
okN = True
for t in tg:
    dN = math.pi-abs(t)  # distance from pi
    dj = min(abs(dN-A), abs(dN-(math.pi-A)))
    if dj < EPS:
        continue
    v = dn_phiN(t)
    if dN < A:
        if not v < 0: okN = False; break
    else:
        if not v > 0: okN = False; break
print("N_PATTERN_STRICT:", okN)

# blow-up quantity: Delta = phi_D - phi_N on boundary grid
B = 4000
Ds = []
for k in range(B):
    t = 2*math.pi*k/B
    z = complex(math.cos(t), math.sin(t))
    pD = sum(c[n]*(z**n) for n in range(1, NTR+1)).real
    pN = sum(c[n]*((-z)**n) for n in range(1, NTR+1)).real
    Ds.append(pD-pN)
M, m = max(Ds), min(Ds)
print("DELTA_MAX=%.4f DELTA_MIN=%.4f (both nonzero => blow-up either convention)" % (M, m))
# pointwise witness at t=0
print("dnD(0)=%.4f dnN(0)=%.4f (opposite strict => no common real part)" % (dn_phiD(0.0), dn_phiN(0.0)))

res = dict(mean_raw=mu, sign_strict_D=bool(ok), margin_GD=float(m_in), margin_KD=float(m_out),
           n_crit=int(len(inside)), morse=bool(morse), min_cval_gap=float(mind),
           sign_strict_N=bool(okN), delta_max=float(M), delta_min=float(m),
           dnD_at_0=float(dn_phiD(0.0)), dnN_at_0=float(dn_phiN(0.0)))
with open(os.path.join(OUT, "phases3.json"), "w") as f:
    json.dump(res, f, indent=1)
print("VERIFY_PHASES3_OK" if (ok and okN and morse and M > 0.05 and m < -0.05) else "VERIFY_PHASES3_FAIL")
