# Sharp affine least-squares stability across cross-polytope face skeleta

## Finding

Let \(d\ge3\) and \(2\le s\le d-1\) be integers. Let
\[
C_d=\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|\le1\},
\]
and let \(S_{d,s}\) be its closed \((s-1)\)-skeleton: the union of faces with \(s\) nonzero signed coordinate vertices. Equip \(S_{d,s}\) with probability measure \(\mu_{d,s}\) obtained by choosing one of its \(2^s\binom ds\) faces of dimension \(s-1\) uniformly and then choosing a point according to normalized Euclidean Hausdorff measure on that face. This is also normalized \((s-1)\)-dimensional Hausdorff measure on the skeleton, since the faces are congruent and their intersections have measure zero.

Let \(P_{d,s}\) be the \(L^2(\mu_{d,s})\)-orthogonal projector onto the restrictions of all real affine functions. Then its sharp endpoint norms are equal and given exactly by
\[
\boxed{\|P_{d,s}\|_{L^1\to L^1}=\|P_{d,s}\|_{L^\infty\to L^\infty}=\Lambda_{d,s}
=1+\frac{s+1}{2}\left(1-\frac{2}{d(s+1)}\right)^s.}
\]
Every signed coordinate vertex is a maximizing evaluation point, and no other points of the skeleton maximize the absolute kernel mass. An \(L^\infty\) extremizer is the sign of the reproducing-kernel row at any vertex.

For fixed \(d\), these constants strictly increase with face cardinality \(s\), including the elementary vertex case \(s=1\) and the previously covered facet case \(s=d\). Uniformly for \(1\le s\le d\),
\[
\boxed{0\le\Lambda_{d,s}-\left(\frac{s+3}{2}-\frac{s}{d}\right)\le\frac1d.}
\]
Thus, for fixed \(s\), \(\Lambda_{d,s}\to(s+3)/2\) as \(d\to\infty\); if \(s/d\to\alpha\in[0,1]\) and \(s\to\infty\), then \(\Lambda_{d,s}-s/2\to3/2-\alpha\). The first two intermediate cases are \(\Lambda_{3,2}=103/54\) and \(\Lambda_{4,2}=49/24\).

The substantive new scope is the complete intermediate-skeleton family \(2\le s<d\), not the classical general kernel identity, the vertex case, or the full-facet boundary value.

## Assumptions and scope

All faces are those of the standard regular cross-polytope, with vertices \(\pm e_i\). The sampling measure is continuous uniform Hausdorff measure on the selected faces, not discrete vertex sampling except at the separate case \(s=1\). The projector acts on equivalence classes in \(L^p(\mu_{d,s})\); its output has a unique continuous affine representative on the entire cross-polytope. The endpoint norms refer to that canonical representative and the support of the sampling measure. The affine space has dimension \(d+1\) and positive-definite Gram matrix because the sampled skeleton affinely spans \(\mathbb R^d\).

For all dimension and monotonicity statements that include \(s=1\) or \(s=d\), use their natural counting/facet measures. The former is a simple finite matrix, while the latter agrees with a limiting weighted-volume calculation already available in the literature comparison and is not an independent novelty claim.

## Proof

**1. Gram matrix and reproducing kernel.** For \(Y\sim\mu_{d,s}\), a face is described by a uniformly chosen \(s\)-subset of \(\{1,\ldots,d\}\), independent fair coordinate signs on that subset, and uniform barycentric weights \((U_1,\ldots,U_s)\) on the standard \((s-1)\)-simplex. Uniform barycentric weights have Dirichlet distribution with all parameters one. Symmetry gives \(\mathbb EY_i=0\) and \(\mathbb EY_iY_j=0\) for \(i\ne j\). Since each coordinate is active with probability \(s/d\) and the second moment of one barycentric weight is \(2/[s(s+1)]\),
\[
\mathbb EY_i^2=\frac{s}{d}\frac{2}{s(s+1)}=\frac{2}{d(s+1)}.
\]
Consequently the orthogonal basis \(1,y_1,\ldots,y_d\) gives the exact reproducing kernel
\[
K_{d,s}(x,y)=1+c_{d,s}\,x\cdot y,\qquad c_{d,s}=\frac{d(s+1)}2.
\]
It satisfies \(\int K(x,y)\,d\mu(y)=1\) and represents \(P_{d,s}f(x)=\int K(x,y)f(y)\,d\mu(y)\).

**2. Sharp evaluation geometry.** For every \(x\in C_d\), let \(F(x)=\int|K(x,y)|\,d\mu(y)\). Since the integrand is the absolute value of an affine function of \(x\), \(F\) is convex. Every \(x\in C_d\) is a convex combination of the signed coordinate vertices, and symmetry makes \(F\) equal at all of them. Thus the maximum occurs at a vertex.

In fact the vertex evaluations are the only maximizers. For any two distinct signed vertices \(v,w\), a relatively open set of sample points near \(-v\) has \(K(v,y)<0<K(w,y)\), because \(c_{d,s}>1\), \(K(v,-v)=1-c_{d,s}<0\), and \(K(w,-v)\ge1\) for \(w\ne v\). This open neighborhood has positive measure even if \(-v\) itself has measure zero. Equality in convexity of absolute value is therefore strict for every nontrivial convex combination of distinct vertex rows. Any nonvertex point is such a combination, so \(F(x)<F(v)\).

