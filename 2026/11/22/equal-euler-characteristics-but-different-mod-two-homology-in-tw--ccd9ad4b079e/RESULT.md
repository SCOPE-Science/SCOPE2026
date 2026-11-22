# Equal Euler characteristics but different mod-two homology in two Petersen-cover general-position complexes

## Finding
For a finite graph \(G\), write \(\mathrm{GP}(G)\) for the simplicial complex of vertex subsets containing no three distinct vertices on a common shortest path in \(G\). Let \(D=G(10,2)\) be the dodecahedral graph and \(H=G(10,3)\) the Desargues graph, with the generalized Petersen convention specified below. Their reduced simplicial homology over \(\mathbb F_2\) is
\[
\widetilde H_i(\mathrm{GP}(D);\mathbb F_2)\cong
\begin{cases}
\mathbb F_2^{10},&i=1,\\
\mathbb F_2^{60},&i=2,\\
\mathbb F_2^{111},&i=3,\\
0,&\text{otherwise},
\end{cases}
\]
and
\[
\widetilde H_i(\mathrm{GP}(H);\mathbb F_2)\cong
\begin{cases}
\mathbb F_2^{40},&i=1,\\
\mathbb F_2^{21},&i=3,\\
0,&\text{otherwise}.
\end{cases}
\]
Both complexes have exactly sixty four-dimensional simplices, the same 20 vertices and 190 edges, and Euler characteristic \(-60\). Nevertheless their reduced mod-two homology is different, in particular in degree two. They cannot be homotopy equivalent.

## Assumptions and scope
For \(k\in\{2,3\}\), the graph \(G(10,k)\) has vertices \(u_i,v_i\), with \(i\in\mathbb Z/10\mathbb Z\), and precisely the three types of edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+k}\). Edges are unoriented and all have unit length. Thus both graphs have twenty vertices and thirty edges. For an unordered triple \(\{a,b,c\}\), the three vertices lie on a common geodesic if and only if at least one of
\[
d(a,c)=d(a,b)+d(b,c),\quad
 d(a,b)=d(a,c)+d(c,b),\quad
 d(b,c)=d(b,a)+d(a,c)
\]
holds, where \(d\) is the all-pairs shortest-path distance. A face is a vertex subset containing no such triple. Homology is **only** asserted with \(\mathbb F_2\) coefficients; neither integral homology nor a homotopy wedge decomposition is claimed.

Both graphs are two-sheeted covers of the Petersen graph \(G(5,2)\): the free involution \(u_i\mapsto u_{i+5}\), \(v_i\mapsto v_{i+5}\) is a graph automorphism, and the quotient has outer and inner five-cycles joined by five spokes (the inner step \(3\) becomes \(-2\) modulo five). This common covering geometry motivates the comparison.

## Proof
**Minimal nonfaces.** All-pairs shortest-path distances computed from the displayed thirty-edge graph give exactly \(540\) bad unordered triples for \(G(10,2)\) and \(720\) for \(G(10,3)\). These are precisely the minimal nonfaces of cardinality three: every singleton and pair is a face, and any larger nonface contains a bad triple by definition. Exhaustive increasing-order face generation, rejecting a newly added vertex whenever it completes one of these triples, therefore generates *every* simplex exactly once.

**Face enumeration.** The complete face vectors, indexed by simplex dimension zero through four, are
\[
\begin{array}{c|rrrrr}
& f_0&f_1&f_2&f_3&f_4\\\hline
G(10,2)&20&190&600&550&60\\
G(10,3)&20&190&420&370&60.
\end{array}
\]
No faces of higher dimension occur; these are complete finite enumerations, not sampled distributions. Both alternating sums equal \(-60\).

