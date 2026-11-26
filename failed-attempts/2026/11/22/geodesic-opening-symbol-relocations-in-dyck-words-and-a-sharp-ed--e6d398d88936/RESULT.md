# Geodesic opening-symbol relocations in Dyck words and a sharp editing diameter

## Finding
For every integer \(n\ge1\), let \(\mathcal D_n\) be all Dyck words of length \(2n\) with \(1\) denoting an opening/up step and \(0\) a closing/down step. In the graph \(U_n\), a move deletes **one** opening symbol and reinserts it anywhere, retaining a valid Dyck word. For \(x\in\mathcal D_n\), uniquely write
\[
x=1^{g_0(x)}0\,1^{g_1(x)}0\cdots1^{g_{n-1}(x)}0.
\]
Then the exact distance between every ordered pair \(x,y\in\mathcal D_n\) is
\[
 d_{U_n}(x,y)=\sum_{i=0}^{n-1}\max\{g_i(x)-g_i(y),0\}
 =\frac12\sum_{i=0}^{n-1}|g_i(x)-g_i(y)|.
\]
Consequently \(U_n\) is connected and has diameter exactly \(n-1\). If the move may instead relocate either a single opening or a single closing symbol (graph \(R_n\)), the graph is also connected and its diameter is likewise exactly \(n-1\). These claims include \(n=1\), when both graphs have one vertex and diameter zero.

## Assumptions and scope
Words are **labelled by their ordered positions**, but equal symbols are indistinguishable. A relocation deletes exactly one symbol, then inserts the same symbol into any of the \(2n\) slots of the shortened word; moves yielding an unchanged word are omitted. Only the endpoints of each move must be valid Dyck words. For \(U_n\), only \(1\) may be moved; for \(R_n\), either \(0\) or \(1\). Distances are shortest numbers of such sequential moves. The graph is undirected because every relocation can be reversed. No upper height bound is imposed.

Write \(G_j(g)=\sum_{i=0}^{j-1}g_i\) for \(1\le j\le n\). The vector \(g\in\mathbb Z_{\ge0}^n\) represents a Dyck word precisely when \(\sum_i g_i=n\) and \(G_j(g)\ge j\) for all \(1\le j\le n\). In particular \(g_0\ge1\). A nontrivial \(1\)-relocation transfers one unit from one gap coordinate to another.

## Proof
**Lower bound for the opening-only distance.** Each opening-only move decreases one gap coordinate by one and increases a different coordinate by one. Thus it can correct at most one surplus relative to a target vector. The number of moves from \(g\) to \(h\) is at least \(\sum_i(g_i-h_i)_+\).

**Matching path without forbidden intermediates.** Pair each surplus unit at a coordinate \(i\) with a deficit unit at some coordinate \(j\), producing exactly \(Q=\sum_i(g_i-h_i)_+\) transfers, using every surplus and deficit once. Execute all transfers with \(j<i\) (leftward) first. A leftward transfer weakly increases every prefix sum \(G_s\) and hence preserves the Dyck inequalities; donor coordinates stay nonnegative because only surplus units are removed. Now let \(g'\) be the vector after all leftward transfers. The remaining pairs all have \(i<j\), and they will move opening symbols rightward. For any prefix \(s\), the difference \(G_s(g')-G_s(h)\) equals the number of pending rightward transfers with \(i<s\le j\). This count is nonnegative. Executing any of these transfers decreases just those prefix differences crossing its interval by one and removes that same transfer from the pending count, so the invariant remains true. Thus throughout all rightward transfers \(G_s\ge G_s(h)\ge s\). The final vector is \(h\), and there are exactly \(Q\) steps. This proves the displayed all-pairs metric and provides a constructive shortest-path algorithm.

**Opening-only diameter.** Every two Dyck gap vectors satisfy \(g_0,h_0\ge1\). Hence \(\sum_i\min(g_i,h_i)\ge1\), so \(Q=n-\sum_i\min(g_i,h_i)\le n-1\). Equality is attained between the mountain word \(1^n0^n\) (gap vector \((n,0,\ldots,0)\)) and the alternating word \((10)^n\) (gap vector \((1,1,\ldots,1)\)). Hence \(\operatorname{diam}(U_n)=n-1\).

**Unrestricted one-symbol-relocation diameter.** As \(U_n\subseteq R_n\), its connectivity and upper diameter bound carry over. For a binary word \(w\), let \(r(w)\) be its number of maximal constant-symbol runs. Deleting one symbol cannot increase this run count; inserting one symbol increases it by at most two. Consequently every single-symbol relocation increases \(r\) by at most two. The mountain has \(r=2\) and the alternating word has \(r=2n\), forcing at least \((2n-2)/2=n-1\) relocations between them, even allowing both symbol types. This matches the upper bound and establishes \(\operatorname{diam}(R_n)=n-1\).

## Verification
The standalone Python files `verify_metric.py` and `verify_routes.py` use independent methods. Run `python verify_metric.py --max-n 7` to construct the two graphs by literal delete-and-insert operations, BFS every source, and compare every ordered pair with the gap formula and sharp diameter. Run `python verify_routes.py --max-n 7` to generate the explicit left-before-right transfer paths independently and check all intermediate gap inequalities for every ordered pair. The complete ordered-pair count across semilengths \(1\) through \(7\) is \(203455\) for each checker; the largest space has \(429\) Dyck words at \(n=7\). These finite checks corroborate, but do not replace, the preceding all-size proofs. Recorded outputs are in `metric_check.txt` and `route_check.txt`.

## Relationship to prior work
The Dyck word is a standard encoding of balanced-parenthesis expressions and rooted plane trees. Mütze's 2022 updated survey of Gray codes discusses Dyck words and several local transposition/shift orders. Vajnovszki and Wong's 2023/2024 work constructs greedy Gray codes under transpositions. Such Hamiltonian listing results do not give the all-pairs shortest relocation metric or the exact diameter for a move that may cross multiple unlike symbols. The result here concerns a distinct edge operation (delete one symbol and reinsert it), not adjacent swaps, and uses a prefix-feasible transport argument.

## Limitations
The exact all-pairs distance formula is proved only for opening-only relocations, not for relocations of either symbol. For the latter graph only connectivity and sharp diameter are established. No claim is made about its radius, eccentricities, number of antipodes, or multiplicities of optimal routes. Earlier equivalent formulations in edit-distance, lattice-path, or parenthesis-routing literature may exist; mathematical priority has not been independently established.

## References
- T. Mütze, *Combinatorial Gray codes—an updated survey* (first arXiv publication 2022-02-02), https://arxiv.org/abs/2202.01280 ; relevant Dyck-word Gray-code section: https://arxiv.org/html/2202.01280v4 .
- V. Vajnovszki and T. Wong, *Greedy Gray codes for Dyck words and ballot sequences*, COCOON 2023 proceedings, DOI: https://doi.org/10.1007/978-3-031-49193-1_3 ; author-hosted full text: https://v.vincent.u-bourgogne.fr/0ABS/0ART/greedy_dyck.pdf .
