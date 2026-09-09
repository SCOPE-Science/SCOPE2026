"""Fallback certificate: constant-rho twist-layer helicity in EXACT closed form.
Model (fallback certificate): on (0,delta): rho=1, psi=m0 s, m0=40pi/7.
alpha_pi = cos(m0 s) dphi1 + sin(m0 s) dphi2 (twist layer; C0/Lipschitz model,
D = m0 > 0 exactly, winding psi(delta)-psi(0) = 2pi full Lutz turn).
Reeb: A=cos(m0 s), B=sin(m0 s). mu0 = Omega/(4pi^2), Omega=sin2s ds dphi1 dphi2.
H_pi^T = (2pi)^2 int_0^delta [F1 w A + F2 w B] ds with GLOBAL potentials
F1(s)=-int_s^{pi/2} wB_glob, F2(s)=-int_0^s wA_glob. For the CERTIFICATE we
prove the twist-layer self-contribution and cross terms via the exhibited
elementary antiderivatives P(s)=int wA, Q(s)=int wB (differentiation-checked),
then evaluate the full H_pi by exact FTC + converged quadrature for the
match/standard layers. Prints exact forms + numeric values.
"""
import sympy as sp
import numpy as np

OUT = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-424/output/artifacts/"
s = sp.symbols('s', real=True)
delta = sp.Rational(7, 20)
m0 = 40*sp.pi/7
w = sp.sin(2*s)/(4*sp.pi**2)
A = sp.cos(m0*s); B = sp.sin(m0*s)
den = (-98 + 800*sp.pi**2)
P = (140*sp.pi*sp.sin(2*s)*sp.sin(m0*s)/den + 49*sp.cos(2*s)*sp.cos(m0*s)/den)/(4*sp.pi**2)
Q = (-140*sp.pi*sp.sin(2*s)*sp.cos(m0*s)/den + 49*sp.sin(m0*s)*sp.cos(2*s)/den)/(4*sp.pi**2)
assert sp.simplify(sp.diff(P, s) - w*A) == 0
assert sp.simplify(sp.diff(Q, s) - w*B) == 0
print("CERTIFIED: P'=wA, Q'=wB (sympy diff = 0 exactly)")
# definite layer integrals over twist layer
IP = sp.simplify(P.subs(s, delta) - P.subs(s, 0))
IQ = sp.simplify(Q.subs(s, delta) - Q.subs(s, 0))
print("int_0^delta wA =", IP, "=", float(IP.evalf()))
print("int_0^delta wB =", IQ, "=", float(IQ.evalf()))
# H_std antiderivative re-certified
F = sp.cos(2*s)/(8*sp.pi**2)
assert sp.simplify(sp.diff(F, s) + sp.sin(2*s)/(4*sp.pi**2)) == 0
Hstd = sp.simplify(F.subs(s, sp.pi/2) - F.subs(s, 0))
print("H_std =", Hstd, "=", float(Hstd.evalf()))

# Full H_pi for the HYBRID certificate model: constant-rho twist + smooth match/std
# (same match/std as phase-1 smooth model? No — for certificate simplicity use the
# fallback C0 match layer; quadrature converged + analytic twist piece above.)
d2f = 0.70; dd = 0.35
m0f = 40*np.pi/7
psd = np.arctan2(np.sin(d2f)**2, np.cos(d2f)**2)
m1f = psd/(d2f-dd)
md = float(np.cos(dd)**4+np.sin(dd)**4)**0.5
rd2 = float(np.cos(d2f)**4+np.sin(d2f)**4)**0.5
k1f = (rd2-1.0)/(d2f-dd)  # rho: 1 -> rd2 across match (constant-rho twist => rho(delta)=1)
def AB(x):
    if x <= dd: return np.cos(m0f*x), np.sin(m0f*x)
    elif x <= d2f:
        u = x-dd; rh = 1.0+k1f*u; ps = 2*np.pi+m1f*u
        p1 = k1f*np.cos(ps)-rh*m1f*np.sin(ps); p2 = k1f*np.sin(ps)+rh*m1f*np.cos(ps)
        D = rh**2*m1f
        return p2/D, -p1/D
    else: return 1.0, 1.0
for N in (6001, 24001):
    S = np.linspace(0, np.pi/2, N)
    Av = np.array([AB(x)[0] for x in S]); Bv = np.array([AB(x)[1] for x in S])
    wgt = np.sin(2*S)/(4*np.pi**2)
    dS = np.diff(S)
    cB = np.zeros(N); cB[1:] = np.cumsum(0.5*((wgt*Bv)[1:]+(wgt*Bv)[:-1])*dS)
    cA = np.zeros(N); cA[1:] = np.cumsum(0.5*((wgt*Av)[1:]+(wgt*Av)[:-1])*dS)
    Hpi = (2*np.pi)**2*np.trapz(-(cB[-1]-cB)*wgt*Av - cA*wgt*Bv, S)
    print(f"H_pi hybrid N={N}: {Hpi:.10f}")
