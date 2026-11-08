# Exact static and online shattering ranks of cycle incidence in \(K_{3,b}\)

## Finding
For each integer \(b\ge3\), let \(G=K_{3,b}\) be the finite simple complete bipartite graph. Its edges are the query domain; the hypotheses are precisely the edge sets of *simple cycles*, with the membership predicate returning one on a queried edge when that edge belongs to the cycle. No empty-cycle hypothesis is adjoined. The following formulas are exact:

\[
\operatorname{VCdim}(\mathcal C_b)=\begin{cases}3,&b=3,\\4,&b\ge4,\end{cases}\qquad
\operatorname{Ldim}(\mathcal C_b)=\begin{cases}3,&b=3,\\5,&b\ge4.\end{cases}
\]

Thus the first nontrivial width increase from \(b=3\) to \(b=4\) creates a stable gap of one between adaptive and static shattering. The claim is restricted to the three-vertex left part; it does not determine dimensions for general \(K_{a,b}\).

## Assumptions and scope
The graph has left vertices \(u_0,u_1,u_2\), right vertices \(v_0,\ldots,v_{b-1}\), and all possible cross edges \(u_i v_j\). A simple cycle is a cyclic sequence of distinct vertices with consecutive vertices adjacent, modulo reversal and rotation. Since there are exactly three left vertices, every cycle has length four or six. A support \(S\) is VC-shattered when every labeling of \(S\) is realized by an edge set of a simple cycle. A complete online mistake tree of depth \(d\) is a full binary tree with \(d\) membership queries on each root-to-leaf path, such that for every leaf some cycle realizes its sequence of answers. The Littlestone dimension is the maximum such depth.

## Proof
**Static upper bound.** A shattered five-edge set must be contained in some cycle (realizing all five positive), necessarily a six-cycle. Label consecutive cycle vertices \(w_1,\ldots,w_6\) and edges \(e_i=w_iw_{i+1}\), indices modulo six. The support consists of all but one of these six edges. Rotate labels so the omitted edge is \(e_6\) and the support is the five-edge path \(e_1,\ldots,e_5\). Suppose a cycle contained \(e_1,e_3,e_4,e_5\) but omitted \(e_2\). These four edges involve all six vertices (two paths with respective endpoints \((w_1,w_2)\) and \((w_3,w_6)\)). A cycle containing them must use all three left vertices, so it has length six and cannot introduce another right vertex. It must join the two paths by two additional edges. One possible pairing uses \(w_2w_3=e_2\), forbidden. The other pairs \(w_1\) with \(w_3\) and \(w_2\) with \(w_6\), both same-side pairs, so neither is a graph edge. Thus this trace is impossible. Hence no five-element support is shattered, and the static dimension is at most four.

**Online upper bound.** A complete tree of depth six would have an all-positive path of six queries, witnessed by a simple cycle. The six queried edges must be distinct: repeating any edge on a path would make one of the two children of the repeated query unrealizable. Every cycle has at most six edges, so those six positive queries are exactly the edges of one six-cycle. Consider the final query along that path. The first five queried edges form a five-edge path in that cycle. Their six endpoints exhaust the three left vertices and three right vertices of any containing cycle. Therefore the only cycle containing the first five positive edges is the six-cycle itself, which necessarily contains the sixth edge. The sibling branch responding zero to the final query is impossible, contradicting the complete depth-six tree. Hence the online dimension is at most five.

**The \(b=3\) boundary.** The graph \(K_{3,3}\) has exactly nine four-cycles (choose two vertices on each side) and six six-cycles (Hamilton cycles of \(K_{3,3}\)), totaling fifteen distinct hypotheses. Thus neither VC nor online dimension can reach four: either notion at dimension four needs at least sixteen distinct hypotheses. The three edges \(u_0v_0,u_0v_1,u_1v_0\) form a shattered support; the executable finite checker independently enumerates the fifteen cycles and verifies all eight traces. Hence both dimensions equal three.

**Lower bounds for \(b\ge4\).** It suffices to work in the induced copy of \(K_{3,4}\), since every cycle there is also a cycle in \(K_{3,b}\) and the same query answers are retained. Consider the four edges \(u_1v_2,u_1v_3,u_2v_2,u_2v_3\) (in that order). The following finite table gives a cycle for each of the sixteen possible traces. Every two-digit token `ij` denotes the edge \(u_i v_j\). Commas separate the complete edge set of the witness cycle. The first column lists the four response bits in the given support order.

