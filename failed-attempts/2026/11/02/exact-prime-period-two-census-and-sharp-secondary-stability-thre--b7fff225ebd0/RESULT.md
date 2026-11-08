# Exact prime-period-two census and sharp secondary stability threshold for a rational kinetic map

## Finding

Consider the real scalar map
\[
T_h(x)=x-\frac{hx}{1+x^2},\qquad h>0,\quad x\in\mathbb R.
\]
Its **complete set of distinct prime-period-two orbits** is as follows.

1. For \(0<h\le2\) there are no prime-period-two orbits.
2. For \(h>2\) there is exactly one symmetric orbit
\[
\mathcal C_{\mathrm{sym}}=\{-s,s\},\qquad s=\sqrt{h/2-1},
\]
with two-step multiplier \(\mu_{\mathrm{sym}}=(3-8/h)^2\). It is linearly attracting exactly when \(2<h<4\), nonhyperbolic at \(h=4\), and repelling when \(h>4\).
3. For \(h>4\), and only then, there are exactly two **additional** distinct asymmetric prime-period-two orbits
\[
\mathcal C_+=\{u_+,-u_-\},\qquad
\mathcal C_-=\{u_-,-u_+\},\qquad
u_\pm=\frac{\sqrt h\pm\sqrt{h-4}}2.
\]
Both have the exact two-step multiplier
\[
\mu_{\mathrm{asym}}=9-2h.
\]
They are linearly attracting exactly for \(4<h<5\), nonhyperbolic with multiplier \(-1\) at \(h=5\), and repelling for \(h>5\).

There are no other real prime-period-two orbits. The value \(h=5\) is the **sharp secondary linear-stability threshold** of the asymmetric period-two branches. At \(h=4\), their formulas coincide with the symmetric orbit rather than produce separate cycles.

## Assumptions and scope

The system is the exact one-dimensional, momentum-free kinetic-map reduction with rational speed \(\phi(x)=x/(1+x^2)\) and gain \(h>0\). A prime-period-two orbit is an unordered pair \(\{x,y\}\) of distinct real numbers such that \(T_h(x)=y\) and \(T_h(y)=x\). Its multiplier is \(T_h'(x)T_h'(y)\). The terms *linearly attracting* and *repelling* refer to the modulus of that multiplier being strictly below and strictly above one, respectively; no nonlinear classification is claimed at a unit-modulus multiplier. The model omits moving-average momentum, stochasticity and floor-clipping of the speed multiplier.

## Proof

**Exact factorization and exhaustiveness.** Put \(q=1+x^2>0\) and \(p=x(q-h)\), so that \(T_h(x)=p/q\). Direct rational algebra gives
\[
T_h^2(x)-x=\frac{-h x\,[2(1+x^2)-h]\,[(1+x^2)^2-hx^2]}{(1+x^2)\{(1+x^2)^2+x^2(1+x^2-h)^2\}}.
\]
The denominator is strictly positive for every real \(x\), and \(h>0\). Consequently every point of period dividing two is either \(x=0\), a root of \(2(1+x^2)=h\), or a root of \((1+x^2)^2=hx^2\). The only fixed point is \(x=0\), since \(T_h(x)-x=-hx/(1+x^2)\).

The middle factor gives precisely \(x=\pm\sqrt{h/2-1}\) for \(h\ge2\). It gives two *distinct* points only for \(h>2\), and each maps to its negative by the defining relation. The final factor, for \(x\ne0\), is equivalent to \((|x|+|x|^{-1})^2=h\). Since \(|x|+|x|^{-1}\ge2\), it has real roots only when \(h\ge4\). For \(h>4\) the positive roots are \(u_+\) and \(u_-\) as displayed, with \(u_+u_-=1\) and \(u_++u_-=\sqrt h\). Directly, \(T_h(u_+)=-u_-\) and \(T_h(u_-)=-u_+\); oddness provides the other two transitions. These four points form two distinct prime-period-two orbits. At \(h=4\), \(u_+=u_-=1\) and only the already counted symmetric orbit remains. This exhausts all roots of the period-two equation and all possibilities for \(h>0\).

