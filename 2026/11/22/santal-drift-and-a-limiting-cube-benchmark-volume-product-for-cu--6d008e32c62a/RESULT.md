# Santaló drift and a limiting cube-benchmark volume product for cubical Cayley polytopes

## Finding
For an integer \(d\ge1\), put \(B_\infty^d=[-1,1]^d\) and \(B_1^d=\{x\in\mathbb R^d:\|x\|_1\le1\}\). Consider the full-dimensional, generally non-centrally-symmetric \((d+1)\)-polytope
\[
C_d=\operatorname{conv}\big((B_\infty^d\times\{1\})\cup(B_1^d\times\{-1\})\big).
\]
Write \(s(C_d)\) for its unique **Santaló point**, the center \(y\in\operatorname{int}C_d\) minimizing \(\operatorname{vol}_{d+1}((C_d-y)^\circ)\), and put \(\mathcal M(C_d)=\operatorname{vol}_{d+1}(C_d)\operatorname{vol}_{d+1}((C_d-s(C_d))^\circ)\).

**Theorem (complete axial Santaló law).** For every \(d\ge1\), the Santaló point is \(s(C_d)=(0,\tau_d)\). Here \(\tau_1=0\); for each \(d\ge2\), the number \(\tau_d\in(0,1)\) is the **unique** solution of
\[
\sum_{j=1}^{d}\frac{j-1}{j+1+(j-1)\tau_d}
=\frac{2\tau_d}{1-\tau_d^2}.
\]
The sequence \((\tau_d)_{d\ge1}\) is strictly increasing, and
\[
1-\tau_d=\frac{2}{d}+O\!\left(\frac{\log d}{d^2}\right).
\]
In the stated standard Euclidean coordinate normalization,
\[
\operatorname{vol}_{d+1}(C_d)=\frac{2^{d+1}}{d+1}\sum_{k=0}^d\frac1{k!},
\]
\[
\operatorname{vol}_{d+1}((C_d-(0,t))^\circ)
=\frac{2^{2d+1}}{(d+1)(1-t^2)\displaystyle\prod_{j=1}^d\big(j+1+(j-1)t\big)},\qquad -1<t<1.
\]
These yield the exact Santaló volume product for **every** \(d\), via substitution \(t=\tau_d\). Relative to the volume product \(4^{d+1}/(d+1)!\) of the \((d+1)\)-cube, one has the sharp asymptotic
\[
\boxed{\displaystyle
\lim_{d\to\infty}\frac{\mathcal M(C_d)}{4^{d+1}/(d+1)!}=\frac{e^2}{4}.}
\]
At \(d=2\) the center and product simplify exactly to
\[
\tau_2=\frac2{\sqrt3}-1,\qquad \mathcal M(C_2)=\frac{20}{\sqrt3}.
\]
The normalization by a cube is a comparison with an explicit polytope, **not** an assertion of any general Mahler lower bound for nonsymmetric bodies.

## Assumptions and scope
The ambient space is \(\mathbb R^{d+1}\) with its standard pairing and Lebesgue volume. Polar means \(K^\circ=\{u:\langle u,v\rangle\le1\ \forall v\in K\}\). Each layer is placed at the stated height, without rescaling the cube or cross-polytope. The Santaló point is computed for the **Cayley body** \(C_d\), not for its polar in the original origin placement. The case \(d=1\) is the symmetric square and is included as a boundary case. The limit refers to integer \(d\to\infty\); no finite-dimensional extremal assertion among arbitrary polytopes is made.

## Proof
**1. Strict uniqueness and symmetry of the center.** For a full-dimensional convex body \(C\subset\mathbb R^m\) and \(y\in\operatorname{int}C\), the polar volume has the radial representation
\[
\operatorname{vol}_m((C-y)^\circ)=\frac1m\int_{S^{m-1}}(h_C(u)-\langle y,u\rangle)^{-m}\,d\sigma(u).
\]
Each integrand is strictly convex in \(y\) whenever \(\langle y,u\rangle\) varies, so integration gives strict convexity; the volume diverges as \(y\to\partial C\). Thus the minimizer is unique. Signed coordinate permutations in the first \(d\) coordinates preserve \(C_d\); their common fixed set is the vertical axis. Hence its Santaló point is \((0,t)\) for some \(-1<t<1\).

