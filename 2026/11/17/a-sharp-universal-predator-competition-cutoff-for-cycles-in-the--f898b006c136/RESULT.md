# A sharp universal predator-competition cutoff for cycles in the Bazykin flow

## Finding
Consider the planar Bazykin predator–prey system
\[
\dot x=rx(1-x/k)-\frac{axy}{x+b},\qquad
\dot y=y\left(\frac{eax}{x+b}-d-\sigma y\right),
\]
with strictly positive parameters \(r,k,a,b,e,d,\sigma\). Fix only the functional-response strength \(a\) and half-saturation scale \(b\), allowing the other positive parameters to vary.

**Sharp universal cutoff.** If \(\sigma\ge a/(4b)\), the positive quadrant contains no nonconstant periodic orbit, for **every** choice of \(r,k,e,d>0\). Conversely, for every \(0<\sigma<a/(4b)\), there are positive choices of \(r,k,e,d\), with \(0<e<1\), for which the system has a nonconstant positive periodic orbit. Consequently the threshold \(a/(4b)\) is necessary and sufficient for a competition coefficient to exclude positive periodic motion *uniformly across the remaining parameters*. Equality belongs to the exclusion side.

The converse may be arranged with exactly one positive equilibrium, and that equilibrium is a hyperbolic repeller. No uniqueness or hyperbolicity of the resulting periodic orbit is asserted.

## Assumptions and scope
All seven coefficients are constant and strictly positive, \((x,y)\in(0,\infty)^2\), and the continuous-time differential equations are interpreted in their usual smooth sense. The threshold is a **universal-in-the-other-parameters** statement, not an if-and-only-if test for a particular fully specified parameter vector below the cutoff. The proof below gives an explicit open-parameter family realizing cycles and a rational parameter witness.

## Proof
### 1. Universal exclusion, including the equality boundary
Use the positive \(C^1\) Dulac multiplier \(B(x,y)=1/(xy)\) throughout the simply connected positive quadrant. Direct differentiation gives
\[
\begin{aligned}
\partial_x(B\dot x)+\partial_y(B\dot y)
&=-\frac{r}{ky}+\frac{a}{(x+b)^2}-\frac{\sigma}{x}\\
&\le -\frac{r}{ky}+\frac{a/(4b)-\sigma}{x},
\end{aligned}
\]
because \((x+b)^2-4bx=(x-b)^2\ge0\). For \(\sigma\ge a/(4b)\), the expression is strictly negative for all \(x,y>0\), even at equality because \(r/(ky)>0\). The Bendixson–Dulac theorem prohibits nonconstant periodic orbits in this quadrant.

