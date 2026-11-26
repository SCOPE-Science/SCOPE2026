# Two strict reset-rate turning points in a finite birth–death splitting probability

## Finding

A finite nearest-neighbor absorbing birth–death chain can have **both a strict interior minimum and a strict interior maximum** in its eventual left-exit probability as a single geometric resetting parameter varies. An explicit eleven-edge chain, with all rates rational and reset to its initial site, has **exactly two** interior critical points. In particular, the multiple-extrema regime proposed for investigation in the recent stochastic-order literature occurs already with one fixed reset location and fully absorbing endpoints; no partial reaction or varying reset destination is necessary.

## Assumptions and scope

The state space is \(\{0,1,\ldots,11\}\), with absorbing endpoints \(0\) and \(11\), and initial and reset site \(z=5\). At transient site \(i\), the reset-free nearest-neighbor walk moves right with probability \(p_i\) and left with probability \(q_i=1-p_i\), where

\[
(p_1,\ldots,p_{10})=\frac{1}{100}(95,10,80,30,1,40,75,45,40,10).
\]

After each step that has not caused absorption, independently reset to site \(5\) with probability \(1-s\), or continue without resetting with probability \(s\), for \(0<s\le1\). Each reset begins a fresh independent excursion. Define \(Q(s)\) as the eventual probability of absorption at the left boundary. (Equivalently, the reset survival weights of an excursion lasting \(n\) steps are \(s^{n-1}\).) No endpoint statement is made about \(s=0\), where absorption is impossible from site \(5\) under a reset after every nonabsorbing step.

Set

\[
L(x)=1-\frac{287}{200}x+\frac{1197}{2500}x^2,
\qquad
R(x)=1-\frac{457}{400}x+\frac{423}{2000}x^2.
\]

For \(0<s\le1\), the exact reset-dependent splitting probability is

\[
\boxed{Q(s)=\frac{231R(s^2)}{231R(s^2)+2sL(s^2)}.}
\]

Its derivative has exactly two distinct zeros in \((0,1)\): one at \(s_1=\sqrt{x_1}\), with \(4/5<x_1<9/10\), and one at \(s_2=\sqrt{x_2}\), with \(99/100<x_2<999/1000\). These are respectively a strict local **minimum** and a strict local **maximum** of \(Q\). Numerically, for orientation only, \(x_1\approx0.828754728626167\), \(x_2\approx0.993911318261862\); the exact root-count proof below does not use these approximations.

## Proof

Let \(T\) be the first exit time of the reset-free walk and \(J\in\{0,11\}\) its exit side. Write \(U(s)=\mathbb E_5[s^T\mathbf1_{\{J=0\}}]\) and \(V(s)=\mathbb E_5[s^T\mathbf1_{\{J=11\}}]\). The per-excursion probabilities of exiting left and right before reset are \(U(s)/s\) and \(V(s)/s\), respectively. Since excursions renew after every reset and each has strictly positive success probability for \(s>0\), summing the geometric number of failed excursions gives \(Q(s)=U(s)/(U(s)+V(s))\).

For each interval of transient states \([u,v]\), let \(D_{u:v}(s)\) be the determinant of the corresponding principal submatrix of \(I-sP\), where \(P\) is the reset-free killed transition matrix. Tridiagonality gives

\[
D_{u:v}(s)=D_{u:v-1}(s)-s^2p_{v-1}q_v D_{u:v-2}(s),
\]

with empty and singleton continuants equal to \(1\). Cramer's rule, or direct forward substitution in the two discounted hitting equations, yields

\[
\frac{U(s)}{V(s)}
=\frac{q_1q_2q_3q_4q_5}{p_5p_6p_7p_8p_9p_{10}}
  s^{-1}\frac{D_{6:10}(s)}{D_{1:4}(s)}.
\]

Evaluating the recurrence with the stated rational probabilities gives \(D_{1:4}(s)=L(s^2)\), \(D_{6:10}(s)=R(s^2)\), and the prefactor \(231/2\). This proves the displayed formula. Both continuants are strictly positive for \(0\le s\le1\): viewed as polynomials in \(x=s^2\), their derivatives are negative throughout \([0,1]\), and \(L(1)=219/5000>0\), \(R(1)=69/1000>0\).

