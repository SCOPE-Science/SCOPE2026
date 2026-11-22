# Strict isotropic majorization for enriched layered chain polytopes

## Finding
Let \(r\ge2\), \(N\ge r\), and let \(m_1,\ldots,m_r\) be positive integers summing to \(N\). Form the ordinal sum of antichains \(P=A_{m_1}\oplus\cdots\oplus A_{m_r}\). Let \(E(\mathbf m)\) be its canonical enriched chain polytope in \(\mathbb R^N\): the convex hull of all signed indicator vectors supported on antichains. The polytope is exactly the orthogonal free sum of the \(r\) coordinate cubes:
\[
 E(\mathbf m)=\left\{x=(x^{(1)},\dots,x^{(r)}):
 \sum_{i=1}^r\|x^{(i)}\|_\infty\le1\right\}.
\]
For \(X\) sampled uniformly by ordinary \(N\)-dimensional Euclidean volume, the covariance and volume are
\[
 \operatorname{Cov}(X)=\bigoplus_{i=1}^r
 \frac{(m_i+1)(m_i+2)}{3(N+1)(N+2)}I_{m_i},
 \qquad \operatorname{Vol}(E(\mathbf m))=2^N\frac{\prod_i m_i!}{N!}.
\]
Define the squared affine-invariant isotropic constant by
\[
 L(E)^2=\frac{\bigl(\det\operatorname{Cov}(X)\bigr)^{1/N}}{\operatorname{Vol}(E)^{2/N}}.
\]
The full exact profile is
\[
 \boxed{L(E(\mathbf m))^{2N}=
 \frac{(N!)^2}{4^N[3(N+1)(N+2)]^N}
 \prod_{i=1}^r\frac{[(m_i+1)(m_i+2)]^{m_i}}{(m_i!)^2}.}
\]
**Sharp fixed-rank profile theorem.** At fixed total dimension \(N\) and fixed number of layers \(r\), the isotropic constant is strictly increased by every integer *anti-balancing transfer*: replace two layer sizes \((a,b)\) by \((a+1,b-1)\) whenever \(a\ge b\ge2\), holding all other sizes fixed. Consequently its minimum occurs exactly when the layer sizes differ by at most one, and its maximum exactly when the sizes, in any order, are \((N-r+1,1,\ldots,1)\). Equality is unique modulo permutation of the layer sizes; when \(N=r\) or \(N=r+1\) the two extremal profiles coincide. Equivalently, the isotropic constant is strictly Schur-convex on positive-integer compositions of fixed length and sum, with equality only for permutations.

For example, with \(N=10,r=3\), the balanced profile \((4,3,3)\) has \(L^2=0.0787700606957807\ldots\), while the extreme \((8,1,1)\) has \(L^2=0.0813050614264350\ldots\).

## Assumptions and scope
All antichains are nonempty finite sets of sizes \(m_i\ge1\); every element of an earlier level is below every element of a later level. Signed indicators use independent \(\pm1\) signs on the support, and also include the origin from the empty antichain. The ambient inner product and volume are the standard Euclidean ones, with coordinates grouped by level. The results concern this canonical placement, while the isotropic constant itself is affine invariant. A strict balancing comparison is meaningful only when two parts differ by at least two. The statement does not compare arbitrary posets, non-orthogonal free sums, or differently weighted cubes.

## Proof
**1. Geometric realization.** An antichain of an ordinal sum of antichains lies entirely in one level. For each level its signed indicator vectors have convex hull the full cube \([-1,1]^{m_i}\), embedded in the corresponding coordinate subspace. The convex hull of their union is the unit ball of the \(\ell_1\)-sum of the \(\ell_\infty\) block norms, which proves the displayed description. Conversely, if \(\sum_i\|x^{(i)}\|_\infty\le1\), use coefficients \(\|x^{(i)}\|_\infty\) on the relevant cubes and the unused weight on the origin.

**2. Uniform-volume law.** Write \(R_i=\|X^{(i)}\|_\infty\). For one \(m_i\)-dimensional cube, radial volume up to radius \(t\) equals \((2t)^{m_i}\). Consequently the joint radial density on \(R_i\ge0\), \(\sum R_i\le1\) is proportional to \(\prod_i m_iR_i^{m_i-1}\). Thus
\[
 (R_1,\ldots,R_r,1-\sum_iR_i)\sim
 \operatorname{Dirichlet}(m_1,\ldots,m_r,1).
\]
The Dirichlet simplex integral gives the volume \(2^N\prod_i m_i!/N!\) and, for every \(i\),
\[
 \mathbb E R_i^2=\frac{m_i(m_i+1)}{(N+1)(N+2)}.
\]
At a fixed radius \(R_i=t\), normalized shell measure on a cube splits equally among its \(2m_i\) facets: one uniformly chosen coordinate is \(\pm t\), and the others are independent uniform variables on \([-t,t]\). Hence, for each coordinate \(j\) in level \(i\),
\[
 \mathbb E[(X^{(i)}_j)^2\mid R_i=t]
 =\frac{t^2}{m_i}+\frac{m_i-1}{m_i}\frac{t^2}{3}
 =\frac{m_i+2}{3m_i}t^2.
\]
Independent coordinate sign symmetries force all means and off-diagonal covariances to zero. Combining the last two identities yields the exact block diagonal covariance matrix. Its determinant divided by squared volume proves the full isotropic formula. No asymptotic approximation is used.

