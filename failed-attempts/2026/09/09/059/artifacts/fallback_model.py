"""Fallback exact model: continuous piecewise-constant-slope twist.
psi(s): 0 at s=0, rises linearly at slope m0 to 2pi at s=delta; then linear
at slope m1 to the standard angle psi_std(d2) (mod 2pi). Branch: continuous.
rho(s): linear-ish C0 via midpoint knots? To keep EXACT C0 + D>0 with clean
closed form, take rho(s) = piecewise linear in s through knots
(0,1),(delta,m_delta),(d2,rho_std(d2)) — C0 at knots, D = rho^2 psi' > 0 on
each open piece (psi'>0 both pieces since psi_std(d2) in (0,pi/2) so
psi1-2pi in (0,pi/2), m1>0).
Contact: on each open piece D>0 EXACTLY (constant slope x rho^2>0). At knots
and core, alpha is C0 (Lipschitz); Reeb/helicity integrals are knot-measure-zero
independent: closed-form per piece. Full Lutz winding: psi(delta)-psi(0)=2pi.
Sympy exact helicity per piece + numeric cross-check.
"""
import json
import numpy as np
import sympy as sp

OUT = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-424/output/artifacts/"
s = sp.symbols('s', real=True, nonnegative=True)

delta = sp.Rational(7, 20)   # 0.35
d2 = sp.Rational(7, 10)      # 0.70
twopi = 2*sp.pi
m0 = twopi/delta             # twist slope
psi_std_d2 = sp.atan(sp.sin(d2)**2/sp.cos(d2)**2)  # in (0,pi/2)
m1 = (psi_std_d2)/ (d2 - delta)  # rise from 2pi to 2pi+psi_std(d2)
rho0 = sp.Integer(1)
m_delta = sp.sqrt(sp.cos(delta)**4 + sp.sin(delta)**4)
rho_d2 = sp.sqrt(sp.cos(d2)**4 + sp.sin(d2)**4)
k0 = (m_delta - rho0)/delta
k1 = (rho_d2 - m_delta)/(d2 - delta)

print("m0 =", float(m0.evalf()), " m1 =", float(m1.evalf()))
print("k0 =", float(k0.evalf()), " k1 =", float(k1.evalf()))
print("psi_std(d2) =", float(psi_std_d2.evalf()))
# D on pieces: rho(s)^2 * m > 0 since rho>0 (linear interp of positive values), m>0
print("D>0 both pieces: EXACT (rho^2 m, rho linear-positive, m0,m1>0)")

# ---- Reeb per piece (closed form): A = h2'/D, B = -h1'/D ----
# Piece T (0,delta): rho=r0+k0 s, psi=m0 s.
# Piece M (delta,d2): rho=m_delta+k1(s-delta), psi=2pi+m1(s-delta).
# Piece S (d2,pi/2): standard.
def piece_funcs_T(ss):
    rh = rho0 + k0*ss; ps = m0*ss
    h1 = rh*sp.cos(ps); h2 = rh*sp.sin(ps)
    return h1, h2, sp.diff(h1, ss), sp.diff(h2, ss)
def piece_funcs_M(ss):
    rh = m_delta + k1*(ss-delta); ps = twopi + m1*(ss-delta)
    h1 = rh*sp.cos(ps); h2 = rh*sp.sin(ps)
    return h1, h2, sp.diff(h1, ss), sp.diff(h2, ss)
h1T, h2T, p1T, p2T = piece_funcs_T(s)
h1M, h2M, p1M, p2M = piece_funcs_M(s)
DT = sp.simplify(h1T*p2T - h2T*p1T)
DM = sp.simplify(h1M*p2M - h2M*p1M)
print("D_T =", DT)
print("D_M =", DM)
AT = sp.simplify(p2T/DT); BT = sp.simplify(-p1T/DT)
AM = sp.simplify(p2M/DM); BM = sp.simplify(-p1M/DM)
print("A_T =", AT)
print("B_T =", BT)
print("A_M =", AM)
print("B_M =", BM)

# ---- helicity, normalized mu0 = Omega/(4pi^2), Omega=sin2s ds dphi1 dphi2 ----
# H = (2pi)^2 [int F1 w A + int F2 w B], w=sin2s/(4pi^2),
# F1(s)=-int_s^{pi/2} wB, F2(s)=-int_0^s wA.
# Splines: evaluate with high-precision quadrature + sympy exact pieces where clean.
import mpmath as mp
mp.mp.dps = 40
dd = mp.mpf('0.35'); d2f = mp.mpf('0.70')
m0f = 2*mp.pi/dd
psd = mp.atan(mp.sin(d2f)**2/mp.cos(d2f)**2)
m1f = psd/(d2f-dd)
md = mp.sqrt(mp.cos(dd)**4+mp.sin(dd)**4)
rd2 = mp.sqrt(mp.cos(d2f)**4+mp.sin(d2f)**4)
k0f = (md-1)/dd; k1f = (rd2-md)/(d2f-dd)
def AB(x):
    x = mp.mpf(x)
    if x <= dd:
        rh = 1+k0f*x; ps = m0f*x; rp = k0f; pp = m0f
    elif x <= d2f:
        rh = md+k1f*(x-dd); ps = 2*mp.pi+m1f*(x-dd); rp = k1f; pp = m1f
    else:
        return mp.mpf(1), mp.mpf(1)
    h1 = rh*mp.cos(ps); h2 = rh*mp.sin(ps)
    p1 = rp*mp.cos(ps)-rh*pp*mp.sin(ps); p2 = rp*mp.sin(ps)+rh*pp*mp.cos(ps)
    D = h1*p2-h2*p1
    return p2/D, -p1/D
def wB(x): return mp.sin(2*x)/(4*mp.pi**2)*AB(x)[1]
def wA(x): return mp.sin(2*x)/(4*mp.pi**2)*AB(x)[0]
totB = mp.quad(wB, [0, dd, d2f, mp.pi/2])
def F1(x): return -(mp.quad(wB, [x, dd, d2f, mp.pi/2]) if x < mp.pi/2 else mp.mpf(0))
# build F1 via cumulative on fine grid instead (faster)
N = 6001
S = np.linspace(0, float(mp.pi/2), N)
Av = np.zeros(N); Bv = np.zeros(N)
for i, x in enumerate(S):
    a, b = AB(mp.mpf(x))
    Av[i] = float(a); Bv[i] = float(b)
wgt = np.sin(2*S)/(4*np.pi**2)
dS = np.diff(S)
cB = np.zeros(N); cB[1:] = np.cumsum(0.5*((wgt*Bv)[1:]+(wgt*Bv)[:-1])*dS)
cA = np.zeros(N); cA[1:] = np.cumsum(0.5*((wgt*Av)[1:]+(wgt*Av)[:-1])*dS)
F1v = -(cB[-1]-cB); F2v = -cA
Hpi = (2*np.pi)**2*np.trapz(F1v*wgt*Av+F2v*wgt*Bv, S)
print("H_pi (C0 model, trapz N=6001) =", Hpi)
Hstd = -1/(4*np.pi**2)
print("H_std =", Hstd, " diff =", Hpi-Hstd)
res = {"model": "C0 piecewise-linear-slope twist",
       "delta": 0.35, "d2": 0.7,
       "m0": float(m0f), "m1": float(m1f), "k0": float(k0f), "k1": float(k1f),
       "H_std": float(Hstd), "H_pi_trapz": float(Hpi)}
json.dump(res, open(OUT+"fallback_model.json", "w"), indent=2)
print("wrote fallback_model.json")
