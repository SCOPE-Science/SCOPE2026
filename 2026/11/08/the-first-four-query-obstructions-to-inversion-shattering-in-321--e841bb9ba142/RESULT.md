# The first four-query obstructions to inversion shattering in \(321\)-avoiding permutations

## Finding
For each integer \(n\ge1\), let \(\operatorname{Av}_n(321)\) be the permutations \(\pi\) of \([n]\) with no indices \(i<j<k\) satisfying \(\pi(i)>\pi(j)>\pi(k)\). A pair query \((i,j)\), \(i<j\), receives label \(1\) when \(\pi(i)>\pi(j)\), and label \(0\) otherwise. A finite support \(S\) of distinct queries is *shattered* when every map from \(S\) to \(\{0,1\}\) is realized by such a permutation.

**Theorem (complete local criterion through four queries).** For every \(n\ge1\) and every support \(S\subseteq\binom{[n]}2\) with \(|S|\le4\), \(S\) is shattered if and only if it contains none of the following configurations, with the indices in each display strictly increasing:

1. **Two-query chain** on \(a<b<c\): \(\{(a,b),(b,c)\}\).
2. **Three-query types** on \(a<b<c<d\):
   \[
   \begin{aligned}
   &\{(a,c),(a,d),(b,c)\},\\
   &\{(a,c),(b,c),(b,d)\},\\
   &\{(a,d),(b,c),(b,d)\}.
   \end{aligned}
   \]
3. **Four-query types** on \(a<b<c<d<e<f\):
   \[
   \begin{aligned}
   Q_A&=\{(a,f),(b,c),(b,e),(d,e)\},\\
   Q_B&=\{(a,f),(b,d),(b,e),(c,e)\}.
   \end{aligned}
   \]

Every listed configuration is an inclusion-minimal nonshattered support. Thus the numbers of minimal nonshattered supports of cardinalities \(2,3,4\) are respectively
\[
\binom n3,\qquad 3\binom n4,\qquad 2\binom n6.
\]
The first minimal four-query obstruction appears at \(n=6\), with exactly two supports. In particular, every three-query subset of either four-query obstruction is shattered, but the full four-query support is not.

**Structural corollary.** For every \(n\ge4\), the complex of all shattered pair-query supports is not a matroid independence complex. The two minimal two-edge obstructions \(\{(1,2),(2,3)\}\) and \(\{(1,2),(2,4)\}\) share \((1,2)\), whereas \(\{(2,3),(2,4)\}\) is shattered, violating circuit elimination.

## Assumptions and scope
The universe consists of *position comparisons*, not a subset of permutation values and not the alternative permutation VC dimension defined by realizing all relative orders on a selected set of positions. The sign convention is inversion = \(1\). Statements hold for arbitrary \(n\), but the criterion classifies only supports with at most four queries; no claim is made about all larger minimal nonshattered supports or the full VC dimension of the class.

## Proof
**1. Reduction to at most eight positions.** The empty support is trivially shattered. For a nonempty \(S\) with \(k\le4\) queries, and write its distinct endpoints as \(r_1<\cdots<r_m\), with \(m\le2k\le8\). Any \(321\)-avoiding permutation on \([n]\), restricted to those endpoints and standardized to the ranks \(1,\ldots,m\), avoids \(321\) and preserves all pair labels. Conversely, let \(\sigma\in\operatorname{Av}_m(321)\). Divide the positions \([n]\) into contiguous blocks \(B_1=[1,r_2-1]\), \(B_j=[r_j,r_{j+1}-1]\) for \(2\le j<m\), and \(B_m=[r_m,n]\) (for \(m=1\), take one block \([1,n]\)). Each block contains its designated endpoint \(r_j\). Inflate the entry \(\sigma(j)\) into a *strictly increasing* block of \(|B_j|\) consecutive values; different blocks receive disjoint value intervals in the relative order prescribed by \(\sigma\). The resulting permutation avoids \(321\), because any decreasing triple would require positions in three distinct blocks and descend in \(\sigma\). Its pair comparisons on all \(r_j\) agree with \(\sigma\). Hence \(S\) is shattered on \([n]\) if and only if its order-standardized support is shattered on \([m]\), where \(m\le8\).