The odds \(F(s)=Q(s)/(1-Q(s))\) equal \((231/2)R(s^2)/(sL(s^2))\). With \(x=s^2\), direct differentiation gives

\[
\operatorname{sgn}Q'(s)=\operatorname{sgn}H(x),\quad
H(x)=-R(x)L(x)+2x\bigl(R'(x)L(x)-R(x)L'(x)\bigr).
\]

Expanding in exact rational arithmetic,

\[
H(x)=-1+\frac{253}{80}x-\frac{271919}{80000}x^2
+\frac{2675169}{2000000}x^3-\frac{506331}{5000000}x^4.
\]

Transform \(x=t/(1+t)\), which bijects \((0,\infty)\) onto \((0,1)\). The polynomial

\[
(1+t)^4H\left(\frac{t}{1+t}\right)
=-1-\frac{67}{80}t+\frac{7081}{80000}t^2
+\frac{54219}{2000000}t^3-\frac{423}{2500000}t^4
\]

has coefficient-sign sequence \((-,-,+,+,-)\), exactly two sign changes. By Descartes' rule, \(H\) has at most two zeros on \((0,1)\), counting multiplicity. Exact evaluations give

\[
H(4/5)=-\frac{776317}{390625000}<0,\qquad
H(9/10)=\frac{2700737}{1562500000}>0,
\]

and

\[
H(99/100)=\frac{54173173819}{500000000000000}>0,\qquad
H(999/1000)=-\frac{707042319104831}{5000000000000000000}<0.
\]

Thus there are at least two different sign-changing roots in the disjoint indicated intervals. The Descartes bound implies these are exactly the two roots, each simple. Since \(s>0\) and \(x=s^2\) is strictly increasing, the first is a strict minimum of \(Q\), the second a strict maximum. This proves the finding without relying on numerical root searches or incomplete enumeration. \(\square\)

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. The checker reconstructs the left and right continuants, the odds prefactor and derivative polynomial using exact fractions, verifies all the transformed coefficient signs and four rational root brackets, and independently solves the full ten-state discounted first-passage linear systems at six rational values of \(s\). It reports **32 exact rational assertions passed**. The written Descartes argument, rather than any finite sampling, proves the global claim of exactly two critical points.

## Relationship to prior work

Newton and Vega Coso, *Stochastic Orders of the Exit Pair and the Monotone Response to Resetting*, arXiv:2611.01756v1 (publicly submitted November 1, 2026), establish the renewal exit-pair identity, uniform-walk monotonicity and a rational inhomogeneous chain with two **exact-time** reversal events (Proposition 7.6 and Corollary 7.9). Their Section 10.3 separately asks about *one or several interior extrema as reset intensity varies*. Temporal reversals do not mathematically imply two geometric-reset-rate extrema; the present explicit rational continuants and Descartes certificate directly establish the latter. The renewal identity and tridiagonal-resolvent framework are credited, not claimed new.

Related finite-chain work establishes a sharp earliest chain size for **one** interior extremum, not two. Reentrant majority changes for a Brownian search between partially absorbing targets have also been reported; those involve different boundary physics and a threshold crossing, not the same twice-critical finite birth–death probability. A full historical classification or minimal chain-size claim is not made here.

## Limitations

The theorem proves existence and exact two-turn behavior for the stated rational environment; it does not classify all environments, give the smallest possible state space for two extrema, or quantify a universal response amplitude. The two extrema in this witness differ by only approximately \(4.9\times10^{-5}\) in probability. The result is robust to sufficiently small perturbations of the transition probabilities because the derivative sign inequalities are strict, but no explicit robustness radius is asserted. Priority against unlocated older special cases is not independently certified. The finite checker is corroborating evidence, not an independent review of the analytical proof.

## References

1. T. Newton and J. A. Vega Coso, *Stochastic Orders of the Exit Pair and the Monotone Response to Resetting*, arXiv:2611.01756v1 (November 1, 2026), https://arxiv.org/html/2611.01756v1, particularly Sections 2, 7, 10.3 and Appendix B.
2. *The sharp eight-vertex onset of interior geometric-reset splitting optima*, published-finding corpus record `2026/11/16` (an earlier single-extremum result; cited for comparison only).
3. *Sharp reentrant capture-majority window for two partially absorbing Brownian targets*, published-finding corpus record `2026/10/27` (related continuum partially absorbing model; cited for comparison only).
