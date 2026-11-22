# Sharp opposite-orientation simplex envelopes of Ulam bodies and their reflection transition

## Finding
Let \(S=\operatorname{conv}\{v_0,\ldots,v_d\}\subset\mathbb R^d\) be a nondegenerate simplex, \(d\ge2\), with centroid \(G=(v_0+\cdots+v_d)/(d+1)\). Define \(M_q(S)\), \(0<q<1\), by its support points: in every nonzero normal direction, take the centroid of the halfspace cap containing a fraction \(q\) of the volume of \(S\). This is the Ulam floating body, also known as the corresponding zonoid-trimmed region.

**Theorem.** The unique least-factor, centroid-centred, positively homothetic simplices in the two prescribed orientations that contain \(M_q(S)\) are
\[
M_q(S)\subseteq G+\rho_d(q)(S-G),\qquad
M_q(S)\subseteq G-\sigma_d(q)(S-G),
\]
where
\[
\boxed{\rho_d(q)=\frac{d(1-q)}q\bigl(1-(1-q)^{1/d}\bigr),\qquad
\sigma_d(q)=d\bigl(1-q^{1/d}\bigr).}
\]
Every one of the \(d+1\) facets of each envelope contains an exposed point of \(M_q(S)\). Define \(D_d(q)=\sigma_d(q)-\rho_d(q)\). For each \(d\ge2\),
\[
D_d(q)>0\ (0<q<1/2),\qquad D_d(1/2)=0,\qquad D_d(q)<0\ (1/2<q<1).
\]
The only centrally symmetric member of the one-parameter family \(M_q(S)\) occurs at \(q=1/2\), and its center is \(G\). For fixed \(q\in(0,1)\),
\[
\lim_{d\to\infty}\rho_d(q)=-\frac{1-q}{q}\log(1-q),\quad
\lim_{d\to\infty}\sigma_d(q)=-\log q,
\]
and therefore
\[
\boxed{\lim_{d\to\infty}D_d(q)=-\log q+\frac{1-q}{q}\log(1-q).}
\]
This limiting signed gap is strictly positive before half-volume and negative after half-volume; it does not disappear with dimension.

**Planar inverse corollary.** For fixed \(q\in(0,1)\), consider the map from full-dimensional triangles in the plane to their buoyancy surfaces \(\partial M_q(T)\), with equality as actual subsets of the plane, not up to congruence. Its fibers have exactly one member for \(q\neq1/2\). At \(q=1/2\), each fiber consists of exactly the two distinct triangles \(T\) and \(2G-T\). This corollary uses the previously published theorem that equal planar buoyancy surfaces yield equal area-normalized difference bodies, and does not assert fixed-density reconstruction for general polygons.

## Assumptions and scope
All measures are uniform Euclidean volume measures. The fraction \(q\) is volume of the selected **cap** divided by volume of the entire simplex; it is not a surface-perimeter fraction, nor the cutting parameter of the classical convex floating body. A homothetic envelope is required to be centered at \(G\) and have exactly one of the two stipulated orientations: \(G+t(S-G)\) or \(G-t(S-G)\) with \(t\ge0\). No optimality is claimed among arbitrary translated or rotated simplex enclosures.

Write \(\lambda_i\) for barycentric affine coordinates, so \(\sum_i\lambda_i=1\), \(\lambda_i(v_j)=\mathbf1_{i=j}\), and \(\lambda_i(G)=1/(d+1)\). The original halfspace-centroid support characterization and affine equivariance of the Ulam body are established in Huang–Slomka–Werner (2019). Its support points trace a full-dimensional convex body for \(0<q<1\).

