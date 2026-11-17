# Crofton simplex-section probabilities in higher-dimensional rectangular boxes

## Finding
For every integer \(d\ge4\) and all positive edge lengths \(a_1,\ldots,a_d\), consider the orthogonal box \(B=\prod_{i=1}^d[0,a_i]\) and an unoriented affine hyperplane chosen according to Euclidean-motion-invariant measure, conditional on intersecting \(B\). Let \(N\) be the number of vertices of its generic \((d-1)\)-dimensional section. Then
\[
\Pr(N=d)=\frac{\sqrt{2\pi}}{\sum_{i=1}^d a_i}
\int_0^\infty\prod_{i=1}^d\operatorname{erfc}\left(\frac{t}{\sqrt2a_i}\right)\,dt.
\]
At fixed sum of positive side lengths this simplex probability is strictly Schur-concave: the unique maximizer, up to common scaling, is the cube. For unit side lengths its exact optimum is
\[
p_d^*=\frac{\sqrt{2\pi}}{d}\int_0^\infty\operatorname{erfc}(t/\sqrt2)^d\,dt,
\qquad \lim_{d\to\infty}d^2p_d^*=\pi.
\]
The three-dimensional rectangular-box Crofton polygon distribution, including the complete four-type cube vector, **is already available in prior work**, and is not asserted as a new result here. The new scope is the higher-dimensional simplex probability, shape inequality and sharp asymptotic.

## Sampling model and exact scope
The invariant measure on unoriented hyperplanes \(H(u,s)=\{x:u\cdot x=s\}\) is proportional to \(d\sigma(u)\,ds\) modulo \((u,s)\sim(-u,-s)\). A normal with absolute coordinates \(u_i\) is weighted after conditioning on intersection by \(w(u)=\sum_i a_i|u_i|\), the box's projected width. In particular, the theorem does **not** concern uniform normals with separately normalized uniform intercepts or central sections. Generic excludes the measure-zero configurations through box vertices or edges; the section then has a simplex exactly when it has \(d\) vertices. No claim is made for arbitrary sheared parallelotopes, higher-codimension sections or the full face-vector distribution for \(d\ge4\).

## Proof
**Minimum edge cuts.** Reflect each coordinate axis so the coefficients of the normal are positive. For a generic intercept, crossed box edges are exactly the boundary edges of the vertex set below the intercept in the graph of the \(d\)-cube. A proper nonempty edge cut in that graph has size at least \(d\), with equality only for a singleton or its complement when \(d\ge3\). One direct proof is by induction: split the graph into opposite \((d-1)\)-cubes, so for \(S=S_0\cup S_1\),
\[
|\partial S|=|\partial S_0|+|\partial S_1|+|S_0\triangle S_1|.
\]
For \(d=3\), a case check over the two square faces gives precisely the singleton equality cases. If both face-subsets are nonempty and proper in dimension \(d\ge4\), their internal cuts contribute at least \(2(d-1)>d\). If one face-subset is empty or full, the displayed formula and the induction bound show that achieving \(d\) requires one face to have a singleton or co-singleton and the separating difference to have size one; the other possibility of an entire face separation contributes \(2^{d-1}>d\). This proves the classification.

The only intercepts producing a simplex are therefore the interval immediately above the lowest box vertex and the interval immediately below the highest vertex. Each has length \(m(u)=\min_i a_i|u_i|\). Consequently, for Haar-uniform \(U\) on the unit sphere,
\[
\Pr(N=d)=\frac{2\mathbb E\min_i a_i|U_i|}{\mathbb E\sum_i a_i|U_i|}.
\]
**Gaussian normalization.** Let \(G=(G_1,\ldots,G_d)\) have independent standard normal coordinates, and write \(G=RU\). Radius and direction are independent. Both numerator and denominator above are homogeneous of degree one, so their common factor \(\mathbb ER\) cancels. Since \(\mathbb E|G_i|=\sqrt{2/\pi}\), and by the layer-cake identity and independence,
\[
\mathbb E\min_i a_i|G_i|
=\int_0^\infty\Pr(a_i|G_i|>t\text{ for all }i)dt
=\int_0^\infty\prod_i\operatorname{erfc}(t/(\sqrt2a_i))dt,
\]
the exact probability follows. All integrands are nonnegative, justifying Tonelli.

