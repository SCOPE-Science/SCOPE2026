"""Lane-424 phase-1 TARGET computation (v2: polar matching layer).
h1 = rho cos psi, h2 = rho sin psi => D = h1 h2' - h2 h1' = rho^2 psi'.
Contact <=> psi' > 0. Twist layer chi(t)=3t^2-(2+eta)t^3+eta t^4 with
small eta>0 so incoming slope is tamable; matching layer = Hermite on
(rho,psi) from (m_delta, 2pi) to (rho_std(d2), 2pi+psi_std(d2)).
Stdlib + sympy + numpy only (np.trapz for compat).
"""
import json
import numpy as np
import sympy as sp

OUT = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-424/output/artifacts/"

# ---------- 1. Symbolic standard model ----------
s = sp.symbols('s', real=True)
h1s = sp.cos(s)**2
h2s = sp.sin(s)**2
Dstd = sp.simplify(h1s * sp.diff(h2s, s) - h2s * sp.diff(h1s, s))
print("D_std =", Dstd)
a_std, b_std = sp.simplify(sp.diff(h2s, s) / Dstd), sp.simplify(-sp.diff(h1s, s) / Dstd)
print("a_std =", a_std, " b_std =", b_std)
pi = sp.pi
w = sp.sin(2*s) / (4*pi**2)
F1 = -sp.integrate(w, (s, s, sp.pi/2))
F2 = -sp.integrate(w, (s, 0, s))
Hstd = (2*pi)**2 * sp.integrate((F1*w*1 + F2*w*1), (s, 0, sp.pi/2))
print("H_std (normalized, Omega-orient) =", sp.simplify(Hstd), float(Hstd.evalf()))

# ---------- 2. Twist layer with tame exit slope ----------
delta, d2, eta = 0.35, 0.70, 0.05
def chi(t):
    return 3*t**2 - (2+eta)*t**3 + eta*t**4
def chip(t):
    return 6*t - 3*(2+eta)*t**2 + 4*eta*t**3
assert abs(chi(0)) < 1e-15 and abs(chi(1) - 1) < 1e-15
assert abs(chip(0)) < 1e-15 and abs(chip(1) - eta) < 1e-15
tg = np.linspace(0, 1, 10001)
assert chip(tg[1:]).min() > 0, "chi must be strictly increasing on (0,1]"
print("chi'>0 on (0,1], min =", chip(tg[1:]).min())
m_delta = float(np.cos(delta)**4 + np.sin(delta)**4) ** 0.5
rho0, rho1 = 1.0, m_delta
N = 20001
sg = np.linspace(0, delta, N)
tt = sg / delta
chiv, chpv = chi(tt), chip(tt)
rhov = rho0 + (rho1 - rho0)*tt**2
psiv = 2*np.pi*chiv
h1t = rhov*np.cos(psiv)
h2t = rhov*np.sin(psiv)
rhd = 2*(rho1 - rho0)*tt/delta
psd = 2*np.pi*chpv/delta
h1p = rhd*np.cos(psiv) - rhov*psd*np.sin(psiv)
h2p = rhd*np.sin(psiv) + rhov*psd*np.cos(psiv)
D = rhov**2*psd
print("twist min D on (0,delta] =", D[1:].min())
print("core D/s ->", D[1]/sg[1], " predicted", 2*np.pi*6/delta**2)

# ---------- 3. Matching layer: Hermite on (rho, psi) ----------
def psi_std(x):
    return np.arctan2(np.sin(x)**2, np.cos(x)**2)
def psi_std_p(x):
    t = np.tan(x)
    return 2*t*(1+t*t)/(1+t**4)
def rho_std(x):
    return np.sqrt(np.cos(x)**4 + np.sin(x)**4)
def rho_std_p(x):
    return -np.sin(2*x)*np.cos(2*x)/rho_std(x)
psi0, psi1 = 2*np.pi, 2*np.pi + psi_std(d2)
m0p, m1p = 2*np.pi*eta/delta, psi_std_p(d2)
r0, r1 = m_delta, rho_std(d2)
mr0, mr1 = 2*(rho1-rho0)/delta, rho_std_p(d2)
print("psi0,psi1 =", psi0, psi1, " slopes:", m0p, m1p)
print("rho0,rho1 =", r0, r1, " slopes:", mr0, mr1)
def hermite(y0, y1, m0, m1, h):
    return (y0, m0*h, 3*(y1-y0)-2*m0*h-m1*h, 2*(y0-y1)+m0*h+m1*h)
h = d2 - delta
cp = hermite(psi0, psi1, m0p, m1p, h)
cr = hermite(r0, r1, mr0, mr1, h)
M = 20001
sm = np.linspace(delta, d2, M)
u = (sm-delta)/h
psim = cp[0]+cp[1]*u+cp[2]*u**2+cp[3]*u**3
psimp = (cp[1]+2*cp[2]*u+3*cp[3]*u**2)/h
rhom = cr[0]+cr[1]*u+cr[2]*u**2+cr[3]*u**3
print("match min psi' =", psimp.min(), " min rho =", rhom.min())
h1m = rhom*np.cos(psim); h2m = rhom*np.sin(psim)
h1mp = ((cr[1]+2*cr[2]*u+3*cr[3]*u**2)/h)*np.cos(psim) - rhom*psimp*np.sin(psim)
h2mp = ((cr[1]+2*cr[2]*u+3*cr[3]*u**2)/h)*np.sin(psim) + rhom*psimp*np.cos(psim)
Dm = rhom**2*psimp
so = np.linspace(d2, np.pi/2, 5001)
ok = (D[1:].min() > 0) and (psimp.min() > 0)
print("CONTACT_OK:", ok)

