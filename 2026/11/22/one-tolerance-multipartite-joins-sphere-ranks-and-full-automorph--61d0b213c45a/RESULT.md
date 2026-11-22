# One-tolerance multipartite joins: sphere ranks and full automorphism characters

## Finding

Let \(r\ge2\), and let \(A_1,\ldots,A_r\) be disjoint vertex classes of sizes \(a_i\ge2\). Put \(D(A_i)=\{\varnothing\}\cup\{\{v\}:v\in A_i\}\), let \(K=D(A_1)*\cdots*D(A_r)\) be the clique complex of the complete multipartite graph on these classes, and put \(X=\mathcal T_1(K)\), where \(\mathcal T_1\) permits deletion of at most one vertex to obtain a face of \(K\).

**Theorem.** The integral homotopy type is
\[
X\simeq\bigvee^{B}S^r,\qquad B=\frac{\sum_{i=1}^r a_i-2}{2}\prod_{i=1}^r(a_i-1).
\]
The displayed multiplicity is a nonnegative integer. Further, the complete character of the natural action of the full multipartite automorphism group on \(\widetilde H_r(X;\mathbb Q)\) is determined as follows. Let \(g\) be an arbitrary automorphism, including a permutation of equal-size vertex classes. Decompose its induced permutation on the set of parts into cycles \(O\). For each such cycle choose one representative class \(A_{i(O)}\), write \(\ell_O=|O|\), and define
\[
f_O=\#\operatorname{Fix}\bigl(g^{\ell_O}|_{A_{i(O)}}\bigr).
\]
When \(\ell_O=1\), let \(c_O\) be the number of disjoint transpositions in the cycle decomposition of \(g|_{A_{i(O)}}\). Then
\[
\boxed{\operatorname{tr}(g_*|\widetilde H_r(X;\mathbb Q))=(-1)^{r+1}\left[\prod_O(1-f_O)+\sum_{\ell_O=1}\left(\binom{f_O}{2}-c_O\right)\prod_{P\ne O}(1-f_P)\right].}
\]
In particular, when every class has two vertices, the full integral homology lattice is the standard augmentation lattice on the set of \(r\) parts, twisted by the product of the within-part signs and the sign of the permutation of parts:
\[
\widetilde H_r(X;\mathbb Z)\cong\left(\bigotimes_{i=1}^r\mathrm{sgn}_{A_i}\right)\otimes\mathrm{sgn}_{\mathrm{parts}}\otimes\ker\left(\mathbb Z^r\xrightarrow{\sum}\mathbb Z\right).
\]
The sign factors refer to the canonical wreath-product action; the tensor product of within-part signs is the one-dimensional character multiplying the parities of all internal swaps.

## Assumptions and scope

All vertex sets are finite and distinct, the classes are nonempty with sizes at least two, and \(r\ge2\). Homotopy equivalence is ordinary, not equivariant. The character formula concerns rational homology under every simplicial automorphism of the complete multipartite graph; equal-sized classes may be exchanged. No assumption of fixed pointwise part preservation is made. Reduced homology is integral unless a coefficient field is shown. The formula does not assert an explicit integral module decomposition for unequal or larger classes.

## Proof

**1. Exact cover and null intersections.** A vertex subset \(S\) lies in \(X\) precisely when
\[
e(S):=\sum_i\max(0,|S\cap A_i|-1)\le1.
\]
Thus no part contributes more than two vertices and at most one part contributes two. Set \(E_i=\operatorname{sk}_1\Delta^{A_i}\), the complete graph on the vertices of \(A_i\), and
\[
X_i=E_i*\mathop{\bigast}_{j\ne i}D(A_j).
\]
Then \(X=\bigcup_iX_i\) and \(X_i\cap X_j=K\) for all distinct \(i,j\); every higher nontrivial intersection is also \(K\). The inclusion \(K\to X_i\) is nullhomotopic: the vertex-set inclusion \(D(A_i)\hookrightarrow E_i\) is nullhomotopic because every map from a finite discrete space to a path-connected graph is nullhomotopic (without preserving separate basepoints), and joining with the remaining nonempty complex preserves that homotopy. As \(r\ge2\), \(K\) and the \(X_i\) are path connected.

**2. Integral homotopy splitting.** Write \(Y_j=X_1\cup\cdots\cup X_j\). Each \(Y_{j-1}\cap X_j=K\), and both structure maps \(K\to Y_{j-1}\) and \(K\to X_j\) are nullhomotopic, the former via the inclusion through \(X_1\). Simplicial inclusions are cofibrations, so their ordinary pushout models a homotopy pushout. The homotopy pushout of two null maps from connected \(K\) is the wedge of the two codomains and \(\Sigma K\). Induction yields
\[
X\simeq\left(\bigvee_{i=1}^{r}X_i\right)\vee\bigvee^{r-1}\Sigma K.
\]
Now \(D(A_i)\simeq\bigvee^{a_i-1}S^0\) as a based zero-dimensional complex, and \(E_i\simeq\bigvee^{\binom{a_i-1}{2}}S^1\), with the zero-summand case \(a_i=2\) interpreted as a contractible graph. Standard based join homotopy formulas give
\[
K\simeq\bigvee^{\prod_j(a_j-1)}S^{r-1},\qquad
X_i\simeq\bigvee^{\binom{a_i-1}{2}\prod_{j\ne i}(a_j-1)}S^r.
\]
All equivalences are integral. Summing the multiplicities gives
\[
\prod_j(a_j-1)\left[r-1+\sum_i\frac{a_i-2}{2}\right]=\frac{\sum_i a_i-2}{2}\prod_j(a_j-1),
\]
proving the wedge and integrality assertions.

