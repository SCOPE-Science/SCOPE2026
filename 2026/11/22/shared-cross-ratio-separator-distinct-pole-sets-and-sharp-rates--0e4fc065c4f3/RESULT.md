# Shared cross-ratio separator, distinct pole sets, and sharp rates in quadratic Ehrlich–Aberth iteration

## Finding
For a quadratic polynomial with two distinct complex roots, the simultaneous (Jacobi) and cyclic (Gauss–Seidel, first coordinate first) Ehrlich–Aberth maps have the same cross-ratio criterion for selecting the limiting root ordering on their respective forward-regular nonroot domains. Their finite-pole exceptional sets are different. The common generic basin separator is one real-algebraic cross-ratio modulus condition, but the precise convergence rates differ: the Jacobi cross ratio is cubed per sweep, whereas the cyclic cross ratio is raised to its fourth power. Both versions have nonroot cycles of every least period at least two, none of which is attracting.

Writing the initial cross ratio as
\[
r_0=\frac{(x_0-\alpha)(y_0-\beta)}{(x_0-\beta)(y_0-\alpha)},
\]
we obtain convergence to \((\alpha,\beta)\) when \(|r_0|<1\), and to \((\beta,\alpha)\) when \(|r_0|>1\), for every orbit that is defined for all sweeps. For \(|r_0|=1\), no forward-regular nonroot orbit converges to either root permutation. Moreover, with the dimensionless maximum root error \(E_k\) defined below,
\[
\lim_{k\to\infty}\frac{1}{q^k}\log\frac{1}{E_k}
=\frac{|\log|r_0||}{q-1},\qquad
q=\begin{cases}3&\text{Jacobi},\\4&\text{cyclic Gauss--Seidel}.\end{cases}
\]
In particular the exact double-logarithmic exponents are \(\log3\) and \(\log4\), respectively.

