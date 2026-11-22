# A two-volume correction law for arbitrary complementary-subspace convex hulls

## Finding
Let \(r\geq2\), and let \(E_1,\ldots,E_r\) be mutually orthogonal linear subspaces of a Euclidean space whose direct sum has dimension \(D=\sum_{i=1}^r d_i\), where \(d_i=\dim E_i\geq1\). For each nonempty compact convex set \(K_i\subset E_i\), define
\[
v_i=\operatorname{vol}_{d_i}(K_i),\qquad c_i=\operatorname{vol}_{d_i}(\operatorname{conv}(K_i\cup\{0\})).
\]
Then, without assuming that any factor contains the origin or has interior,
\[
\boxed{\operatorname{vol}_{D}\!\left(\operatorname{conv}\bigcup_{i=1}^r K_i\right)
=\frac{\prod_{i=1}^r d_i!}{D!}\left[\prod_{i=1}^r c_i-\prod_{i=1}^r(c_i-v_i)\right].}
\]
This is an exact dimension-independent identity: each factor contributes only its ordinary volume and its volume after adjoining the origin. In particular, if at least one factor contains the origin the correction vanishes, recovering the usual free-sum product, whereas arbitrary origin-exterior factors have a generally nonzero correction.

The identity also applies samplewise to independent random compact convex factors \(K_i\) (including empty factors with the convention that both associated volumes are zero). If the volume expectations are finite, then
\[
\mathbb E\operatorname{vol}_{D}\!\left(\operatorname{conv}\bigcup_iK_i\right)
=\frac{\prod_i d_i!}{D!}
\left[\prod_i\mathbb E c_i-\prod_i(\mathbb E c_i-\mathbb E v_i)\right].
\]
The factorization gives an exact expected-volume reduction for independent vertex deletions in mutually perpendicular polygon layers, even though the retained polygons can be lower-dimensional.

For example, let the vertices of a unit regular square and a unit regular pentagon in orthogonal planes of \(\mathbb R^4\) be independently retained with probability \(p\). Write \(q=1-p\), \(s_1=\sin(2\pi/5)\), and \(s_2=\sin(4\pi/5)\). The two-dimensional expected area pairs are
\[
(C_4,V_4)=\bigl(2p^2,\,2p^2(1-q^2)\bigr),
\]
\[
(C_5,V_5)=\frac{5p^2}{2}\bigl(s_1+s_2q,\;s_1+s_2q-s_2q^2-s_1q^3\bigr).
\]
Consequently the expected four-volume is exactly \([C_4C_5-(C_4-V_4)(C_5-V_5)]/6\). At \(p=1/2\) it equals
\[
\frac{155}{3072}\sin\frac{2\pi}{5}+\frac{35}{1536}\sin\frac{4\pi}{5}
=0.0613797941686920\ldots.
\]

## Assumptions and scope
All volumes are intrinsic Euclidean Lebesgue volumes in their indicated subspaces, with the \(d_i\)-dimensional volume of a lower-dimensional set defined as zero. The subspaces are linearly independent and orthogonal, so the ambient Lebesgue product factor has no additional Jacobian. No strict convexity, genericity, rationality, origin containment, or full-dimensionality of the individual factors is required. The samplewise stochastic consequence assumes independence across factors, not independence among points within any factor, and integrable factor volumes.

## Proof
**1. Origin-adjoined hull.** Put \(C_i=\operatorname{conv}(K_i\cup\{0\})\), and \(H=\operatorname{conv}(\bigcup_i C_i)\). Since each \(C_i\) contains zero, the standard free-sum volume formula, with this normalization, is
\[
\operatorname{vol}_D(H)=\frac{\prod_i d_i!}{D!}\prod_i\operatorname{vol}_{d_i}(C_i).
\]
For completeness, this follows from the Minkowski gauges \(\gamma_i\) of the \(C_i\): \(H\) consists precisely of points with \(\sum_i\gamma_i(x_i)\leq1\). For nonempty interiors, the gauge sublevel \(\{x_i:\gamma_i(x_i)\leq t\}\) has volume \(c_it^{d_i}\); integrating the associated Stieltjes measures \(d_i c_it^{d_i-1}dt\) over \(\{t_i\geq0,\sum_i t_i\leq1\}\), the Dirichlet beta integral gives \((\prod_i d_i! /D!)\prod_i c_i\). Degenerate sets follow by approximation.

**2. Origin-visible facets in the factors.** First suppose all \(K_i\) are full-dimensional polytopes. If some \(0\in K_i\), then \(0\in\operatorname{conv}(\bigcup_iK_i)\), hence this convex hull equals \(H\), and \(c_i=v_i\); the identity follows from step 1. Otherwise \(0\notin K_i\) for every \(i\). In this case also \(0\notin P:=\operatorname{conv}(\bigcup_iK_i)\): projecting an expression \(0=\sum_i\lambda_ix_i\) onto \(E_i\) forces \(\lambda_ix_i=0\) and hence every \(\lambda_i=0\), incompatible with \(\sum_i\lambda_i=1\).

For a facet \(F_i\) of \(K_i\) with outward unit normal \(u_i\), let its signed support distance from zero be \(h_i=\langle u_i,x\rangle\) for \(x\in F_i\). It is visible from the origin exactly when \(h_i<0\). The portion \(C_i\setminus K_i\) decomposes, up to measure-zero boundaries, into the pyramids \(\operatorname{conv}(\{0\}\cup F_i)\) over these visible facets. Therefore, with \(w_i(F_i)=(-h_i)\operatorname{vol}_{d_i-1}(F_i)/d_i>0\),
\[
\sum_{F_i\text{ visible}}w_i(F_i)=c_i-v_i.
\]
For \(d_i=1\), a facet is an endpoint and its zero-dimensional volume is one; the same identity holds.