## Proof
**1. Coordinate extremizers.** If \(X\) is uniform in \(S\), then its barycentric coordinate \(Y=\lambda_i(X)\) has density \(d(1-y)^{d-1}\) on \([0,1]\); equivalently \(\Pr(Y\ge t)=(1-t)^d\). Maximizing an affine functional over the Ulam body selects the upper \(q\)-volume cap in that functional, and minimizing selects the lower \(q\)-volume cap. Thus the maximum and minimum barycentric coordinates on \(M_q(S)\) are the upper- and lower-tail conditional means of \(Y\), respectively:
\[
U_d(q):=\max_{x\in M_q(S)}\lambda_i(x)
=1-\frac{d}{d+1}q^{1/d},
\]
\[
L_d(q):=\min_{x\in M_q(S)}\lambda_i(x)
=1-\frac{d}{(d+1)q}\left[1-(1-q)^{1+1/d}\right].
\]
These formulas hold for each \(i\), since all barycentric marginals coincide. To derive them directly, the upper tail starts at \(1-q^{1/d}\) and the conditional residual to \(1\) is a scaled \(\mathrm{Beta}(d,1)\) variable; the lower mean follows by subtracting the first moment of the complementary upper \((1-q)\)-tail from the full mean \(1/(d+1)\). This proves the formulas without an approximation or a finite enumeration.

**2. Optimal envelopes and contacts.** The positively oriented centroid homothet \(G+t(S-G)\) is defined by \(\lambda_i\ge(1-t)/(d+1)\) for every \(i\); hence it contains \(M_q(S)\) exactly when \(t\ge1-(d+1)L_d(q)\). The opposite homothet \(G-t(S-G)\) is defined by \(\lambda_i\le(1+t)/(d+1)\); it contains the body exactly when \(t\ge(d+1)U_d(q)-1\). Inserting the tail means gives the stated \(\rho_d(q)\) and \(\sigma_d(q)\). Since the extreme affine value is attained for every \(i\), each chosen facet touches the body; any smaller factor misses at least one such point. The two factors are strictly positive for every interior \(q\).

**3. Sign and unique crossing.** Set \(\alpha=1+1/d\in(1,2)\) and
\[
H(q)=2q-1-q^\alpha+(1-q)^\alpha.
\]
A direct rearrangement yields \(D_d(q)=dH(q)/q\). One has \(H(0)=H(1/2)=H(1)=0\) and \(H(1-q)=-H(q)\). Furthermore
\[
H''(q)=\alpha(\alpha-1)\big[(1-q)^{\alpha-2}-q^{\alpha-2}\big]<0
\quad(0<q<1/2).
\]
Strict concavity between two zero endpoints forces \(H(q)>0\) for \(0<q<1/2\). Antisymmetry gives strict negativity for \(1/2<q<1\). No additional crossing is possible. In dimension one, excluded from the theorem, both factors coincide for all \(q\), as expected for intervals.

**4. Central symmetry.** Every affine permutation of the vertices of \(S\) preserves the uniform volume law and therefore preserves \(M_q(S)\). A full-dimensional convex body has at most one center of point-reflection symmetry; if \(M_q(S)\) has one, it must be fixed by all vertex permutations. Their unique common fixed point is \(G\). Reflection symmetry about \(G\) would force \(U_d(q)+L_d(q)=2/(d+1)\), or equivalently \(D_d(q)=0\). Part 3 shows this is impossible away from \(q=1/2\). At \(q=1/2\), opposite caps partition \(S\) and have opposite centroids relative to \(G\), proving \(M_{1/2}(S)-G=-(M_{1/2}(S)-G)\). Consequently \(G\) is also the unique symmetry center. The same permutation argument shows that the Euclidean-volume centroid of \(M_q(S)\) is always \(G\).

**5. Dimensional limit.** For each fixed \(a\in(0,1)\), \(d(1-a^{1/d})\to-\log a\). Apply this twice to the exact factors. The limiting gap is nonzero for \(q\neq1/2\), by the strict concavity argument or the strict binary entropy inequality just established.

