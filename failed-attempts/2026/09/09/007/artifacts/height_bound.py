"""S5a: canonical height lower bound H0 + naive height of P1 (stdlib only, pure Python).
Naive logarithmic height h(P)=log(max(|num|,|den|)) of x in lowest terms.
Canonical height bound: use Silverman (Adv. Std. Alg. NT X, Thm 5.4 / Hindry-Silverman):
  h(P) - hhat(P) <= (1/2)log(max(1,|c4|/48,|c6|/...))... simplest certified route:
  (a) P1 naive height computed exactly (int arithmetic).
  (b) Universal gap: Cremona-Prickett-Siksek / Silverman explicit: for curves with
      integral model, hhat(P) >= c1*h(P) - c2 with tabulated constants; but to keep
      this artifact self-contained and rigorous we prove a *naive-height* lower bound:
      any missing generator Q independent of P1: h(Q) >= log(n) via x-denominator analysis
      is false in general; instead we certify: regulator-free bound H0 via David/Masser?
  Honest approach: compute h(P1) exactly and state the searched naive-height range log;
  for H0 use the theorem of Petsche (explicit Lehmer-type): hhat(P) >= c/N^... too weak.
  Practical certified H0: use mod-3/5 reduction + torsion=V4: nonzero point reduces
  nontrivially; Silverman H. VIII Thm 5.4: hhat(P) >= (1/48)log|N(Delta)| - ... for
  everywhere good? Not applicable (multiplicative/additive).
  => We log h(P1) exactly + state Bremner-Silverman-Tzanakis David bound structure,
  and give an explicit *conditional* search certificate: every rational point with
  x=a/d^2 in lowest terms, d<=D0 or |a|<=A0 enumerated. This is honest fallback data.
"""
from fractions import Fraction
import math
n=799657; D=n*n
x=Fraction(-94381225,289)
num,den=abs(x.numerator),x.denominator
h=math.log(max(num,den))
print("h(P1) =",h)
print("num digits:",len(str(num)),"den digits:",len(str(den)))
print("x(P1) square denominator? 289=17^2:",289==17**2)
print("canonical height of P1: NOT computable in stdlib-only env (needs Tate series);",
      "logged as open with naive height above.")
print("Delta digits:",len(str(64*D**3))," log|Delta| =",math.log(64*D**3))
