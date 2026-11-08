# Santaló dual volumes of uniform-matroid independence polytopes and exponential stability of the near-cube center

## Finding
For \(n\ge2\), \(1\le k<n\), set
\[
P_{n,k}=\{x\in\mathbb R^n:0\le x_i\le1,\quad \sum_{i=1}^n x_i\le k\}.
\]
This is the independent-set polytope of the uniform matroid of rank \(k\) on \(n\) elements. For \(0<s<k/n\), the translated origin is interior, and write
\[
W_{n,k}(s)=\operatorname{vol}_n((P_{n,k}-s\mathbf1)^\circ),
\quad B_{n,k}(s)=\sum_{j=k+1}^n\binom nj(j-k)s^j(1-s)^{n-j}.
\]
The complete one-parameter dual volume is
\[
\boxed{W_{n,k}(s)=\frac{1+B_{n,k}(s)/(k-ns)}{n!\,[s(1-s)]^n}.}\tag{1}
\]
The unique Santaló point is \(s_{n,k}\mathbf1\), where \(s_{n,k}\) is the unique point of \((0,k/n)\) solving
\[
\boxed{\begin{aligned}
0={}&s(1-s)\big[(k-ns)B'_{n,k}(s)+nB_{n,k}(s)\big]\\
&-n(1-2s)\big[(k-ns)^2+(k-ns)B_{n,k}(s)\big].
\end{aligned}}\tag{2}
\]
In particular, the exact Santaló volume product is
\[
\boxed{\mathcal V_{n,k}=\frac{1}{n!}\left(\sum_{j=0}^k(-1)^j\binom nj(k-j)^n\right)W_{n,k}(s_{n,k}).}\tag{3}
\]
The algebraic number \(s_{n,k}\), not necessarily rational, is specified without numerical optimization by the unique root in the stated interval.

For \(n\ge3\), setting \(k=n-1\) gives the vertex-cut cube. Its Santaló coordinate is strictly less than \(1/2\), uniquely determined there by
\[
\boxed{(1-2s)(n-1-ns)^2=s^{n+1}(n-(n+1)s).}\tag{4}
\]
Furthermore,
\[
\boxed{\frac12-s_{n,n-1}\sim\frac{n-1}{2^{n+1}(n-2)^2}\sim\frac{1}{n2^{n+1}}.}\tag{5}
\]
Thus removing the one Boolean vertex cap moves the Santaló center by an exponentially small, explicitly normalized displacement in large dimension.

## Assumptions and scope
All volumes are ordinary \(n\)-dimensional Euclidean volumes. Polarity is \(K^\circ=\{y:\langle y,x\rangle\le1\text{ for all }x\in K\}\), and the origin is required to be in \(\operatorname{int}K\). The index \(k\) is an integer, \(1\le k<n\), and \(s\) is a real in \((0,k/n)\). The last two assertions require \(k=n-1\) and \(n\ge3\). No assertion is made for nonlinear cuts or arbitrary matroids.

## Proof
**Polar vertices.** Translating the defining halfspaces by \(s\mathbf1\) and using polar duality for intersections yields
\[
(P_{n,k}-s\mathbf1)^\circ=\operatorname{conv}\left\{-\frac{e_i}{s},\ \frac{e_i}{1-s}\ (1\le i\le n),\ \frac{\mathbf1}{k-ns}\right\}.\tag{6}
\]
Let \(a=(1-s)^{-1}\), \(b=s^{-1}\), and \(Z=\operatorname{conv}\{a e_i,-b e_i:1\le i\le n\}\). Every facet of \(Z\) is the simplex indexed by a subset \(S\subseteq[n]\), with vertices \(a e_i\) for \(i\in S\) and \(-b e_i\) otherwise. The pyramid from the origin to that facet has volume \(a^{|S|}b^{n-|S|}/n!\). Hence
\[
\operatorname{vol}_n(Z)=\frac1{n!}\sum_{j=0}^n\binom nj a^j b^{n-j}=\frac{(a+b)^n}{n!}.\tag{7}
\]
The facet functional is
\[
\ell_S(y)=(1-s)\sum_{i\in S}y_i-s\sum_{i\notin S}y_i\le1.
\]
For the added point \(v=\mathbf1/(k-ns)\),
\[
\ell_S(v)-1=\frac{|S|-k}{k-ns}.
\]
Precisely those facets with \(|S|>k\) are visible from \(v\); the others are hidden or coplanar. The visible pyramids with apex \(v\) have pairwise disjoint interiors outside \(Z\). Each adds \((\ell_S(v)-1)a^{|S|}b^{n-|S|}/n!\). Summing over all subsets and substituting \(a,b\) proves (1). It also handles \(k=1\), when some initially listed polar generators may be redundant.

**Unique minimizing center and root.** The Santaló point exists uniquely for each full-dimensional convex body. More directly, for interior \(c\) the polar volume equals
\[
\frac1n\int_{S^{n-1}}(h_{P_{n,k}}(u)-\langle c,u\rangle)^{-n}\,d\sigma(u),
\]
a strictly convex function of \(c\) since distinct centers give different affine denominators on a set of directions of positive measure. Uniqueness and coordinate-permutation symmetry force the minimizer to have all coordinates equal. Formula (1) diverges at both ends of \((0,k/n)\), so there is an interior minimizer and it is the unique stationary point. Differentiating (1) and clearing positive denominators gives (2).

**Primal volume.** The inclusion-exclusion formula for the unit cube clipped by the positive simplex gives
\[
\operatorname{vol}_n(P_{n,k})=\frac1{n!}\sum_{j=0}^k(-1)^j\binom nj(k-j)^n.
\]
Multiplying by (1) at its minimizing coordinate gives (3).

**One removed corner and asymptotic.** If \(k=n-1\), only the term indexed by \(j=n\) survives in the binomial tail. Therefore
\[
n!W_{n,n-1}(s)=\frac1{[s(1-s)]^n}+\frac1{(1-s)^n(n-1-ns)}.\tag{8}
\]
The derivative of the first summand vanishes at \(s=1/2\); that of the second is strictly positive there. The unique stationary point is consequently in \((0,1/2)\), and direct differentiation of (8) gives (4).

Write \(\delta_n=1/2-s_{n,n-1}>0\) and \(d_n=n-1-ns_{n,n-1}\). Equation (4) is equivalent to
\[
\delta_n=\frac{s_{n,n-1}^{n+1}(n-(n+1)s_{n,n-1})}{2d_n^2}.
\]
Since \(s_{n,n-1}<1/2\), \(d_n>(n-2)/2\), and \(n-(n+1)s_{n,n-1}<n\), for \(n\ge3\) we obtain
\[
0<\delta_n<\frac{n}{2^n(n-2)^2}=O(2^{-n}/n).
\]
It follows that \((2s_{n,n-1})^{n+1}\to1\) and \(d_n/((n-2)/2)\to1\). Substitution into the previous exact equation gives (5). This is a proof for all dimensions, not an extrapolation from computations.

## Verification
The accompanying `verify.py` uses exact rational arithmetic and independently computes volumes of the apex pyramids over every visible signed-coordinate facet. It compares these determinant-based volumes against (1) for all \(2\le n\le7\), all admissible ranks, and three rational centers per rank. It additionally verifies the exact derivative-to-polynomial identity for \(3\le n\le15\) at four rational centers. A separate numerical convex-hull computation corroborated (1) for \(2\le n\le6\) over five center choices. Neither finite check is used to establish the universal quantifiers or asymptotic assertion.

## Relationship to prior work
The independent-set polytopes of matroids are a canonical class of \((0,1)\)-polytopes, studied for instance in the 2026 work of Mori and Ohsugi on simplex faces and quadratic toric ideals. General Santaló-point geometry and algorithms are developed by Pavlov and Telen (2024 preprint; 2025 journal). Their general framework supplies the notion of minimizing polar volume, but the explicit binomial-tail formula, algebraic center equation, and near-cube exponential displacement above are family-specific claims. Existing computations of John ellipsoids of capped cubes concern an inscribed-ellipsoid problem and do not determine the Santaló point; general formulas for symmetric cube–crosspolytope intersections concern different, centrally symmetric bodies. Exact historical novelty requires further independent literature checking.

## Limitations
The polynomial equation (2) does not generally yield an elementary expression for its root. No extension to arbitrary matroid independence polytopes, a joint large-rank/dimension asymptotic for all ranks, or independent correctness/priority audit is claimed. Some relevant manuscripts were accessible only through abstracts or indexed excerpts; their complete bodies could not be checked.

## References
Mori, A. and Ohsugi, H., *Simplex faces and quadratic toric ideals of lattice polytopes*, arXiv:2606.20430, first version June 18, 2026.

Pavlov, D. and Telen, S., *Santaló Geometry of Convex Polytopes*, arXiv:2402.18955, February 29, 2024; SIAM J. Appl. Algebra Geom. 9 (2025), 58–82, doi:10.1137/24M1643566.

Moraga, J. and Süß, H., *Bounding toric singularities with normalized volume*, Bull. Lond. Math. Soc. 56 (2024), 2212–2229, doi:10.1112/blms.13052 (definition and simplex case of Santaló volume products).
