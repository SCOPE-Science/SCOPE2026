# Two-degree sphere wedges for leafless-middle caterpillar higher independence complexes

## Finding

For integers \(a,c\geq1\), let \(T_{a,c}\) be the tree on \(a+c+3\) vertices consisting of three path vertices \(u-v-w\), \(a\) pendant leaves at \(u\), \(c\) pendant leaves at \(w\), and **no pendant leaf at \(v\)**. For an integer \(r\geq1\), define the higher independence complex \(\operatorname{Ind}_r(G)\) to have faces all vertex subsets whose induced graph has every connected component of order at most \(r\). Write \(\binom nk=0\) when \(k<0\) or \(k>n\).

**Theorem (complete integral homotopy classification).** For all \(a,c,r\geq1\),
\[
\operatorname{Ind}_r(T_{a,c})\simeq
\left(\bigvee^{\binom{a-1}{r-1}\binom{c-1}{r-1}} S^{2r-1}\right)
\vee
\left(\bigvee^{\binom{a+c-1}{r-3}}S^{r-1}\right).
\]
A zero-fold wedge means a point. In particular, all reduced integral homology is free abelian. Whenever \(3\leq r\leq\min(a,c)\), both displayed multiplicities are positive, producing a genuine mixed-dimensional sphere wedge. For example,
\[
\operatorname{Ind}_3(T_{3,3})\simeq S^2\vee S^5,
\qquad
\operatorname{Ind}_4(T_{4,4})\simeq\bigvee^7S^3\vee S^7.
\]

## Assumptions and scope

All graphs are finite, simple, undirected. Exactly two end hubs have pendant leaves, at least one at each end; the middle hub has none. The theorem holds for all integers \(r\geq1\), including \(r\geq a+c+3\), when the complex is a simplex. The equivalence asserted is ordinary integral homotopy equivalence, not a canonical simplicial isomorphism or an equivariant homotopy equivalence. The listed multiplicities add if dimensions coincide; here the two displayed dimensions are distinct for every positive \(r\).

## Proof

**Step 1: the star complexes.** Let \(S_a\) be a star with center \(u\) and leaf set \(A\), \(|A|=a\), and write \(J_s(a)=\operatorname{Ind}_s(S_a)\). Every face either omits the center, or includes the center together with at most \(s-1\) leaves. Therefore
\[
J_s(a)=\Delta(A)\cup\bigl(u*\operatorname{skel}_{s-2}\Delta(A)\bigr).
\]
For \(s=1\), the two components \(\Delta(A)\) and \(\{u\}\) give \(J_1(a)\simeq S^0\). For \(2\leq s\leq a\), the two contractible pieces meet in the \((s-2)\)-skeleton of the leaf simplex. That skeleton is homotopy equivalent to \(\bigvee^{\binom{a-1}{s-1}}S^{s-2}\), by the standard simplex-skeleton calculation. The union is its suspension. If \(s\geq a+1\), the whole complex is a simplex. Thus, uniformly for \(s\geq1\),
\[
J_s(a)\simeq\bigvee^{\binom{a-1}{s-1}}S^{s-1}.
\tag{1}
\]

**Step 2: deletion of the bare middle hub.** Let \(K_r=\operatorname{Ind}_r(T_{a,c})\). On deleting \(v\), the graph separates into the two stars \(S_a\) and \(S_c\). Higher independence complexes of disjoint unions form simplicial joins, so
\[
D_r:=\operatorname{del}_{K_r}(v)=J_r(a)*J_r(c).
\]
The join of the wedge descriptions in (1) has homotopy type
\[
D_r\simeq\bigvee^{\binom{a-1}{r-1}\binom{c-1}{r-1}} S^{2r-1}.
\tag{2}
\]
This remains correct when a factor is contractible (the multiplicity vanishes). At \(r=1\), it says \(S^0*S^0\simeq S^1\).

**Step 3: link of the middle hub.** For \(r\geq2\), form the double star \(B_{a,c}\) from the same two end hubs and their leaves, with an edge directly joining \(u\) and \(w\). When \(v\) is selected in \(T_{a,c}\), any chosen end hub is connected through \(v\); the total size of that component is one more than the size of the corresponding component in the selected subgraph of \(B_{a,c}\). If neither end hub is selected, all selected leaves are isolated. Consequently there is an exact equality of face sets on \(V(T_{a,c})\setminus\{v\}\):
\[
L_r:=\operatorname{lk}_{K_r}(v)=\operatorname{Ind}_{r-1}(B_{a,c}),\qquad r\geq2.
\tag{3}
\]
For \(r=1\), the link consists of all subsets of the end leaves and is a simplex.

