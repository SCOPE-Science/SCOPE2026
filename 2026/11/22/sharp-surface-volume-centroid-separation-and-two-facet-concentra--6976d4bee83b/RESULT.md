# Sharp surface–volume centroid separation and two-facet concentration in Euclidean simplices

## Finding

For every nondegenerate Euclidean \(d\)-simplex \(S\), \(d\ge3\), the maximum discrepancy between its volume centroid and surface-area centroid, divided by width in the same direction, is determined **exactly by the distribution of its facet areas**:

\[
G(S)=\sup_{u\ne0}\frac{|\langle c(\partial S)-c(S),u\rangle|}{w_S(u)}
=\frac1{2d}\sum_{i=0}^d\left|\frac{A_i}{\sum_jA_j}-\frac1{d+1}\right|.
\]

Here \(A_i\) is the Euclidean \((d-1)\)-area of the facet opposite vertex \(v_i\). Every such simplex satisfies the **sharp strict** estimate

\[
G(S)<\frac{d-1}{d(d+1)},\qquad
\sup_{S\text{ nondegenerate}}G(S)=\frac{d-1}{d(d+1)}.
\]

There is also a **quantitative two-facet concentration law**. Put \(a=1/(d+1)\) and \(\eta=d((d-1)/(d(d+1))-G(S))\). Whenever \(0<\eta<a\), precisely two normalized facet areas \(p_i=A_i/\sum_jA_j\) exceed \(a\); every other facet together has normalized area **exactly** \(\eta\). If \(\nu_p,\nu_q\) denote the corresponding outward unit facet normals, then

\[
\|\nu_p+\nu_q\|\le4\eta.
\]

Thus near-extremality forces two nearly opposite dominant facets, not merely a small algebraic deficit.

## Assumptions and scope

All centroids use uniform Euclidean measures: \(c(S)\) is normalized \(d\)-volume mean and \(c(\partial S)\) is normalized \((d-1)\)-dimensional surface-area mean over the facets. The width is \(w_S(u)=\max_{x\in S}\langle x,u\rangle-\min_{x\in S}\langle x,u\rangle\) for nonzero \(u\). The result is about unrestricted nondegenerate simplices and all directions, with no regularity or symmetry condition. The published planar sharp inequality (dimension two) is not claimed as a new result; the new sharp class-wide statement concerns \(d\ge3\).

## Proof

**1. Centroids as signed vertex weights.** Write \(T=\sum_{i=0}^{d}A_i\), \(p_i=A_i/T\) and \(a=1/(d+1)\). The centroid of facet \(i\) is \(d^{-1}\sum_{j\ne i}v_j\), while the volume centroid is \(c(S)=\sum_j av_j\). Summing surface-area weights shows

\[
c(\partial S)-c(S)=\frac1d\sum_{i=0}^d(a-p_i)v_i.\tag{1}
\]

For any nonconstant affine functional \(f\), normalize its vertex values by \(t_i=(f(v_i)-\min_jf(v_j))/(\max_jf(v_j)-\min_jf(v_j))\). Then \(0\le t_i\le1\), and the centroid discrepancy divided by its directional width is \(d^{-1}|\sum_i(a-p_i)t_i|\). Since the vertices are affinely independent, **every** assignment of the \(d+1\) values \(t_i\) is realized by a unique affine functional. The maximum of this signed linear expression over the unit cube is reached by setting \(t_i=1\) on positive coefficients and \(t_i=0\) on negative ones (or conversely). As \(\sum_i(a-p_i)=0\),

\[
G(S)=\frac1d\sum_{i:p_i>a}(p_i-a)=\frac1{2d}\sum_{i=0}^{d}|p_i-a|.\tag{2}
\]

This proves the exact profile, including all tie cases. An optimizing direction is the gradient of an affine functional that takes values zero and one at the respective sign classes of vertices; values at vertices with \(p_i=a\) may be arbitrary between the extremes.

**2. The geometric restriction on facet weights.** The divergence theorem applied to constant vector fields yields \(\sum_i A_i\nu_i=0\), where \(\nu_i\) are outward unit normals. Therefore \(A_i\le\sum_{j\ne i}A_j\). Equality would require every other outward normal to point exactly opposite \(\nu_i\), impossible for a nondegenerate simplex in dimension at least two. Consequently

\[
0<p_i<\frac12,\qquad\sum_i p_i=1.\tag{3}
\]

