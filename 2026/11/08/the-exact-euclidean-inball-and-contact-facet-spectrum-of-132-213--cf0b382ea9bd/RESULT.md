# The exact Euclidean inball and contact-facet spectrum of \(132,213\)-avoiding permutahedra

## Finding

For every integer \(d\ge2\), the canonically embedded \(d-1\)-dimensional permutahedron \(P_d\) obtained by forbidding the permutation patterns \(132\) and \(213\) has an explicitly solvable unique largest inscribed Euclidean ball. In contrast to the ordinary permutahedron, its inradius remains bounded as the dimension increases, even though its minimum-enclosing sphere is exactly the same sphere as that of the ordinary permutahedron.

Write
\[
H_d=\sqrt{d(d-1)},\quad
\rho_d=(d,d-1,\ldots,1),\quad
\mu_d=\tfrac{d+1}{2}\mathbf1,\quad
\lambda_d=\frac{2\sqrt2}{H_d+\sqrt2}.
\]
Then the **unique incenter** and **exact inradius** are
\[
\boxed{c_d=(1-\lambda_d)\rho_d+\lambda_d\mu_d,\qquad
r_d=\frac{\sqrt2 H_d}{H_d+\sqrt2}.}
\]
At \(c_d\), every adjacent-difference facet has distance \(r_d\), and the rank-\(k\) prefix-sum facet has distance
\[
\boxed{\operatorname{dist}(c_d,B_k)=r_d\sqrt{\frac{k(d-k)}{d-1}},\qquad 1\le k<d.}
\]
For \(d\ge3\), precisely \(d+1\) of the \(2(d-1)\) facets are tangent: all \(d-1\) adjacent-difference facets and only the two extremal prefix-sum facets. When \(d=2\), both facets are tangent; for \(d=3\), all four facets are tangent. When \(d\ge4\), the remaining \(d-3\) prefix-sum facets are strictly noncontacting.

The unique smallest enclosing ball has center \(\mu_d\) and radius
\[
\boxed{R_d=\sqrt{\frac{d(d^2-1)}{12}}.}
\]
Exactly the \(2^{d-1}\) vertices touch this outer sphere. Consequently \(R_d/r_d\sim d^{3/2}/\sqrt{24}\), whereas the ordinary permutahedron with the same outer sphere has inradius \(H_d/2\) and aspect ratio of order \(\sqrt d\). This is an explicit Euclidean shape distortion under removal of permutation vertices, despite the avoidance polytope retaining the cube face lattice.

## Assumptions and scope

The patterns \(132\) and \(213\) have their usual subsequence meaning. Let \(\operatorname{Av}_d(132,213)\) be the permutations of \([d]\) avoiding both, and set
\[
P_d=\operatorname{conv}\{(\pi_1,\ldots,\pi_d):\pi\in\operatorname{Av}_d(132,213)\}.
\]
All radii, lengths, and distances are measured with the standard Euclidean norm restricted to the affine hyperplane
\[
H=\{x\in\mathbb R^d:\sum_{i=1}^d x_i=d(d+1)/2\}.
\]
For \(1\le k<d\), define the adjacent-difference facets \(A_k: x_k-x_{k+1}\ge-1\) and the prefix-sum facets
\[
B_k:\sum_{i=1}^k x_i\le M_k,\quad M_k=\frac{k(2d-k+1)}2.
\]
Their irredundancy and completeness, as well as the fact that the avoidance class has exactly \(2^{d-1}\) elements, are **previously established facts**, not part of the new claim: see Tamayo Jiménez [2] and de Castro [1].

## Proof

**Intrinsic facet normals.** The normal of \(A_k\) lies in the tangent space \(H-H\) and has norm \(\sqrt2\), so its nonnegative slack \(1+x_k-x_{k+1}\) divided by \(\sqrt2\) is the distance to its supporting hyperplane. The projection of the normal \(\mathbf1_{\{1,\ldots,k\}}\) of \(B_k\) onto \(H-H\) has norm \(\sqrt{k(d-k)/d}\).

**Deficits and necessary inball conditions.** Define \(u_k=M_k-\sum_{i=1}^k x_i\) and put \(u_0=u_d=0\). The inverse map is \(x_k=d-k+1+u_{k-1}-u_k\). Let \((Lu)_k=2u_k-u_{k-1}-u_{k+1}\) denote the Dirichlet path Laplacian. As established in [1, Section 2], the facet inequalities are equivalent to \(u_k\ge0\) and \((Lu)_k\le2\). The ball of radius \(r\ge0\) centered at \(x\) can lie in \(P_d\) only if, for every \(k\),
\[
 u_k\ge r\sqrt{\frac{k(d-k)}d},\qquad
 (Lu)_k\le 2-\sqrt2\,r.
\tag{1}
\]
These are also sufficient because the facet description is complete.

**Green-matrix upper bound.** The inverse of \(L\) has the strictly positive entries
\[
 (L^{-1})_{ij}=\frac{\min(i,j)\,[d-\max(i,j)]}{d},\qquad 1\le i,j<d.
\]
Each column is piecewise affine with a unit Laplacian at its index and zero Dirichlet endpoints, verifying this identity directly. Consequently, from (1) and positivity,
\[
 u_k\le(2-\sqrt2\,r)\frac{k(d-k)}2,
\]
since \(L^{-1}\mathbf1\) is the parabolic vector with entry \(k(d-k)/2\). At \(k=1\), the lower and upper bounds yield
\[
 r\sqrt{\frac{d-1}{d}}\le \frac{d-1}{2}(2-\sqrt2\,r),
\]
which rearranges to the sharp bound
\[
 \boxed{r\le \frac{\sqrt2\sqrt{d(d-1)}}{\sqrt{d(d-1)}+\sqrt2}=r_d.}
\tag{2}
\]
All signs are valid: (1) and the positivity of \(L^{-1}\) force the right side of (1) to be nonnegative for a feasible ball.

