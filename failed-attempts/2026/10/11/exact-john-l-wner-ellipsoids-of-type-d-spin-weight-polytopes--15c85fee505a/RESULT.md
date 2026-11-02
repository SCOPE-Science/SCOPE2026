# Exact John–Löwner ellipsoids of type-D spin weight polytopes
## Finding
For every integer
\[
n\ge4,
\]
consider the type-\(D_n\) spin fundamental-weight polytope
\[
H_n^+
=
P_{D_n}(\lambda_n).
\]
Using the standard orthonormal basis \(e_1,\ldots,e_n\), the type-\(D_n\) fundamental weight is
\[
\lambda_n=\frac12(e_1+\cdots+e_n),
\]
and the Weyl group consists of coordinate permutations together with an even number of sign changes. Hence
\[
\boxed{
H_n^+
=
\operatorname{conv}
\left\{
\frac12\varepsilon:
\varepsilon\in\{\pm1\}^n,\ 
\prod_{i=1}^n\varepsilon_i=1
\right\}.
}
\tag{1}
\]
The other spin fundamental-weight polytope
\[
P_{D_n}(\lambda_{n-1})
\]
is the opposite-parity half of the cube and is isometric to \(H_n^+\). All statements below therefore hold for both spin polytopes.

Their unique Euclidean incenter and circumcenter are the origin, with
\[
\boxed{
r_{\mathrm{in}}(H_n^\pm)=\frac12,
\qquad
R_{\mathrm{circ}}(H_n^\pm)=\frac{\sqrt n}{2}.
}
\tag{2}
\]

More strongly, their John and Löwner ellipsoids are exactly
\[
\boxed{
E_J(H_n^\pm)=\frac12 B_2^n,
\qquad
E_L(H_n^\pm)=\frac{\sqrt n}{2}B_2^n.
}
\tag{3}
\]

The inball contact pattern has a sharp dimension-four transition. For \(n=4\), the centered radius-\(\frac12\) ball is tangent to all \(16\) facets. For
\[
n\ge5,
\]
it is tangent exactly to the \(2n\) coordinate facets
\[
x_i=\pm\frac12.
\tag{4}
\]
The remaining
\[
2^{n-1}
\]
facets are simplex facets and are strictly farther away, at distance
\[
\boxed{
\frac{n-2}{2\sqrt n}.
}
\tag{5}
\]

Every one of the
\[
2^{n-1}
\]
vertices lies on the Löwner sphere. Consequently
\[
H_n^\pm\subseteq \sqrt n\,E_J(H_n^\pm)
\tag{6}
\]
and equality in radial norm occurs at every vertex. When \(n\) is even, \(H_n^\pm\) is centrally symmetric, so (6) attains the sharp \(\sqrt n\) containment factor from the symmetric John theorem.

## Assumptions and scope
The realization is the standard Euclidean type-\(D_n\) weight-polytope realization used in Coxeter geometry. The normalization in (1) is the one induced by the standard type-\(D_n\) fundamental weight
\[
\lambda_n=\frac12(e_1+\cdots+e_n).
\]

The theorem is stated for \(n\ge4\), the irreducible \(D_n\) range. It concerns the two spin fundamental weights \(\lambda_{n-1},\lambda_n\), not the other fundamental weights.

The John ellipsoid means the maximum-volume ellipsoid contained in the polytope. The Löwner ellipsoid means the minimum-volume ellipsoid containing it.

## Proof
Ardila, Castillo, Eur, and Postnikov define a weight polytope by
\[
P_\Phi(x)=\operatorname{conv}\{wx:w\in W_\Phi\}.
\]
For type \(D_n\), they give
\[
\lambda_n=\frac12(e_1+\cdots+e_n)
\]
and describe \(W_{D_n}\) as the evenly signed coordinate permutations. This proves (1).

We next use the standard parity-polytope halfspace description. After translating and scaling the \(0/1\) even- or odd-parity polytope to the cube \([-\frac12,\frac12]^n\), one obtains
\[
H_n^+
=
\left\{
x\in\mathbb R^n:
-\frac12\le x_i\le\frac12,\quad
s\cdot x\le\frac{n-2}{2}
\text{ for all }
s\in\{\pm1\}^n,\ \prod_i s_i=-1
\right\}.
\tag{7}
\]
For \(n\ge4\), all inequalities in (7) are facet-defining. The other spin polytope has the same description with the parity class of \(s\) reversed, hence is isometric.

The origin has distance
\[
\frac12
\]
from every coordinate facet. A parity-facet normal \(s\) has Euclidean norm
\[
\|s\|_2=\sqrt n,
\]
so its distance from the origin is
\[
\frac{(n-2)/2}{\sqrt n}
=
\frac{n-2}{2\sqrt n}.
\tag{8}
\]
For \(n=4\), (8) equals \(\frac12\). For \(n\ge5\),
\[
\frac{n-2}{2\sqrt n}>\frac12
\]
because
\[
(n-2)^2>n.
\]
Thus the centered radius-\(\frac12\) ball is feasible, with the asserted tangency pattern.