# ---------- 4. Overtwisted radii + orbit slope sweep ----------
tv = np.linspace(0, 1, 200001)
chv = chi(tv)
for tgt, nm in [(0.25, "psi=pi/2"), (0.5, "psi=pi"), (0.75, "psi=3pi/2")]:
    i = int(np.searchsorted(chv, tgt))
    print(nm, "s in [%.7f, %.7f]" % (delta*tv[i-1], delta*tv[i]))
sig = -h1p[1:]/h2p[1:]
fin = np.isfinite(sig)
print("twist slope: frac finite =", fin.mean(), " range(clip) =",
      np.clip(np.where(fin, sig, 0), -1e4, 1e4).min(), np.clip(np.where(fin, sig, 0), -1e4, 1e4).max())
def crossings(arr_s, sval, val):
    out = []
    for i in range(len(arr_s)-1):
        a, b = sval[i], sval[i+1]
        if np.isfinite(a) and np.isfinite(b) and abs(a) < 60 and abs(b) < 60:
            if (a-val)*(b-val) < 0:
                out.append((float(arr_s[i]), float(arr_s[i+1]), float(a), float(b)))
    return out
cr32 = crossings(sg[1:], sig, 1.5)
cr23 = crossings(sg[1:], sig, 2.0/3.0)
print("sigma=3/2 brackets:", cr32[:6])
print("sigma=2/3 brackets:", cr23[:6])

# ---------- 5. Global assembly, helicity pair, energies ----------
S = np.concatenate([sg, sm[1:], so[1:]])
H1 = np.concatenate([h1t, h1m[1:], np.cos(so[1:])**2])
H2 = np.concatenate([h2t, h2m[1:], np.sin(so[1:])**2])
P1 = np.concatenate([h1p, h1mp[1:], -np.sin(2*so[1:])])
P2 = np.concatenate([h2p, h2mp[1:], np.sin(2*so[1:])])
DD = H1*P2 - H2*P1
A = np.zeros_like(S); B = np.zeros_like(S)
A[1:] = P2[1:]/DD[1:]; B[1:] = -P1[1:]/DD[1:]
A[0] = 1.0; B[0] = 0.0
wgt = np.sin(2*S)/(4*np.pi**2)
dS = np.diff(S)
cumB = np.zeros_like(S); cumB[1:] = np.cumsum(0.5*((wgt*B)[1:]+(wgt*B)[:-1])*dS)
cumA = np.zeros_like(S); cumA[1:] = np.cumsum(0.5*((wgt*A)[1:]+(wgt*A)[:-1])*dS)
F1v = -(cumB[-1]-cumB); F2v = -cumA
Hpi = (2*np.pi)**2*np.trapz(F1v*wgt*A + F2v*wgt*B, S)
Hstv = float(Hstd.evalf())
print("H_std =", Hstv, " H_pi =", Hpi, " ratio =", Hpi/Hstv)
Vpi = -np.trapz(DD, S)*(2*np.pi)**2
print("V_pi =", Vpi, " V_std =", 4*np.pi**2)
Em = np.trapz((A**2*np.cos(S)**2+B**2*np.sin(S)**2)*np.cos(S)*np.sin(S), S)*(2*np.pi)**2
Est = np.trapz((np.cos(so)**2+np.sin(so)**2)*np.cos(so)*np.sin(so), so)*(2*np.pi)**2
print("E_pi =", Em, " E_std =", Est)
res = {
    "delta": delta, "d2": d2, "eta": eta,
    "D_twist_min": float(D[1:].min()), "psip_match_min": float(psimp.min()),
    "contact_ok": bool(ok), "chi_increasing": True,
    "H_std_normalized": Hstv, "H_pi_normalized": float(Hpi),
    "helicity_ratio": float(Hpi/Hstv),
    "V_std": float(4*np.pi**2), "V_pi": float(Vpi),
    "E_pi": float(Em), "E_std": float(Est),
    "overtwist_brackets": {"psi_pi/2_s": [float(delta*tv[int(np.searchsorted(chv,0.25))-1]),
                                           float(delta*tv[int(np.searchsorted(chv,0.25))])],
                           "psi_pi_s": [float(delta*tv[int(np.searchsorted(chv,0.5))-1]),
                                        float(delta*tv[int(np.searchsorted(chv,0.5))])],
                           "psi_3pi/2_s": [float(delta*tv[int(np.searchsorted(chv,0.75))-1]),
                                           float(delta*tv[int(np.searchsorted(chv,0.75))])]},
    "trefoil_sigma3/2_brackets": [[c[0], c[1]] for c in cr32[:4]],
    "slope2/3_brackets": [[c[0], c[1]] for c in cr23[:4]],
}
with open(OUT+"target_model.json", "w") as f:
    json.dump(res, f, indent=2)
print("wrote target_model.json")