```
0000 : 00,01,10,11
0001 : 00,03,20,23
0010 : 00,02,20,22
0011 : 02,03,22,23
0100 : 00,03,10,13
0101 : 10,13,20,23
0110 : 02,03,10,13,20,22
0111 : 00,02,10,13,22,23
1000 : 00,02,10,12
1001 : 02,03,10,12,20,23
1010 : 10,12,20,22
1011 : 00,03,10,12,22,23
1100 : 02,03,12,13
1101 : 00,02,12,13,20,23
1110 : 00,03,12,13,20,22
1111 : 12,13,22,23
```

Every listed edge set is a simple four- or six-cycle in \(K_{3,4}\). Thus VC dimension is at least four. To prove the adaptive lower bound of five, the accompanying `cycle_witness.json` provides a *complete* binary query tree with 31 internal nodes and 32 leaves. Each internal node contains an edge index in the row-major enumeration \((u_0v_0,\ldots,u_0v_3,u_1v_0,\ldots,u_2v_3)\), and each leaf supplies a twelve-bit integer encoding the full edge set of a simple cycle. The standalone `verify_cycle.py`, using an independently implemented exhaustive cycle enumerator, proves by recursive inspection that every root-to-leaf trace is realized by its leaf witness, that no query repeats along a path, and that the certificate has all 32 leaves. This finite certificate is a complete combinatorial proof of the fixed \(K_{3,4}\) lower bound. It embeds in all larger \(b\). Together with the upper bound, this proves the asserted dimensions.

## Verification
Run `python verify_cycle.py cycle_witness.json` with Python 3 and its standard library. It independently enumerates all simple cycles of \(K_{3,3}\) and \(K_{3,4}\), checks the support traces, checks each depth-five certificate leaf and its complete answer history, and confirms that every four-edge support in \(K_{3,3}\) fails to be shattered. The deterministic successful output is `CYCLE_K3_B_SHATTERING_VERIFIED cycles3=15 cycles4=42 vc3=3 vc4=4 online_depth5_leaves=32 internal=31`. The upper bounds are proved above for unbounded \(b\); no extrapolation from finite trials is used.

## Relationship to prior work
Alireza Mofidi's 2022 investigations establish VC-theoretic general bounds for graph cycle hypergraphs, including the general circumference-based bound, and determine some other graph families such as wheels and friendship graphs. In \(K_{3,b}\), circumference is six, so a general at-most-five bound alone does not settle the sharp static dimension four. Neither examined paper supplies the simultaneous exact online and static formula with the \(b=3\) boundary. The finite-size upper bound on the online dimension here is a separate rigidity argument using the three-vertex bipartition. Classical VC definitions and online shattering are used unchanged; novelty is not claimed for these definitions or for basic counting of cycles. An unindexed or differently formulated earlier treatment may exist.

## Limitations
Only nonempty simple-cycle concepts are included, and all queries are edges, not vertices. The parameter \(b\) ranges over integers at least three; smaller \(b\), nonsimple cycles, cycle spaces closed under symmetric difference, and larger left bipartition sizes are outside scope. The online lower bound has a completely checkable finite certificate rather than a short symbolic decision tree. Scientific priority is only evaluated against accessible sources and records; independent audit has not been performed.

## References
[1] A. Mofidi, “On the Number of Cycles of Graphs and VC-Dimension,” *Facta Universitatis, Series: Mathematics and Informatics* 37(1), 121–135 (2022), DOI: 10.22190/FUMI210301011M, https://casopisi.junis.ni.ac.rs/index.php/FUMathInf/article/viewFile/7505/pdf.

[2] A. Mofidi, “On the VC-dimension, covering and separating properties of the cycle and spanning tree hypergraphs of graphs,” *Transactions on Combinatorics* 11(1), 29–43 (2022), DOI: 10.22108/toc.2021.127880.1832, https://toc.ui.ac.ir/article_25746_890e066e8b9dd269c189910e7e780475.pdf.
