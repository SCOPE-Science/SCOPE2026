"""Fallback FULL-EXACT certificate: rho=1 on (0,d2], piecewise-linear psi.
All six potential-antiderivatives PT,PM,PS,QT,QM,QS are elementary (sympy).
H_pi = (2pi)^2 sum over pieces of int [F1 wA + F2 wB], F1=-int_s^{pi/2}wB,
F2=-int_0^s wA. Since F1,F2 are themselves built from the exact
antiderivatives, H_pi reduces to exact FTC evaluations + products of trig:
evaluate inner potentials at knots exactly, then per-piece product integrals
int P_prod... via integration by parts EXACTLY:
int_a^b F(s) j(s) ds with F'=g (known antiderivative G) and j having known
antiderivative J: = [G... ] — do directly: F1(s) = -(Qtot - Qpart(s)) etc.
Simplest exact route: F1, F2 piecewise closed forms from the six antis;
then integrand per piece = F*trig, integrated by sympy exactly.
Verifies diff-checks + prints closed-form H_pi + inequality.
"""
import sympy as sp

s = sp.symbols('s', real=True)
delta = sp.Rational(7, 20); d2 = sp.Rational(7, 10); S1 = sp.pi/2
m0 = 2*sp.pi/delta
psi1 = sp.atan(sp.sin(d2)**2/sp.cos(d2)**2)
m1 = psi1/(d2-delta)
w = sp.sin(2*s)/(4*sp.pi**2)
AT = sp.cos(m0*s); BT = sp.sin(m0*s)
AM = sp.cos(2*sp.pi+m1*(s-delta)); BM = sp.sin(2*sp.pi+m1*(s-delta))

PT = sp.integrate(sp.simplify(w*AT), s)
QT = sp.integrate(sp.simplify(w*BT), s)
PM = sp.integrate(sp.simplify(w*AM), s)
QM = sp.integrate(sp.simplify(w*BM), s)
PS = -sp.cos(2*s)/(8*sp.pi**2)
QS = -sp.cos(2*s)/(8*sp.pi**2)
# diff checks
for X, j in [(PT, w*AT), (QT, w*BT), (PM, w*AM), (QM, w*BM), (PS, w), (QS, w)]:
    assert sp.simplify(sp.diff(X, s)-sp.simplify(j)) == 0
print("ALL SIX diff-checks = 0 EXACT")

def ev(X, pt): return sp.simplify(X.subs(s, pt))
# total integrals
tA_T = ev(PT, delta)-ev(PT, 0); tB_T = ev(QT, delta)-ev(QT, 0)
tA_M = ev(PM, d2)-ev(PM, delta); tB_M = ev(QM, d2)-ev(QM, delta)
tA_S = ev(PS, S1)-ev(PS, d2); tB_S = ev(QS, S1)-ev(QS, d2)
totA = sp.simplify(tA_T+tA_M+tA_S); totB = sp.simplify(tB_T+tB_M+tB_S)
print("totA =", float(totA.evalf()), " totB =", float(totB.evalf()))
# global potentials at knots: F2(s) = -int_0^s wA; F1(s) = -(totB - int_0^s wB)
F2_0 = sp.Integer(0)
F2_d = sp.simplify(-(tA_T)); F2_d2 = sp.simplify(-(tA_T+tA_M)); F2_S1 = sp.simplify(-totA)
G_d = sp.simplify(tA_T); G_d2 = sp.simplify(tA_T+tA_M)  # int_0^s wB at knots
F1_0 = sp.simplify(-totB); F1_d = sp.simplify(-(totB-G_d)); F1_d2 = sp.simplify(-(totB-G_d2)); F1_S1 = sp.Integer(0)
# per-piece H: int_a^b (F1 wA + F2 wB) with F1(s)=c1-Ppart(s)... write exact:
# Twist: int_0^s wA = PT(s)-PT(0) := pT(s); int_0^s wB = qT(s).
# F2(s) = -pT(s); F1(s) = F1_0 + ... F1(s) = -(totB - qT(s)) = -totB + qT(s).
pT = sp.simplify(PT-PT.subs(s, 0)); qT = sp.simplify(QT-QT.subs(s, 0))
F1T = sp.simplify(-totB+qT); F2T = sp.simplify(-pT)
HT = sp.integrate(sp.simplify(F1T*w*AT+F2T*w*BT), (s, 0, delta))
print("twist H done:", float(HT.evalf()))
pM = sp.simplify(PM-PM.subs(s, delta)); qM = sp.simplify(QM-QM.subs(s, delta))
F1M = sp.simplify(F1_d+qM); F2M = sp.simplify(F2_d-pM)
HM = sp.integrate(sp.simplify(F1M*w*AM+F2M*w*BM), (s, delta, d2))
print("match H done:", float(HM.evalf()))
pS = sp.simplify(PS-PS.subs(s, d2)); qS = sp.simplify(QS-QS.subs(s, d2))
F1S = sp.simplify(F1_d2+qS); F2S = sp.simplify(F2_d2-pS)
HS = sp.integrate(sp.simplify(F1S*w+F2S*w), (s, d2, S1))
print("std H done:", float(HS.evalf()))
Hpi = sp.simplify((2*sp.pi)**2*(HT+HM+HS))
print("H_pi EXACT =", Hpi)
print("H_pi float =", float(Hpi.evalf()))
Hstd = sp.Rational(-1, 1)/(4*sp.pi**2)
print("H_std =", Hstd, float(Hstd.evalf()))
print("diff =", float((Hpi-Hstd).evalf()))
import json
OUT = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-424/output/artifacts/"
json.dump({"H_pi_exact": str(Hpi), "H_pi_float": float(Hpi.evalf()),
           "H_std_exact": "-1/(4*pi**2)", "H_std_float": float(Hstd.evalf()),
           "diff_float": float((Hpi-Hstd).evalf())},
          open(OUT+"fallback_exact.json", "w"), indent=2)
print("wrote fallback_exact.json")