**3. Visible facets of the joined hull.** Every facet of \(P\) visible from zero has negative support value \(h<0\). Its intersections with the orthogonal factors are exposed proper faces, since a supporting functional with nonzero support cannot be identically zero on any entire positive-dimensional subspace. The dimension of the join of these faces is the sum of their dimensions plus \(r-1\); to attain the facet dimension \(D-1\), all must be facets \(F_i\) of \(K_i\). Their outward supports all equal \(h<0\), so each is visible from zero. Conversely, every tuple of visible facets \((F_1,\ldots,F_r)\) defines one visible facet \(F=\operatorname{conv}(\bigcup_iF_i)\) of \(P\): rescale the outward normal to each \(F_i\) by the positive factor \(1/(-h_i)\), so all summands have common support \(-1\). These constructions are inverse, including nonsimplicial facets.

The pyramid \(\operatorname{conv}(\{0\}\cup F)\) has volume
\[
\frac{\prod_i d_i!}{D!}\prod_i w_i(F_i).
\]
To see the normalization directly, parameterize its interior using radial parameters \(t_i\geq0\), \(\sum_i t_i\leq1\), and points of \(F_i\). In the orthogonal blocks the volume element is \(\prod_i[d_iw_i(F_i)t_i^{d_i-1}dt_i]\); the Dirichlet integral evaluates to the stated product. The apex pyramids over visible facets of \(P\) tile \(H\setminus P=\operatorname{conv}(\{0\}\cup P)\setminus P\) up to their boundaries. Hence
\[
\operatorname{vol}_D(H)-\operatorname{vol}_D(P)
=\frac{\prod_i d_i!}{D!}\prod_i\sum_{F_i\text{ visible}} w_i(F_i)
=\frac{\prod_i d_i!}{D!}\prod_i(c_i-v_i).
\]
Subtract this from the formula in step 1.

**4. General convex sets and random factors.** Approximate each compact convex \(K_i\) in the Hausdorff metric by full-dimensional polytopes, for example by first thickening it by a radius tending to zero and then taking inscribed polytopes. Convex-hull formation and Euclidean volume are continuous under such approximations, so the equality persists even for a singleton or a segment. Empty factors follow by a vanishing-factor approximation and the convention stated above. Apply the deterministic identity to each sample; independence factorizes the expectations of the products of the \(c_i\) and the \(c_i-v_i\).

**5. Regular polygon deletion example.** For a regular \(n\)-gon, a directed retained boundary edge spanning \(\ell\) cyclic steps occurs with probability \(p^2q^{\ell-1}\). Shoelace integration gives the expected retained-hull area
\[
V_n=\frac{np^2}{2}\sum_{\ell=1}^{n-1}\sin(2\pi\ell/n)q^{\ell-1}.
\]
Adjoining the origin replaces a cyclic edge spanning more than a half-turn by two radial segments with zero signed area, hence
\[
C_n=\frac{np^2}{2}\sum_{1\leq\ell\leq n/2}\sin(2\pi\ell/n)q^{\ell-1}.
\]
These identities hold for every retained subset, including zero, one, or two vertices (opposite-directed two-vertex terms cancel in \(V_n\)). Substitution at \(n=4,5\) yields the displayed expressions and the value at \(p=1/2\).

## Verification
The deterministic identity was independently compared against numerical convex-hull volumes in 100 pseudorandom placements for each of five two-factor dimension patterns \((1,1),(1,2),(2,2),(1,3),(2,3)\), and 100 placements for each of five patterns involving three or four factors \((1,1,1),(1,1,2),(1,2,2),(1,1,1,1),(2,2,2)\). These tests found no discrepancies above numerical tolerances (and skip Qhull-degenerate samples). An independent exhaustive check of all \(2^9=512\) vertex-retention subsets of the orthogonal square and pentagon matched the closed-form \(p=1/2\) expectation to floating-point accuracy. The accompanying script reproduces the primary two-dimensional and four-dimensional sample checks. These finite tests are corroboration only; the proof of the general statement is the facet and Dirichlet argument above.

## Relationship to prior work
Chen and Davis (2017, Theorem 1.2) prove the normalized-volume product for free sums where **both factors contain zero**, explicitly noting that the uncorrected product fails for origin-exterior factors. Here, a separate product of two origin-visible cone-volume deficits is subtracted, with any number of factors and arbitrary nonlattice convex bodies. Medgyes (2026, Sections 2.4 and 3) studies signed four-volume within the square–pentagon join type and identifies the centered orthogonal configuration; those specific facts do not furnish the origin-exterior correction or the general random-factor expectation. The new identity preserves the established centered free-sum formula as a special case rather than claiming it anew.

## Limitations
The formula requires complementary orthogonal subspaces and Euclidean product-volume normalization. It is not a formula for arbitrary overlapping affine subspaces. In the random example it gives an expectation, not the complete law or a shape optimizer after deletion. No independent mathematical audit or historical-priority certification has been performed. Comparisons to indexed literature and accessible records may miss other formulations under different terminology.

## References
- C. Medgyes, *The inscribed 4-polytope of maximal volume with nine vertices*, arXiv:2611.10078v1, 6 November 2026, https://arxiv.org/html/2611.10078v1 .
- T. Chen and R. Davis, *A Product Formula for the Normalized Volume of Free Sums of Lattice Polytopes*, arXiv:1711.11130v2, 2017 (version read: March 2019), https://arxiv.org/html/1711.11130v2 .
- M. Freyer, M. Henk and S. Kipp, *Affine subspace concentration conditions for centered polytopes*, 2023, https://doi.org/10.1112/mtk.12189 (background on cone volumes).
