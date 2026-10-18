# The Petersen matching complex is \(\bigvee^{5}S^2\vee\bigvee^{5}S^3\)
## Finding
Let \(P\) be the Petersen graph, realized on vertices \(0,\ldots,9\) as an outer pentagon, five spokes, and an inner pentagram. Its ordinary matching complex \(\operatorname{Match}(P)\) is the simplicial complex whose vertices are the fifteen edges of \(P\), with a face for every nonempty matching. Then
\[
\operatorname{Match}(P)\simeq \bigvee^{5}S^2\vee\bigvee^{5}S^3.
\]

## Assumptions and scope
The assertion concerns the ordinary matching complex: each graph vertex is incident to at most one selected edge. It does not concern a generalized \(r\)-matching complex, a Morse complex, or a perfect-matching complex. The graph model is the standard Petersen graph with outer edges \(\{i,i+1\}\) modulo five, spokes \(\{i,5+i\}\), and inner pentagram edges \(\{5+i,5+i+2\}\) modulo five.

## Proof
Order the fifteen graph edges, after lexicographic sorting, by the index sequence
`[2,3,8,13,11,12,14,6,1,0,10,7,5,4,9]`.
Starting with every nonempty face of \(\operatorname{Match}(P)\), process these edge indices in order. At a stage, pair each still-unmatched face \(\sigma\) not containing the chosen edge with \(\sigma\cup\{e\}\) whenever the latter is still present. This gives 160 face-coface pairs.

The directed Hasse diagram obtained by orienting every unmatched cover downward and every matched cover upward is acyclic. Hence Forman's discrete Morse theorem reduces the complex to a CW complex with one cell for each critical face. The critical-cell inventory is exactly one cell in dimension \(0\), five cells in dimension \(2\), and five cells in dimension \(3\). Thus the Morse \(2\)-skeleton is \(\bigvee^5S^2\).

To determine the five attaching maps in dimension \(3\), orient every simplex by increasing edge index and perform exact integral gradient-path cancellation. The resulting Morse boundary matrix from critical \(3\)-cells to critical \(2\)-cells is the zero \(5\times5\) matrix. Since \(\bigvee^5S^2\) is simply connected, Hurewicz identifies \(\pi_2(\bigvee^5S^2)\) with \(H_2(\bigvee^5S^2;\mathbb Z)\cong\mathbb Z^5\); the coordinate degrees of an attaching map are exactly its cellular boundary coefficients. All five attaching maps are therefore null-homotopic. Attaching five \(3\)-cells trivially yields
\[
\bigvee^5S^2\vee\bigvee^5S^3.
\]

## Verification
`verify.py` reconstructs the graph and all matching faces from first principles. It verifies 331 nonempty faces with face vector
\[
(15,75,145,90,6),
\]
all 975 nonempty-face Hasse covers, the 160 matching pairs, acyclicity, and the critical-cell counts. It then independently computes the full simplicial boundary ranks over \(\mathbf F_2\) as \(14,61,79,6\), giving reduced Betti ranks \(5\) in dimensions \(2\) and \(3\) and zero otherwise. Finally it performs exact signed integral gradient-path elimination and verifies that the Morse boundary \(C_3^{\mathrm{Morse}}\to C_2^{\mathrm{Morse}}\) is identically zero. Running `python verify.py` reproduces the certificate and ends with `VERIFY_OK`.

## Relationship to prior work
Donovan and Scoville develop star-cluster methods for matching, Morse, and generalized Morse complexes, and compute ordinary matching complexes for several graph families such as paths, cycles, and Dutch windmills; their full text does not contain a Petersen-graph ordinary matching-complex computation. Jelić Milutinović, Jenne, McDonough, and Vega emphasize that exact topology of matching complexes is known for comparatively few graph families and study trees and polygonal-line tilings; the identity \(\operatorname{Match}(G)=\operatorname{Ind}(L(G))\) was also checked as an equivalent formulation. Barmak's claw-free independence-complex theorem applies to line graphs and gives connectivity information, but it does not determine this exact mixed-dimensional wedge. Searches for the Petersen graph under both matching-complex and line-graph independence-complex terminology found no published statement implying the claimed homotopy type. A published-index search did locate a Petersen \(2\)-matching-complex result, but that is a different complex and does not imply the ordinary matching-complex statement.

## Limitations
The claim is only about the ordinary matching complex of the Petersen graph. It does not classify ordinary matching complexes of all generalized Petersen graphs, and it does not assert a general formula for cubic graphs. The finite computation is exhaustive for this single complex; it is not evidence for an infinite-family statement. Literature searches cannot rule out every unindexed or differently phrased prior computation, so an ordinary residual originality risk remains despite the equivalent-formulation and broader-coverage checks.

## References
1. Donovan, M.; Scoville, N. *Star clusters in the Matching, Morse, and Generalized Morse complex*. arXiv:2207.13780, first posted 2022-07-27. Primary MSC 57Q70.
2. Jelić Milutinović, S.; Jenne, E.; McDonough, A.; Vega, J. *Matching complexes of trees and applications of the nerve theorem*. arXiv:1905.10560, first posted 2019-05-25.
3. Barmak, J. A. *Star clusters in independence complexes of graphs*. arXiv:1007.0418; *Advances in Mathematics* 241 (2013), 33–57.
