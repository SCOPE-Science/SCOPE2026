# First VC–Littlestone gap for domino tilings of two-row ladders and connected planar amplifiers

## Finding

Let \(L_n=P_2\square P_n\) be the two-row ladder with \(n\ge1\) columns. Write \(\mathcal P(G)\) for the Boolean concept class whose concepts are the **edge-incidence sets of perfect matchings** of a finite graph \(G\); the query domain is the entire edge set \(E(G)\). Let \(\operatorname{VC}\) and \(\operatorname{Ldim}\) denote the VC and Littlestone dimensions of this class.

**Theorem.** For \(1\le n\le5\), the exact triples \((|\mathcal P(L_n)|,\operatorname{VC}(\mathcal P(L_n)),\operatorname{Ldim}(\mathcal P(L_n)))\), in increasing order of \(n\), are
\[
(1,0,0),\quad(2,1,1),\quad(3,1,1),\quad(5,2,2),\quad(8,2,3).
\]
In particular, the five-column ladder is the first two-row ladder where static and adaptive edge-query shattering differ.

Moreover, for each integer \(s\ge1\), let \(G_s\) consist of \(s\) disjoint copies of \(L_5\) arranged in a chain, with one bridge joining the upper-right corner of copy \(j\) to the upper-left corner of copy \(j+1\) for every \(1\le j<s\). Then \(G_s\) is a connected planar bipartite graph of maximum degree three, has \(10s\) vertices, and satisfies
\[
|\mathcal P(G_s)|=8^s,\qquad
\operatorname{VC}(\mathcal P(G_s))=2s,\qquad
\operatorname{Ldim}(\mathcal P(G_s))=3s.
\]
Thus the VC–Littlestone gap is unbounded among **perfect-matching incidence concept classes of connected planar subcubic bipartite graphs**.

## Assumptions and scope

Graphs are finite, undirected, loopless and unweighted. A perfect matching covers every vertex exactly once. An edge-membership query returns one precisely when that edge is selected. Each horizontal ladder domino occupies one edge in each row, whereas a vertical domino occupies one rung. The finite sharp-onset statement concerns the ladders \(L_1,\ldots,L_5\), and the infinite-family statement concerns exactly the graphs \(G_s\) defined above.

Name the vertical rung in column \(i\) by \(V_i\); name the top and bottom horizontal edges across columns \(i,i+1\) by \(T_i\) and \(B_i\). In every perfect matching \(T_i\) and \(B_i\) occur together, so writing \(H_i\) for their paired occurrence causes no loss of tiling information. There is a bijection from perfect matchings of \(L_n\) to monomer–dimer tilings of an interval of length \(n\): a rung \(V_i\) covers one column and a horizontal pair \(H_i\) covers two consecutive columns. This bijection also proves \(a_n=a_{n-1}+a_{n-2}\) for the number of matchings, with \(a_0=a_1=1\).

## Proof

**1. The initial ladder orders.** The recurrence gives \(a_1=1,a_2=2,a_3=3,a_4=5,a_5=8\). For every nonempty finite concept class, a complete shattered binary tree of depth \(d\) needs at least \(2^d\) *distinct* concepts. Hence the upper bounds on Littlestone dimensions for these orders are \(0,1,1,2,3\), respectively. For \(n=2,3\), a nonconstant edge query proves dimension at least one. For \(n=4\), the two edge queries \(T_1,T_3\) are VC-shattered: their four assignments are realized by the tilings \(H_1H_3\), \(H_1V_3V_4\), \(V_1V_2H_3\), and \(V_1V_2V_3V_4\). Thus both dimensions equal two at \(n=4\).

**2. Static shattering in \(L_5\).** The eight matchings, in a fixed order used by `certificate.json`, are
\[
\begin{array}{llll}
1:V_1V_2V_3V_4V_5,&2:V_1V_2V_3H_4,&3:V_1V_2H_3V_5,&4:V_1H_2V_4V_5,\\
5:V_1H_2H_4,&6:H_1V_3V_4V_5,&7:H_1V_3H_4,&8:H_1H_3V_5.
\end{array}
\]
Each shorthand \(H_i\) stands for both \(T_i\) and \(B_i\). The numbers of these eight matchings containing \(V_1,\ldots,V_5\) are respectively \((5,3,4,3,5)\), and those containing either horizontal edge at each position \(1,\ldots,4\) are \((3,2,2,3)\). Thus **only** the query \(V_3\) occurs in exactly four matchings. If three distinct edge queries were VC-shattered, all eight binary patterns would be realized by exactly eight concepts, so each chosen query would have to be true in exactly four concepts. Three such queries do not exist. Therefore \(\operatorname{VC}(\mathcal P(L_5))\le2\). The queries \(T_1,T_4\) realize all four label pairs (as seen in matchings \(7\), \(6\), \(2\), and \(1\)), giving the matching lower bound.

**3. Adaptive shattering in \(L_5\).** The following complete decision tree has depth three. Query \(V_3\) at the root. If the answer is zero, query \(T_2\), then query \(V_1\) when the second answer is zero and \(V_4\) otherwise. If the root answer is one, query \(V_1\), then query \(V_4\) regardless of the second answer. For a three-bit answer path, read bits from root to leaf; the corresponding matching indices from the list above are
\[
000\mapsto8,\quad001\mapsto3,\quad010\mapsto5,\quad011\mapsto4,\quad
100\mapsto7,\quad101\mapsto6,\quad110\mapsto2,\quad111\mapsto1.
\]
Every path is realized, and the eight paths have distinct witnesses. Hence \(\operatorname{Ldim}\ge3\); the eight-concept cardinality bound gives \(\operatorname{Ldim}=3\). Combined with step 2 and the initial orders, this proves the first-gap assertion.