**6. Triangle inverse fibers.** Let \(M_q(T)=M_q(T')\), or equivalently let the buoyancy surfaces coincide. The published planar recovery theorem (Dann–Herscovici–Myroshnychenko, revised 2026, Corollary 2) gives
\[
\frac{T-T}{\operatorname{area}(T)^{1/3}}
=\frac{T'-T'}{\operatorname{area}(T')^{1/3}}.
\]
A nondegenerate triangle's difference body is a six-vertex centrally symmetric hexagon whose three pairs of opposite extreme vertices are precisely its three unoriented edge vectors. Therefore equality of difference bodies up to scale forces \(T'=sT+v\) or \(T'=-sT+v\) for some \(s>0\). Indeed among these three independent-sign choices the only triples of oriented edge vectors summing to zero are the original cycle and its global reversal. Writing \(A'=s^2A\), the normalized difference-body equality gives \(s=(A'/A)^{1/3}=s^{2/3}\), hence \(s=1\). The centroid of \(M_q(T)\) is the triangle centroid, so equality of the two Ulam bodies makes their triangle centroids agree: in the positive case \(v=0\); in the negative case \(v=2G\). For \(q\neq1/2\), equality with \(M_q(2G-T)=2G-M_q(T)\) would make the Ulam body centrally symmetric, contradicted by part 4. At \(q=1/2\), the complementary-cap identity makes the two Ulam bodies equal. No triangle equals its centroid reflection, so the fiber contains exactly two distinct members.

## Verification
The standalone program `verify.py` numerically integrates the independent \(\mathrm{Beta}(1,d)\) marginal density on the correct tail intervals and checks all four cap masses and conditional means against the exact formulas in a grid of seven dimensions and nineteen cap fractions. It independently checks the two envelope identities, the sign transition, the equivalent signed-gap identity, and six high-dimensional limit values. All 1,076 scalar comparisons pass at the stated tolerances. These numerical experiments corroborate, but do not replace, the analytic arguments; the triangle inverse step separately depends on the cited published normalized-difference-body theorem.

## Relationship to prior work
Huang, Slomka and Werner developed the Ulam floating body and proved the cap-centroid characterization, affine equivariance and complementary-density property; those facts are premises, not new claims. The revised 2026 work of Dann, Herscovici and Myroshnychenko proves normalized difference-body recovery for polygons and openly leaves general single-density buoyancy reconstruction unresolved; the triangle corollary uses that theorem as an essential premise. An earlier May 2026 version of that paper stated a broader fixed-density injectivity theorem; it did not supply the sharp simplex envelope coefficients or their high-dimensional orientation gap, and its half-density assertion is incompatible with the well-known complementary-cap reflection. The October 2026 published exact all-level Ulam triangle boundary describes dimension two, and the corresponding two-dimensional coordinate extrema can be derived from it; this is acknowledged rather than presented as independently new. The contribution isolated here is the arbitrary-dimensional **two-orientation sharp envelope profile, its unique signed transition, and its nonvanishing dimensional limit**, with the triangle inverse statement an application of already published planar recovery.

## Limitations
The formulas concern only uniform measure on a simplex, and only homothetic envelopes fixed at its centroid. They neither give the complete Euclidean Hausdorff mismatch nor determine a general convex polytope from one buoyancy surface. The triangle inverse corollary relies on an external planar difference-body theorem whose proof is not reproduced. Historical priority remains provisional under statistical zonoid trimming and metronoid terminology; an inaccessible older paper may contain equivalent one-dimensional support calculations. No independent mathematical audit has been performed.

## References
1. S. Dann, O. Herscovici and S. Myroshnychenko, *Flotation Rigidity for Convex Polytopes*, arXiv:2605.09776v2, 2026-11-11, https://arxiv.org/html/2605.09776v2 (particularly Corollary 2, Section 5.3).
2. S. Dann, O. Herscovici and S. Myroshnychenko, *Uniqueness of Flotation and Buoyancy Surfaces for Convex Polytopes*, arXiv:2605.09776v1, first publicly available 2026-05-10, https://arxiv.org/html/2605.09776v1 (original-version claims distinguished from revised work).
3. H. Huang, B. A. Slomka and E. M. Werner, *Ulam floating bodies*, arXiv:1803.08224, 2018, https://ar5iv.labs.arxiv.org/html/1803.08224; *J. Lond. Math. Soc.* 100 (2019), 425–446.
4. *Exact all-level area and conic boundary of the Ulam floating body of a triangle*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-all-level-area-and-conic-boundary-of-the-ulam-floating-bod--618bc0d26120 .
5. G. Koshevoy and K. Mosler, *Zonoid trimming for multivariate distributions*, *Ann. Statist.* 25 (1997), 1998–2017.