## Assumptions and scope
Let \(p(z)=(z-\alpha)(z-\beta)\), with \(\alpha,\beta\in\mathbb C\) and \(\alpha\ne\beta\). The elementary Ehrlich–Aberth coordinate update, in denominator-cleared rational form, is
\[
F_p(z;w)=z-\frac{p(z)(z-w)}{p'(z)(z-w)-p(z)}.
\]
The Jacobi full sweep updates both old coordinates in parallel:
\[
J(x,y)=(F_p(x;y),F_p(y;x)).
\]
The cyclic sweep updates the first coordinate and uses it immediately in the second update:
\[
G(x,y)=(X,F_p(y;X)),\qquad X=F_p(x;y).
\]
Both are considered in exact complex arithmetic on their natural finite, noncolliding domains. A *forward-regular nonroot orbit* starts with finite distinct \(x_0,y_0\notin\{\alpha,\beta\}\), remains finite and distinct on every full sweep, and, in the cyclic case, also avoids an equality between the newly updated first coordinate and the old second coordinate. Rational continuation at a cancellation is understood only when the displayed rational map is well-defined; this theorem does not assign values to genuine poles.

Set
\[
a_k=\frac{x_k-\alpha}{x_k-\beta},\quad
b_k=\frac{y_k-\alpha}{y_k-\beta},\quad
r_k=\frac{a_k}{b_k},\quad
N_k(q)=\frac{q^k-1}{q-1}.
\]
For the two basins, define \((X_*,Y_*)=(\alpha,\beta)\) if \(|r_0|<1\), and \((X_*,Y_*)=(\beta,\alpha)\) if \(|r_0|>1\). Define
\[
E_k=\frac{\max\{|x_k-X_*|,|y_k-Y_*|\}}{|\alpha-\beta|}.
\]
The rate formula concerns sufficiently large \(k\), for which \(0<E_k<1\).

## Proof
**1. Exact conjugacy.** The affine change of variable sending the roots to \(1\) and \(-1\) commutes with the rational update. For \(p(z)=z^2-1\), direct denominator clearing gives
\[
F_p(x;y)=-\frac{x^2y-2x+y}{x^2-2xy+1}.
\]
Substitute \(x=(1+a)/(1-a)\) and \(y=(1+b)/(1-b)\). The cross-ratio coordinate of the updated first component is exactly \(a^2/b\). The updated second component under Jacobi is \(b^2/a\). Under a cyclic sweep it is instead \(b^2/(a^2/b)=b^3/a^2\). Therefore the two maps on nonzero cross-ratio coordinates are
\[
J:(a,b)\longmapsto(a^2/b,b^2/a),\qquad
G:(a,b)\longmapsto(a^2/b,b^3/a^2).
\]
In particular \(ab\) is invariant for Jacobi and \(a^2b\) for cyclic updates.

**2. Closed forms.** Division of the two transformed coordinates yields \(r_{k+1}=r_k^3\) for Jacobi and \(r_{k+1}=r_k^4\) for cyclic updates. Consequently, for every regular iterate,
\[
r_k=r_0^{q^k},\qquad a_k=a_0r_0^{N_k(q)},\qquad
b_k=b_0r_0^{-\delta N_k(q)},
\]
where \((q,\delta)=(3,1)\) or \((4,2)\). These identities follow by induction from the exact one-step formulas; they are not numerical extrapolations.

**3. Basins and sharp rate.** The inverse coordinate is \(z=(\alpha-\beta a)/(1-a)\). If \(|r_0|<1\), then \(|a_k|\to0\) and \(|b_k|\to\infty\), hence \(x_k\to\alpha\) and \(y_k\to\beta\). If \(|r_0|>1\), the two limits are reversed. In either case \(|r_0|^{N_k(q)}\) has logarithm \(-N_k(q)|\log|r_0||\) in the decaying direction. The inverse-coordinate identities
\[
\frac{x-\alpha}{\alpha-\beta}=\frac{a}{1-a},\qquad
\frac{x-\beta}{\alpha-\beta}=\frac{1}{1-a}
\]
(and their versions for \(y,b\)) show that the slower of the two root errors is asymptotically a positive constant times \(|r_0|^{N_k(q)}\) or its reciprocal in the appropriate branch. The other error has the same exponent for Jacobi and twice that exponent for the cyclic map. Thus
\[
\log(1/E_k)=N_k(q)|\log|r_0||+O(1),
\]
and division by \(q^k\) gives the stated exact coefficient. Taking logarithms once more gives \(k^{-1}\log\log(1/E_k)\to\log q\).

If \(|r_0|=1\), both \(|a_k|=|a_0|\) and \(|b_k|=|b_0|\) remain fixed, nonzero and finite. Neither coordinate can therefore approach either root (which would require its transformed modulus to tend to zero or infinity). The basin separator follows. Outside this separator, the only other failures of forward regularity arise on the explicit, variant-dependent finite-pole preimages
\[
a_0r_0^{N_k(q)}=1\quad\text{or}\quad
b_0r_0^{-\delta N_k(q)}=1
\]
for some nonnegative integer \(k\). These lie in a countable union of proper complex algebraic sets in the finite nonroot parameter domain. For each variant the convergence regions are open, by uniform tail convergence on neighborhoods bounded away from \(|r_0|=1\), and their union is dense and has full real four-dimensional Lebesgue measure. These open sets are not literally identical between variants: with \(p(z)=z^2-1\), the initial transformed pair \((a_0,b_0)=(4,2)\) makes the parallel second coordinate infinite after one sweep, whereas the cyclic orbit is regular and converges to \((-1,1)\). Conversely, \((a_0,b_0)=(8,4)\) makes the cyclic second coordinate infinite after one sweep, whereas the parallel orbit is regular and converges to \((-1,1)\). On the separator additional collision or intermediate-update singularities may occur; the preceding nonconvergence conclusion applies only to forward-regular orbits.

**4. All-period nonroot cycles.** A forward-regular nonroot point has period dividing \(m\) exactly when
\[
r_0^{N_m(q)}=1.
\]
For each integer \(m\ge2\), choose \(r_0\) a primitive \(N_m(q)\)-th root of unity and take \(a_0=2\), \(b_0=2/r_0\). Along this orbit both coordinate moduli equal \(2\), so neither corresponds to an infinite affine iterate; the ratio never becomes \(1\), and for cyclic sweeps it never becomes \(-1\). Since \(N_m(q)>q^j-1\) for every \(1\le j<m\), the constructed orbit has least period exactly \(m\). On nonzero coordinates the derivative is conjugate to the integer exponent matrix
\[
M_J=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad
M_G=\begin{pmatrix}2&-1\\-2&3\end{pmatrix}
\]
at a periodic return. Therefore the multipliers of an \(m\)-periodic regular nonroot orbit are exactly \(1\) and \(q^m\). Such a cycle cannot attract an open neighborhood.

## Verification
The standalone `verify_quadratic_ehrlich_aberth.py` checks the rational Jacobi and cyclic conjugacies symbolically in \(\mathbb Q(a,b)\), the exact invariant and ratio recurrences, the two exponent matrices and their first six return spectra, six exact-rational native-iterate comparisons per update rule, a nonroot Jacobi period-two witness and prime-period divisibility checks for orders two through fourteen. Execute `python verify_quadratic_ehrlich_aberth.py` with SymPy installed. The all-iteration claims are established by the preceding algebraic proof; the finite checks are supplementary, not exhaustive over initial data.

## Relationship to prior work
Grabbel, Srkalovic and Schleicher establish attracting nonroot cycles of the Jacobi Ehrlich–Aberth map in every degree at least seven and describe its Möbius equivariance, but do not give the present global two-root basin criterion or a cyclic-versus-parallel sharp-rate comparison. Reinke studies diverging higher-degree root-finder orbits and defines both update conventions; his stated Jacobi Ehrlich–Aberth divergence theorem begins at degree four. Shemyakov and colleagues compare the computational performance of Newton and Ehrlich–Aberth root finders and discuss both update modes, rather than the exact two-root orbit classification here. Classical local cubic convergence for Jacobi updates is consistent with, but does not imply, the full complex basin partition and cyclic fourth-power exponent. 

## Limitations
The classification excludes repeated roots, floating-point rounding, arbitrary polynomial degree and all initial conditions at which the rational iteration ceases to be defined in finite distinct coordinates. It is not a convergence guarantee for the high-degree cases known to support attracting nonroot cycles. The periodic-orbit assertion concerns regular nonroot cycles, not singular projective continuations. While the exact formulas are elementary once the conjugacy is exposed, an unindexed equivalent quadratic treatment, including forthcoming special-case work, remains a literature possibility; no independent mathematical validation is claimed.

## References
1. T. Grabbel, N. Srkalovic and D. Schleicher, *The Ehrlich–Aberth root finder is not generally convergent*, arXiv:2611.02143v1 (first public 2026-11-01), https://arxiv.org/html/2611.02143v1.
2. B. Reinke, *Diverging orbits for the Ehrlich–Aberth and the Weierstrass root finders*, arXiv:2011.01660 (first public 2020-11-03), https://arxiv.org/abs/2011.01660; Proc. Amer. Math. Soc. 150 (2022), 1287–1300.
3. S. Shemyakov, R. Chernov, D. Rumiantsau, D. Schleicher, S. Schmitt and A. Shemyakov, *Finding polynomial roots by dynamical systems — a case study*, arXiv:2004.03217 (2020), https://arxiv.org/abs/2004.03217; Discrete Contin. Dyn. Syst. 40 (2020), 6945–6965.
4. D. A. Bini, *Numerical computation of polynomial zeros by means of Aberth's method*, Numer. Algorithms 13 (1996), 179–200, https://doi.org/10.1007/BF02207694.
