# A universal cubic Gaussian correction for the extreme sides of random spherical triangles

## Finding
Let \(U_1,U_2,U_3\) be independent uniform directions on \(S^{d-1}\), with integer \(d\ge3\). Define their shortest great-circle side lengths \(\Theta_{ij}=\arccos\langle U_i,U_j\rangle\), and write \(\Theta_{\max,d}=\max_{i<j}\Theta_{ij}\) and \(\Theta_{\min,d}=\min_{i<j}\Theta_{ij}\). For every fixed \(T>0\), uniformly for \(|t|\le T\) as \(d\to\infty\),
\[
\Pr\bigl(\sqrt d(\Theta_{\max,d}-\pi/2)\le t\bigr)
=\Phi(t)^3+\frac{\phi(t)^3}{\sqrt d}+O_T(d^{-1}),
\]
\[
\Pr\bigl(\sqrt d(\Theta_{\min,d}-\pi/2)\le t\bigr)
=1-\Phi(-t)^3+\frac{\phi(t)^3}{\sqrt d}+O_T(d^{-1}).
\]
Here \(\Phi(t)=\int_{-\infty}^t(2\pi)^{-1/2}e^{-u^2/2}\,du\) and \(\phi=\Phi'\). In particular, \(\Pr(\Theta_{\max,d}\le\pi/2)=1/8+(2\pi)^{-3/2}d^{-1/2}+O(d^{-1})\). The **sharp coefficient** \(\phi(t)^3\) is positive for every finite \(t\) and explains the first deviation from three independent Gaussian side-length approximations.

The stronger assertion is a total-variation-strength density expansion. With \(Z_d=\sqrt d\,(\langle U_1,U_2\rangle,\langle U_1,U_3\rangle,\langle U_2,U_3\rangle)\), its joint density, extended by zero off its support, satisfies
\[
\int_{\mathbb R^3}\left|f_d(z)-\phi(z_1)\phi(z_2)\phi(z_3)\left(1+\frac{z_1z_2z_3}{\sqrt d}\right)\right|\,dz=O(d^{-1}).
\]
The comparison signed density need not be nonnegative in the extreme tails; the assertion is its integrated error against a genuine probability density.

## Assumptions and scope
All probabilities concern **exactly three** points, each sampled independently from normalized rotation-invariant surface measure on the unit sphere; \(d\) is the Euclidean ambient dimension, not the intrinsic sphere dimension. Each shorter geodesic side lies in \([0,\pi]\), almost surely strictly within. The limit holds for fixed finite \(t\), uniformly on compact intervals, not for \(t\) diverging with \(d\). No limit in the number of sampled points is taken. The normal density and cdf have the normalizations above. All remainder constants may depend on \(T\) but not on \(t\) or \(d\) in the stated ranges.

## Proof
**1. Exact joint Gram density.** Put \(r_1=\langle U_1,U_2\rangle\), \(r_2=\langle U_1,U_3\rangle\), and \(r_3=\langle U_2,U_3\rangle\). The positive Gram determinant is
\[
\Delta(r)=1-r_1^2-r_2^2-r_3^2+2r_1r_2r_3.
\]
For \(d\ge3\) the triple has joint Lebesgue density
\[
g_d(r)=c_d\,\Delta(r)^{(d-4)/2}\mathbf1_{\{\Delta(r)>0,\ |r_i|<1\}},\qquad
c_d=\frac{\Gamma(d/2)^2}{\pi^{3/2}\Gamma((d-1)/2)\Gamma((d-2)/2)}.
\]
To verify the normalizing constant without appeal to a table, condition first on \(U_1\). The coordinates \(r_1\) and \(r_2\) are independent and have respective common density \(\Gamma(d/2)[\sqrt\pi\Gamma((d-1)/2)]^{-1}(1-r^2)^{(d-3)/2}\). Given them, decompose the two other points into their components along \(U_1\) and independent uniform directions in its \((d-1)\)-dimensional orthogonal complement. Their remaining normalized inner product \(w\) has density \(\Gamma((d-1)/2)[\sqrt\pi\Gamma((d-2)/2)]^{-1}(1-w^2)^{(d-4)/2}\), and
\[
r_3=r_1r_2+\sqrt{(1-r_1^2)(1-r_2^2)}\,w.
\]
The Jacobian and cancellation of powers give exactly \(g_d\). This derivation also covers \(d=3\), whose determinant exponent is \(-1/2\).

**2. Integrated cubic expansion.** Change variables \(z_i=\sqrt d\,r_i\). The density becomes
\[
f_d(z)=c_dd^{-3/2}\left(1-\frac{z_1^2+z_2^2+z_3^2}{d}+\frac{2z_1z_2z_3}{d^{3/2}}\right)^{(d-4)/2}\mathbf1_{\text{Gram-positive}}.
\]
The gamma-ratio form of Stirling's formula yields \(c_dd^{-3/2}=(2\pi)^{-3/2}(1+O(d^{-1}))\). On the ball \(\|z\|\le d^{1/16}\), the logarithm and exponential have a uniformly controlled expansion of the form
\[
\log\left(\frac{f_d(z)}{\phi(z_1)\phi(z_2)\phi(z_3)}\right)
=\frac{z_1z_2z_3}{\sqrt d}+O\!\left(\frac{1+\|z\|^2+\|z\|^4+\|z\|^6}{d}\right).
\]
The \(\|z\|^6\) allowance controls the quadratic term when exponentiating. Gaussian-polynomial integrability then gives an integrated \(O(d^{-1})\) difference between \(f_d\) and \(\phi(z_1)\phi(z_2)\phi(z_3)(1+d^{-1/2}z_1z_2z_3)\) on this ball. Outside it, the event entails at least one \(|\sqrt d\,\langle U_i,U_j\rangle|>d^{1/16}/\sqrt3\). Each marginal has density proportional to \((1-r^2)^{(d-3)/2}\), hence a tail bound \(C\exp(-c d^{1/8})\) for all sufficiently large \(d\). The same bound, up to a polynomial factor, holds for the Gaussian comparison density. Thus the entire integrated error is \(O(d^{-1})\).

**3. The two extreme side laws.** The event \(\sqrt d(\Theta_{\max,d}-\pi/2)\le t\) is exactly the event that every \(z_i\) exceeds \(b_d(t)=-\sqrt d\sin(t/\sqrt d)=-t+O_T(d^{-1})\). The leading Gaussian integral equals \(\Phi(-b_d(t))^3=\Phi(t)^3+O_T(d^{-1})\). Its cubic correction equals
\[
\frac1{\sqrt d}\prod_{i=1}^{3}\int_{b_d(t)}^{\infty}z_i\phi(z_i)\,dz_i
=\frac{\phi(t)^3}{\sqrt d}+O_T(d^{-1}).
\]
The integrated density error controls every event, proving the maximum formula. Similarly, \(\Theta_{\min,d}>\pi/2+t/\sqrt d\) iff every \(z_i<b_d(t)\). Now \(\int_{-\infty}^{b_d(t)}z\phi(z)\,dz=-\phi(b_d(t))\), so its cubic term is \(-d^{-1/2}\phi(t)^3+O_T(d^{-1})\). Taking the complement proves the minimum formula. Every normalization and the signs of the two corrections are thereby fixed.

## Verification
The complete proof is analytic; the standalone checker `check_extreme_spherical_sides.py` independently constructs random triples, compares the geometric maximum/minimum events against the predicted two-term cdf, evaluates an exact one-dimensional right-angle probability, and checks the \(d=3\) formula \(\Pr(\Theta_{\max,3}\le\pi/2)=1/4-1/(4\pi)\). It uses only ordinary numerical sampling/integration and supplies no infinite-dimensional certification. Reproduce with `python check_extreme_spherical_sides.py` after installing `numpy` and `scipy`.

## Relationship to prior work
Cai–Fan–Jiang (2013, arXiv:1306.0256) give the exact one-angle density, the pairwise independence of distinct sampled angles, and extreme-angle limits as the number of points grows. Their results do not give the compact-\(t\) sharp fixed-three-point correction above. Bubeck–Ding–Eldan–Rácz (arXiv:1411.5713) analyze precisely the same three-edge threshold event in high-dimensional spherical geometric graphs: Lemma 1 proves a positive excess over an independent-edge probability of at least constant order \(d^{-1/2}\) for sufficiently large \(d\); Lemma 5 and its equation (41) give an exact one-dimensional integral at the right-angle threshold. Neither the positive-excess phenomenon nor that exact special integral is claimed new. Those earlier results do not identify the **all-threshold explicit coefficient \(\phi(t)^3\)** or the stronger full three-coordinate \(L^1\) expansion with \(O(d^{-1})\) error.

Allen-Perkins (arXiv:1807.06220) derives the overlap area of two caps for a random spherical graph in ordinary three-dimensional Euclidean space and treats graph clustering. Qi–Yang (arXiv:2609.05330) derive joint extremes in a different regime, with the number of sampled points itself tending to infinity. The present claim is a fixed-three-point, growing-ambient-dimension refinement. Some components (particularly Gram determinant structure and triangular dependence) can be recovered from known random-correlation-matrix calculations; the claimed contribution is the exact extremal-cdf correction together with a uniform integrated remainder, rather than the cubic moment identity alone.

## Limitations
The theorem concerns only a fixed triangle and fixed compact normalized thresholds, not the regime of increasing numbers of sampled vertices or moderate deviations. It does not assert novelty of pairwise independence, the sign of the triangle excess, the exact right-angle integral, or the Gram determinant identity. The first-order coefficient is a genuine improvement over previously inspected \(d^{-1/2}\)-order bounds, but historical priority remains provisional: an earlier specialized high-dimensional geometric-graph expansion could possibly contain the same coefficient implicitly. Numerical agreement is not a proof, and independent mathematical or historical evaluation has not been performed.

## References
1. T. Cai, J. Fan, T. Jiang, *Distributions of Angles in Random Packing on Spheres*, arXiv:1306.0256v1 (public June 2, 2013), Journal of Machine Learning Research **14** (2013), 1837–1864.
2. S. Bubeck, J. Ding, R. Eldan, M. Z. Rácz, *Testing for high-dimensional geometry in random graphs*, arXiv:1411.5713v1 (public November 20, 2014), *Random Structures & Algorithms* **49** (2016), 503–532. See Lemmas 1 and 5.
3. A. Allen-Perkins, *Random spherical graphs*, arXiv:1807.06220v1 (public July 17, 2018), in particular the spherical-cap overlap and clustering calculation.
4. Y. Qi, L. Yang, *Joint Distributions of Minimum and Maximum Angles on High-Dimensional Spheres*, arXiv:2609.05330v1 (public September 4, 2026).