**Multipliers.** Differentiating gives
\[
T_h'(x)=1-\frac{h(1-x^2)}{(1+x^2)^2}.
\]
On the symmetric orbit, \(h=2(1+s^2)\), so \(T_h'(s)=T_h'(-s)=3-8/h\); this gives \(\mu_{\mathrm{sym}}\). For \(h>2\), the strict inequality \(|3-8/h|<1\) holds exactly on \(2<h<4\), while \(3-8/h>1\) when \(h>4\).

On an asymmetric orbit take \(u,v>0\) such that \(uv=1\) and \(u+v=\sqrt h\). Then \(h=(1+u^2)(1+v^2)\). Substitution into the derivative formula yields \(T_h'(u)=2-v^2\) and \(T_h'(-v)=2-u^2\). Therefore
\[
\mu_{\mathrm{asym}}=(2-u^2)(2-v^2)
=4-2(u^2+v^2)+(uv)^2=9-2h,
\]
because \(u^2+v^2=h-2\). The criterion \(|9-2h|<1\), together with \(h>4\), is equivalent to \(4<h<5\). Equality \(\mu_{\mathrm{asym}}=-1\) occurs precisely at \(h=5\), and \(\mu_{\mathrm{asym}}<-1\) above it. This proves every assertion.

## Verification

A standalone standard-library program, `verify.py`, verifies the numerator factorization as an identity of bivariate integer polynomials and checks derivative/multiplier identities with exact rational arithmetic. It also checks five parameter instances by floating-point substitution, solely as a diagnostic. Execute `python3 verify.py` from a directory containing the program. The full classification and its parameter quantifiers are justified by the factorization and sign arguments above; finite numerical checks are not a substitute for that proof.

## Relationship to prior work

Itin, *Physics-Inspired Optimizers beyond the Edge of Stability* (arXiv:2610.27321v1, posted 2026-10-19), §2.2, Fig. 1, §3 and Appendix A, introduces the same reduced momentum-free velocity-regularized map, proves the symmetric orbit formula and its \(2<h<4\) linear-stability range, and reports asymmetric cycles after \(h=4\) numerically. Those aspects are **prior results**, not contributions of this note. The contribution here is the algebraically exhaustive real prime-period-two census, exact asymmetric coordinates and multiplier, and the sharp second boundary \(h=5\).

Ma–Kunin–Wu–Ying, arXiv:2204.11326, establish global convergence to a symmetric two-cycle for a different class with strictly decreasing curvature. The logarithmic potential corresponding to the present update has \(f''(x)=(1-x^2)/(1+x^2)^2\), which is not strictly decreasing in \(|x|\) throughout the real line, and their theorem does not cover this period-two diagram. Yuan–Wen, *Separation Laws for Flip Bifurcations and Endogenous Switching Boundaries in Gradient Maps* (2026), study gradient clipping and generic flip contact; their results do not give this rational map's exact asymmetric cycles or multiplier. The original VRAdam paper by Vaidhyanathan and coauthors (arXiv:2505.13196) introduces the optimizer/damping mechanism rather than this complete rational period-two classification.

## Limitations

The result is about prime-period-two orbits only. No claim is made about all longer cycles, chaos, basins of attraction, or the existence or criticality of a period-four bifurcation at \(h=5\). The linear result at \(h=5\) does not determine nonlinear stability. A historical source with stronger explicit coverage could still affect priority; the closest identified full-text comparisons are described above.

## References

- A. Itin, *Physics-Inspired Optimizers beyond the Edge of Stability: Period-Two Orbits and Delayed Instability*, arXiv:2610.27321v1 (first posted 2026-10-19). https://arxiv.org/abs/2610.27321
- C. Ma, D. Kunin, L. Wu and L. Ying, *Beyond the Quadratic Approximation: The Multiscale Structure of Neural Network Loss Landscapes*, arXiv:2204.11326 (first posted 2022-04-24). https://arxiv.org/abs/2204.11326
- Z. Yuan and X. Wen, *Separation Laws for Flip Bifurcations and Endogenous Switching Boundaries in Gradient Maps*, Preprints.org 202610.0191v2 (posted 2026-10-12). https://www.preprints.org/manuscript/202610.0191
- P. Vaidhyanathan, L. Schorling, N. Ares and M. A. Osborne, *A Physics-Inspired Optimizer: Velocity Regularized Adam*, arXiv:2505.13196 (first posted 2025-05-19). https://arxiv.org/abs/2505.13196