**2. Explicit nonrealizability.** The two-query chain cannot have both labels \(1\), as that would be a descending triple. For the three-query types, take the queries in the order displayed: the respective forbidden label vectors are \((0,1,1)\), \((1,0,1)\), and \((1,1,0)\). In each case the inequalities force a decreasing triple. For either four-query type, the label vector \((1,1,0,1)\), again in the displayed query order, is impossible: the first inversion gives \(\pi(a)>\pi(f)\); the second inversion on \((b,c)\) or \((b,d)\), together with \(a<b\), forces \(\pi(a)<\pi(b)\) to avoid \(321\); the third label gives \(\pi(b)<\pi(e)\); the last inversion on \((d,e)\) or \((c,e)\), with \(e<f\), forces \(\pi(e)<\pi(f)\). Thus \(\pi(a)<\pi(b)<\pi(e)<\pi(f)<\pi(a)\), a contradiction. In every case, a larger support containing the configuration is not shattered.

**3. Exhaustive finite converse and minimality.** The attached standalone exact-arithmetic checker `check_local.py` enumerates every permutation of each length \(m=1,\ldots,8\), filters those avoiding \(321\) by direct triple tests, enumerates *every* support with \(0\le|S|\le4\), and computes all realized label vectors by direct comparisons. Independently, it constructs the stated forbidden families by ordered index tuples and tests their containment. It asserts equality between the observed shattering predicate and the forbidden-subset predicate on every support; it also asserts the separate minimal-obstruction counts. The run passes for all eight lengths. This is exhaustive, not a sample: the largest case checks all \(\sum_{k=0}^4\binom{28}{k}\) supports on eight endpoints against all \(1430\) avoiding permutations. Step 1 turns this finite exhaustive result into the asserted statement for *all* \(n\). The counting formulas follow because each obstruction uses exactly \(3,4,6\) distinct ordered vertices respectively and the listed patterns are distinct and minimal. The matroid corollary then follows from circuit elimination as stated.

## Verification
Run `python3 check_local.py` from the directory containing this result. The final output is `AV321_LOCAL_SHATTERING_4_PASS`. Its table records, for each \(m=1,\ldots,8\), the Catalan-sized hypothesis family, the numbers of shattered supports of sizes \(0,1,2,3,4\), and the minimal-obstruction counts. At \(m=8\) these are \((1,28,322,1820,4977)\) and \((0,0,56,210,56)\) respectively.

The separate `check_padding.py` builds increasing-block inflations over every subset of endpoint positions for all \(n\le8\); it validates avoidance and preservation of comparisons on \(16{,}169\) combinations, outputting `PADDING_321_PASS 16169`. These finite padding tests corroborate, but do not replace, the unrestricted inflation proof in Step 1.

## Relationship to prior work
Janson's *Patterns in random permutations avoiding the pattern 321* (arXiv:1709.08427, first public 2017-09-25) develops \(321\)-avoiding permutations, inversion graphs, and pattern-counting asymptotics. Its inversion-graph discussion supplies context but does not state this all-labelings comparison-support problem or its local forbidden families. Bożyk et al., *Vertex Deletion into Bipartite Permutation Graphs* (IPEC 2020, DOI 10.4230/LIPIcs.IPEC.2020.5), study deletion algorithms and unlabelled graph obstructions, rather than ordered position-comparison traces. Raz's *VC-dimension of sets of permutations* (Combinatorica 2000, DOI 10.1007/s004930070023) uses a different notion, in which \(k\) positions must realize all \(k!\) total orders; the present theorem concerns all binary assignments on a chosen set of pair queries. These results are neither claimed as new nor used to infer a noncoverage guarantee from titles alone.

## Limitations
The finite converse relies on transparent, executable exhaustive computation through eight endpoints, rather than a hand-derived classification of every small case. The reduction proves precisely why this suffices for four-query supports, not for supports with more queries. Unsearched terminology and inaccessible relevant results could affect historical priority, and no external or independent mathematical audit has occurred. A 2026 work on maximal Lehmer codes of \(321\)-avoiders is a potentially related source whose full text was unavailable; its reported maximal-code counting is not the present all-labelings criterion.

## References
1. S. Janson, *Patterns in random permutations avoiding the pattern 321*, arXiv:1709.08427 (first public 2017-09-25), https://arxiv.org/abs/1709.08427.
2. Ł. Bożyk, J. Derbisz, T. Krawczyk, J. Novotná, and K. Okrasa, *Vertex Deletion into Bipartite Permutation Graphs*, IPEC 2020, DOI 10.4230/LIPIcs.IPEC.2020.5, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.IPEC.2020.5.
3. R. Raz, *VC-dimension of sets of permutations*, Combinatorica 20 (2000), 241–255, DOI 10.1007/s004930070023.
4. A. Beveridge, Y. Hu, and Y. Liu, *Maximal Lehmer Codes for Permutations with Classical and Consecutive 321-Avoidance*, arXiv:2609.33137 (2026); plausible related object, full-text comparison incomplete.
