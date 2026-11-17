# Exact algebraic-area variance for edge-permuted closed polygons and Haar–Stiefel polygons

## Finding

For every integer \(n\ge3\), fix a finite ordered list of planar edge vectors \(e_1,\ldots,e_n\in\mathbb R^2\) satisfying \(\sum_i e_i=0\). Choose a uniformly random permutation \(\sigma\) and concatenate the edges in that order, allowing self-intersection. Write \(A_\sigma\) for its **signed algebraic area**, defined by the usual oriented shoelace sum, and write \(Q=\sum_i e_i e_i^{\mathsf T}\) for the edge second-moment matrix. Then

\[
\mathbb E_\sigma A_\sigma=0,\qquad
\operatorname{Var}_\sigma(A_\sigma)
=\frac1{12}\sum_{i<j}\det(e_i,e_j)^2
=\frac1{12}\det Q.
\]

Consequently, for \(S=\sum_i\lVert e_i\rVert^2\),

\[
0\le\operatorname{Var}_\sigma(A_\sigma)\le\frac{S^2}{48},
\]

with equality on the left exactly when all edges are collinear, and equality on the right exactly when \(Q=(S/2)I_2\) (including the zero list as the degenerate common equality case). For nonzero fixed \(S\), the upper bound is attained, for example, by edge vectors along a regular polygon.

For the **Haar–Stiefel law** of closed planar polygons of perimeter \(2\), sample a Haar-uniform orthonormal pair \((u,v)\in V_2(\mathbb R^n)\) and take complex edges \(e_j=(u_j+\mathrm i v_j)^2\). For its signed algebraic area \(A_n\),

\[
\boxed{\operatorname{Var}(A_n)=\frac{4(n-2)}{3(n+1)(n+2)(n+4)}}\qquad(n\ge3).
\]

Among all positive integers \(n\ge3\), this variance has its **unique maximum at \(n=4\)**, where it equals \(1/90\), and it decays as \(4/(3n^2)\). The triangle case \(n=3\), equal to \(1/105\), is already implied by the known triangle-area representation; the higher-order formula and the edge-permutation area identity are the contribution assessed here.

## Assumptions and scope

The first identity is deterministic conditional on any **fixed zero-sum edge list**, with no need for generic position, convexity, distinct lengths, or nonzero edges. Only the edge order is randomized. Signed area counts winding multiplicity and must not be confused with the unsigned enclosed area or the convex-hull area for a self-intersecting polygon.

For the second identity, the two columns of the \(n\times2\) frame are orthonormal in \(\mathbb R^n\), with the Haar probability law on the real Stiefel manifold. Orthogonality implies \(\sum_j e_j=0\), and the perimeter identity \(\sum_j|e_j|=2\) fixes the scale. Row permutation invariance of Haar measure makes the resulting edge sequence exchangeable. Rotation and reflection of the frame do not affect the squared algebraic area.

## Proof

**1. The random-order identity.** Put \(c_{ij}=\det(e_i,e_j)=-c_{ji}\). By the shoelace formula,

\[
2A_\sigma=\sum_{p<q}\det(e_{\sigma(p)},e_{\sigma(q)})
=\sum_{i<j}\varepsilon_{ij}(\sigma)c_{ij},
\]

where \(\varepsilon_{ij}\) is \(+1\) if \(i\) precedes \(j\) in the permutation and \(-1\) otherwise. Each such sign has zero mean. The signs for two disjoint unordered pairs have zero covariance. For distinct indices \(i<j<k\), direct enumeration of their six orders gives

\[
\mathbb E(\varepsilon_{ij}\varepsilon_{ik})=
\mathbb E(\varepsilon_{ik}\varepsilon_{jk})=\frac13,
\qquad\mathbb E(\varepsilon_{ij}\varepsilon_{jk})=-\frac13.
\]

Therefore, writing \(B=\sum_{i<j}c_{ij}^2\) and

\[
T=\sum_{i<j<k}
(c_{ij}c_{ik}-c_{ij}c_{jk}+c_{ik}c_{jk}),
\]

we have \(4\mathbb E A_\sigma^2=B+(2/3)T\). Closure gives \(\sum_{j\ne i}c_{ij}=\det(e_i,\sum_j e_j)=0\) for each \(i\). Expanding \(\sum_i(\sum_{j\ne i}c_{ij})^2=0\) yields \(0=2B+2T\), hence \(T=-B\). Thus \(\operatorname{Var}_\sigma(A_\sigma)=B/12\).

Cauchy–Binet for the \(2\times n\) edge matrix gives \(B=\det Q\). If the eigenvalues of \(Q\) are \(\lambda_1,\lambda_2\ge0\), then \(\det Q=\lambda_1\lambda_2\le (\lambda_1+\lambda_2)^2/4=S^2/4\), with equality precisely for equal eigenvalues. The determinant vanishes precisely when the edge span has rank at most one. This proves the sharp bound and equality cases.