**3. Evaluation at a vertex.** Put \(x=e_1\) and \(c=c_{d,s}>1\). The first coordinate of \(Y\) is zero with probability \(1-s/d\); otherwise it is \(\varepsilon U\), where \(\varepsilon\) is a fair sign and \(U\) has \(\mathrm{Beta}(1,s-1)\) distribution if \(s\ge2\). (At \(s=1\), \(U\equiv1\).) Averaging over signs,
\[
\tfrac12\bigl(|1+cU|+|1-cU|\bigr)=\max\{1,cU\}=1+(cU-1)_+.
\]
Thus
\[
F(e_1)=1+\frac{s}{d}\,\mathbb E(cU-1)_+.
\]
For \(s\ge2\), the beta density is \((s-1)(1-u)^{s-2}\) on \([0,1]\). Integrating and using \(a=1-1/c\),
\[
\begin{aligned}
\mathbb E(cU-1)_+
&=(s-1)\int_{1/c}^1(cu-1)(1-u)^{s-2}\,du\\
&=(c-1)a^{s-1}-\frac{c(s-1)}s a^s
=\frac cs a^s.
\end{aligned}
\]
The same identity holds directly for \(s=1\). Therefore
\[
F(e_1)=1+\frac cd\left(1-\frac1c\right)^s
=1+\frac{s+1}{2}\left(1-\frac{2}{d(s+1)}\right)^s,
\]
which proves the sharp \(L^\infty\) norm. The choice \(f(y)=\operatorname{sgn}K(e_1,y)\) attains it. Since \(K\) is symmetric, its integral-operator \(L^1\) norm equals the \(L^\infty\) norm by duality. For continuous face sampling, no claim is made that an \(L^1\) extremizer exists.

**4. Rank monotonicity.** For fixed \(d\), extend the excess \(\Lambda_{d,s}-1\) to real \(t=s+1\ge2\) as
\[
g_d(t)=\frac t2\left(1-\frac{2}{dt}\right)^{t-1}.
\]
Writing \(u=2/(dt)\), logarithmic differentiation yields
\[
\frac{g_d'(t)}{g_d(t)}
=\frac1t+\log(1-u)+\frac{(t-1)u}{t(1-u)}
>\frac{1-2u}{t(1-u)}\ge0,
\]
where \(\log(1-u)>-u/(1-u)\) for \(0<u<1\), and \(u\le1/2\). Therefore the constants increase strictly from one skeleton to the next.

**5. Uniform dimension bounds.** Bernoulli's inequality and the second-order Taylor bound give, for \(a=2/[d(s+1)]\),
\[
1-sa\le(1-a)^s\le1-sa+\frac{s(s-1)}2a^2.
\]
Multiplying by \((s+1)/2\) and adding one gives
\[
0\le\Lambda_{d,s}-\left(\frac{s+3}{2}-\frac sd\right)
\le\frac{s(s-1)}{d^2(s+1)}\le\frac1d.
\]
The stated limits follow, with no need to exchange unproved limits or extrapolate finite computation.

## Verification

The accompanying standalone `verify.py` uses rational arithmetic. It checks the beta integral using an independent term-by-term binomial expansion, covariance normalization, monotonicity, a uniform two-sided remainder bound, and the full-facet identity, for every \(2\le d\le31\) and every \(1\le s\le d\). It also verifies four low-dimensional exact values. The completed checker passes 1,984 assertions. These are finite arithmetic checks; the full parameter theorem rests on the five analytic steps above.

## Relationship to prior work

Hangelbroek, Narcowich, Sun and Ward (arXiv:1005.2424, first public May 13, 2010) study \(L^p\)-stability of least-squares projections generated by localized kernels on smooth manifolds. Their full accessible preprint concerns kernel spaces and general stability, rather than the finite-rank affine projection for stratified cross-polytope sampling and its exact sharp norms. Zhou, Narayan and Xu (arXiv:1401.0894) study deterministic discrete collocation grids on product domains, again with a different sampling measure and objective.

A published exact affine-projector result for a single full-volume simplex yields a different beta moment. For the standard cross-polytope, the previously available weighted-volume formula also recovers the full-facet case \(s=d\) in its singular radial limit; that case is included only as a consistency check, not claimed as an independent discovery. A face-balanced simplex-skeleton calculation uses unsigned barycentric geometry on one simplex, whereas the present intermediate cross-polytope skeleta mix signed coordinate faces and have a different covariance and norm law. Neither earlier special case implies the intermediate-family formula by restriction or parameter substitution.

The contribution is the exact, attained full intermediate-skeleton profile, uniqueness of maximizing evaluation vertices, strict monotonicity across face rank, and a uniform dimension/rank asymptotic band. This addresses a concrete continuous geometric sampling family rather than a generic projection-kernel identity.

## Limitations

The result concerns only degree-one affine least squares and equal-area skeletal sampling of regular cross-polytopes. It does not treat higher-degree polynomial spaces, unequal face weights, arbitrary polytope geometries, or optimal projections among all possible operators. The formula proves sharp operator norms, not claims of unique maximizing inputs (the sign of each maximizing row gives an extremizer). The result is subject to normal bibliographic priority uncertainty: unpublished or differently indexed work may include an equivalent signed-skeleton computation. The scalar beta calculation is elementary after the structural covariance and extremal-geometry reductions; the claimed significance is the complete natural family and its sharp quantitative profile, not a new probability identity.

## References

1. T. Hangelbroek, F. J. Narcowich, X. Sun and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L^\infty\)-norm of the \(L^2\)-projector*, arXiv:1005.2424 (first posted 2010-05-13); SIAM J. Math. Anal. 43 (2011), 662–684.
2. T. Zhou, A. Narayan and Z. Xu, *Multivariate discrete least-squares approximations with a new type of collocation grid*, arXiv:1401.0894 (first posted 2014-01-05); SIAM J. Sci. Comput. 37 (2015).
3. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, publicly indexed mathematical research record, 2026-10-04, identifier `2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34`.
