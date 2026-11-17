# Exact Euclidean diameters and parity-rigid contacts of biclique cycle-space zonotopes

## Finding
Let \(p,q\ge2\) be integers. Give the edge space of the complete bipartite graph \(K_{p,q}\) the standard Euclidean (Frobenius) metric by identifying its oriented edges with the cells of a \(p\times q\) matrix. Let
\[
H_s=I_s-\frac1s\mathbf1_s\mathbf1_s^{\mathsf T},\qquad
Z_{p,q}=\{H_p XH_q:X\in[0,1]^{p\times q}\}.
\]
This is the orthogonal cycle-space projection of the edge cube, a centrally symmetric cographic zonotope of dimension \((p-1)(q-1)\). Put
\[
\varepsilon_s=\begin{cases}1,&s\text{ odd},\\0,&s\text{ even},\end{cases}\qquad
\eta_{p,q}=\max\left\{\varepsilon_p\frac qp,\ \varepsilon_q\frac pq\right\}.
\]
Then the exact Euclidean diameter and minimum-enclosing-sphere radius are
\[
\boxed{\operatorname{diam}_F(Z_{p,q})^2=pq-\eta_{p,q},\qquad
R_F(Z_{p,q})^2=\frac{pq-\eta_{p,q}}4.}
\]
The minimum enclosing sphere has the **unique** center zero, and all diametral pairs are precisely the antipodal pairs among its outer contacts. The contact points are exactly
\[
\frac12H_p\sigma H_q,\qquad \sigma\in\{-1,1\}^{p\times q},
\]
for the following fully characterized sign matrices (with any repeated images counted as the same point):

- When \(p,q\) are both even: every row sum and every column sum of \(\sigma\) equals zero.
- When \(p\) is odd and \(\varepsilon_p q/p\ge\varepsilon_q p/q\), with \(\varepsilon_p q/p>0\): every column sum is \(\pm1\), and all row sums are equal.
- In the remaining case, necessarily \(q\) is odd and \(\varepsilon_q p/q>\varepsilon_p q/p\): every row sum is \(\pm1\), and all column sums are equal.

The two descriptions agree when \(p=q\) is odd. Every outer contact is a vertex of the zonotope, and no nonvertex point is an outer contact. The scalar formula is equivalently the sharp mixed-operator-norm identity
\[
\bigl\|X\mapsto H_p XH_q\bigr\|_{\ell_\infty^{pq}\to\ell_2^{pq}}^2=pq-\eta_{p,q}.
\]

## Assumptions and scope
Orient each edge from the first color class to the second. The real edge-flow cycle space is
\[
C=\{Y\in\mathbb R^{p\times q}:Y\mathbf1_q=0,\ \mathbf1_p^{\mathsf T}Y=0\}.
\]
The orthogonal projection from the full edge space onto \(C\) is \(P(X)=H_pXH_q\). The polytope \(Z_{p,q}=P([0,1]^{p\times q})\) is defined with the metric induced from the original edge coordinates; a different integral Gale-coordinate realization of a cographic zonotope need not be Euclidean-isometric to this one. Distances, radii, and contact classifications in this theorem use precisely this orthogonal realization. Zero belongs to the polytope because \(P\mathbf1=0\); it is its center of symmetry. The inequalities are for all integers \(p,q\ge2\), including the four-cycle.

## Proof
**1. Euclidean projection and diameter reduction.** Because \(H_p\) and \(H_q\) are orthogonal idempotents, \(P\) is the orthogonal projector onto the zero-row-sum and zero-column-sum subspace \(C\). Its rank is \((p-1)(q-1)\). The image \(Z_{p,q}\) is centrally symmetric about zero, since \(P(\mathbf1-X)=-P(X)\). Consequently, if \(R=\max_{z\in Z_{p,q}}\|z\|_F\), its diameter is exactly \(2R\), attained by any opposite outer contacts; the triangle inequality gives the converse bound. Moreover \(P([0,1]^{p\times q})=\frac12P([-1,1]^{p\times q})\). Convexity of the squared norm shows that its maximum on the sign cube occurs at a corner \(\sigma\in\{-1,1\}^{p\times q}\). Thus
\[
4R^2=\max_{\sigma\in\{-1,1\}^{p\times q}}\|H_p\sigma H_q\|_F^2.
\]

**2. A two-sided exact variance identity.** For a sign matrix write \(r_i=\sum_j\sigma_{ij}\) for row sums, \(c_j=\sum_i\sigma_{ij}\) for column sums, and \(t=\sum_i r_i=\sum_jc_j\). Orthogonality of the four matrix blocks associated to the constant and zero-sum subspaces yields
\[
\|H_p\sigma H_q\|_F^2
=pq-\frac1q\sum_{i=1}^p r_i^2
-\frac1p\sum_{j=1}^q c_j^2+\frac{t^2}{pq}.
\]
Equivalently,
\[
\|H_p\sigma H_q\|_F^2
=pq-\frac1p\sum_jc_j^2-\frac1q\sum_i(r_i-t/p)^2,
\]
and, on interchanging row and column,
\[
\|H_p\sigma H_q\|_F^2
=pq-\frac1q\sum_ir_i^2-\frac1p\sum_j(c_j-t/q)^2.
\]
If \(p\) is odd, each column sum \(c_j\) is odd, hence \(\sum_jc_j^2\ge q\); the first nonnegative-variance identity gives an upper bound \(pq-q/p\). Equality holds precisely when every \(|c_j|=1\) and the row sums are constant. If \(q\) is odd, the transposed argument gives \(pq-p/q\), with equality precisely when every \(|r_i|=1\) and column sums are constant. When both dimensions are even, the trivial \(\|P\sigma\|_F\le\|\sigma\|_F=\sqrt{pq}\) is an upper bound, with equality exactly when all row and column sums vanish. Combining the relevant bounds gives \(\|P\sigma\|_F^2\le pq-\eta_{p,q}\) and all the stated equality conditions, provided that the bound is attained.

