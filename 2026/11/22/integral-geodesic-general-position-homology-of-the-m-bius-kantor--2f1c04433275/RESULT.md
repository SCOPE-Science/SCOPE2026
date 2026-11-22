# Integral geodesic general-position homology of the Möbius–Kantor graph

## Finding

Let \(M=\operatorname{GP}(8,3)\) be the Möbius–Kantor graph, and let \(\mathcal G(M)\) be the simplicial complex of its geodesic general-position vertex sets. Its complete reduced integral homology is

\[
\widetilde H_j(|\mathcal G(M)|;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{24},&j=1,\\
\mathbb Z^{4},&j=2,\\
\mathbb Z,&j=3,\\
0,&\text{otherwise}.
\end{cases}
\]

In particular the integral homology is torsion-free, and this natural complex has nontrivial homology in three distinct positive dimensions. This is a **homology calculation**, not a claimed wedge-of-spheres homotopy classification.

## Assumptions and scope

The graph is the simple connected cubic graph with vertices \(u_i,v_i\), \(i\in\mathbb Z/8\mathbb Z\), and edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\). Indices are reduced modulo eight; these specify exactly 24 undirected edges. Set the vertex order to \(u_0,\ldots,u_7,v_0,\ldots,v_7\). Distances are ordinary unweighted shortest-path distances. A face of \(\mathcal G(M)\) is a subset \(S\) such that for all *distinct* \(a,b,c\in S\), none of the equations \(d(a,b)+d(b,c)=d(a,c)\) and its two permutations holds. The empty set is included as usual. All homology is simplicial homology with integer coefficients and the standard increasing-vertex orientation.

## Proof

A completely finite, exhaustive calculation gives the following reproducible certificate.

1. Breadth-first distances from every vertex and independent Floyd–Warshall distances agree. Applying the stated betweenness criterion to all \(\binom{16}{3}=560\) triples yields exactly 336 forbidden triples. Testing all \(2^{16}=65,536\) vertex subsets against these triples gives the face vector \((f_0,f_1,f_2,f_3,f_4)=(16,120,224,220,80)\), with no higher-dimensional faces. An independent facewise test repeats the distance criterion for every generated face.
2. The file `collapses.json` lists exactly 227 ordered pairs of face bitmasks. `check.py` replays every pair, verifies that its first face has the second as its *unique* remaining codimension-one coface, and deletes the pair. Thus each is a genuine elementary simplicial collapse. The pairs comprise 35 edge–triangle, 112 triangle–tetrahedron, and 80 tetrahedron–four-simplex collapses. The resulting subcomplex has face vector \((16,85,77,28)\) in dimensions zero through three.
3. On this remaining simplicial complex, form the oriented signed integer boundary matrices \(\partial_1\), \(\partial_2\), \(\partial_3\), of sizes \(16\times85\), \(85\times77\), and \(77\times28\). Their compositions are zero. Exact integral elementary row and column operations, choosing only pivots equal to \(\pm1\), reduce these matrices respectively to \(\operatorname{diag}(I_{15},0)\), \(\operatorname{diag}(I_{46},0)\), and \(\operatorname{diag}(I_{27},0)\). Since every operation is unimodular, **all nonzero Smith factors are one**, not merely nonzero modulo a selected prime.
4. The ranks in reduced positive homology therefore are \(85-15-46=24\), \(77-46-27=4\), and \(28-27=1\). Connectivity follows from \(\operatorname{rank}\partial_1=15\) on 16 vertices. Unimodular Smith forms prove no homology torsion in any dimension; the absence of cells above dimension three proves all other groups vanish. As a check, \(16-120+224-220+80=-20=1-24+4-1\).

The unimodular unit-pivot procedure is stronger than rational or mod-two rank computation. No theorem about unspecified larger graphs or an infinite family is inferred.

## Verification

The adjacent standalone files `check.py` and `collapses.json` constitute the full reproducibility package. With ordinary Python 3.9 or later, run `python check.py` from any directory after extracting the files together. The verifier uses only the standard library. It reconstructs the graph, compares two shortest-path methods, enumerates every candidate face, independently tests all included triples, replays and validates every listed collapse, checks chain-complex identities, and runs a completely integral unit-pivot reduction. Expected final reduced ranks in degrees zero through three are \((0,24,4,1)\). No computational experiment is used to assert an infinite generalization.

## Relationship to prior work

Manuel and Klavžar (2017) introduce the graph-geodesic general-position framework and compute maximum cardinalities on interconnection networks. Iršič, Klavžar, Rus, and Tuite (2024) study its counting polynomial, including Petersen and other graph families. Those counting results do not imply the present chain-boundary or homology groups, and the inspected papers do not compute this complex on \(\operatorname{GP}(8,3)\). The same graph has a different **two-independence** complex (whose faces forbid induced three-vertex paths rather than every geodesic triple); the triple \(\{u_0,u_1,u_3\}\) lies in that larger complex but not in \(\mathcal G(M)\). Consequently, homology calculations of the two-independence, matching, Rips, and neighborhood complexes of this graph do not determine the result here. A literature search did not identify a dominating geodesic-general-position homology theorem for this object.

## Limitations

The conclusion gives integral homology groups only. It does not determine attaching maps, the homotopy type, a complete automorphism representation, or all generalized Petersen graphs. Previously unpublished or unindexed equivalent calculations may exist. The full accessible texts of three nearest indexed mathematical results were compared, but other unindexed or inaccessible equivalent work remains a residual originality risk; no search can establish absolute novelty.

## References

1. P. Manuel and S. Klavžar, *The graph theory general position problem on some interconnection networks*, arXiv:1710.00244, first posted 2017-09-30. https://arxiv.org/html/1710.00244v1
2. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General position polynomials*, arXiv:2401.05696, first posted 2024-01-11. https://arxiv.org/html/2401.05696v1
3. E. W. Weisstein, *Möbius–Kantor Graph*, MathWorld, https://mathworld.wolfram.com/Moebius-KantorGraph.html (graph identification and standard presentation).
