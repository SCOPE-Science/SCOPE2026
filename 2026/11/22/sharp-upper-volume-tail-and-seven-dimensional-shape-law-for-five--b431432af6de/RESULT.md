# Sharp upper-volume tail and seven-dimensional shape law for five random spherical vertices

## Finding
Let \(X_1,\ldots,X_5\) be independent points, each uniform in surface area on the Euclidean unit sphere \(S^2\subset\mathbb R^3\). Write \(P=\operatorname{conv}\{X_1,\ldots,X_5\}\), \(V=\operatorname{vol}_3(P)\), and \(V_*=\sqrt3/2\). Then
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-7/2}
\Pr\left(V>V_*(1-\varepsilon)\right)=\frac{24}{7}.
\]
There are exactly twenty labelled near-maximizing branches, indexed by the ten unordered choices of two apices and the two cyclic orientations of the other three vertices. Given \(V>V_*(1-\varepsilon)\), the branch index becomes uniform over these twenty choices; after removing rigid rotations and applying the exact positive-definite Hessian normalization specified below, the seven local shape parameters converge **in total variation** to uniform volume measure on the unit seven-ball. In particular the relative volume deficit divided by \(\varepsilon\) tends to \(\operatorname{Beta}(7/2,1)\).

## Assumptions and scope
The points have the product of five normalized surface-area measures; no interior sampling, dependence, alternative surface density or growing sample size is included. The local limit is taken as \(\varepsilon\downarrow0\) with exactly five points in dimension three. Volumes are ordinary nonnegative three-dimensional Lebesgue volumes. The maximum \(V_*\) and its equality configurations follow from the known classification of inscribed \(d+2\)-vertex volume maximizers, applied at \(d=3\) [2]. A maximizer has two antipodal vertices and three vertices forming an equilateral triangle in the orthogonal equatorial plane. Its volume is twice a height-one pyramid over an equilateral triangle of circumradius one, giving \(\sqrt3/2\).

## Proof
**1. Localization at the maximizing orbits.** By the global equality classification [2, Theorem 2], the only maximizing configurations are regular triangular bipyramids. Compactness of \((S^2)^5\), continuity of hull volume and the strict inequality away from the maximizing set imply that every sufficiently small-deficit configuration is close to one of these configurations. Each has a unique unordered apex pair. Fix that pair of labels and choose one of the two cyclic orders of the other three labels; these are disjoint open neighborhoods when sufficiently small. Thus there are \(\binom52\cdot2=20\) components with equal probability by exchangeability and reflection invariance.

**2. A seven-coordinate rotation quotient.** Fix the first chosen apex at \(p_1=(0,0,1)\) by rotational invariance. Write its opposite apex and three equatorial points as
\[
\begin{aligned}
p_2&=(u,v,-\sqrt{1-u^2-v^2}),\\
b_j&=(\sqrt{1-z_j^2}\cos\phi_j,
       \sqrt{1-z_j^2}\sin\phi_j,z_j),\\
\phi_1&=0,\qquad \phi_2=\frac{2\pi}{3}+t_2,
\qquad \phi_3=\frac{4\pi}{3}+t_3.
\end{aligned}
\]
The additional common equatorial rotation \(\phi_1\) has been integrated out. Denote the seven remaining real coordinates by \(x=(u,v,z_1,z_2,z_3,t_2,t_3)^T\). At a maximizer, \(x=0\). For all sufficiently small \(x\), the two apices lie on opposite sides of the base triangle and the exact hull volume is
\[
V(x)=\frac16 (p_1-p_2)\cdot
\big((b_2-b_1)\times(b_3-b_1)\big),
\]
using the displayed cyclic orientation. This follows by summing the two pyramid volumes with the common triangular base; it is not merely a first-order approximation.

**3. Exact Hessian.** Taylor differentiation of the preceding elementary expression gives a zero gradient and
\[
\frac{V_*-V(x)}{V_*}=\frac12 x^T Hx+O(\|x\|^3),
\qquad H=\begin{pmatrix}
\tfrac12&0&-\tfrac13&\tfrac16&\tfrac16&0&0\\
0&\tfrac12&0&-\tfrac{\sqrt3}{6}&\tfrac{\sqrt3}{6}&0&0\\
-\tfrac13&0&\tfrac23&0&0&0&0\\
\tfrac16&-\tfrac{\sqrt3}{6}&0&\tfrac23&0&0&0\\
\tfrac16&\tfrac{\sqrt3}{6}&0&0&\tfrac23&0&0\\
0&0&0&0&0&\tfrac23&-\tfrac13\\
0&0&0&0&0&-\tfrac13&\tfrac23
\end{pmatrix}.
\]
The positive eigenvalues are \(1/6,1/6,1/3,2/3,1,1,1\), and \(\det H=1/162\). In particular the quadratic form is coercive: in every sufficiently small branch, \(\|x\|=O(\sqrt\varepsilon)\) whenever the relative deficit is below \(\varepsilon\). The symbolic derivative and eigenvalue checks are reproduced by `verify.py`.