**3. A strictly convex discrete potential.** Since all factors depending on \(N,r\) are constant, maximizing or minimizing \(L^{2N}\) amounts to maximizing or minimizing
\[
 F(\mathbf m)=\sum_{i=1}^r f(m_i),\qquad
 f(k)=k\log[(k+1)(k+2)]-2\log(k!),\quad k\ge1.
\]
For \(k\ge1\), put \(m=k+2\ge3\). Direct cancellation gives
\[
 f(k+2)-2f(k+1)+f(k)=
 2\log(1+1/m)+m\log\left(1-\frac{2}{m(m+1)}\right).
\]
At \(m=3\) the right side is \(\log(2000/1944)>0\). For \(m\ge4\), apply elementary strict logarithmic bounds \(\log(1+t)>2t/(2+t)\) and \(-\log(1-u)<u/(1-u)\) for \(t>0\) and \(0<u<1\). They imply
\[
 2\log(1+1/m)>\frac4{2m+1}
 \ge\frac{2m}{m(m+1)-2}
 >-m\log\left(1-\frac{2}{m(m+1)}\right).
\]
The middle weak inequality is equivalent to \(m\ge4\). Therefore every second forward difference of \(f\) is strictly positive.

**4. Majorization and equality.** Strictly increasing first differences show that for any \(a\ge b\ge2\),
\[
 f(a+1)+f(b-1)>f(a)+f(b).
\]
Every nonbalanced positive integer composition can be balanced by a finite sequence of the reverse transfers (moving one unit from a part at least two larger to a smaller part), each of which strictly lowers \(F\). Conversely, from any nonextreme profile, moving units from some nonsingleton part to a largest part strictly raises \(F\) until there is one nonsingleton part. These finite transfer processes terminate and characterize the two equality orbits. General integer majorization is generated by these transfers, proving strict Schur-convexity.

## Verification
The accompanying `verification/verify.py` checks the exact integer form of the strict second-difference inequality for \(m=3,\ldots,800\), compares all \(31{,}161\) positive compositions with \(2\le N\le18\) and \(2\le r\le6\) against the claimed exact extremal values and equality cases, and independently triangulates eleven low-dimensional free sums. In the triangulations, convex-hull software identifies candidate facets, while all nondegenerate cone-simplex determinants, volumes and first and second moments are computed exactly as rational numbers. The computed volumes and full covariances agree exactly with the formulas. These are finite independent diagnostics: the proof for all \(N,r\) is the Dirichlet integral and strict discrete log-convexity argument above.

## Relationship to prior work
Ohsugi and Tsuchiya introduced enriched chain polytopes and their signed-antichain construction (first arXiv posting 2018-12-05). Their foundational triangulation and Ehrhart results supply the objects, not the present isotropic extremizers. A published treatment of isotropic constants for all Hanner polytopes gives a broad general covariance recursion for arbitrary orthogonal \(\ell_1\)- and \(\ell_\infty\)-sums; the exact specialization to free sums of cubes is therefore not claimed as an independent first. The mathematical contribution here is the strict discrete-convexity mechanism and sharp finite-dimensional *fixed-number-of-layers* classification under size majorization, including all equality cases. A published two-level enriched order/chain comparison gives their covariance and isotropic ratio at specified layer sizes, but not a global majorization theorem across sizes. An ordinary unsigned layered chain-polytope covariance calculation concerns a different, noncentrally-symmetric body. Related balanced-partition theorems for mean widths and face gaps optimize different invariants and do not imply the determinant comparison. These statement-level distinctions do not prove absolute historical uniqueness; see limitations.

## Limitations
The result classifies these particular centrally symmetric enriched layered bodies and does not improve the published universal upper and lower isotropic bounds over all Hanner polytopes. Its strictly ordered part profiles concern **fixed dimension and number of levels**; changing the level count is a different problem. The exact formulas are structurally compatible with known Hanner covariance recursions, and an older unindexed rearrangement theorem could already imply the extremal order. No independent mathematical audit has been performed. Computational checks do not constitute proof outside their finite ranges.

## References
1. H. Ohsugi and A. Tsuchiya, *Enriched chain polytopes*, arXiv:1812.02097v1 (first posted 2018-12-05), https://arxiv.org/abs/1812.02097; *Israel Journal of Mathematics* **237** (2020), 485–500.
2. S. Okada and A. Tsuchiya, *Two enriched poset polytopes*, arXiv:2003.12271 (first posted 2020-03-27), https://arxiv.org/abs/2003.12271.
3. *Sharp isotropic-constant range of all Hanner polytopes*, public mathematical research record, 2026, identifier `7976b0937cd2`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-isotropic-constant-range-of-all-hanner-polytopes--7976b0937cd2.
4. *A rank-one covariance gap between enriched order and chain polytopes*, public mathematical research record, 2026, identifier `6e78acb8dee8`, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-rank-one-covariance-gap-between-enriched-order-and-chain-polyt--6e78acb8dee8.
5. *An exact isotropic determinant and a below-cube limit for layered chain polytopes*, public mathematical research record, 2026, identifier `3f62e89efe3b`, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-covariance-determinants-and-a-below-cube-isotropic-crossover-for--3f62e89efe3b.