**2. Exact Cayley volume.** For \(a,b\ge0\), membership in \(aB_\infty^d+bB_1^d\) is equivalent to \(\sum_i(|x_i|-a)_+\le b\). In each orthant, choose the \(k\) coordinates with \(|x_i|>a\); the excess coordinates fill a \(k\)-simplex of volume \(b^k/k!\), and the other coordinates lie in intervals of length \(a\). Boundary overlaps have zero volume. Consequently
\[
\operatorname{vol}_d(aB_\infty^d+bB_1^d)
=2^d\sum_{k=0}^d\binom dk\frac{a^{d-k}b^k}{k!}.
\]
The height slice of \(C_d\) at \(z=2\lambda-1\) is \(\lambda B_\infty^d+(1-\lambda)B_1^d\). Integrate \(0\le\lambda\le1\) with height factor \(2\) and apply
\(\int_0^1\lambda^{d-k}(1-\lambda)^k\,d\lambda=(d-k)!k!/(d+1)!\). This proves the first volume formula.

**3. Exact shifted polar volume.** The cube and cross-polytope support functions are \(\|u\|_1\) and \(\|u\|_\infty\). In coordinates \((u,v)\) dual to \((x,z)\), the polar of \(C_d-(0,t)\) is specified by
\[
\|u\|_1+(1-t)v\le1,\qquad
\|u\|_\infty-(1+t)v\le1.
\]
The length of its vertical fiber is therefore
\[
\frac{\big(2-(1+t)\|u\|_1-(1-t)\|u\|_\infty\big)_+}{1-t^2}.
\]
For \(a,b>0\), partition the unit ball of the norm \(N(u)=a\|u\|_1+b\|u\|_\infty\) into its \(2^dd!\) sign/order chambers. In the chamber \(u_1\ge\cdots\ge u_d\ge0\), the determinant-one substitution \(w_j=u_j-u_{j+1}\), with \(u_{d+1}=0\), converts \(N(u)\le1\) into the simplex inequality \(\sum_{j=1}^d(aj+b)w_j\le1\). Thus
\[
\operatorname{vol}_d\{N\le1\}=\frac{2^d}{\prod_{j=1}^d(aj+b)}.
\]
For any such homogeneous norm, the layer-cake identity gives
\(\int_{\mathbb R^d}(2-N(u))_+\,du=\frac{2^{d+1}}{d+1}\operatorname{vol}_d\{N\le1\}\). Substitution \(a=1+t\), \(b=1-t\) proves the polar-volume formula.

**4. Unique center, strict dimension monotonicity.** Let
\[
F_d(t)=(1-t^2)\prod_{j=1}^d\big(j+1+(j-1)t\big).
\]
Minimizing polar volume is equivalent to maximizing \(F_d\). Its logarithmic derivative is the left side minus the right side of the stationarity equation. Its second logarithmic derivative is
\[
-\frac{2(1+t^2)}{(1-t^2)^2}
-\sum_{j=1}^d\frac{(j-1)^2}{(j+1+(j-1)t)^2}<0.
\]
For \(d\ge2\), the first derivative at zero is strictly positive, while it tends to \(-\infty\) as \(t\uparrow1\); hence there is one critical point in \((0,1)\), necessarily the unique global maximum. At \(d=1\) the maximum is \(t=0\). Passing from \(d\) to \(d+1\) adds the positive summand \(d/(d+2+dt)\) to the logarithmic derivative, so its unique zero strictly increases.

**5. Sharp asymptotic drift.** Put \(\delta_d=1-\tau_d\) and \(H_d=\sum_{j=1}^d1/j\). Stationarity is exactly
\[
\frac1{\delta_d}=\frac1{2-\delta_d}+\sum_{j=1}^d\frac{j-1}{2j-(j-1)\delta_d}.
\]
Every summand is at least \((j-1)/(2j)\), giving \(\delta_d\le2/(d-H_d+1)\). Therefore \(\delta_d=O(1/d)\). Expanding the summands uniformly for \(\delta_d=O(1/d)\) yields
\[
\frac1{\delta_d}=\frac{d-H_d}{2}+O(1)=\frac d2+O(\log d),
\]
which rearranges to \(\delta_d=2/d+O((\log d)/d^2)\).