**3. Sharp global bound.** Let \(H=\{i:p_i>a\}\) with \(h=|H|\). If \(h=1\), then \(dG=p_i-a<1/2-a\le1-2a\) for \(d\ge3\). If \(h\ge2\), then \(dG=\sum_{i\in H}p_i-ha<1-ha\le1-2a\) because every complementary weight is positive. If \(H\) is empty, then all \(p_i=a\) and \(G=0\). Hence \(G<(1-2a)/d=(d-1)/(d(d+1))\), and equality is impossible for a nondegenerate simplex.

**4. Sharpness with an explicit degenerating simplex.** Take

\[
S_t=\operatorname{conv}\{0,e_1,\ldots,e_{d-1},t e_d\},\qquad t>0.
\]

The areas of its facets, in the order opposite \(0,e_1,\ldots,e_{d-1},te_d\), are proportional to

\[
\big(\sqrt{1+(d-1)t^2},\;t,\ldots,t,\;1\big).\tag{4}
\]

The first and last normalized weights tend to \(1/2\) while the other \(d-1\) tend to zero. Formula (2) gives \(G(S_t)\to(1-2a)/d\). More concretely the affine functional \(f(x)=x_1+\cdots+x_{d-1}\) has width one, takes value zero at the two dominant opposite-facet vertices, and takes value one at the other \(d-1\) vertices; evaluating (1) along this functional gives the same sharp limit. No nondegenerate optimizer exists.

**5. Quantitative inverse statement.** For \(d\ge3\), if \(h=1\), then \((1-2a)-dG\ge1/2-a\ge a\); if \(h\ge3\), then \((1-2a)-dG\ge a\). Thus \(\eta=(1-2a)-dG<a\) forces \(h=2\). Label the two indices \(p,q\). Since \(p_p+p_q=1-\sum_{i\ne p,q}p_i\), formula (2) gives the exact identity

\[
\eta=1-2a-dG=\sum_{i\ne p,q}p_i.\tag{5}
\]

Moreover \(p_p,p_q\le1/2\), so the deficits \(1/2-p_p\) and \(1/2-p_q\) are nonnegative and sum to \(\eta\). The facet-normal equilibrium \(\sum_i p_i\nu_i=0\) implies \(\|p_p\nu_p+p_q\nu_q\|\le\eta\). Therefore

\[
\frac12\|\nu_p+\nu_q\|\le
\|p_p\nu_p+p_q\nu_q\|+(1/2-p_p)+(1/2-p_q)\le2\eta.
\]

This establishes the stated stability estimate.

## Verification

The package includes `verify.py`, a finite consistency checker with rational input vertices, exact rational Gram determinants, and floating evaluations only when taking square roots. It checks the facet-centroid identity, the exact finite-vertex sign maximization, the strict class-wide bound, and the explicit flattening-family facet areas. Its 90 test cases passed. The universal theorem and inverse law are proved by the preceding algebraic and geometric argument and **do not** rely on finite tests.

## Relationship to prior work

Myroshnychenko, Ryabogin, Tatarko and Yaskin establish a universal sharp constant \(D_d\) for **all** convex bodies in each dimension (arXiv:2611.11635v1). Their result supplies the motivating general centroid-separation problem but not the facet-area exact profile or the strictly smaller sharp constant restricted to simplices in dimensions at least three. Nazarov, Ryabogin and Yaskin establish the planar sharp bound \(1/6\), using thin triangles as examples (arXiv:2305.15646v1); this earlier two-dimensional case is explicitly excluded from the originality claim. The exact dependence on all facet weights and the quantitative two-dominant-facet geometry are the added statements. Related work about squared-distance moments of simplex boundary measures studies a different observable, not this first-moment width ratio.

## Limitations

The class-wide supremum is not attained by any nondegenerate simplex. Near-extremal inverse control is stated only for the explicitly quantified gap \(\eta<1/(d+1)\); no optimal estimate for arbitrary gaps or classification of arbitrary convex bodies is asserted. The bound controls directional displacement relative to width and does not by itself identify the sharp ratio to Euclidean diameter. The literature comparison supports provisional originality, not guaranteed historical priority. Independent mathematical audit has not been performed.

## References

- S. Myroshnychenko, D. Ryabogin, K. Tatarko, V. Yaskin, *The sharp bound on the distance between the centers of mass of a convex body and its boundary*, arXiv:2611.11635v1 (first publicly posted 2026-11-08), https://arxiv.org/abs/2611.11635.
- F. Nazarov, D. Ryabogin, V. Yaskin, *On the maximal distance between the centers of mass of a planar convex body and its boundary*, arXiv:2305.15646v1 (first posted 2023-05-25), https://arxiv.org/abs/2305.15646.
