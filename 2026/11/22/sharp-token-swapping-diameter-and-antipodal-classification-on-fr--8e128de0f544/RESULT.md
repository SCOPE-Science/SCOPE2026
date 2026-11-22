# Sharp token-swapping diameter and antipodal classification on friendship graphs

## Finding
Let \(F_t\) be the *friendship graph* (Dutch windmill) made of \(t\ge2\) triangles meeting in one central vertex \(0\), with paired peripheral vertices \(\{a_i,b_i\}\) for \(1\le i\le t\). Put one uniquely labelled token on every vertex. A legal move interchanges the tokens at two endpoints of an edge of \(F_t\). Write \(\mathcal T_t\) for the resulting graph of token configurations, with adjacent states differing by one move.

**Theorem.** The connected, bipartite, vertex-transitive graph \(\mathcal T_t\) has \((2t+1)!\) vertices, degree \(3t\), and
\[
\operatorname{rad}(\mathcal T_t)=\operatorname{diam}(\mathcal T_t)=3t.
\]
Relative to any chosen reference configuration, the configurations at distance exactly \(3t\) are **precisely** those obtained by fixing the central token and applying a fixed-point-free involution to the \(2t\) peripheral tokens in which every transposition joins two *different* triangles. The number of such antipodes per reference state is
\[
A_t=\sum_{j=0}^{t}(-1)^j\binom{t}{j}(2t-2j-1)!!,
\qquad(-1)!!=1.
\]
Hence there are exactly \(\frac12(2t+1)!A_t\) unordered diameter pairs and \(\frac12(2t+1)!(3t)\) edges. The first antipode counts, for \(t=2,3,4\), are \(2,8,60\), respectively. By contrast, \(F_1\) is a triangle and its swapping diameter is \(2\).

Adding the \(t\) peripheral edges to the \(2t\)-spoke star increases the number of available swaps by fifty percent but **does not improve the worst-case number of moves** for any \(t\ge2\); the theorem characterizes every configuration that remains worst-case.

## Assumptions and scope
Vertices and tokens are distinguishable. Every vertex contains exactly one token, swaps are *sequential*, and every edge (hub--leaf or paired peripheral) is usable. Distances are numbers of swaps, not graph distances between token destinations, parallel rounds, or the length of a walk on the base graph. All formulas apply to every integer \(t\ge2\), without a computational cutoff. A reference state is arbitrary because simultaneous relabelling of tokens acts transitively on the configuration graph.

## Proof
**1. A star-only upper bound and equality conditions.** Delete all peripheral edges of \(F_t\), leaving the star with \(2t\) leaves and hub \(0\). For any permutation of token placements relative to the identity, decompose it into disjoint cycles. Let the cycle containing \(0\) include \(h\) peripheral vertices, and let the remaining nontrivial cycles have lengths \(\ell_1,\ldots,\ell_q\ge2\), using \(s=\sum_j\ell_j\) peripheral vertices. A cycle through \(0\) is implemented using \(h\) hub--leaf transpositions. Each disjoint leaf cycle of length \(\ell\) is implemented using \(\ell+1\) hub--leaf transpositions (bring the hub into the cycle, visit its other vertices, then return). Since the cycles are disjoint, this constructs a legal sequence of length
\[
h+s+q\ \le\ h+\frac32s\ \le\ 3t-\frac12h\ \le\ 3t.
\]
This proves \(\operatorname{diam}(\mathcal T_t)\le3t\). Moreover, equality in the displayed inequalities is possible only when \(h=0\), \(s=2t\), and \(q=t\). Thus, if a configuration has distance \(3t\) even with all the peripheral edges available, its hub is fixed and its peripheral permutation consists of exactly \(t\) disjoint transpositions.

If any one of these transpositions interchanges the two vertices \(a_i,b_i\) of the same triangle, that pair can be corrected by a single peripheral-edge swap, and the other \(t-1\) pairs can be corrected by three hub swaps apiece. The total is \(1+3(t-1)=3t-2\). Consequently **every antipode must pair only different triangles**.

**2. A connected-factorization lower bound.** We prove the elementary lemma: Let a permutation \(\pi\) on \(N\) symbols have \(c\) cycles, including fixed points. If \(\pi\) is written as a product of \(m\) transpositions and the graph formed by those transposition edges is connected on all \(N\) symbols, then
\[
m\ge N+c-2.
\]
To prove it, expose the transpositions in their given order. Start with \(N\) isolated vertices in the graph of already-used transposition edges. At least \(N-1\) transpositions connect two distinct components of that evolving graph. Prior to such a transposition, the partial permutation preserves each component, so its endpoints lie in different permutation cycles; the transposition therefore *decreases* the cycle count by one. If \(D\) is the total number of cycle-decreasing steps and \(I\) the number of cycle-increasing steps, then \(D\ge N-1\), \(D-I=N-c\), and \(m=D+I=2D-(N-c)\ge N+c-2\), as asserted.

