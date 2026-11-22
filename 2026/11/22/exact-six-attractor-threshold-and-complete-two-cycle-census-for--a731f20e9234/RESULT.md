# Exact six-attractor threshold and complete two-cycle census for cubic implicit Euler

## Finding

For the backward-Euler relation of the scalar double-well gradient equation
\[
\dot u=u-u^3,\qquad x_n=H_h(x_{n+1}),\qquad H_h(t)=(1-h)t+ht^3,\quad h>0,
\]
there are exactly zero, one, or three distinct real primitive period-two orbits (up to cyclic interchange): zero for \(0<h\le2\), one for \(2<h\le3\), and three for \(h>3\). For \(h>2\), the antipodal orbit is
\[
\{\sqrt{1-2/h},-\sqrt{1-2/h}\}.
\]
For \(h>3\), the other two orbits are
\[
\left\{\frac{\epsilon\sqrt{1-3/h}+\sqrt{1+1/h}}2,
\frac{\epsilon\sqrt{1-3/h}-\sqrt{1+1/h}}2\right\},\quad \epsilon\in\{-1,1\}.
\]
At forward-regular points, their exact two-step multipliers are, respectively,
\[
M_{\rm anti}=(2h-5)^{-2},\qquad
M_{\rm asym}=[9-2(h-1)^2]^{-1}.
\]
The two symmetry-breaking cycles are forward singular at \(h=1+3/\sqrt2\), have multiplier \(-1\) at \(h=1+\sqrt5\), and are locally attracting precisely for \(h>1+\sqrt5\). The antipodal two-cycle is locally attracting precisely for \(h>3\). The three constant solutions \(-1,0,1\) are also locally attracting for every \(h>1+\sqrt5\). Hence **the first step interval exhibiting six distinct locally attracting periodic orbits of periods one or two is exactly \(h>1+\sqrt5\)**. None of the three nonconstant cycles is a periodic trajectory of the underlying one-dimensional autonomous differential equation.

## Assumptions and scope

