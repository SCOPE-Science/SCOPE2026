# Exact swapping diameter and four antipodes of the pentagonal prism

## Finding

Let \(G=C_5\square K_2\) be the pentagonal prism (also called the five-rung circular ladder), with one distinct token on each of its ten vertices. A legal move exchanges the two tokens at the ends of one edge, with one exchange per move. The resulting permutation reconfiguration graph \(\mathcal T(G)\) is connected, bipartite, vertex-transitive and \(15\)-regular, on \(10!=3{,}628{,}800\) states. Its radius and diameter are both exactly

\[\operatorname{rad}(\mathcal T(G))=\operatorname{diam}(\mathcal T(G))=17.\]

**All four antipodes have a simple geometric form.** Identify prism sites with \((i,a)\), \(i\in\mathbb Z/5\mathbb Z\) and \(a\in\{0,1\}\). For any initial placement \(p\), exactly four target placements are at distance \(17\):

\[q(i,0)=p(i+s_0,1),\qquad q(i,1)=p(i+s_1,0),\qquad(s_0,s_1)\in\{2,3\}^2.\]

Consequently there are exactly \(7{,}257{,}600\) unordered diametral pairs. The complete distance-shell vector from every configuration, at distances \(0\) through \(17\), is

\[(1,15,135,895,4734,20606,73914,213600,478259,789069,908113,691531,332274,96706,16840,1974,130,4).\]

For a placement \(p\), define the usual transportation lower bound

\[B(p)=\left\lceil\frac12\sum_{v\in V(G)} d_G(v,p(v))\right\rceil,\]

with token labels identified with their destination vertices. Then the exact maximum deficit \(d_{\mathcal T(G)}(e,p)-B(p)\) is \(4\), attained by precisely \(1{,}440\) placements from any specified start. The four diameter placements instead each have transportation deficit \(2\).

## Assumptions and scope

The vertex order is \(0,1,2,3,4,5,6,7,8,9\), with \(0,\ldots,4\) on one cyclic rail and \(5,\ldots,9\) on the other. There are exactly fifteen undirected edges: \(\{i,(i+1)\bmod5\}\), \(\{5+i,5+((i+1)\bmod5)\}\), and \(\{i,5+i\}\), for \(i=0,\ldots,4\). Both rails are closed cycles; the network is not the open five-rung ladder and not the Petersen graph \(GP(5,2)\).

Write \(p(v)\) for the token present at vertex \(v\), so a placement is a bijection of \(\{0,\ldots,9\}\). The reference placement \(e\) has \(e(v)=v\). A move exchanges two values \(p(u),p(v)\) exactly when \(\{u,v\}\) is a prism edge. Every edge has unit cost. The transportation lower bound uses shortest-path distances in the ten-vertex base graph, not in the factorial-size reconfiguration graph. All assertions concern this fixed graph; no formula for arbitrary prism length is asserted.

## Proof

**Cayley reduction.** Since the base graph is connected, its edge transpositions generate all permutations of ten labels: transpositions along a spanning tree suffice. Every reconfiguration state is therefore reachable. Relabelling all tokens by the same bijection commutes with swapping positions. Such relabelling carries any chosen start to \(e\), so it preserves reconfiguration distances and proves vertex transitivity. Each of the fifteen distinct base edges gives a different neighbor, proving regularity. Every swap changes permutation parity, proving bipartiteness. Hence a distance census from \(e\) determines the full radius, diameter, and numbers of antipodes at every start.

**Exact exhaustive certificate.** The file `enum_factoradic.cpp` ranks every permutation in the interval \(0\le r<10!\) by its factorial-number-system code. Its inverse obtains the permutation by repeatedly taking the indexed smallest unused label; factorial decoding and ranking are inverse bijections. A breadth-first search beginning at \(e\) decodes every dequeued permutation, swaps positions along each of the fifteen defined edges, and inserts a newly discovered rank into a FIFO queue with distance one greater. Every possible legal neighbor is visited and no other move is admitted. Standard BFS induction proves that the distance stored at first discovery is the true shortest path distance. The final number of distinct discovered ranks is exactly \(3{,}628{,}800=10!\), so this is exhaustive, not a sample. The number of states at each layer is the vector stated above; the maximal nonempty layer is layer \(17\).

The layer of radius \(17\), in digit-string notation \(p(0)\cdots p(9)\), is exactly

`7895623401`, `7895634012`, `8956723401`, `8956734012`.

These are precisely the four rail-interchange, independent-two-step-rotation placements specified in the finding. The count of unordered diameter pairs follows from four farthest states per placement, counting each unordered pair twice.