**Exact boundary ranks.** Form the mod-two boundary map \(\partial_d:C_d\to C_{d-1}\) by sending every \(d\)-simplex to the sum, over \(\mathbb F_2\), of its \(d+1\) codimension-one faces. Exact XOR Gaussian elimination gives the boundary ranks
\[
\begin{array}{c|rrrr}
&\operatorname{rank}\partial_1&\operatorname{rank}\partial_2&\operatorname{rank}\partial_3&\operatorname{rank}\partial_4\\\hline
G(10,2)&19&161&379&60\\
G(10,3)&19&131&289&60.
\end{array}
\]
Here \(\partial_0=\partial_5=0\). Since \(\partial_{d-1}\partial_d=0\), the dimension of degree-\(d\) homology is \(f_d-\operatorname{rank}\partial_d-\operatorname{rank}\partial_{d+1}\), and the reduced degree-zero dimension is \(f_0-\operatorname{rank}\partial_1-1=0\). Substituting both face vectors and boundary ranks gives exactly the groups in the Finding. The dimension-five and higher groups vanish because there are no such simplices.

In particular the degree-two ranks are \(600-161-379=60\) and \(420-131-289=0\). This difference proves non-homotopy-equivalence independently of the equal Euler characteristics.

## Verification
The accompanying `verify_gp_covers.py` is a Python 3 standard-library-only, standalone verifier. Run `python3 verify_gp_covers.py` from the directory containing the file. It reconstructs both edge sets; independently computes distance matrices using breadth-first search and Floyd–Warshall; enumerates all 1,140 vertex triples; builds every permissible face with increasing-label recursion; checks all listed faces against forbidden triples and face closure; verifies every composition \(\partial_{d-1}\partial_d=0\); and calculates each boundary rank twice using column-oriented and row-oriented binary elimination. It also checks the fixed-point-free five-step involution and both Euler identities.

The expected deterministic output is:
```
GP(10,2): bad=540; f=[20, 190, 600, 550, 60]; rank_boundary_1_to_4=[19, 161, 379, 60]; reduced_F2_betti=[0, 10, 60, 111, 0]; chi=-60; checks=PASS
GP(10,3): bad=720; f=[20, 190, 420, 370, 60]; rank_boundary_1_to_4=[19, 131, 289, 60]; reduced_F2_betti=[0, 40, 0, 21, 0]; chi=-60; checks=PASS
ALL CHECKS PASS
```
All computations are finite, exact integer/bit operations. The preceding graph definitions and algorithm specify the complete reproducible proof certificate.

## Relationship to prior work
Manuel and Klavžar introduced the geodesic general-position set problem in 2017. Their work defines the admissible triples and studies maximal cardinalities, rather than the mod-two homology of the two complexes above. Iršič, Klavžar, Rus and Tuite subsequently introduced general-position polynomials, which count admissible subsets by size; their paper treats the Petersen graph but not the two twenty-vertex covering graphs' homology. The standard identification of \(G(10,2)\) and \(G(10,3)\) with the dodecahedral and Desargues graphs is also described in the literature on generalized Petersen graph symmetries.

Published results on independence, matching, dominance, neighborhood and higher-independence complexes of these two graphs concern different face conditions and therefore cannot determine the present boundary ranks. The above statements are about actual graph-geodesic general-position complexes, not the ordinary independence complexes.

## Limitations
This is a finite, fully specified classification of reduced homology over \(\mathbb F_2\) for two graphs. Equality of Euler characteristic neither implies equality of their integral homology nor their mod-two Betti signatures, and no integral torsion, homotopy type, all-cover formula, or broader generalized Petersen classification is claimed. Literature searches are not a proof of global novelty; a bibliographic equivalent outside inspected sources remains possible.

## References
1. P. Manuel and S. Klavžar, *Graph theory general position problem*, arXiv:1708.09130v1 (first submitted 2017-08-30), https://arxiv.org/html/1708.09130v1.
2. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General Position Polynomials*, arXiv:2401.05696v1 (2024-01-11), https://arxiv.org/html/2401.05696v1.
3. *Beyond symmetry in generalized Petersen graphs*, Journal of Algebraic Combinatorics, https://link.springer.com/article/10.1007/s10801-023-01282-y (graph-identification background only).