**Strict optimality.** For fixed positive \(x_i\), \(a\mapsto\min_i(a_ix_i)\) is concave as the pointwise minimum of affine functions. Averaging with exchangeable, continuous positive Gaussian absolute coordinates gives a symmetric concave numerator. If \(a_i\ne a_j\), average the vector with its coordinate transposition. On a positive-measure event where \(|G_i|\) and \(|G_j|\) are close, and all other products are larger, the identity of the active minimum switches between those two vectors; strict concavity occurs there. The denominator depends only on \(\sum_i a_i\). Thus averaging any unequal pair strictly improves the probability, which proves strict Schur concavity and the unique uniform-side maximizer.

**Sharp asymptotic.** Put \(Q(t)=\operatorname{erfc}(t/\sqrt2)\). Since \(Q(t)=1-\sqrt{2/\pi}\,t+O(t^3)\), for each fixed \(s\ge0\) one has \(Q(s/d)^d\to\exp(-\sqrt{2/\pi}s)\). On \([0,1]\), \(Q(t)\le e^{-ct}\) for some \(c>0\); beyond \(1\), \(Q(t)\le Q(1)<1\) and \(\int_1^\infty Q(t)dt<\infty\). Splitting the integral at \(t=1\) justifies dominated convergence after the substitution \(s=dt\) and makes the remaining tail exponentially small. Therefore
\[
\lim_{d\to\infty}d\int_0^\infty Q(t)^d dt
=\int_0^\infty e^{-\sqrt{2/\pi}s}ds=\sqrt{\pi/2},
\]
which yields \(d^2p_d^*\to\pi\). This completes the proof.

## Prior results and originality boundary
The dimension-three probability of each polygon type for **all rectangular boxes** is established in *Elementary Crofton section-type law and quadratic hexagon extinction for rectangular boxes* (published 18 October 2026, https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-elementary-crofton-section-type-law-and-quadratic-hexagon-extinc--ecdb5fa9f8fa). This earlier result also explains that cube values and the rectangular-box triangular-section formula/shape extremizer had been studied previously. The three-dimensional distribution must not be credited here. Earlier papers on central hyperplane sections, fixed-offset slice volumes and expected section-vertex counts (Lonke, Marichal–Mossinghoff, Swan) concern distinct or weaker observables, and do not themselves imply the stated all-dimensional \(d\ge4\) event probability, strict shape law or \(\pi/d^2\) limit. Any more general prior stochastic-geometric theorem covering those conclusions would affect historical priority and must be evaluated on its actual mathematical implications; this comparison is best-of-knowledge, not an independence certificate.

## Checks and limitations
The finite checker associated with the original package explores generic edge cuts, numerical Gaussian integrals and conditional affine sampling; such checks do not establish a claim for every dimension or all real side lengths. The arguments above establish the unrestricted conclusions in their stated domain. They do not determine full high-dimensional face-vector distributions, nonorthogonal shapes, robustness to a different plane measure, or novelty relative to inaccessible unindexed literature.

## References
- B. M. Bray, *Invariant measures on multifids of convex polytopes*, Ph.D. thesis, University of Wollongong (2009), Chapter 10, https://ro.uow.edu.au/theses/3403.
- Y. Lonke, *On random sections of the cube*, arXiv:math/9812123, https://arxiv.org/abs/math/9812123.
- J.-L. Marichal and M. J. Mossinghoff, *Slices, slabs, and sections of the unit hypercube*, arXiv:math/0607715, https://arxiv.org/abs/math/0607715.
- H. Swan, *Expected Number of Vertices of a Hypercube Slice*, arXiv:1808.09482, https://arxiv.org/abs/1808.09482.