**2. Evaluation for a Haar–Stiefel frame.** Row exchangeability and the first identity imply

\[
\operatorname{Var}(A_n)=\frac{n(n-1)}{24}
\mathbb E\big[\det(e_1,e_2)^2\big].
\]

Write \(a=u_1^2+v_1^2\). Orthogonal invariance in the two columns allows rotation of the frame so that the first row is \((\sqrt a,0)\). That rotation changes all complex squared edges by a common phase and preserves determinants. The first complex edge becomes \(a\), and \(\det(e_1,e_2)=2a u_2v_2\).

For a Haar frame, the first-row squared norm has beta law

\[
a\sim\operatorname{Beta}\left(1,\frac{n-2}{2}\right).
\]

Conditional on \(a\), the remaining entries \((u_2,\ldots,u_n)\) are uniform on the sphere of squared radius \(1-a\) in dimension \(n-1\), while \((v_2,\ldots,v_n)\) is uniform on the unit sphere in the subspace perpendicular to that vector. Standard sphere moments, valid for \(n\ge3\), give

\[
\mathbb E[u_2^2v_2^2\mid a]
=\frac{1-a}{(n-1)(n+1)},
\qquad
\mathbb E[a^2(1-a)]
=\frac{8(n-2)}{n(n+2)(n+4)}.
\]

Thus

\[
\mathbb E\det(e_1,e_2)^2
=\frac{4}{(n-1)(n+1)}\mathbb E[a^2(1-a)]
=\frac{32(n-2)}{n(n-1)(n+1)(n+2)(n+4)},
\]

and substitution proves the announced variance.

**3. Unique maximum.** Denoting the variance by \(V_n\), direct division gives

\[
\frac{V_{n+1}}{V_n}=
\frac{(n-1)(n+1)(n+4)}{(n-2)(n+3)(n+5)}.
\]

The denominator minus numerator equals \(2(n^2-13)\). The ratio is greater than one for \(n=3\) and less than one for every integer \(n\ge4\), proving the unique maximum at \(n=4\). The large-order asymptotic follows by comparing polynomial degrees.

## Verification

The standalone file `check_area_variance.py` checks the fixed-edge formula by **exact rational exhaustive enumeration** of all permutations for 18 closed edge lists of lengths \(3\) through \(7\). It separately generates 180,000 independent Haar–Stiefel frames for each of \(n=3,4,5,10,25\) via Gaussian QR decomposition; the empirical area variances agree with the displayed exact formula within the declared sampling tolerance. Successful completion prints `EXCHANGEABLE_SIGNED_AREA_VARIANCE_OK`. These finite checks corroborate the separate algebraic proof and are not its substitute.

## Relationship to prior work

Cantarella, Deguchi and Shonkwiler [1] introduced the Haar–Stiefel closed-polygon measure and its **edge-set ensemble** symmetrization. Their Proposition 15 averages squared chord lengths over edge orders, not squared algebraic area. The present sign-correlation identity is not an algebraic restatement of that chord result: it depends on pairwise oriented determinants and survives self-intersections.

Cantarella, Needham, Shonkwiler and Stewart [2] develop the same planar Grassmannian model and identify the perimeter-2 triangle area as \(|xyz|\) with a uniform spherical vector. Their result already implies the special \(n=3\) second moment \(1/105\). Their planar quadrilateral classification gives shape-category probabilities, not the signed-area variance for arbitrary \(n\).

Bárány and Steiger [3] study the variance of **convex hull area** for random points inside a convex body; that area functional and sampling model differ from the present fixed-edge signed area. These comparisons do not establish exhaustive historical priority.

## Limitations

The theorem gives the second moment of **signed** area, not the variance of absolute area or the area of the polygon's interior as an unsigned region. It does not characterize the full area law, stable statistical reconstruction, or other random-polygon ensembles without the stipulated exchangeability. The novel-status comparison is based on inspected sources and targeted literature searches, not an exhaustive historical proof.

## References

[1] J. Cantarella, T. Deguchi and C. Shonkwiler, *Probability Theory of Random Polygons from the Quaternionic Viewpoint*, first publicly posted 2012-06-14, arXiv:1206.3161, https://arxiv.org/abs/1206.3161 (especially the closed planar Stiefel model and Section 6 on edge-set ensembles).

[2] J. Cantarella, T. Needham, C. Shonkwiler and G. Stewart, *Random Triangles and Polygons in the Plane*, first posted 2017-02-01, arXiv:1702.01027, https://arxiv.org/abs/1702.01027 (especially the triangle area identity and Grassmannian symmetry).

[3] I. Bárány and W. H. Steiger, *On the Variance of Random Polygons*, Computational Geometry 46 (2013), 173–180, doi:10.1016/j.comgeo.2012.01.003 (convex-hull area in a distinct model).