Now choose any fixed-point-free involution \(\pi\) of the peripheral vertices whose \(t\) transpositions all connect distinct triangles, fixing \(0\). In any factorization of this permutation into legal \(F_t\)-edge swaps, let \(H\) be the graph of all transposition edges used (ignoring repetitions). Each transposed pair must lie in the same component of \(H\), since the product of swaps preserves every component of \(H\). But the only path in \(F_t\) between different triangles goes through \(0\). Thus the component of \(H\) containing either endpoint of each transposed pair also contains \(0\). Every peripheral vertex belongs to such a pair; hence \(H\) is connected on all \(N=2t+1\) vertices. The permutation \(\pi\) has \(c=t+1\) cycles (\(t\) two-cycles and the fixed hub). The lemma gives
\[
\operatorname{dist}_{\mathcal T_t}(\mathrm{id},\pi)\ge (2t+1)+(t+1)-2=3t.
\]
The star-only construction in Step 1 attains exactly \(3t\), proving equality. Such a permutation exists for every \(t\ge2\): pair each \(a_i\) with \(b_{i+1}\), taking the index cyclically modulo \(t\). Each of the \(2t\) peripheral vertices occurs in exactly one pair, and no pair belongs to one triangle. Together with Step 1, this proves the exact antipodal classification and both radius and diameter; vertex transitivity makes every eccentricity equal.

**3. Counting and other graph properties.** All \((2t+1)!\) token assignments exist. At each configuration the \(2t\) hub edges and \(t\) peripheral edges give \(3t\) distinct neighboring states, hence the edge count by the handshake lemma. Every swap reverses permutation parity, establishing bipartiteness. The star edges alone generate all permutations, establishing connectivity and vertex transitivity. The specified antipodes are exactly perfect matchings on the \(2t\) peripheral labels which avoid the \(t\) designated within-triangle edges. Inclusion--exclusion over the forbidden edges gives the displayed sum \(A_t\). Since there are \(A_t\) antipodes at each of the \((2t+1)!\) states, unordered diameter pairs number \((2t+1)!A_t/2\). This completes the proof.

## Verification
Run `python3 checker.py` using Python 3.9 or later. The standalone script constructs the swap graph independently by breadth-first search from the identity, covering all \(6\), \(120\), \(5040\) and \(362880\) configurations for \(t=1,2,3,4\). For \(t=2,3,4\) it checks equality of the **complete sets** of farthest states with the theorem's cross-triangle involution condition, as well as the formula for their numbers. The saved output is `checker_output.txt`.

The finite checks corroborate the formulas but do not establish any infinite claim. The all-order proof consists of the explicit star sequences, the connected-transposition-factorization lemma, the articulation argument, and inclusion--exclusion; none of these steps depends on the finite experiments.

## Relationship to prior work
Aichholzer and collaborators, *Hardness of Token Swapping on Trees* (arXiv:2103.06707, first posted 2021-03-11), discuss shortest swaps on trees and cite the exact star diameter; they do not state a friendship-graph diameter or characterize its antipodes. Bonnet, Miltzow and Rzążewski, *Complexity of Token Swapping and Its Variants* (open-access Algorithmica, online 2017-10-20), treats complexity and the polynomial special case of stars, not the added within-petal edges. Ganesan's results on Cayley graphs generated by **transposition trees** provide a comparable tree baseline, whereas \(F_t\) contains triangles. Gijswijt and de Meijer (2024) address automorphism groups of Cayley graphs with general transposition sets, not their shortest-swap antipodes. Kiya and collaborators (2022) study the *different* sequential-walk swap rule, requiring successive used edges to form a walk.

The new assertion here is the exact friendship-graph diameter *together with an if-and-only-if characterization and census of all extreme token assignments*. The transitive-factorization inequality itself and the star-only upper bound are elementary background tools, not claimed as newly discovered. The comparison does not establish uniqueness against every unpublished or unindexed treatment.

## Limitations
The theorem concerns friendship graphs, not all block graphs, arbitrary trees, or general token swaps. It does not give a closed formula for the distance between every pair of configurations or a polynomial algorithm for every graph. Its extremal classification depends on triangles sharing a single articulation vertex and paired peripheral edges. An unindexed previous equivalent result is a residual priority risk; independent external mathematical validation has not yet occurred.

## References
1. O. Aichholzer et al., *Hardness of Token Swapping on Trees*, arXiv:2103.06707 (first publicly posted 2021-03-11), https://arxiv.org/abs/2103.06707.
2. É. Bonnet, T. Miltzow and P. Rzążewski, *Complexity of Token Swapping and Its Variants*, Algorithmica 80 (2018), first online 2017-10-20, https://doi.org/10.1007/s00453-017-0387-0.
3. A. Ganesan, *Diameter of Cayley graphs of permutation groups generated by transposition trees*, arXiv:1111.3114 (2011), https://arxiv.org/abs/1111.3114.
4. D. Gijswijt and F. de Meijer, *Automorphism Groups of Cayley Graphs Generated by General Transposition Sets*, Electronic Journal of Combinatorics 31(3) (2024), https://doi.org/10.37236/12771.
5. H. Kiya, Y. Okada, H. Ono and Y. Otachi, *Sequentially Swapping Tokens: Further on Graph Classes*, arXiv:2210.02835 (first publicly posted 2022-10-06), https://arxiv.org/abs/2210.02835.