**4. Probability measure and coefficient.** After fixing \(p_1\) by isotropy, its four remaining independent uniform sphere points each have normalized area measure \(d\phi\,dz/(4\pi)\), using height \(z\). For \(p_2\) near the south pole the local area element is \(du\,dv/\sqrt{1-u^2-v^2}\). Integrating the common azimuth of \(b_1\) over \(2\pi\) leaves the local seven-dimensional density
\[
f(x)=\frac{2\pi}{(4\pi)^4}\frac1{\sqrt{1-u^2-v^2}}
=\frac1{128\pi^3}(1+O(\|x\|^2)).
\]
The seven-dimensional unit-ball volume is \(\kappa_7=16\pi^3/105\), so the ellipsoid \(\{x: x^THx<2\varepsilon\}\) has volume \(\kappa_7(2\varepsilon)^{7/2}/\sqrt{\det H}\). Summing the twenty components yields
\[
20\cdot\frac1{128\pi^3}\cdot
\frac{16\pi^3}{105}\cdot
\frac{2^{7/2}}{\sqrt{1/162}}
=\frac{24}{7}.
\]
The cubic Taylor remainder, strict Hessian positivity and compactness localization justify replacing each small-deficit region by its ellipsoid with a relative \(o(1)\) error in its volume. Hence the asserted probability equivalent follows.

**5. Conditional shape.** Within each branch let \(H^{1/2}\) be the positive symmetric matrix square root and set \(Y_\varepsilon=H^{1/2}x/\sqrt{2\varepsilon}\). On every fixed compact set the transformed density tends uniformly to a constant, and the transformed sublevel indicator tends almost everywhere to \(\mathbf1_{\{\|y\|<1\}}\). Coercivity bounds its support inside a fixed ball for sufficiently small \(\varepsilon\). Dominated convergence therefore gives \(L^1\), hence total-variation, convergence of each conditional mark to uniform measure on \(B^7\). The branch weights converge to \(1/20\). The radial distribution of a uniform seven-ball has \(\Pr(\|Y\|^2\le s)=s^{7/2}\) for \(0\le s\le1\). By the same local approximation the normalized deficit converges to this squared radius, proving its stated beta limit.

## Verification
The standalone `verify.py` differentiates the **actual coordinate volume formula**, rather than presupposing the displayed Hessian. It confirms the exact maximum \(\sqrt3/2\), vanishing first derivatives, all \(49\) Hessian entries, its eigenvalues, determinant \(1/162\), the rotationally reduced probability density and the prefactor \(24/7\). Running `python verify.py` with SymPy prints `ALL_CHECKS_PASSED`. This symbolic computation checks local calculus; the global equality classification and limiting-measure reasoning are supplied mathematically above, not inferred from numerical simulation.

## Relationship to prior work
Bárány, Fodor and Vígh [1] study intrinsic-volume variance and strong laws for **interior-uniform** random polytopes, principally in a many-point regime; the source's first publicly verifiable version is arXiv:0906.0309v1 (June 1, 2009), and the published paper lists MSC 52A22 as primary. Horváth and Lángi [2] already classify all volume-maximizing \(d+2\)-vertex spherical polytopes; their theorem supplies the bipyramid maximum and uniqueness and is not claimed here. Bonnet and O'Reilly [3] investigate expected facet numbers and facet heights of sphere-boundary random polytopes, particularly dimension/sample-size regimes. None of these inspected works supplies the fixed-five-vertex sharp upper-volume probability \(24\varepsilon^{7/2}/7\) or its conditional seven-coordinate ellipsoid law. The result is a quantified rarity and local-shape refinement of a known deterministic maximizer, not a new proof of its extremality.

## Limitations
The assertion is specific to five independent uniform points on \(S^2\); the finite-threshold volume distribution, higher-order tail terms, anisotropic sampling and other vertex counts are not determined. No independence or external mathematical audit has been performed. The historical-priority search is necessarily incomplete, so a previously unindexed evaluation of this near-maximal distribution could overlap. Neither the generic local Morse/Laplace principle nor the already known global maximizer by itself evaluates the specific seven-dimensional Hessian and surface-measure coefficient.

## References
[1] I. Bárány, F. Fodor and V. Vígh, *Intrinsic volumes of inscribed random polytopes in smooth convex bodies*, arXiv:0906.0309v1 (first public June 1, 2009); *Advances in Applied Probability* 42 (2010), 605–619; DOI: 10.1239/aap/1282924055. Published primary MSC2020 family: 52A22. https://arxiv.org/abs/0906.0309

[2] Á. G. Horváth and Zs. Lángi, *Maximum volume polytopes inscribed in the unit sphere*, arXiv:1402.6496v1 (February 26, 2014), Theorem 2. https://arxiv.org/abs/1402.6496

[3] G. Bonnet and E. O'Reilly, *Facets of spherical random polytopes*, arXiv:1908.04033 (August 12, 2019), *Mathematische Nachrichten* 295 (2022), 1901–1933, DOI: 10.1002/mana.202000314. https://onlinelibrary.wiley.com/doi/full/10.1002/mana.202000314
