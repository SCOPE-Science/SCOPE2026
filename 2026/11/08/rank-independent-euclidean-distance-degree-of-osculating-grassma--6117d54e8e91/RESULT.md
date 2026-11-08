# Rank-independent Euclidean distance degree of osculating Grassmann curves

## Finding
For every integer \(d\ge2\) and each \(1\le r\le d\), the Euclidean distance degree of the curve of orthogonal projections onto the \(r\)-dimensional osculating spaces of the degree-\(d\) rational normal curve is
\[
\operatorname{EDdeg}(\mathcal C_{d,r})=2d.
\]
This is independent of the osculating rank. The two complex isotropic parameters each contribute a pole of exact order \(d\) to a generic trace objective.

## Assumptions and scope
Work over \(\mathbb C\), with real form given by \(\operatorname{Sym}^d\mathbb R^2\). Let \(V_d=\operatorname{Sym}^d(\mathbb C^2)\) and use the basis \(e_j=\binom dj s^{d-j}u^j\), for \(0\le j\le d\). Its inner product is \(\langle e_i,e_j\rangle=\delta_{ij}\binom di\); the real restriction is positive definite. Put \(v(t)=(s+tu)^d\), and \(U_{d,r}(t)=\langle v(t),v'(t),\ldots,v^{(r-1)}(t)\rangle\). The osculating spaces include the natural limiting value at \(t=\infty\). Let \(P_{d,r}(t)\) denote the orthogonal projector onto \(U_{d,r}(t)\) when the restricted bilinear form is nondegenerate. All projectors are expressed in an orthonormal coordinate system before measuring ordinary Frobenius distance; writing formulas in the weighted basis is merely an isometry.

The data matrix \(S\) is a generic complex symmetric endomorphism relative to this metric, **not** required to be a rank-\(r\) projector. Because \(P_{d,r}^2=P_{d,r}\) and \(\operatorname{tr}P_{d,r}=r\), the squared Frobenius-distance objective differs by a nonzero scalar and additive constant from \(f_S(t)=\operatorname{tr}(S P_{d,r}(t))\). ED degree counts its isolated complex critical points on the smooth nondegenerate projection curve.

## Proof
**1. Projection-curve and its domain.** The full osculating flag at \(t=0\) is the coordinate flag \(U_{d,r}(0)=\langle e_0,\ldots,e_{r-1}\rangle\), whose orthogonal projector is \(P_0=\operatorname{diag}(1^r,0^{d+1-r})\). Let \(T(t)=\begin{psmallmatrix}1&-t\\ t&1\end{psmallmatrix}\), and write \(M_d(t)=\operatorname{Sym}^dT(t)\). This sends the coordinate osculating flag to the flag at \(t\), and \(M_d(-t)M_d(t)=(1+t^2)^dI\). Its action is conformal orthogonal for the chosen bilinear form, so
\[
P_{d,r}(t)=\frac{M_d(t)P_0M_d(-t)}{(1+t^2)^d},\qquad t^2+1\ne0. \tag{1}
\]
The matrix coefficients of \(M_d(t)\) are polynomials of degree at most \(d\). For real \(t\) the metric is positive and the denominator is nonzero. Over \(\mathbb C\) the restricted metric is nondegenerate exactly for \(t\ne\pm i\): its Gram determinant is a nonzero constant times \((1+t^2)^{r(d-r+1)}\), as follows either from the transformed osculating wedge or from the \(\mathrm{SO}(2)\) action and the scalar triangular change of jet basis. The projector has a regular value at \(t=\infty\), using \(1/t\) as local parameter.

The map from parameter to the ordinary Grassmannian is an injective immersion: at zero, variation of its highest osculating vector has a nonzero \(e_r\) component outside \(\langle e_0,\ldots,e_{r-1}\rangle\). Projective changes of coordinate carry the same statement to all parameters. Injectivity follows because the only point of the rational normal curve lying on its osculating \((r-1)\)-plane is its contact point: after moving that point to zero, the coefficient of \(e_d\) in \(v(t)\) is nonzero for every other finite parameter (and the point at infinity is also outside for \(r\le d\)). The projection-coordinate map embeds the nondegenerate Grassmannian. Thus \(\mathcal C_{d,r}\) is smooth and the indicated parameterization is one-to-one on its domain.

**2. Laurent-degree upper bound.** Put \(z=(1+it)/(1-it)\), the character of the complexified rotation torus. The eigenweights of the torus on \(V_d\) are \(d,d-2,\ldots,-d\). Consequently its conjugation action on \(\operatorname{End}(V_d)\) has integer \(z\)-weights from \(-d\) to \(d\). Equation (1) is the torus orbit of \(P_0\) and therefore
\[
P_{d,r}(z)=\sum_{k=-d}^{d}z^k A_k,
\qquad f_S(z)=\sum_{k=-d}^{d}c_k(S)z^k,\quad c_k(S)=\operatorname{tr}(SA_k). \tag{2}
\]
This expresses the only possible poles of the trace objective as \(z=0,\infty\), corresponding to \(t=\pm i\), of orders at most \(d\).

**3. Both endpoint weights really occur at every rank.** The extremal torus eigenvectors are the isotropic pure powers \(h_+=(s+iu)^d\), \(h_-=(s-iu)^d\), paired nondegenerately by the bilinear form. The coefficient of the extremal conjugation weight in \(P_0\) is nonzero precisely when the matrix coefficient \(\langle h_+,P_0h_+\rangle\) is nonzero. Directly,
\[
\langle h_+,P_0h_+\rangle=\sum_{j=0}^{r-1}(-1)^j\binom dj=(-1)^{r-1}\binom{d-1}{r-1}\ne0. \tag{3}
\]
Complex conjugation exchanges the two endpoint weights. Thus \(A_d\ne0\) and \(A_{-d}\ne0\). For generic symmetric data \(S\), both \(c_d(S)\) and \(c_{-d}(S)\) are nonzero: the endpoints of \(P_0\)'s conjugation are self-adjoint-compatible matrix coefficients, and the trace pairing on the space of self-adjoint matrices is nondegenerate. (Equivalently, the coefficients of the matrix-valued Laurent polynomial cannot vanish under every self-adjoint linear functional.) Hence \(f_S\) has poles of exact order \(d\) at both excluded points, simultaneously for all ranks.

**4. Critical point count and simplicity.** For such generic \(S\), the meromorphic differential \(df_S\) on \(\mathbb P^1\) has poles of order \(d+1\) at each of \(z=0,\infty\), and no other poles. The canonical divisor of \(\mathbb P^1\) has degree \(-2\), so the total number of zeros of \(df_S\), with multiplicities, is
\[
2(d+1)-2=2d. \tag{4}
\]
These zeros are generically distinct. Indeed, the linear system of differentials \(\{df_S\}\), viewed after clearing the two fixed pole divisors as a subsystem of \(H^0(\mathbb P^1,\mathcal O(2d))\), has no base points. On the open curve this follows from \(dP_{d,r}/dz\ne0\): a nonzero derivative matrix pairs nontrivially with some self-adjoint \(S\). At the two pole parameters, (3) supplies a nonzero leading coefficient of a section. A generic member of a basepoint-free linear system on the smooth curve \(\mathbb P^1\) has simple zeros by characteristic-zero Bertini (equivalently, by the incidence argument for multiple zeros). No zero lies at a pole, and the source curve is one-to-one and immersive, so these \(2d\) zeros correspond to \(2d\) distinct ED-critical projectors. This proves the theorem.

## Verification
A standalone standard-library verifier is supplied as `verify.py`. In the finite field \(\mathbb F_{1009}\) it builds the exact symmetric-power transformation matrices \(M_d(t)\), computes the cleared stationarity numerator \((1+t^2)N'_S(t)-2dtN_S(t)\) for sample symmetric matrices, and finds full degree \(2d\) with squarefree roots and no pole roots for all \(44\) pairs \(2\le d\le9\), \(1\le r\le d\). It separately checks the nonzero endpoint-binomial identity for \(20099\) pairs \(2\le d\le200\). All tests passed. This finite certificate corroborates the unrestricted proof but does not replace it; the stated result is for characteristic zero and arbitrary \(d,r\).

## Relationship to prior work
Friedman, Hoşten and Rosana (2026) define ED and GD degree in the projection Grassmannian and calculate them for product, matroid and Schubert models. Friedman, Rosana and Sturmfels (2026) introduce GD degree for lines. Neither inspected paper gives the rank-independent osculating-flag curve computation (4). Their general optimization formalism is credited and is not claimed as new. Kozhasov, Mourrain and Parusiński (2026) optimize distance to discriminant and to *osculating varieties of binary forms in the coefficient space*, not distance to the *curve of osculating subspaces in a projection Grassmannian*. Di Rocco, Rose and Sodomaco investigate higher-order polar/distance loci, a different invariant. No implication from these different ambient objects to (4) was found. Classical rational normal curve equivariance and the differential-divisor method are background, not originality claims.

## Limitations
The theorem uses the specific positive Bombieri metric and generic **unrestricted symmetric** data. It does not compute GD degree, where data itself must be a projector; finite GD experiments alone do not prove the same answer. It does not address arbitrary embeddings or curves other than osculating flags of the rational normal curve. A self-review was performed; no independent mathematical audit or exhaustive historical-priority certification was conducted.

## References
- H. Friedman, S. Hoşten, A. Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018v2 (first public version 2026-10-01), https://arxiv.org/html/2610.02018v2.
- H. Friedman, A. Rosana, B. Sturmfels, *Distance Optimization in the Grassmannian of Lines*, arXiv:2601.22843v1 (2026-01-30), https://arxiv.org/html/2601.22843v1.
- K. Kozhasov, B. Mourrain, A. Parusiński, *On the Distance to Discriminants and Osculating Varieties*, arXiv:2610.06538 (2026-10-05), https://arxiv.org/abs/2610.06538.
- S. Di Rocco, K. Rose, L. Sodomaco, *Osculating Geometry and Higher-Order Distance Loci*, arXiv:2507.02823 (first public 2025-07-24), https://arxiv.org/abs/2507.02823.
