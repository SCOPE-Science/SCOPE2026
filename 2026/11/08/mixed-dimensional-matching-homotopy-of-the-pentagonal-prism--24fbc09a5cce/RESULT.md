# Mixed-dimensional matching homotopy of the pentagonal prism

## Finding
For the pentagonal-prism graph \(G=C_5\square K_2\), the ordinary matching complex satisfies the **integral homotopy equivalence**
\[
\mathcal M(G)\simeq S^2\vee S^2\vee S^3\vee S^3.
\]
Thus \(\widetilde H_2(\mathcal M(G);\mathbb Z)\cong\mathbb Z^2\), \(\widetilde H_3(\mathcal M(G);\mathbb Z)\cong\mathbb Z^2\), and all other reduced integral homology groups vanish. This is an exact computation for a natural circular-ladder graph, not a claim for every ladder width.

## Assumptions and scope
The graph is the finite simple Cartesian product of a five-cycle and a two-vertex path. Its ten vertices are \((i,j)\), where \(i\in\mathbb Z/5\mathbb Z\) and \(j\in\{0,1\}\); its fifteen edges are the ten rim edges \(\{(i,j),(i+1,j)\}\) and the five spokes \(\{(i,0),(i,1)\}\). Index these edges by \(e_{2i+j}=\{(i,j),(i+1,j)\}\) for \(0\le i\le4\), \(j\in\{0,1\}\), and \(e_{10+i}=\{(i,0),(i,1)\}\) for \(0\le i\le4\). The ordinary matching complex consists of **all** pairwise vertex-disjoint edge subsets, including those not extendable to a perfect matching; its abstract simplex vertices are the fifteen graph edges. This is not the perfect matching complex.

## Proof
**1. Complete face model.** Represent an edge set by a 15-bit nonnegative integer. It is a face precisely when no two selected graph edges share an endpoint. Exhaustive iteration over the \(2^{15}\) bitmasks gives \(342\) faces including the empty face. The nonempty face vector, by increasing simplex dimension, is \((15,75,145,95,11)\). The face poset has \(341\) nonempty elements and \(1020\) cover incidences. These enumerations are independently reconstructible from the explicit graph definition in `verify.py`.

**2. Complete acyclic matching.** On nonempty faces, process the edge indices in the fixed order `7,12,3,9,1,4,8,2,11,6,5,13,10,14,0`. At each index, pair every as-yet-unmatched face missing that index with its coface obtained by adding the index, when both are still unmatched. This constructs \(168\) distinct codimension-one pairs. Precisely five critical cells remain: one zero-cell, two two-cells and two three-cells. Reverse the \(168\) matched arrows in the directed Hasse diagram, orienting every other cover arrow toward the lower-dimensional face. An exhaustive topological sort visits all \(341\) vertices, proving the directed diagram is acyclic. Hence this is a valid discrete-Morse matching on the **entire** finite complex, not merely on sampled faces.

**3. Signed integral Morse differential.** Orient every simplex by ascending edge index. For a critical simplex \(c\), compute its cellular Morse boundary by expanding the signed simplicial boundary and recursively eliminating the matched lower members \(a\) using their matched upper members \(b\). In this elimination, the coefficient \([a:\partial b]\) is always \(+1\) or \(-1\); thus the elimination is over \(\mathbb Z\), without division by a nonunit. For each matched pair, the chain projection satisfies
\[
P(a)=-[a:\partial b]\sum_{f\ne a}[f:\partial b]P(f),
\]
where critical simplices project to their own generators and matched upper simplices project to zero. Acyclicity guarantees the recursion terminates. Substitution for the two critical three-cells produces the **zero** \(2\times2\) integer boundary matrix to the two critical two-cells. There are no critical one-cells; boundaries of two-cells are necessarily zero. The executable certificate computes all incidences and signed coefficients directly and checks these conclusions exactly.

**4. Homotopy conclusion.** The resulting finite CW complex has one zero-cell, no one-cells, two two-cells, and two three-cells. Its two-skeleton is \(S^2\vee S^2\), which is simply connected. By the Hurewicz isomorphism \(\pi_2(S^2\vee S^2)\cong H_2(S^2\vee S^2;\mathbb Z)\), the zero integral attaching-degree columns mean that both three-cell attaching maps are nullhomotopic. Attaching the two three-cells therefore adds two wedge summands \(S^3\), yielding the claimed homotopy equivalence. No unresolved higher attaching maps remain because the Morse CW model has no cells above dimension three.

## Verification
Run the standard-library-only script `verify.py` with Python 3. The script independently enumerates all matchings, verifies the five-dimensional face vector and the complete Hasse graph, tests the proposed acyclic matching, computes all signed integral Morse differentials, and also calculates the original simplicial reduced homology over three prime fields. The recorded output is in `verification_results.txt`; successful execution ends with `ALL_VERIFY_OK`. The finite checker is exhaustive for the **specified ten-vertex graph**. It is not an extrapolation to an infinite graph family.

## Relationship to prior work
Agarwal and Basak's revised 2026 work, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs* (arXiv:2608.30601v2), establishes a classification for **independence complexes and perfect matching complexes**. Its Theorem 25 makes the pentagonal prism's perfect matching complex contractible; its Problem 26 explicitly proposes studying the **ordinary matching complex** of circular ladders as future work. The present result shows a different, mixed-dimensional homotopy type for the ordinary matching complex of this same graph. Bayer, Jelić Milutinović and Vega's outerplanar-graph theorem does not cover this cubic graph: every nonempty outerplanar graph has a vertex of degree at most two, whereas every vertex here has degree three. Their polygonal-line tilings concern linearly attached polygon systems rather than the closed circular ladder. Matching complexes of rectangular grids concern different boundary conditions. These literature distinctions concern mathematical scope; they are not assertions of absolute publication priority.

## Limitations
The calculation is restricted to the graph \(C_5\square K_2\). It gives no uniform formula for all \(C_n\square K_2\), no integral equivariant decomposition, and no independent validation. Exact computational verification supplements the explicit finite discrete-Morse proof. Search-based priority assessment cannot exclude all unindexed results.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2 (revised 14 September 2026), especially Theorem 25 and Problem 26. https://arxiv.org/abs/2608.30601
2. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601 (2024; updated 2026). https://arxiv.org/abs/2411.04601
3. M. Bayer, M. Jelić Milutinović and J. Vega, *General polygonal line tilings and their matching complexes*, arXiv:2211.12559 (2022). https://arxiv.org/abs/2211.12559
4. P. Chauhan, A. Sharma and S. Shukla, *Homology of matching complexes of three-by-n grid graphs*, arXiv:2609.27366 (2026). https://arxiv.org/abs/2609.27366
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
