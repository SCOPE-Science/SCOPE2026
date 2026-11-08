# Exact shortest sorting-supersequences for unit intervals of ply two

## Finding
Let \(\mathcal I=\{I_1,\ldots,I_n\}\) be any nonempty labeled family of open unit intervals on the real line, with ply at most two: no real point belongs to three intervals. Reindex by nondecreasing left endpoint. Let \(c\) denote the number of connected components (singletons included) of the interval-overlap graph, whose vertices are the labeled intervals and whose edges represent nonempty intersections. A *sorting-supersequence* is a word in the interval labels containing, as a subsequence, the increasing-label order of the points for **every** choice of pairwise distinct \(p_i\in I_i\), when labels are listed according to increasing chosen point.

**Theorem.** The minimum possible length of a sorting-supersequence equals
\[
\operatorname{OPT}(\mathcal I)=2n-c.
\]
This minimum is attained by an explicit word computable in \(O(n\log n)\) total time (and \(O(n)\) time after ordering left endpoints). Moreover, if the component sizes are \(s_1,\ldots,s_c\), then the number of distinct realizable strict sorted orders is exactly
\[
\prod_{j=1}^{c} F_{s_j+1},
\]
where \(F_1=F_2=1\) are Fibonacci numbers. In particular, a connected overlap path of \(n\) unit intervals needs exactly \(2n-1\) symbols, with equality attained for every \(n\ge1\).

## Assumptions and scope
All interval lengths are precisely one, intervals are open, and all labels are distinct, even if two underlying intervals coincide. Intersections at a common boundary point do not constitute overlap. The sample points are required to be pairwise distinct, so their sorting permutation is unambiguous. The case \(n=1\) is included. The ply bound concerns the open intervals themselves, not their closures. All supersequence words may repeat labels without restriction; length counts every occurrence.

## Proof
**1. The overlap graph is a disjoint union of consecutive paths.** Write \(I_i=(a_i,a_i+1)\) with \(a_1\le\cdots\le a_n\). If \(j\ge i+2\) and \(I_i\cap I_j\ne\varnothing\), any point in this intersection also belongs to \(I_{i+1}\): its coordinate is larger than \(a_j\ge a_{i+1}\) and smaller than \(a_i+1\le a_{i+1}+1\). This would violate ply two. Thus edges can join only successive indices. Conversely any collection of present successive-index edges defines disjoint path components consisting of consecutive labels. Intervals from distinct components are disjoint and force their component order.

**2. All realizable orders are precisely the disjoint adjacent swaps.** For indices \(i<j-1\), their intervals are disjoint with \(I_i\) strictly to the left of \(I_j\), hence any chosen points satisfy \(p_i<p_j\). Therefore the only possible inverted pairs in a realized order are neighboring labels \(i,i+1\) whose intervals overlap. Two adjacent inversions cannot coexist: if \(p_{i+1}<p_i\) and \(p_{i+2}<p_{i+1}\), then \(p_{i+2}<p_i\), contrary to the forced nonneighbor order. The inverted adjacent pairs consequently form a matching in the overlap-path graph; its permutation is the identity with precisely those pairwise disjoint neighboring positions exchanged.

Conversely, fix any matching-swap permutation \(\pi\). Every disjoint pair \(I_u,I_v\) with \(u<v\) is prescribed in the order \(u\) before \(v\): swapping only neighboring labels cannot reverse a nonneighbor pair, and any present neighboring edge is an overlapping pair. We now give a direct interval-realizability argument. More generally, suppose a permutation \(\pi\) respects the left-to-right order of all disjoint interval pairs. Put \(A_t=\max\{a_{\pi(s)}:1\le s\le t\}\). For each \(t\) we have \(A_t<a_{\pi(t)}+1\): otherwise some earlier interval starts at or beyond the current interval's right endpoint, which would force the current label earlier by the assumed disjoint-pair order. Since there are finitely many strict inequalities, choose \(\varepsilon>0\) so small that \(A_t+t\varepsilon<a_{\pi(t)}+1\) for all \(t\). Taking \(p_{\pi(t)}=A_t+t\varepsilon\) gives strictly increasing sample points, each strictly inside its corresponding interval. Hence every matching-swap order is realizable. Every component of size \(s\) has exactly the number of matchings of a path on \(s\) vertices, namely \(F_{s+1}\), possible orders, independently of other components.

**3. Sharp universal-word lemma for one path.** Let \(\mathcal P_m\) consist of the permutations of \(1,\ldots,m\) obtained by swapping any matching of consecutive pairs. Let \(u_m\) be the minimum length of a word containing every member of \(\mathcal P_m\) as a subsequence. Then
\[
u_m=2m-1\qquad(m\ge1).
\]
For the upper bound set \(W_1=(1)\) and recursively \(W_m=W_{m-1}\,m\,(m-1)\). Every permutation in \(\mathcal P_m\) either ends in \(m\), with preceding part in \(\mathcal P_{m-1}\), or ends in \(m,m-1\), with preceding part in \(\mathcal P_{m-2}\). The latter part is a subsequence of \(W_{m-1}\) because it can be extended by \(m-1\) to a member of \(\mathcal P_{m-1}\). Hence \(W_m\) contains both types, and \(|W_m|=2m-1\).

