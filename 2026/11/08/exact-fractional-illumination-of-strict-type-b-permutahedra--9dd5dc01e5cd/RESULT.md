# Exact fractional illumination of strict type-\(B\) permutahedra
## Finding
For every integer \(n\ge 1\) and every strictly ordered positive sequence \(0<a_1<\cdots<a_n\), form the signed-permutation polytope
\[
 P=\operatorname{conv}\{(\varepsilon_1 a_{\sigma(1)},\ldots,\varepsilon_n a_{\sigma(n)}):\sigma\in S_n,\ \varepsilon_i\in\{-1,1\}\}\subset\mathbb R^n.
\]
Its fractional directional illumination number is exactly
\[
 \boxed{I^*(P)=\frac{4^n}{\binom{2n}{n}}\sim\sqrt{\pi n}.}
\]
More strongly, every direction outside finitely many signed-subset-sum hyperplanes illuminates exactly
\[
 \boxed{\alpha_n=(2n-1)!!=\frac{(2n)!}{2^n n!}}
\]
of the \(2^n n!\) vertices, whereas every other direction illuminates at most \(\alpha_n\) vertices. The formula is independent of the particular positive strictly increasing sequence.

In three dimensions this class includes the regular truncated cuboctahedron, whose vertices are the signed permutations of \((1,1+\sqrt 2,1+2\sqrt 2)\); its exact fractional illumination number is \(16/5\). For dimensions \(1,2,3,4\), the values are respectively \(2\), \(8/3\), \(16/5\), and \(128/35\).

## Assumptions and scope
A nonzero vector \(u\) illuminates a boundary point \(x\) of a full-dimensional convex body \(K\) when \(x+\varepsilon u\in\operatorname{int}K\) for some \(\varepsilon>0\). A finite nonnegative measure on directions is a fractional illumination if, for every boundary point, the total weight of directions illuminating that point is at least one. Its minimum possible total mass is \(I^*(K)\).

For a polytope it suffices to verify fractional constraints at all vertices. Indeed, for a boundary point \(x\) in a face \(F\), choose a vertex \(v\) of \(F\). Every facet inequality active at \(x\) is also active at \(v\); therefore any direction decreasing all facet inequalities active at \(v\) also illuminates \(x\). No probability distribution is imposed on illumination directions.

The strict inequalities \(0<a_1<\cdots<a_n\) are necessary for the stated generic type-\(B\) normal-fan description. When coordinates coincide or the smallest coordinate vanishes, the fan may coarsen and illumination counts can change; those boundary families are excluded. All dimensions and all nondegenerate parameter values satisfying the inequalities are covered.

## Proof
### 1. Normal-cone reduction
At the vertex \(v=(a_n,a_{n-1},\ldots,a_1)\), the outward normal cone is the standard type-\(B\) Weyl chamber
\[
 N_P(v)=\{w\in\mathbb R^n:w_1\ge w_2\ge\cdots\ge w_n\ge0\}.
\]
This follows directly from the rearrangement inequality: a linear functional with nonnegative weakly decreasing coordinates is maximized on the signed-permutation orbit at \(v\). Conversely the strict inequalities in the parameters make every adjacent order or sign exchange a genuine support change, so the displayed cone is the full normal cone. Its extreme rays are \(e_1\), \(e_1+e_2\), \(\ldots\), \(e_1+\cdots+e_n\).

Thus \(u\) illuminates \(v\) exactly when
\[
 u_1<0,\quad u_1+u_2<0,\quad\ldots,\quad u_1+\cdots+u_n<0.
\tag{1}
\]
At an arbitrary vertex, first reorder its coordinates in strictly decreasing absolute value and then multiply the corresponding coordinates of \(u\) by the signs of that vertex. Condition (1) holds for the resulting signed permutation. As the vertex ranges over all \(2^n n!\) possibilities, these signed sequences run once through the entire signed-permutation orbit of the direction's coordinate values.