**Existence, all facet distances, and uniqueness.** Take \(r=r_d\), define \(b=2-\sqrt2 r_d=2r_d/H_d\), and set
\[
 u_k^*=\frac{b}{2}k(d-k)=\frac{r_d}{H_d}k(d-k).
\]
Then \(Lu^*=b\mathbf1\), so the \(A_k\) inequalities have distance exactly \(r_d\). The \(B_k\) distances are
\[
 \frac{u_k^*}{\sqrt{k(d-k)/d}}
 =r_d\sqrt{\frac{dk(d-k)}{d(d-1)}}
 =r_d\sqrt{\frac{k(d-k)}{d-1}}\ge r_d.
\]
The last inequality is equality precisely for \(k=1\) or \(k=d-1\), because \(k(d-k)\ge d-1\) for all \(1\le k<d\). Thus (2) is attained and the asserted contact classification follows. The inverse formula for \(x_k\) gives
\[
 x_k=d-k+1+\frac{r_d}{H_d}(2k-d-1)
 =(1-\lambda_d)(\rho_d)_k+\lambda_d(\mu_d)_k
\]
with \(\lambda_d=2r_d/H_d\).

If another center \(u\) supports radius \(r_d\), (1) and the Green-matrix bound force \(u_1=u_1^*\). Put \(z=b\mathbf1-Lu\), which is coordinatewise nonnegative. Then
\[
 u^*-u=L^{-1}z,\qquad (u^*-u)_1=0.
\]
Every entry of the first row of \(L^{-1}\) is strictly positive, so \(z=0\) and hence \(u=u^*\). The incenter is therefore unique.

**Outer sphere and its contacts.** Every vertex is a permutation of the numbers \(1,\ldots,d\), hence lies at squared distance
\[
 \sum_{i=1}^d\left(i-\frac{d+1}2\right)^2=\frac{d(d^2-1)}{12}
\]
from \(\mu_d\). Both increasing and decreasing permutations avoid \(132\) and \(213\), and their coordinate vectors are antipodal about \(\mu_d\). Any enclosing sphere must contain this antipodal pair and so have radius at least \(R_d\); if equality holds, its center must be their midpoint \(\mu_d\), proving uniqueness. All vertices lie on this sphere. Strict convexity of squared Euclidean distance shows that every proper convex combination of distinct vertices lies strictly inside; hence no nonvertex contact exists.

## Verification

The standalone standard-library program `verification/verify_avoiding_inball.py` reconstructs all \(2^{d-1}\) pattern-avoiding vertices by cuts through \(d=10\), verifies their facet signatures with exact integers (8,194 tests), and performs 14,850 high-precision Laplacian, distance-shell, and Green-matrix positivity checks for \(2\le d\le100\). All 23,044 checks passed. A separate linear-programming maximization of the Euclidean inball radius agreed with the formula for every \(2\le d\le32\). Neither finite check proves the unrestricted claim; the Green-matrix inequality and equality reconstruction above do.

To reproduce the self-contained checks, run `python3 verification/verify_avoiding_inball.py` from the extracted finding directory. The script needs only the Python standard library and no network resources.

## Relationship to prior work

Tamayo Jiménez [2, Section 3.5] already identified the avoidance vertices, the paired facets, and the cubical combinatorics; de Castro [1, Sections 2–3] provided a self-contained facet proof and identified the polytope up to lattice equivalence with a chain-poset permutahedron and with a discriminant Newton polytope. The map to the chain model has linear part \(-I\) and therefore preserves intrinsic Euclidean distances, but neither source gives the present inradius, unique incenter, exact Euclidean facet-distance spectrum, or radius-vs-dimension contrast. Davis and Sagan [3] initiated this family; Black, Rehberg, and Sanyal [4] studied poset permutahedra principally through their combinatorics and lattice geometry. A general convex optimization method computes an inball for any known finite facet system, but does not imply this closed form or equality classification without the positive Green-matrix argument.

## Limitations

The result applies specifically to the canonical coordinate realization of the \(132,213\)-avoiding permutahedra and the intrinsic Euclidean metric; a general lattice equivalence does not preserve Euclidean radii. The theorem does not address other avoidance classes or the Ehrhart-root conjectures. The new facet-distance formula gives distances to supporting hyperplanes, not necessarily nearest points in the relative interiors of their individual facets; only tangency for facets attaining the minimum is used. Unindexed equivalent metric calculations could exist despite the focused literature comparison. No independent mathematical review has been performed.

## References

[1] P. M. M. de Castro, *On the real-rootedness of Ehrhart \(h^*\)-polynomials of \((132,213)\)-avoiding permutahedra*, arXiv:2609.06096, first public version September 5, 2026, revised October 29, 2026. https://arxiv.org/html/2609.06096v2

[2] D. Tamayo Jiménez, *Pattern Avoiding Subpolytopes of the Permutahedron*, undergraduate thesis, Universidad de los Andes, May 2017, Section 3.5 and Appendix B. https://repositorio.uniandes.edu.co/bitstreams/c815ce77-06dc-441f-ab37-9f7ad22e7c98/download

[3] R. Davis and B. Sagan, *Pattern-Avoiding Polytopes*, arXiv:1608.08525, Sections 1–3. https://arxiv.org/abs/1608.08525

[4] A. Black, J. Rehberg, and R. Sanyal, *Poset Permutahedra*, 2025, cited for the chain-poset model and related enumerative geometry (see [1, Section 3.1]).