**4. Connected amplification.** Every bridge \(e\) of \(G_s\) separates its vertices into two sets each having a multiple of ten vertices. Any perfect matching crosses an even-cardinality vertex cut in an even number of edges, since the vertices on one side not incident with cut edges must be paired internally. The cut here contains only \(e\), so no perfect matching can contain \(e\). Consequently, choosing a perfect matching of \(G_s\) is exactly the same as choosing independently one perfect matching in each copy of \(L_5\); there are \(8^s\) choices.

For a VC-shattered subset of graph edges, its restriction to each block's edge set must be VC-shattered by that block's perfect-matching class, while no bridge can be selected because every bridge query is constant zero. Therefore its cardinality is at most \(2s\). Conversely, taking \(T_1,T_4\) in each block gives a shattered set of \(2s\) edges through independent choices of tilings. Thus \(\operatorname{VC}=2s\). To obtain a complete depth-\(3s\) online tree, apply the depth-three tree in step 3 to block 1, then to block 2 at every leaf, and so forth. Every complete answer path has a compatible product matching. The count \(|\mathcal P(G_s)|=8^s=2^{3s}\) gives the matching upper bound \(\operatorname{Ldim}\le3s\). A row-wise planar embedding, proper two-colouring by successive blocks, and the fact that bridges attach only at degree-two corners establish planarity, bipartiteness, and maximum degree three.

**5. Why the query domain matters.** For arbitrary \(n\ge1\), the horizontal-pair indicators \((H_1,\ldots,H_{n-1})\) range over all binary strings with no adjacent ones, equivalently all independent sets of a path on \(n-1\) vertices. For the concept class using *only* these horizontal queries, VC and Littlestone dimensions both equal \(\lfloor n/2\rfloor\): choose a maximum independent set and all its subsets for the lower bound; for any shattered adaptive tree, its all-one branch consists of distinct queried elements and must be an independent set, giving the upper bound. The full edge-query class includes additional derived rung tests
\[
\mathbf 1[V_i\in M]=\mathbf1[H_{i-1}\notin M\ \text{and}\ H_i\notin M],
\]
where nonexistent endpoint pairs are always absent. At \(n=5\), these redundant local NOR features preserve VC dimension two but increase the adaptive dimension from two to three. This explains why a hypercube code for a resonance graph does not by itself determine the dimension under *physical edge queries*.

## Verification

The self-contained `verify.py` uses two enumeration methods: a one-dimensional monomer–dimer recursion and independent graph-vertex perfect-matching backtracking. It checks equality of the resulting complete families for \(1\le n\le5\), exhaustively computes both dimensions through the usual finite shattered-tree recurrence, checks every leaf of the supplied depth-three certificate, and confirms the balancing obstruction to VC dimension three. It additionally generates \(G_s\) for \(s=1,2,3\), confirming \(8^s\) matchings, bridge exclusion, bipartiteness, and maximum degree three by direct graph enumeration.

Run `python3 verify.py` beside `certificate.json`. The supplied `verification_output.txt` contains a recorded successful invocation ending in `ALL_MATCHING_SHATTERING_CHECKS_PASS`. These finite tests corroborate the proof; the statements for arbitrary positive \(s\) are established by the bridge-parity and independent-block arguments, not by extrapolating finite results.

## Relationship to prior work

Manurangsi and Rubinstein study general complexity and definitions of VC and Littlestone dimensions, rather than perfect-matching incidence classes. Oh develops exact monomer–dimer and domino-tiling enumeration via state matrices, without static/adaptive edge-query shattering results. Brezovnik, Tratnik and Žigert Pleteršek derive binary codings and resonance-graph structure for outerplane bipartite graphs; these are codings of matchings under a different query coordinate system, not formulas for the dimensions of the original edge-incidence class. Che relates cube-free resonance graphs to Clar number but does not, in the accessible abstract, establish the adaptive claim. The local NOR-coordinate phenomenon and the connected exact-amplification result are not formal corollaries of these inspected statements. No exhaustive priority assertion is made.

## Limitations

The complete classification of full edge-query dimensions is proved only for ladders through five columns; it is not a formula for all larger ladders. The constructed connected graphs have bridges unused by every perfect matching, so the theorem does not establish an unbounded gap for two-edge-connected, matching-covered, or cubic graphs. The finite verifier is not a proof of any unbounded claim. Independent external validation and an exhaustive historical literature census have not been performed.

## References

1. P. Manurangsi and A. Rubinstein, *Inapproximability of VC Dimension and Littlestone's Dimension*, arXiv:1705.09517v1 (first submitted 26 May 2017), https://arxiv.org/abs/1705.09517 .
2. S. Oh, *State matrix recursion method and monomer–dimer problem*, arXiv:1901.07847v1 (first submitted 23 January 2019), https://arxiv.org/abs/1901.07847 .
3. S. Brezovnik, N. Tratnik and P. Žigert Pleteršek, *Resonance Graphs and a Binary Coding of Perfect Matchings of Outerplane Bipartite Graphs*, MATCH Commun. Math. Comput. Chem. 90 (2023), 453–468, https://doi.org/10.46793/match.90-2.453B .
4. Z. Che, *Cube-free resonance graphs*, Discrete Applied Mathematics 284 (2020), 262–268, https://doi.org/10.1016/j.dam.2020.03.036 (abstract inspected only).