### 2. A signed-permutation persistence count
Call a direction \(u\) *noncancelling* if
\[
 \sum_{i=1}^n\delta_i u_i\ne0
 \qquad\text{for every }(\delta_1,\ldots,\delta_n)\in\{-1,0,1\}^n\setminus\{0\}.
\tag{2}
\]
These directions are the complement of a finite union of proper hyperplanes and therefore form an open dense set. In particular their absolute coordinate values are distinct and nonzero, and no signed partial sum vanishes.

Choose a signed permutation of the coordinates of such a fixed \(u\) uniformly at random, obtaining \((X_1,\ldots,X_n)\). This finite random vector is exchangeable under all coordinate permutations and sign-invariant under independent coordinate sign flips. All its nonempty partial sums are nonzero. The exchangeable, sign-invariant version of Sparre Andersen's fluctuation identity (Berger--Béthencourt, arXiv:2304.09031, Theorem 2.1) therefore applies and gives
\[
 \mathbb P\bigl(X_1<0,\ X_1+X_2<0,\ldots,\ X_1+\cdots+X_n<0\bigr)
 =\frac{\binom{2n}{n}}{4^n}.
\tag{3}
\]
This is an exact finite-set probability, not a limiting or independent-increments approximation. Multiplying (3) by the number \(2^n n!\) of signed permutations and using (1), each noncancelling direction illuminates exactly
\[
 \alpha_n=2^n n!\frac{\binom{2n}{n}}{4^n}
 =\frac{(2n)!}{2^n n!}=(2n-1)!!
\tag{4}
\]
vertices. The value is the same for every noncancelling direction, independent of its magnitudes.

### 3. No nongeneric direction does better
Let \(u\ne0\) be arbitrary, and let \(V(u)\) denote its finite set of illuminated vertices. At each vertex, illumination requires finitely many strict linear inequalities. Hence there is an open neighborhood of \(u\) in which every vertex of \(V(u)\) remains illuminated. The noncancelling directions defined by (2) are dense, so some direction in that neighborhood is noncancelling. Formula (4) implies
\[
 |V(u)|\le\alpha_n.
\tag{5}
\]
Thus the exact maximum incidence of a direction is \(\alpha_n\).

### 4. Lower and upper fractional bounds
Write \(N=2^n n!\). If \(\mu\) is an admissible fractional illumination, summing the weight requirements over the \(N\) vertices and interchanging a finite sum and the integral yields
\[
 N\le \int \#V(u)\,d\mu(u)\le\alpha_n\,\mu(\mathbb S^{n-1}),
\]
so \(I^*(P)\ge N/\alpha_n\).

Conversely, fix any noncancelling vector, for example \(u_0=(1,3,9,\ldots,3^{n-1})\). Take its complete signed-permutation orbit of \(N\) directions. Each of the \(N\) directions illuminates precisely \(\alpha_n\) vertices by (4). The signed-permutation symmetry group acts transitively on vertices, so every vertex is illuminated by precisely \(\alpha_n\) of the orbit directions: the total number of incidences is \(N\alpha_n\), and symmetry makes the number at every vertex equal. Assign mass \(1/\alpha_n\) to each orbit direction. Every vertex, hence the entire boundary, receives illuminating weight one, while the total weight is \(N/\alpha_n\). This matches the lower bound and proves
\[
 I^*(P)=\frac{N}{\alpha_n}=\frac{4^n}{\binom{2n}{n}}.
\]
The final asymptotic follows from Stirling's formula for the central binomial coefficient. The stated rank-three and low-rank values are direct substitutions, not extra independent assertions.

## Verification
Run the standalone Python 3 program `verify.py` with `python3 verify.py`. It uses only the standard library and exact integer arithmetic. For ranks \(1\) through \(6\), it exhausts every signed permutation of the generic direction \((1,3,\ldots,3^{n-1})\), checks noncancellation of all signed subsets, and confirms the \((2n-1)!!\) incidence count and the central-binomial identity. At rank \(4\) it tests three distinct noncancelling direction magnitude sets. At rank \(3\) it independently checks all \(48\) directions against all \(48\) vertices and certifies equal coverage of \(15\) directions per vertex. A successful run prints `SIGNED_PERMUTAHEDRON_EXACT_OK`.