**3. Explicit sign witnesses in every parity regime.** If \(p,q\) are even, take the checkerboard sign matrix \(\sigma_{ij}=(-1)^{i+j}\); every row and column sum vanishes. If \(p\) is odd and \(q\) even, choose any sign vector \(v\in\{-1,1\}^p\) with sum one and group the columns into opposite pairs \(v,-v\). Every column sum is \(\pm1\), and each row sum is zero. The case of even \(p\), odd \(q\) follows by transposition. If both \(p,q\) are odd, transpose if necessary to arrange \(p\le q\). Choose a length-\(p\) sign vector \(v\) with sum one. Take its \(p\) cyclic shifts as the first \(p\) columns; every one of those column sums is one, and every row sum of this square block is one. Fill the remaining even number of columns in opposite pairs \(v,-v\). All column sums have modulus one, while all row sums remain one. This attains \(pq-q/p\), the sharper bound when \(p\le q\). Therefore the bound and equality classifications hold for every \(p,q\ge2\).

**4. Contact points, absence of nonvertex contacts, and the unique center.** If a point \(z\in Z_{p,q}\) attains \(\|z\|_F=R\), express it as a convex combination of the projected sign corners \(\frac12P\sigma\). Every such corner has norm at most \(R\). Strict convexity of squared Euclidean norm implies that all projected corners in a positive-weight combination for \(z\) must be the same point. Hence every contact is represented by a maximizing sign corner and is an extreme point; no nonvertex point contacts the outer sphere. The converse is immediate from the variance identity. For any \(z,w\in Z_{p,q}\), equality in \(\|z-w\|_F\le\|z\|_F+\|w\|_F\le2R\) is possible only if \(w=-z\) and both norms are \(R\). Thus the diameter pairs are precisely antipodal outer contacts. Finally, any Euclidean ball of radius \(R\) enclosing both \(z\) and \(-z\) with \(\|z\|=R\) must have center zero (the two radius-\(R\) balls about opposite endpoints meet only at their midpoint). This proves uniqueness of the center and completes the theorem.

## Verification
Run `python3 check_biclique_cycle_diameter.py` using Python's standard library. It independently evaluates the exact rational squared norm from the projection identity, verifies explicit witnesses for all 2,401 parameter pairs with \(2\le p,q\le50\), and exhausts all binary sign matrices for 13 parameter pairs with dimensions through \(4\times4\), checking both the maximum and the necessary-and-sufficient contact criterion. The reproducible success marker is `BICLIQUE_CYCLE_DIAMETER_PASS`. These computations check finite instances only; the parity bounds, constructions, and rigidity argument above prove the all-parameter claim.

## Relationship to prior work
Bach, Beck and Rehberg introduce and study **tocyclotopes** and general lattice Gale zonotopes, with Ehrhart and oriented-matroid results (arXiv:2409.15227v1). Their integral Gale realizations motivate considering cographic zonotopes, but the present Euclidean normalization is the *orthogonal edge-space projection*, not an assumed metric property of the lattice Gale realization. In that inspected work there is no corresponding \(K_{p,q}\) Euclidean diameter, parity formula, or outer-contact classification.

Dilworth, Kutzarova and Ostrovskii study invariant projections onto graph cycle spaces (arXiv:2305.12582); symmetry and projection techniques are known background. The prior public biclique projection result *Symmetry-optimal biclique projections and the exceptional uniqueness of the square* identifies the **same** orthogonal operator \(H_p(\cdot)H_q\), proves its optimality in row/column-invariant operator-norm problems, and computes \(\ell_1\to\ell_1\) and \(\ell_\infty\to\ell_\infty\) endpoint norms. Neither the projection identity nor the same-exponent endpoint constants are asserted as new here. The present result is specifically the different mixed \(\ell_\infty\to\ell_2\) norm, its exact parity-imbalance formula, and complete Euclidean diameter/contact geometry. The related complete-graph circulation-zonotope radius result concerns a different graph and parity obstruction, not this biclique statement.

## Limitations
The result holds for unweighted complete bipartite graphs under the standard Frobenius metric on the original edge coordinates; general graphs, edge weights, arbitrary \(\ell_p\) norms, and different metric realizations are not covered. The theorem characterizes contact sign matrices, but does not give a closed formula for the number of distinct contact vertices in every parameter pair; multiple sign corners may potentially project to the same point. The standalone checker does not certify infinitely many instances. Historical priority is provisional: an older unindexed theorem on double-centered sign matrices or mixed operator norms could conceivably imply the claimed result. No independent audit or external formal certification is claimed.

## References
1. E. Bach, M. Beck and S. Rehberg, *Acyclotopes and Tocyclotopes*, arXiv:2409.15227v1 (first public 2024-09-23), https://arxiv.org/abs/2409.15227 . The tocyclotope/lattice Gale construction and Ehrhart theory.
2. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle Spaces: Invariant Projections and Applications to Transportation Cost*, arXiv:2305.12582 (2023), https://arxiv.org/abs/2305.12582 . Invariant cycle projections.
3. *Symmetry-optimal biclique projections and the exceptional uniqueness of the square*, public full research statement (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-symmetry-optimal-biclique-projections-and-the-exceptional-unique--4fee91105690 . Explicit prior projector identity and same-exponent norms.
4. *Cycle-length facet shells and tournament contacts in near-top acyclohedra*, public full research statement (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-cycle-length-facet-shells-and-tournament-contacts-in-near-top-ac--32c5a604eada . Complete-graph circulation-zonotope comparison.