**Explicit upper-bound witness.** A shortest route to the first listed antipode has seventeen swaps. First use the five rungs \((0,5),(1,6),(2,7),(3,8),(4,9)\). Next use on the first rail \((0,1),(1,2),(2,3),(4,0),(0,1),(1,2)\). Finally repeat these six swaps on the other rail, adding five to both endpoints. Direct substitution yields `7895623401`. Exhaustive BFS establishes that no shorter route to this state, or a longer required route to another state, exists.

**Transportation comparison.** For each of the ten labels, the ring part of its graph distance from vertex \(i\) to token destination \(j\) is \(\min(|(i\bmod5)-(j\bmod5)|,5-|(i\bmod5)-(j\bmod5)|)\), plus one if the rails differ. Each swap can reduce the sum of these distances by at most two; thus its ceiling-half is a lower bound on the required swap count. Both exhaustive implementations calculate that bound and subtract it from every exact BFS depth, finding maximum deficit four and exactly \(1{,}440\) equality states. At each of the four antipodes all ten tokens travel base-graph distance three, so \(B=15\) and the deficit is \(17-15=2\).

**Separate computational cross-check.** `enum_packed.cpp` independently represents each permutation as a 40-bit word (one four-bit digit per site), stores visited words in a hash map, and computes neighbors through bitwise position exchanges rather than factorial indexing. It recomputes the entire distance-shell vector, all four antipodes, and the maximum transportation deficit and its count. `verify.py` builds both programs and checks their complete reported invariants, as well as the explicit route. Both implementations visit exactly the full factorial state count and agree on every reported statistic.

## Verification

With a C++17 compiler and Python 3, run `python3 verify.py` in the directory containing the three source files. The script compiles both enumerators, executes each separately, verifies the identical eighteen distance-shell counts, confirms the exact four digit-string antipodes, confirms the sharp transportation deficit and count, and checks the seventeen-swap witness. The expected terminal line begins `VERIFY_OK:`. The two C++ sources can also be built and run separately using `g++ -std=c++17 -O3 enum_factoradic.cpp -o enum_a` and `g++ -std=c++17 -O3 enum_packed.cpp -o enum_b`.

The results are a deterministic exhaustive finite proof with a fully specified state space and transition rule. Neither the code nor the result asserts a formula for other prism lengths; computational agreement is not an independent external audit.

## Relationship to prior work

Aichholzer et al., *Hardness of Token Swapping on Trees* (arXiv:2103.06707; ESA 2022), study sequential and parallel token swapping on trees and hardness/approximation; the pentagonal prism is not a tree, and their theorems do not entail this exact finite diameter. Bonnet, Miltzow and Rzążewski, *Complexity of Token Swapping and Its Variants* (Algorithmica, 2017 online), prove general complexity, approximation and special-class results, not the complete five-prism metric. Adin, Alon and Roichman, *Circular Sorting* (2025), analyze token order on a single circle modulo common rotation; that is a different configuration space and move graph from two fully labelled rings with inter-rail swaps.

A published exact token-swapping computation for the Petersen graph, another cubic graph on ten vertices, reports diameter thirteen. Its graph is \(GP(5,2)\), whereas the present graph is \(GP(5,1)\). The two sets of allowed transpositions differ and neither exact finite census implies the other. Other work on circular-ladder zero-forcing reconfiguration concerns different combinatorial objects and movement rules. The novelty proposed here is restricted to the exact five-prism sequential-swap metric, antipode geometry, and transportation-deficit classification; the general BFS method and Cayley symmetry are standard.

## Limitations

This is a finite exact result for one canonical ten-vertex network, not a theorem for general prisms or arbitrary cubic graphs and not a general polynomial-time token-swapping algorithm. Individual distances are computable from the included exhaustive census but no closed-form distance expression for arbitrary target permutations is claimed. Indexed searches and inspection of the stated literature do not eliminate the possibility of an earlier unindexed tabulation or a result under another name. Verification is reproducible computational checking, with no independent external mathematical audit reported.

## References

1. Oswin Aichholzer et al., *Hardness of Token Swapping on Trees*, arXiv:2103.06707 (first public 2021-03-11), https://arxiv.org/abs/2103.06707 ; ESA 2022, https://doi.org/10.4230/LIPIcs.ESA.2022.3.
2. Édouard Bonnet, Tillmann Miltzow and Paweł Rzążewski, *Complexity of Token Swapping and Its Variants*, Algorithmica 80 (2018), online 2017-10-20, https://link.springer.com/article/10.1007/s00453-017-0387-0.
3. Ron M. Adin, Noga Alon and Yuval Roichman, *Circular Sorting*, dated 2025-02-11, https://web.math.princeton.edu/~nalon/PDFS/cycsort1.pdf.
4. *Exact token-swapping diameter and distance spectrum of the Petersen graph*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-token-swapping-diameter-and-distance-spectrum-of-the-peter--8bd9f80f9e2c.
