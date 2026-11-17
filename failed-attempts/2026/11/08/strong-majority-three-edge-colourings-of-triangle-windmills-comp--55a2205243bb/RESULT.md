# Strong-majority three-edge colourings of triangle windmills: complete classification and enumeration

## Finding
For \(m\ge2\), let \(F_m=K_1\vee(mK_2)\) be the friendship graph (\(m\) triangles sharing one common vertex). All vertices and edges are labelled. A strong-majority edge-colouring of a finite simple graph assigns colours to edges, not necessarily properly, so that for every edge and every colour at most half the edges adjacent to it have that colour. Adjacent edges are distinct edges sharing an endpoint.

Give the three available colours the names \(1,2,3\). For blade \(i\), write \(a_i,d_i\) for its spoke-edge colours and \(b_i\) for the third, outer edge colour. Define the **global missing-spoke set**
\[U=\{c\in\{1,2,3\}:\text{some blade has neither spoke coloured }c\}.\]

**Classification theorem.** An edge assignment is strong-majority if and only if the two spokes of every triangle have different colours and every outer edge has a colour in \(U\):
\[a_i\neq d_i\quad\text{and}\quad b_i\in U\qquad (1\le i\le m).\]
This determines every optimal assignment and implies \(\operatorname{Maj}'(F_m)=3\).

**Exact enumerator.** The number \(N_m\) of assignments using the three named colours (which the condition forces all to occur) is
\[
N_m=2^m\Bigl[3+3(2^m-2)2^m+(3^m-3\cdot2^m+3)3^m\Bigr]
=2^m\bigl(9^m-3\cdot6^m+3\cdot4^m+3\cdot3^m-6\cdot2^m+3\bigr).
\]
The values for \(m=2,3,4\) are respectively \(108,2472,57456\).

**Asymptotic and orbit consequences.** Among all \(3^{3m}\) unrestricted named assignments, the strongly majority fraction equals \(N_m/3^{3m}\), asymptotic to \((2/3)^m\). For \(m\ge2\), the centre is unique; automorphisms permute triangles and swap the two outer vertices in each triangle. Hence an optimal assignment, modulo graph automorphisms and permutation of palette names, is completely specified by a nonnegative integral \(3\times3\) array \((h_{cb})\), where \(h_{cb}\) is the number of blades with missing spoke colour \(c\) and rim colour \(b\). The sum of all entries is \(m\), and a column can be nonzero only when its indexed row has positive sum. Arrays are equivalent precisely under simultaneous permutation of row and column labels.

## Assumptions and scope
The parameter \(m\) is any integer at least two; a blade has two individually labelled outer vertices, and the rim joins those vertices. The hub is adjacent to each outer vertex. Three colours are named and distinguishable for the count. There is no properness requirement: a rim may share its colour with one of its adjacent spokes, depending on the global missing-spoke set. Colour palettes of other sizes are not counted by \(N_m\). The one-blade graph is a triangle and obeys the same calculation with \(N_1=6\), but the nontrivial infinite-family statement and orbit assertion concern \(m\ge2\).

## Proof
The two edges adjacent to a rim edge are exactly its two spokes. With two adjacent edges, the strong-majority bound is one edge of each colour at most; therefore the two spokes must have different colours. Conversely, this condition settles every rim-edge constraint.

Fix any spoke assignment with different colours on the two spokes of each blade. Let \(q_c\) be the number of triangles whose spoke pair omits colour \(c\). Since every blade has one spoke of each of its two used colours, the total number of spokes coloured \(c\) is exactly \(s_c=m-q_c\). The adjacent edges of any spoke are the other \(2m-1\) spokes and its own rim, so there are exactly \(2m\) of them and the admissible per-colour maximum is \(m\). For a spoke of colour \(a\) in blade \(i\), the count of adjacent edges of colour \(c\) equals
\[s_c-\mathbf{1}_{c=a}+\mathbf{1}_{c=b_i}.\]
If \(q_c\ge1\), this is at most \(s_c+1\le m\), for every spoke. If \(q_c=0\), the colour \(c\) appears on precisely one spoke of each blade. If the rim of any blade were coloured \(c\), then its *other* spoke (whose colour differs from \(c\)) would have \(s_c+1=m+1\) adjacent edges of colour \(c\), violating the condition. Thus a rim colour is permitted if and only if it is missing from some spoke pair, exactly the asserted condition \(b_i\in U\). This proves necessity and sufficiency for all \(m\ge2\).

For the optimal palette size, a two-colour assignment would still require different spoke colours in every blade, so both colours would appear in every spoke pair and \(U\) would be empty. No rim could be coloured. One colour is impossible already at a rim. On the other hand, assigning the same two different colours to the two spokes of every blade and a third colour to every rim gives a valid three-colour assignment; the index is exactly three.

For each blade, choose the one of three colours missing from its spoke pair; there are exactly two orders for the other two colours on the labelled spokes. The \(m\) missing-colour choices form a map from the \(m\) blades to a nonempty subset \(U\) of the three palette colours. Conditional on this missing-colour word and its image size \(u=|U|\), the outer edges each have exactly \(u\) independently available colours. Thus there are \(2^m u^m\) assignments for each missing-colour word. There are precisely \(3\) words with image size one; \(3(2^m-2)\) with image size two; and \(3^m-3\cdot2^m+3\) with image size three, the last identity being onto-map inclusion--exclusion. Multiplying by the appropriate \(2^m u^m\), summing, and expanding yields the displayed formula.

Dividing by \(3^{3m}\) gives
\[\frac{N_m}{3^{3m}}=\left(\frac23\right)^m\left[1-3\left(\frac23\right)^m+3\left(\frac49\right)^m+3\left(\frac13\right)^m-6\left(\frac29\right)^m+3\left(\frac19\right)^m\right].\]
The bracket tends to one, proving the asymptotic. Finally, the centre of \(F_m\) has degree \(2m>2\), whereas each outer vertex has degree two. Graph automorphisms therefore consist exactly of arbitrary blade permutations and independent spoke-endpoint swaps. These erase spoke order but preserve the missing-spoke and rim-colour labels on a blade. Under colour-name permutations both labels transform together. The histogram \((h_{cb})\) is therefore a complete orbit invariant with the stated support condition.

## Verification
Run `python3 verify.py` using Python 3 standard library. It constructs the graph edge list, independently finds adjacent-edge neighborhoods by endpoint intersection, and checks all \(3^{3m}\) named assignments for \(1\le m\le4\) directly against the original strong-majority definition and against the classification. It also exhaustively rules out two-colour assignments for these orders and separately checks the exponential formula by aggregating missing-colour words through \(m=8\). Expected terminal output: `VERIFY_OK`. The finite experiments corroborate, but do not substitute for, the unrestricted proof above.

## Relationship to prior work
Kalinowski, Kamyczura, Pilśniak and Woźniak introduced strong-majority edge colourings and proved general bounds and results for cycles and complete graphs in their May 22, 2026 preprint [1]. Antoniuk, Prorok and Salia subsequently proved a five-colour general upper bound and degree-class constructions [2]. Pękała and Przybyło established a three-colour existence bound for graphs of minimum degree at least five [3], not applicable to friendship graphs, whose minimum degree is two. None of those reported the all-colourings histogram and exponential count for the triangle-windmill family in the material inspected. Exact minimum-colourability of the one-blade triangle is standard and is not claimed new. The local derivation here is independent of all general upper-bound proofs.

## Limitations
This theorem counts labelled, named, optimal three-colour assignments; it does not give an enumerator for larger palettes or for arbitrary cactus graphs, and does not claim a full closed formula for the number of colour-permutation/graph-automorphism orbits. A related August 2026 manuscript [3] was available via abstract and secondary descriptive material, not verified line-by-line against its complete primary text; although its published minimum-degree hypothesis is inapplicable, this is a residual priority risk. Full historical priority and independent mathematical assessment remain open.

## References
[1] R. Kalinowski, M. Kamyczura, M. Pilśniak and M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828v1, first publicly submitted 2026-05-22, especially Sections 2--3, Observations 11 and Theorem 12. https://arxiv.org/abs/2605.23828

[2] S. Antoniuk, M. Prorok and N. Salia, *Strong Majority Edge-Coloring*, arXiv:2607.00212v1, first publicly submitted 2026-06-30, especially Theorems 2 and 4 and Sections 1--2. https://arxiv.org/abs/2607.00212

[3] P. Pękała and J. Przybyło, *On Strong Majority Edge Colourings with Few Colours*, arXiv:2608.04122v1, first publicly submitted 2026-08-04. https://arxiv.org/abs/2608.04122