For the lower bound use induction, with \(u_1=1\). Let \(V\) be any common supersequence of \(\mathcal P_m\). Removing every occurrence of label \(m\) leaves a common supersequence of \(\mathcal P_{m-1}\), because each permutation \(\pi\in\mathcal P_{m-1}\) occurs inside target \(\pi m\in\mathcal P_m\). If \(V\) contains at least two occurrences of \(m\), this yields \(|V|\ge u_{m-1}+2=2m-1\). Otherwise \(V\) has exactly one \(m\); it must occur, since targets contain it. For every \(\pi\in\mathcal P_{m-1}\), the target \(\pi m\) requires the prefix of \(V\) preceding that sole \(m\) to contain \(\pi\). This prefix has length at least \(u_{m-1}=2m-3\). The target ending in the reversed final pair \(m,m-1\) additionally forces at least one symbol after the sole \(m\). Thus again \(|V|\ge (2m-3)+1+1=2m-1\). Induction proves the lemma.

**4. Components add exactly.** Let \(C_j\) be an overlap component of size \(s_j\). Take the word \(W_{s_j}\) from step 3 and replace \(1,\ldots,s_j\) by the actual consecutive labels of \(C_j\). Concatenating these words in component order covers all realizable orders and has length \(\sum_j (2s_j-1)=2n-c\). Conversely, project any valid global sorting-supersequence onto the labels belonging to \(C_j\). Since every path matching on \(C_j\) extends to a realizable global order by choosing identity orders in other components, that projection must cover \(\mathcal P_{s_j}\), so it contains at least \(2s_j-1\) symbols. Summing independent counts over the disjoint label sets yields the matching lower bound.

**5. Construction time.** Sort unit intervals by left endpoint, scan successive pairs for nonempty overlap (\(a_{i+1}<a_i+1\)), list their path components, emit the recursive words iteratively, and concatenate. Output length is at most \(2n-1\); the scan and emission take linear time after the initial sort. This completes the proof.

## Verification
Run `python3 checker.py` from this file's directory. It enumerates all path matching-swap orders for sizes through eleven, checks the length and subsequence property of the constructive words, and independently finds the minimum common-supersequence length by breadth-first search through size six. It then enumerates all 255 possible consecutive overlap-edge masks on sizes one through eight and tests the component formula against all 1,930 resulting realizable strict orders. The finite checker is corroboration, not a proof of unbounded sizes; the argument above is the proof.

## Relationship to prior work
Löffler and Raichel (2026, arXiv:2601.19453), Lemma 13 and Theorem 5, introduce the sorting-supersequence construction for uncertain unit intervals and prove a general upper bound of \(4\Delta n\) for ply \(\Delta\), with smoothness guarantees. At \(\Delta=2\), their bound is \(8n\), not the exact optimum for individual instances. The present theorem adds an exact minimum of \(2n-c\), a complete description and count of realizable sorted orders, and a linear-time optimal construction for precisely the unit-ply-two case. Their smoothness guarantee is a different property: an optimal minimum-length word here is not asserted to satisfy their smoothness bounds.

Löffler and Raichel (2025, arXiv:2502.03633; see especially the updated preprint's Section 4.3, Lemma 34) invoke the same \(4\Delta n\) sorting-supersequence bound to construct geometric convex-hull supersequences. The generic universal-word estimates of Radomirović (2012) address all permutations on a finite alphabet, rather than the matchings-of-a-path restriction here. These broader or distinct statements do not logically imply the exact parameter-dependent minimum given above.

## Limitations
The classification uses equal unit lengths and ply at most two. It is not proved for arbitrary unequal interval lengths or ply three; nonunit length-two-ply interval families can have a nonpath overlap graph. Ties between selected points are excluded. The result concerns the minimum word length of a sorting-supersequence, not optimal reconstruction time under arbitrary computational models, nor minimum length subject to an additional smoothness constraint. Although primary sources were inspected and index searches found no equivalent, comprehensive historical priority cannot be guaranteed; independent validation remains unperformed.

## References
1. M. Löffler and B. Raichel, *Preprocessing Uncertain Data into Supersequences for Sorting and Gaps*, arXiv:2601.19453, first posted 2026-01-27, https://arxiv.org/abs/2601.19453 . Lemma 13 and Theorem 5.
2. M. Löffler and B. Raichel, *Preprocessing Disks for Convex Hulls, Revisited*, arXiv:2502.03633, first posted 2025-02-05, https://arxiv.org/abs/2502.03633 . Updated preprint Section 4.3 and Lemma 34.
3. S. Radomirović, *A Construction of Short Sequences Containing All Permutations of a Set as Subsequences*, Electronic Journal of Combinatorics 19(4), P31 (2012), https://doi.org/10.37236/2859 . General universal-word upper bound; the complete text was not used in the proof.