All states and step sizes are real, with \(h>0\). An admissible primitive period-two orbit is an unordered pair of distinct real states \(\{x,y\}\) satisfying \(x=H_h(y)\) and \(y=H_h(x)\). A forward transition \(x\mapsto y\) is **locally regular** when \(H_h'(y)\ne0\); the inverse-function theorem then defines the local forward successor near that transition. A **locally attracting periodic orbit** means there exists a neighborhood of this particular ordered cycle on which its selected smooth local successor branches produce an attracting periodic orbit, not that the algebraic step has a unique global successor or that an arbitrary nonlinear solver selects it. A two-cycle with a singular forward transition is not assigned a finite forward Floquet multiplier. Other periods are not classified.

## Proof

**All primitive cycles.** Set \(R_x=x-H_h(y)\) and \(R_y=y-H_h(x)\). Exact polynomial factorization yields
\[
R_x-R_y=(x-y)\{2-h+h(x^2+xy+y^2)\},
\]
\[
R_x+R_y=-h(x+y)(x^2-xy+y^2-1).
\]
For a period-two orbit \(x\ne y\), these vanish, so
\[
x^2+xy+y^2=1-2/h,
\]
and either \(x+y=0\) or \(x^2-xy+y^2=1\). If \(x+y=0\), then \(x^2=1-2/h\), providing exactly one unordered nonconstant cycle when \(h>2\). If \(x+y\ne0\), subtracting the two quadratic conditions gives \(xy=-1/h\); it follows that
\[
(x+y)^2=1-3/h,\qquad(x-y)^2=1+1/h.
\]
Thus \(h>3\) is necessary. The two choices of the nonzero sum and the exchange symmetry give exactly the two displayed unordered cycles. Conversely, substituting each displayed pair into both factorized equations (or directly into \(R_x=R_y=0\)) establishes sufficiency. At \(h=3\) the two sum choices coalesce with the antipodal cycle, so no additional primitive cycle occurs. This is an exhaustive algebraic classification over the reals, not a finite sampling argument.

An independent factorization of the same full two-step polynomial gives
\[
H_h(H_h(t))-t=h\,t(t-1)(t+1)(ht^2-h+2)
\bigl(h^2t^4-h^2t^2+ht^2+1\bigr).
\]
The last factor is quadratic in \(t^2\), with discriminant \(h^2(h-3)(h+1)\); this independently confirms that the four asymmetric points occur precisely for \(h>3\) and merge with the antipodal pair at \(h=3\).

**Floquet multipliers and thresholds.** At a forward-regular transition, differentiating \(x=H_h(y)\) gives \(dy/dx=1/H_h'(y)\), where \(H_h'(z)=1-h+3hz^2\). Consequently the two-step multiplier of the orbit \(\{x,y\}\) is \(1/[H_h'(x)H_h'(y)]\). On the antipodal pair, both factors equal \(2h-5\), so the multiplier is \((2h-5)^{-2}\); its two transitions are singular at \(h=5/2\), and the multiplier magnitude is less than one if and only if \(h>3\) within its existence range. On the asymmetric pair, \(x^2+y^2=1-1/h\) and \(xy=-1/h\), giving
\[
H_h'(x)H_h'(y)=(1-h)^2+3h(1-h)(x^2+y^2)+9h^2x^2y^2
=9-2(h-1)^2.
\]
This product equals zero at \(h=1+3/\sqrt2\), equals \(-1\) at \(h=1+\sqrt5\), and is strictly below \(-1\) thereafter. For \(3<h<1+\sqrt5\), away from the singular point, its absolute value is strictly below one, hence the inverse two-step multiplier has magnitude greater than one. At the singular parameter a smooth forward return is unavailable. Exactly at \(h=1+\sqrt5\), the multiplier equals \(-1\). Thus the two asymmetric cycles become regular locally attracting cycles precisely for \(h>1+\sqrt5\).

**Fixed points and the six-attractor boundary.** The fixed-point equation is \(hz(z^2-1)=0\), hence exactly \(-1,0,1\). Their local forward multipliers are \((1+2h)^{-1}\) at \(\pm1\), and \((1-h)^{-1}\) at zero whenever regular. The first two are attracting for all \(h>0\); zero is attracting precisely when \(h>2\), is singular at \(h=1\), and is neutral at \(h=2\). Consequently all three fixed points and all three primitive two-cycles are attracting simultaneously precisely when \(h>1+\sqrt5\). For lesser steps there are either fewer primitive cycles or at least one nonattracting/singular asymmetric orbit; equality gives a neutral \(-1\) multiplier. Their attraction is local to the chosen implicit branches.

## Verification

Execute `python3 verify.py` using Python 3.10+ and SymPy. The checker reproduces both exact polynomial factorizations, all explicit orbit identities and multiplier formulas over rational step values, as well as the radical fold/flip thresholds and fixed-point conditions; in the supplied run it passed 105 exact symbolic checks. The analytic factorization, inequality arguments and inverse-function theorem prove the continuum-of-parameters assertions. Symbolic test values alone are not a completeness proof.

## Relationship to prior work

Oliveira (2026, arXiv:2611.03336v1, primary MSC 37G15) establishes a general cyclic bifurcation framework for implicit maps, not this exact global census. Buescu and Oliveira (2026, arXiv:2611.12327v1, Section 7.6) analyze the same cubic backward-Euler component in a planar mixed fold/flip example, exhibit the antipodal orbit for \(h>2\), and calculate its longitudinal multiplier \((2h-5)^{-2}\); the two asymmetric cycles, their threshold \(h>3\), their complete forward multipliers, and the all-six-attracting threshold are not derived there. Stuart and Peplow (1991) describe spurious two-cycles and include a backward-Euler example for a different cubic equation, while Oliveira (2016, arXiv:1608.01898v1) treats a different scalar fifth-degree equation. A 2026 analysis of the bounded-past repeller of exactly this cubic step proves a three-symbol coding for \(h\ge64\), which entails three primitive two-cycles for sufficiently large steps; it does not determine the sharp finite-step census, the singular crossing or the all-six-sink threshold. General implicit-step multivaluedness is known and not claimed as novel.

## Limitations

The result concerns algebraically admissible period-one and period-two orbits and local selections of smooth implicit successor branches. It neither guarantees which branch a numerical root finder selects nor gives global basins or counts of higher periods. At singular steps the local successor can be multivalued or fail to exist and no finite forward multiplier is assigned. General spurious-periodic-orbit theory is substantial and may contain an earlier equivalent specialization; full historical priority needs external review. No independent mathematical audit has been performed.

## References

1. H. M. Oliveira, *Lyapunov–Schmidt reduction for periodic orbits of implicit discrete dynamical systems*, arXiv:2611.03336v1 (2 November 2026), https://arxiv.org/html/2611.03336v1.
2. J. Buescu and H. M. Oliveira, *Singular bifurcations in implicit discrete dynamical systems*, arXiv:2611.12327v1 (9 November 2026), https://arxiv.org/html/2611.12327v1.
3. A. M. Stuart and A. T. Peplow, *The Dynamics of the Theta Method*, SIAM J. Sci. Stat. Comput. 12 (1991), 1351–1372, https://doi.org/10.1137/0912074.
4. H. M. Oliveira, *Bifurcation equations for periodic orbits of implicit discrete dynamical systems*, arXiv:1608.01898v1 (5 August 2016), https://arxiv.org/abs/1608.01898.
5. K. R. Green, G. W. Patrick and R. J. Spiteri, *On theoretical upper limits for valid timesteps of implicit ODE methods*, AIMS Mathematics 4 (2019), 1841–1853, https://doi.org/10.3934/math.2019.6.1841.
6. *A three-symbol past repeller and a three-term dimension law for an implicit cubic step*, (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-three-symbol-past-repeller-and-a-three-term-dimension-law-for--b1fdedf22da7.