### 2. A periodic orbit for every coefficient below the cutoff
Fix \(a,b>0\) and \(0<\sigma<a/(4b)\). Choose \(k>3b\) large enough that
\[
\sigma<\frac{a(k-3b)}{4b(k-b)}.
\]
This is possible because the right-hand side tends to \(a/(4b)\) as \(k\to\infty\). Choose any \(e\in(0,1)\), then \(r>0\) sufficiently small to satisfy simultaneously
\[
\frac{ea}{2}>\frac{2\sigma rb(k-b)}{ak},\qquad
\frac ra<\frac{4eab}{\sigma(k+b)^2},\qquad
r<\frac{ea^2k}{4\sigma b(k-3b)}.
\]
Define
\[
y_*=\frac{2rb(k-b)}{ak}>0,\qquad d=\frac{ea}{2}-\sigma y_*>0.
\]
The positive equilibrium equations are the intersections of the prey and predator nullclines
\[
g(x)=\frac{r(k-x)(b+x)}{ak},\qquad
h(x)=\frac{eax/(x+b)-d}{\sigma}, \quad 0<x<k.
\]
They meet at exactly \((b,y_*)\). To see uniqueness, note that \(h'(x)=eab/[\sigma(x+b)^2]>0\). On \(0<x<(k-b)/2\), \(g'(x)>0\), with \(g'(x)<r/a\), whereas
\[
h'(x)\ge\frac{4eab}{\sigma(k+b)^2}>\frac ra.
\]
On the remaining interval \((k-b)/2<x<k\), \(g'(x)\le0<h'(x)\). Thus \(g-h\) decreases strictly from a positive value at \(x=0\) to a negative value at \(x=k\) and has precisely one zero. No equilibrium with \(x\ge k\) can have \(y>0\), since the prey equation is then strictly negative.

At the unique positive equilibrium, the Jacobian is
\[
J_*=
\begin{pmatrix}
\dfrac{r(k-3b)}{2k}&-\dfrac a2\\[4pt]
\dfrac{er(k-b)}{2k}&-\dfrac{2\sigma rb(k-b)}{ak}
\end{pmatrix}.
\]
Its trace and determinant are
\[
\operatorname{tr}J_*=
\frac r k\left(\frac{k-3b}{2}-\frac{2\sigma b(k-b)}a\right)>0,
\]
\[
\det J_*=
y_*\left(\frac{ea^2}{8b}-\frac{\sigma r(k-3b)}{2k}\right)>0.
\]
The choice of \(k\) makes the trace positive; the final smallness condition on \(r\) makes the determinant positive. Hence the unique interior equilibrium is a hyperbolic repeller.

All positive forward solutions are bounded: comparison gives \(x(t)\le\max\{x(0),k\}\) and, since \(ea x/(x+b)<ea\), an analogous logistic upper bound on \(y(t)\). The axes are invariant. The boundary equilibria are \((0,0)\) and \((k,0)\); at \((0,0)\) the stable direction lies on the predator axis, and at \((k,0)\) it lies on the prey axis, because \(d<ea/2<eak/(k+b)\). Neither saddle has a stable separatrix in the positive interior, and there is no boundary heteroclinic loop. The planar Poincaré–Bendixson classification therefore rules out a boundary omega-limit set for a positive orbit. Starting at any positive point other than the repelling equilibrium, its bounded interior omega-limit set cannot equal the repeller and must contain a positive periodic orbit. This establishes existence without invoking a Hopf nondegeneracy assumption.

### 3. An exact rational witness
The following rational coefficients realize the converse:
\[
a=b=1,\quad\sigma=\tfrac15,\quad k=30,\quad
r=\tfrac1{100},\quad e=\tfrac12,\quad d=\tfrac{923}{3750}.
\]
The only positive equilibrium is \((1,29/1500)\), and its Jacobian satisfies
\[
\operatorname{tr}J_*=\frac{19}{30000}>0,
\qquad\det J_*=\frac{2233}{1875000}>0.
\]
The prey-only boundary state has a positive predator invasion exponent \(27637/116250\). Thus the exact parameter vector supports at least one positive periodic orbit. The inequalities used above are strict, so the witness also belongs to an open family with the same existence conclusion.

## Verification
The standalone file `verify.py` requires Python 3 and SymPy. Execute `python verify.py` in the directory containing the file. It verifies the general Dulac identity, the sharp denominator inequality, the derived equilibrium Jacobian, both sign formulas, and the rational witness using exact symbolic arithmetic. Expected output:

```text
VERIFY_OK symbolic_dulac=1 sharp_maximum=1 general_repeller=2 rational_witness=7
rational_witness trace=19/30000 determinant=2233/1875000 d=923/3750
```

The code checks finite algebraic identities, **not** the Bendixson–Dulac or Poincaré–Bendixson arguments for infinitely many trajectories. Those parts are analytical and appear above.

## Relationship to prior work
Chan-López, Martín-Ruiz, and Castellanos (2026), in their Section 3 and Theorem 8, characterize where a Bazykin coexistence equilibrium may undergo Hopf bifurcation: it must lie on the rising part of the prey nullcline. That is a local spectral localization theorem; it neither gives this competition-only all-parameter cutoff nor rules out finite-amplitude cycles above such a cutoff. The present statement excludes **all** positive cycles at and above the sharp level and realizes cycles at **every** smaller competition coefficient by varying the other positive parameters.

Wang and Yu (2021) analyze a broader Bazykin variant with an additional prey mortality term, using Dulac multipliers in restricted global-stability criteria (Theorems 2.1–2.2); the statement here is a distinct sharp universal parameter characterization. Liu (2005) develops geometric cycle-exclusion criteria for Gause-type systems without quadratic predator self-competition; those theorems do not directly cover the present equations. Lu and Huang (2021) conduct extensive global bifurcation analysis of this same model; their full text was not available in the inspected sources, making historical priority relative to that article an open limitation. The result relies on standard Dulac and planar Poincaré–Bendixson principles, so originality, if sustained, lies in the exact **sharp universal parameter threshold** and its realization on the opposing side, rather than either proof technique.

## Limitations
The absence result is global within the strictly positive quadrant but makes no statement about transient amplitudes. Below the cutoff the finding guarantees **existence for some positive parameters**, not existence for all choices. It does not prove uniqueness, stability, or a period formula for the surviving cycle. The sharp universal formulation may be implied by older global Bazykin theory not available in full text; further historical-priority verification is warranted. The nonlinear conclusions are for continuous time, not numerical time-stepping or spatially extended ecosystems.

## References
1. E. Chan-López, A. Martín-Ruiz, V. Castellanos, *Nullcline geometry constrains the location of oscillatory instabilities in planar predator–prey systems*, arXiv:2603.24418v1 (2026-03-25), revised arXiv:2603.24418v2 (2026-08-17), Section 3 and Theorem 8. https://arxiv.org/abs/2603.24418
2. S. Wang, H. Yu, *Stability and bifurcation analysis of the Bazykin's predator-prey ecosystem with Holling type II functional response*, Mathematical Biosciences and Engineering 18 (2021), 7877–7918, Theorems 2.1–2.2. https://www.aimspress.com/aimspress-data/mbe/2021/6/PDF/mbe-18-06-391.pdf
3. Y. Liu, *Geometric criteria for the nonexistence of cycles in Gause-type predator-prey systems*, Proceedings of the American Mathematical Society 133 (2005), 3619–3626, DOI:10.1090/S0002-9939-05-08026-3.
4. M. Lu, J. Huang, *Global analysis in Bazykin's model with Holling II functional response and predator competition*, Journal of Differential Equations 280 (2021), 99–138, DOI:10.1016/j.jde.2021.01.025 (abstract examined, full text unavailable).
5. Bendixson–Dulac theorem and Poincaré–Bendixson theorem, standard planar dynamical-systems results.