**6. Exact Mahler product and normalized limit.** Write \(E_d=\sum_{k=0}^d1/k!\) and \(a_j=(j-1)/(2j)\). Multiplying the formulas in Steps 2–3 and comparing to the \((d+1)\)-cube gives the exact identity
\[
\frac{\mathcal M(C_d)}{4^{d+1}/(d+1)!}
=\frac{E_d}{(d+1)\delta_d(2-\delta_d)}
\prod_{j=1}^d(1-a_j\delta_d)^{-1}.
\]
Here \(E_d\to e\), the denominator preceding the product tends to \(4\), and
\[
\log\prod_{j=1}^d(1-a_j\delta_d)^{-1}
=\delta_d\sum_{j=1}^d a_j+O(d\delta_d^2)
=\delta_d\frac{d-H_d}{2}+o(1)\longrightarrow1.
\]
Thus the product tends to \(e\), proving the limiting factor \(e^2/4\). For \(d=2\), the stationary equation is \(3\tau^2+6\tau-1=0\); the indicated root and exact product follow by substitution. All asserted claims now follow.

## Verification
Run `python checker.py` in the extracted package directory. The standard-library portion makes 96 exact-rational integrations and Beta-integral checks in dimensions \(1\) through \(16\), checks stationary roots and strict increases through dimension \(63\), and compares the dimension-two closed form and the asymptotic normalized ratio. When NumPy and SciPy are present, 16 further cases compute actual convex-hull and halfspace-intersection volumes in dimensions \(2\) through \(5\), independently of the integration formula. All checks passed in the package-building environment. The universal claims follow from the six analytic steps, not from these bounded computations.

## Relationship to prior work
Pavlík (arXiv:2611.13896, §§2 and 5) introduced the polar Cayley realization of bipolar face lattices and proved that cubes and cross-polytopes meet the requisite interval condition, but does not give the Santaló center or affine volume product of these realizations. The publicly available record *An Ehrhart quasiperiod reversal for a cube–cross-polytope Cayley polar* treats precisely the origin polar \(K_d=C_d^\circ\), including the **already-known** volume at \(t=0\); that part of Step 3 is not asserted original. Its claims concern Ehrhart series and quasiperiods, not the shifted polar, Santaló center, or limit above. Pavlov and Telen's general Santaló geometry gives the existence and rational-volume framework, not this infinite-family evaluation. A previously recorded analogous Santaló result for Cayley joins of regular simplices concerns a different layer pair and does not imply the cube-specific product or constant. The contribution here is the all-dimensional **optimal center**, its monotone drift, and the explicit Santaló volume-product limit \(e^2/4\).

## Limitations
The center and product are for the exact standard cube/cross-polytope Cayley hull, not arbitrary bipolar realizations. The asymptotic comparison uses the cube's volume product only as a reference; since \(C_d\) is not generally symmetric, no universal lower-bound claim is made. Finite numerical checks do not establish uniqueness or the limit; the analytic derivation does. Historical novelty is based on identified public literature and records, not a proof against all unpublished or unindexed results. Independent mathematical audit has not been performed.

## References
- Jan Pavlík, *Face lattices of polytopes and bipolar polytopes*, arXiv:2611.13896v1, first public 2026-11-10, https://arxiv.org/abs/2611.13896 (especially Theorems 5.2 and 5.8).
- Dmitrii Pavlov and Simon Telen, *Santaló Geometry of Convex Polytopes*, arXiv:2402.18955, first public 2024-02-29, https://arxiv.org/abs/2402.18955 (strict convexity and rational dual-volume framework).
- Public mathematical record, *An Ehrhart quasiperiod reversal for a cube–cross-polytope Cayley polar*, https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-an-ehrhart-quasiperiod-reversal-for-a-cube-cross-polytope-cayley--afb298f7e006/RESULT.md (identical unshifted polar and previously obtained volume).
