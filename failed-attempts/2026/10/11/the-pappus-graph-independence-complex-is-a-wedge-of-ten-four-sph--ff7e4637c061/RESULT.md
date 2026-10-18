# The Pappus graph independence complex is a wedge of ten four-spheres
## Finding
Let \(P\) be the undirected eighteen-vertex Pappus graph and let \(\operatorname{Ind}(P)\) be its ordinary simplicial independence complex. There is an integral homotopy equivalence
\[
\operatorname{Ind}(P)\simeq\bigvee^{10}S^{4}.
\]
Thus, for every integer \(i\),
\[
\widetilde H_i(\operatorname{Ind}(P);\mathbb Z)\cong
\begin{cases}\mathbb Z^{10},&i=4,\\0,&i\ne4.\end{cases}
\]
The face vector in dimensions zero through eight is \((18,126,438,801,756,348,90,18,2)\). In particular, the complex is eight-dimensional even though its homotopy type is supported in dimension four.

## Assumptions and scope
All complexes are finite abstract simplicial complexes and homotopy equivalences concern their geometric realizations. Vertices of \(P\) are labeled by the integers \(0\) through \(17\). The LCF sequence is \([5,7,-7,7,-7,-5]^3\): include every cycle edge between successive residues modulo eighteen and, for each vertex, the chord specified by its corresponding LCF entry, ignoring duplicate undirected edges. This gives exactly twenty-seven edges, and each vertex has degree three.

An independent face is any set of graph vertices containing no complete graph edge. To independently identify the graph as the incidence graph of the classical Pappus configuration, use nine point vertices \(0\) through \(8\) and nine line vertices \(9\) through \(17\). The nine lines, in order, contain these point triples:

```
(0,1,2) (3,4,5) (0,4,6) (3,1,6) (0,5,7)
(3,2,7) (1,5,8) (4,2,8) (6,7,8)
```

An explicit map from the LCF vertex labels to these incidence labels, indexed by LCF vertex, is

```
[0,13,7,17,6,11,4,10,5,15,8,16,2,14,3,12,1,9]
```

The certificate verifies that this permutation maps all twenty-seven graph edges bijectively to the incidence edges. It prevents accidentally substituting the line graph, the nine-point collinearity graph or another graph sharing the name Pappus.

## Proof
**Exhaustive face construction.** For each integer bitmask from zero through \(2^{18}-1\), interpret its set bits as graph vertices and include the mask precisely when it contains no graph edge. This enumerates 2,598 faces including the empty face, hence 2,597 nonempty faces, in the dimensions and quantities stated above. The highest-dimensional faces have nine vertices.

**A finite acyclic discrete-Morse matching.** Start with the entire face set including the empty face. Visit the graph vertices in the order

```
[9,6,12,3,4,7,13,15,1,5,14,0,2,17,16,11,8,10]
```

At a visited vertex, simultaneously pair each still-active face not containing that vertex with its still-active one-vertex extension when the two are present; remove both from the active set. There are 1,294 disjoint pairs including one pair consisting of the empty face and a singleton. Omit that pair when passing to the ordinary nonaugmented face poset: one singleton becomes critical and the remaining 1,293 pairs form the ordinary matching. Its other ten critical faces have these bitmask identifiers:

```
[42113,73873,75040,83985,84004,147748,148516,149776,164996,166148]
```

Each has exactly five vertices, thus dimension four. There are no additional critical cells. The verifier constructs every cover relation among the 2,597 nonempty faces, orienting matched covers upward and unmatched covers downward. The resulting directed graph contains exactly 11,430 cover incidences. A complete topological sort removes all 2,597 vertices, establishing acyclicity of the entire matching, rather than just of a sample of gradient paths. The matching is therefore an acyclic discrete vector field in Forman's sense.

**Homotopy conclusion.** The discrete-Morse CW reduction has exactly one zero-cell and ten four-cells; it has no cells in dimensions one, two, three or above four. Consequently every four-cell is attached to the single zero-cell by the unique map from its attaching three-sphere. The CW complex is a wedge of ten four-spheres. This is a homotopy equivalence of the integral realizations, not merely an equality of field-homology ranks.

## Verification
Run `python3 verify_morse.py` and `python3 verify_independent.py` with Python 3.10 or later; both use the standard library only. The first script independently checks the LCF-to-incidence isomorphism, all faces, pairing cardinalities, exact critical masks and acyclicity on the complete ordinary Hasse diagram. The second reconstructs the graph directly from incidence triples and performs modular simplicial boundary eliminations over \(\mathbb F_2\) and \(\mathbb F_3\). For both fields, its boundary ranks from degrees one through eight are \((17,109,329,472,274,74,16,2)\), yielding ordinary Betti vector \((1,0,0,0,10,0,0,0,0)\). The face-vector alternating sum independently gives Euler characteristic eleven.

The modular calculations are cross-checks only: the proof of the integral homotopy type is the exhaustive acyclic matching and its critical-cell dimensions.

## Relationship to prior work
Barmak's theorem for triangle-free graphs implies that the independence complex of the Pappus graph is a suspension; it does not determine the number or dimensions of wedge summands. Tsukuda's incidence-graph theorem supplies another equivalence, via the suspension of the Alexander dual of the independence complex of the underlying incidence hypergraph. That equivalence does not evaluate the Pappus incidence configuration's dual complex, and in particular does not imply the numerical wedge decomposition without an additional calculation. The result here supplies that exact calculation by a finite certificate.

The Pappus graph is also studied through its ordinary matching complex, but a matching complex has graph edges as its vertices; it is not the independence complex considered here. A field-homology calculation for the matching complex therefore supplies no direct calculation of this graph-vertex independence-complex homotopy type.

## Limitations
This theorem concerns the explicitly specified Pappus graph and its ordinary independence complex. It does not assert a classification for all cubic incidence graphs or all \(9_3\) configurations. The verification enumerates every face of this particular finite complex; it is not a computational proof of an unbounded graph-family statement. Bibliographic search cannot eliminate the possibility of an equivalent calculation in unindexed literature.

## References
1. Jonathan Ariel Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (first public submission July 2, 2010), Theorem 3.4. https://arxiv.org/abs/1007.0418
2. Shuichi Tsukuda, *Independence complexes and incidence graphs*, *Contributions to Discrete Mathematics* 12 (2017), 28–46, especially Corollaries 4.11 and 5.3. https://doi.org/10.55016/ojs/cdm.v12i1.62277
3. Eric W. Weisstein, *Pappus Graph*, MathWorld, graph parameters and LCF representation. https://mathworld.wolfram.com/PappusGraph.html