No larger ball can fit. Indeed, if a radius-\(r\) ball centered at \(c\) lies in \(H_n^+\), the opposite coordinate facets require
\[
\frac12-c_i\ge r,
\qquad
\frac12+c_i\ge r
\]
for every \(i\). Adding gives
\[
r\le\frac12.
\]
At equality, both inequalities force
\[
c_i=0
\]
for every \(i\). This proves the inradius and uniqueness of the incenter.

Every vertex in (1) has norm
\[
\frac{\sqrt n}{2}.
\tag{9}
\]
The minimum enclosing Euclidean ball of a compact set is unique. Since \(W_{D_n}\) acts orthogonally and preserves \(H_n^+\), its circumcenter must be fixed by all evenly signed permutations. The only fixed vector is \(0\). Equation (9) therefore proves
\[
R_{\mathrm{circ}}=\frac{\sqrt n}{2}
\]
and shows that every vertex is a contact point.

It remains to identify the two extremal ellipsoids. Both the John ellipsoid and Löwner ellipsoid are unique. Therefore each is preserved by the full \(W_{D_n}\)-action.

Any ellipsoid preserved by all coordinate permutations and all even sign changes has center \(0\) and scalar quadratic form. To see this, permutation invariance makes all diagonal entries of its quadratic form equal and all off-diagonal entries equal. Changing the signs of two coordinates leaves the ellipsoid invariant but reverses selected off-diagonal entries, forcing every off-diagonal entry to vanish. Hence any \(W_{D_n}\)-invariant ellipsoid is a Euclidean ball.

The largest invariant ball contained in \(H_n^\pm\) is therefore the inball found above, and the smallest invariant ball containing it is the circumball. This proves (3).

Finally, the ratio of the two radii is
\[
\frac{R_{\mathrm{circ}}}{r_{\mathrm{in}}}=\sqrt n,
\]
which gives (6). If \(n\) is even, changing all signs uses an even number of sign changes, so the polytope is centrally symmetric. Thus the symmetric John containment factor \(\sqrt n\) is attained.

## Verification
The proof is arbitrary-dimensional. Its source-dependent inputs were checked directly in the full text of the Coxeter-weight-polytope source: the orbit definition of weight polytopes, the type-\(D_n\) fundamental spin weights, and the description of the type-\(D_n\) Weyl group as evenly signed permutations.

The parity-polytope halfspace description was independently compared with the standard Jeroslow inequality system as reproduced in the convex-optimization literature. Under the affine change from \(0/1\) coordinates to \(\pm\frac12\) coordinates, those inequalities become exactly (7).

The accompanying `verify.py` enumerates all spin-weight vertices for \(4\le n\le12\). It checks every coordinate and parity inequality, verifies the two facet distances, confirms the complete contact transition at \(n=4\), and checks affine independence of the equality vertices for representative facets. These finite checks are corroborative only.

## Relationship to prior work
Ardila, Castillo, Eur, and Postnikov place fundamental weight polytopes among the canonical deformations of Coxeter permutohedra. Their paper explicitly gives the type-\(D_n\) spin weights and evenly signed Weyl action, and emphasizes fundamental weight polytopes as distinguished extremal objects in the symmetric deformation cone.

The parity-polytope literature gives the exact halfspace description used in (7), but its role there is combinatorial optimization rather than the Euclidean John–Löwner geometry of type-\(D_n\) spin weight polytopes.

The directly inspected Coxeter source contains no occurrence of “inradius”, “circumradius”, “Euclidean”, or “Löwner”, and no John-ellipsoid statement in the relevant metric sense. Targeted searches for demihypercube, halfcube, parity-polytope, and type-\(D\) spin-weight inradii, circumradii, John ellipsoids, Löwner ellipsoids, and exact contact facets did not locate a theorem implying (2)--(6).

The result is not a restatement of uniformity. Vertex transitivity immediately places the vertices on one sphere, but it does not by itself determine the maximum inscribed ellipsoid, the unique incenter, or which of the two exponentially different facet orbits controls the inball.

## Limitations
The theorem concerns the canonical spin fundamental-weight normalization. Rescaling the weight rescales every radius, while arbitrary affine images need not preserve Euclidean balls or ellipsoids.

Only the two spin fundamental-weight polytopes are treated. Other type-\(D_n\) fundamental weight polytopes have different vertex and facet systems.

The facet-distance computation is short once the parity-polytope H-description is supplied, so an equivalent observation may exist as folklore under coding-theory or parity-polytope terminology. Search nonappearance is not treated as a formal global novelty certificate.

## References
1. Federico Ardila, Federico Castillo, Christopher Eur, and Alexander Postnikov, *Coxeter submodular functions and deformations of Coxeter permutahedra*, arXiv:1904.11029, first public version 2019-04-24; Advances in Mathematics 365 (2020), 107039, DOI 10.1016/j.aim.2020.107039.
2. James Saunderson, Pablo A. Parrilo, and Alan S. Willsky, *Semidefinite Descriptions of the Convex Hull of Rotation Matrices*, SIAM Journal on Optimization 25 (2015), 1314--1343, DOI 10.1137/14096339X. The paper records the standard parity-polytope facet description attributed to Jeroslow.