**3. Exact equivariant Lefschetz calculation.** Fix \(g\) in the full multipartite automorphism group. A \(g\)-invariant face is a union of vertex cycles of \(g\). Write \(k(\sigma)\) for the number of such cycles in the invariant face \(\sigma\), and define
\[
F_g(z)=\sum_{\substack{\sigma\in X\\g\sigma=\sigma}}z^{k(\sigma)},
\]
including the empty face. For each part orbit \(O\), if each constituent part contributes at most one vertex, one may choose either no vertex cycle or one of \(f_O\) cycles of length \(\ell_O\), contributing \(1+f_Oz\). Because \(e(\sigma)\le1\), a part with two selected vertices must be fixed under \(g\); it can contribute two individually fixed vertices (\(\binom{f_O}{2}z^2\)) or one actual two-cycle (\(c_Oz\)). There can be only one such exceptional fixed part. Therefore the complete invariant-face enumerator is exactly
\[
F_g(z)=\prod_O(1+f_Oz)+\sum_{\ell_O=1}\left(\binom{f_O}{2}z^2+c_Oz\right)\prod_{P\ne O}(1+f_Pz).
\]
On the oriented augmented chain spanned by a nonempty invariant simplex \(\sigma\), the sign of \(g\) is \((-1)^{|\sigma|-k(\sigma)}\). Hence its contribution to the reduced alternating chain trace is \((-1)^{k(\sigma)-1}\); the empty simplex contributes \(-1\). Thus the reduced Lefschetz number is \(-F_g(-1)\). By Step 2, reduced rational homology is supported only in degree \(r\), so this number also equals \((-1)^r\operatorname{tr}(g_*|\widetilde H_r)\). Evaluating the preceding polynomial at \(-1\) yields the announced formula for arbitrary part permutations and internal cycles.

**4. Integral special case.** If every \(a_i=2\), each \(X_i\) is contractible, and \(K\cong(S^0)^{*r}\) is an integral sphere of dimension \(r-1\). The relative long exact sequence for \((X,K)\) and the quotient splitting \(X/K=\bigvee_iX_i/K\) identify \(\widetilde H_r(X;\mathbb Z)\) with the kernel of the augmentation sum \(\mathbb Z^r\to\mathbb Z\), tensored with \(\widetilde H_{r-1}(K;\mathbb Z)\). Internal swaps reverse the fundamental orientation of \(K\), and exchanging two join factors of dimension zero also reverses it; therefore \(\widetilde H_{r-1}(K;\mathbb Z)\) carries precisely the within-part product-sign character times the part-permutation sign. The quotient relative groups are permuted on their part indices, yielding the stated integral equivariant lattice.

## Verification

Run `python3 CHECK.py` from this package. The standard-library-only checker independently enumerates all invariant faces and their signed chain actions for all \(2{,}448\) automorphisms of five distinct complete multipartite input patterns, including nontrivial permutations of equal-sized parts. It compares the results to the closed character formula. It also computes complete reduced homology over \(\mathbb F_2\) and \(\mathbb F_3\) by sparse exact simplicial boundary reduction for eight distinct size patterns, checking vanishing outside degree \(r\) and the top rank. These finite checks do not replace the homotopy-pushout proof or the all-element Lefschetz derivation.

## Relationship to prior work

Kim–Lew established tolerance-complex Leray bounds and the general definition. Selvaraja's 10 November 2026 paper determines collapsibility/Leray behavior for numerous families and, in Section 8, explicitly identifies tolerance complexes of matroids with matroid elongations; the fact that \(X\) is a matroid independence complex, and consequently has a top-dimensional sphere-wedge homotopy type, is therefore **not claimed new**. The exact all-size multiplicity and especially the compact closed **full automorphism character** with part-exchange cycles are the asserted refinements. Moci–Pezzoli provide general equivariant homology descriptions for arbitrary matroids, and work out explicit characters for complete-graph matroids; their broad framework may be used as another conceptual route, but does not state this partition-elongation wreath-product formula. Related results for clique-free, path-free, or graph-geodesic complexes use different face predicates. An unindexed equivalent specialization remains possible.

## Limitations

The sphere splitting is nonequivariant. The general automorphism result determines rational characters, not full integral module extensions or equivariant homotopy types; only the all-two-vertex special case has an explicitly identified integral representation. No assertion extends to higher tolerance parameters, arbitrary partition quotas, or nonmultipartite graphs. A targeted literature search cannot certify global priority, and the computation is bounded to the listed finite input patterns.

## References

- M. Kim and A. Lew, *Leray Numbers of Tolerance Complexes*, arXiv:2109.03030 (first public 2021); Combinatorica 43 (2023), 985–1006. https://arxiv.org/abs/2109.03030
- S. Selvaraja, *Tolerance complexes of chordal graphs and squarefree symbolic powers*, arXiv:2611.14384v1 (first public 10 November 2026), especially Sections 7–8. https://arxiv.org/html/2611.14384v1
- L. Moci and G. M. Pezzoli, *Representations of automorphism groups on the homology of matroids*, arXiv:2001.03760 (first public 2020), especially Section 4. https://arxiv.org/abs/2001.03760