The exact all-rank conclusions are proved by the normal-cone geometry, the cited finite exchangeable sign-invariant fluctuation theorem, generic perturbation, and symmetry averaging. Testing ranks through six is a reproducibility check, not an induction proof or an infinite certificate.

## Relationship to prior work
Gorodzha (arXiv:2609.23913v1, first publicly posted 2026-09-20) proves the general optimal universal bound \(I^*(K)\le 2^n\) and its parallelotope equality characterization. It does not state the strict type-\(B\) permutahedron value or the direction-independent exact incidence count. That recent universal theorem motivates resolving concrete symmetric families far below the exponential ceiling.

Godland and Kabluchko (arXiv:2009.04186; *Results in Mathematics* 2023, Theorem 4.4) establish that strict type-\(B\) permutahedra have the type-\(B\) Weyl fan; their angle-sum and projection theorems concern different invariants and do not themselves evaluate fractional illumination. Their normal-fan theorem is used, with a direct rearrangement argument supplied here.

Berger and Béthencourt (arXiv:2304.09031, Theorem 2.1) give the exchangeable sign-invariant persistence identity. The present application to inward tangent cones is the step turning that probabilistic theorem into a sharp geometric illumination incidence invariant. The probabilistic identity is not claimed as new.

A prior exact illumination study of the regular dodecahedron and icosahedron established the vertex-transitive fractional identity \(I^*(P)=f_0(P)/\max_u\#V(u)\). Its full public result was examined; this identity is acknowledged as prior and is also proved directly in the final step above. Its Platonic-solid counts do not imply the signed-permutahedron incidence formula. Other published exact values for products of simplices and certain regular solids concern different normal fans or different figures.

Searches on type-\(B\) permutahedra, sign-permutation orbits, Sparre Andersen persistence, fractional illumination, central binomial coefficients, and the regular truncated cuboctahedron located no previous statement covering (3)--(5) as a geometric illumination result. This is provisional historical assessment, not proof of historical priority.

## Limitations
The result concerns strict type-\(B\) signed-permutation polytopes; it is not asserted for repeated or zero generator coordinates, general signed orbit polytopes with coarsened normal fans, or other reflection types. The exact ordinary illumination number is not determined. The geometric result uses an existing fluctuation identity and an existing normal-fan description, and independent mathematical validation and comprehensive historical-priority assessment remain open. No assumption of mathematical independence or novelty certification is made.

## References
1. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913v1 (2026-09-20).
2. T. Godland and Z. Kabluchko, *Projections and Angle Sums of Belt Polytopes and Permutohedra*, *Results in Mathematics* 78 (2023), article 140, DOI 10.1007/s00025-023-01918-2; preprint arXiv:2009.04186.
3. Q. Berger and L. Béthencourt, *An application of Sparre Andersen's fluctuation theorem for exchangeable and sign-invariant random variables*, arXiv:2304.09031 (2023); *Séminaire de Probabilités LII*, Lecture Notes in Mathematics 2363 (2025).
4. M. Naszódi, *Fractional illumination of convex bodies*, *Contributions to Discrete Mathematics* 4 (2009), 83--88, DOI 10.55016/ojs/cdm.v4i2.62022.
5. *Exact fractional illumination of the regular dodecahedron and icosahedron*, public published-finding corpus mathematical research record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-fractional-illumination-of-the-regular-dodecahedron-and-ic--760696b5ce34.
6. *Exact ordinary and fractional illumination of every product of simplices*, public published-finding corpus mathematical research record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-ordinary-and-fractional-illumination-of-every-product-of-s--24a86928f4ea.