The double star has two adjacent nonleaf vertices, each with at least one pendant leaf. Deshpande--Singh's theorem for graphs whiskered at every nonleaf vertex (Theorem 3.10, arXiv:2001.05448) applies *to this double star* and gives
\[
L_r\simeq\bigvee^{\binom{a+c-1}{r-3}}S^{r-2},\qquad r\geq2.
\tag{4}
\]
At \(r=2\) the right side is contractible; when \(r-1\geq a+c+2\), it is also contractible, as required.

**Step 4: the attaching map is null.** For \(r\geq2\), the inclusion \(L_r\hookrightarrow D_r\) factors as
\[
L_r\longrightarrow J_{r-1}(a)*J_{r-1}(c)
\longrightarrow J_r(a)*J_r(c)=D_r.
\tag{5}
\]
Indeed, selecting \(v\) can only *increase* component sizes, so any face permitted with \(v\) restricts to an \((r-1)\)-independent face in each star. By (1), each inclusion \(J_{r-1}(a)\to J_r(a)\) is nullhomotopic: its domain is a wedge of \((r-2)\)-spheres (or contractible), while the codomain is \((r-2)\)-connected (or contractible). This includes \(r=2\): a map from a disjoint union of two contractible pieces into a path-connected complex is nullhomotopic. The same holds for the \(c\)-star. Taking simplicial joins of the two nullhomotopies makes the second map in (5) nullhomotopic. Hence \(L_r\to D_r\) is nullhomotopic. When \(r=1\), \(L_1\) is a simplex and its inclusion is also nullhomotopic.

**Step 5: split the homotopy cofibration.** The standard deletion-link union is
\[
K_r=D_r\cup_{L_r}(v*L_r).
\]
Since \(v*L_r\) is a cone and the attaching map is nullhomotopic, the associated CW homotopy pushout splits as
\[
K_r\simeq D_r\vee\Sigma L_r.
\]
Insert (2) and (4): suspension contributes exactly \(\binom{a+c-1}{r-3}\) spheres of dimension \(r-1\). At \(r=1\) the link is contractible, so only the \(S^1\) summand from (2) remains. For \(r\geq a+c+3\), every subset is admissible, so the complex is a simplex and both multiplicities are zero. This proves the formula in all ranges. Because the splitting is an actual homotopy splitting and all factors are sphere wedges, the conclusion is integral and excludes torsion without needing coefficient-field extrapolation. \(\square\)

## Verification

The accompanying standalone `verify.py` enumerates all faces directly from the induced connected-component sizes, independently constructs mod-two boundary matrices, and checks the predicted reduced Betti numbers for all \(1\leq a,c\leq4\) and every \(1\leq r\leq a+c+3\): 128 parameter triples and 54,249 face instances. It also checks the deletion/link partition. The reported outcome is `VERIFY_OK`. These calculations test finite cases and are not the proof of the unrestricted theorem; the integral conclusion rests on the homotopy splitting above and the cited double-star theorem.

## Relationship to prior work

Deshpande and Singh (arXiv:2001.05448, Theorem 3.10) give the exact sphere count for connected graphs whose **every** nonleaf vertex has at least one adjacent leaf. This hypothesis does not hold for \(T_{a,c}\), since the middle hub has degree two but no pendant leaf. Their formula is used only for the double-star link (3), where both nonleaf hubs do have leaves. Their Corollary 3.13 likewise assumes strictly positive leaf multiplicities at all spine vertices. The small special case \(T_{2,2}\) is also a perfect binary tree of height two, and its scale-\(4\) homotopy type was already computed in their Section 5 (Example 5.1). That previously calculated individual case is not claimed as new.

Abdelmalek and collaborators (arXiv:2106.10863, Theorem 3.12) establish vertex decomposability of higher independence complexes of caterpillars, including ones with leafless spine vertices. Sawant (arXiv:2605.25150, Theorem 3.6, first public 24 May 2026) extends vertex decomposability to every tree. These results imply general structural properties but provide neither the exact two-degree multiplicities above nor the null-attaching splitting for a bare middle vertex. The new assertion is the explicit *integral homotopy classification*, not vertex decomposability itself.

## Limitations

No analogous formula is asserted for a middle hub carrying additional leaves, more than three spine hubs, or arbitrary trees. Although the statement is integral, no canonical basis for the homology groups or induced automorphism representation is established here. Finite mod-two calculations alone cannot certify integral homotopy or originality; the proof and source comparisons are necessary. General literature search cannot exclude every unindexed equivalent result.

## References

1. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, initially public 15 January 2020, especially Theorem 3.10 and Corollary 3.13. https://arxiv.org/abs/2001.05448
2. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, A. Singh, *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863, initially public 21 June 2021, especially Theorem 3.12. https://arxiv.org/abs/2106.10863
3. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, initially public 24 May 2026, especially Theorem 3.6. https://arxiv.org/abs/2605.25150
