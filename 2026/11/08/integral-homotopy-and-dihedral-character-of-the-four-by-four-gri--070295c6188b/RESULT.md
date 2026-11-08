# Integral homotopy and dihedral character of the four-by-four grid total four-cut complex

## Finding
Let \(G=P_4\square P_4\) be the ordinary sixteen-vertex square grid. Its total four-cut complex, defined below, has the **integral homotopy type**
\[
|\Delta^t_4(G)|\simeq\bigvee^{84}S^8.
\]
The natural dihedral action on rational degree-eight reduced homology has character
\[
\bigl(84,0,4,0,-10,-10,-10,-10\bigr)
\]
on \(e,r,r^2,r^3,s,rs,r^2s,r^3s\), where \(r\) is a quarter-turn and \(s\) a reflection. If \(Q\) denotes the set of nine unit squares, then, as rational dihedral modules,
\[
\widetilde H_8(\Delta^t_4(G);\mathbb Q)\cong
\operatorname{or}\otimes_{\mathbb Q}\mathbb Q\!\left[\binom Q3\right],
\]
where \(\operatorname{or}\) is the determinant sign character and the second factor is the permutation module on three-element subsets of \(Q\). This is **not** asserted as an integral module isomorphism.

## Assumptions and scope
The vertices are \((i,j)\) for \(0\le i,j\le3\), encoded by integer \(4i+j\). Two vertices are adjacent exactly when their Manhattan distance is one. Let \(I_4(G)\) consist of four-vertex independent sets. A subset \(S\) is a simplex of \(\Delta^t_4(G)\) if and only if \(V(G)\setminus S\) contains an element of \(I_4(G)\). Thus the facets are the complements of the independent four-sets and all have dimension eleven. The dihedral generators are \(r(i,j)=(j,3-i)\) and \(s(i,j)=(i,3-j)\), acting on both vertices and unit squares.

## Proof
**Finite simplicial construction.** Enumerate all \(\binom{16}{4}=1820\) unordered vertex quadruples and retain those with no grid edge. Exactly 405 remain. Take the downward closure of their sixteen-vertex complements. Independently, inspect every one of the \(2^{16}\) subsets and check that it has an independent quadruple in its complement; the resulting sets agree exactly. The complex has 60,723 nonempty faces and the face counts by dimension zero through eleven are
\[
(16,120,560,1820,4368,8008,11440,12870,11440,7096,2580,405).
\]

**A complete acyclic face matching.** Encode a face as a sixteen-bit mask. Process pivot vertices in the order
`(12,4,5,10,15,1,2,11,6,13,9,0,8,7,14,3)`.
At a pivot \(v\), pair every as-yet-unmatched nonempty face \(\sigma\) omitting \(v\) with \(\sigma\cup\{v\}\), provided the latter is also still unmatched. The pairs at that pivot are disjoint because their lower members omit \(v\) and their upper members contain \(v\); across pivots only unmatched faces are used. The algorithm constructs exactly 30,319 pairs, leaving precisely one critical vertex and 84 critical eight-dimensional faces.

To verify **global** acyclicity, form every codimension-one Hasse incidence between nonempty faces. There are exactly 469,288 such incidences. Direct each unmatched incidence upward and each matched incidence downward. A complete topological sort visits all 60,723 nodes, so the directed graph has no cycles. Forman's discrete Morse theorem now gives a CW model with one zero-cell, 84 eight-cells, and no other cells. The attaching maps of the eight-cells have a point as target and are null. Hence this CW model is a wedge of 84 eight-spheres, establishing the integral homotopy equivalence without inferring it merely from Betti numbers.

**Dihedral character.** For each automorphism \(g\), calculate the reduced simplicial Lefschetz number directly from the complete face set:
\[
\widetilde L(g)=-1+\sum_{\substack{\varnothing\ne\sigma\in\Delta^t_4(G)\\g\sigma=\sigma}}
(-1)^{|\sigma|-1}\operatorname{sgn}(g|_{\sigma}),
\]
where the sign is the parity of the permutation of the vertices of \(\sigma\) in increasing order. The exact values on the eight listed group elements are
\[
(84,0,4,0,-10,-10,-10,-10).
\]
By the homotopy classification, only reduced degree-eight homology is nonzero, so its trace equals \(\widetilde L(g)\). Independently permute the nine elementary grid squares under every group element, count invariant three-element subsets, and multiply by \(\det(g)\). The same character values result: fixed-triple counts are \((84,0,4,0,10,10,10,10)\). Equality of characters for all dihedral elements implies isomorphism over \(\mathbb Q\) by semisimplicity of finite-group representations. No equivariant homotopy equivalence is claimed.

## Verification
Run `python3 verify.py` with Python 3 standard library. The standalone script enumerates all facets twice via independent tests, checks all faces, constructs all matching pairs, builds the **entire** directed Hasse graph, performs a complete acyclicity check, and computes two independent descriptions of each of the eight character values. A successful execution ends with `ALL_VERIFY_OK`. A plain-text transcript of one executed replay is in `verify_output.txt`. The face-poset calculation, not the transcript by itself, supplies the finite proof certificate.

## Relationship to prior work
Bayer et al. [1, Table 3] **already report the degree-eight Betti number 84** for this very complex. That numerical rank is explicitly **not** presented here as new. Their table does not prove its integral homotopy type or determine the dihedral homology character. Chandrakar et al. [2] establish homotopy formulas for narrower grid families (two-row total complexes and three-row total three-cut complexes), without this case. Filakovský [3, Theorem 1, Corollary 4] treats rectangular grids at robust thresholds two and three, while higher thresholds are addressed in an edge-glued-square subclass and by a general conjecture; the present four-by-four, threshold-four case is outside those proved statements. Carnero Bravo [4] discusses higher products in other total-cut regimes but does not give this classification. The non-equivariant homotopy equivalence and the rational dihedral character are the new claims here. In particular, the known total **three**-cut grid classification is a different simplicial complex and does not imply either new claim.

## Limitations
This is an exhaustive finite proof for the **single** four-by-four grid, not a theorem about all grid sizes or all robustness thresholds. The representation assertion is over \(\mathbb Q\), not an integral module classification. The explicit character coincidence does not establish an equivariant homotopy model. Possible equivalent unindexed work remains an originality risk. Independent mathematical validation has not been performed.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Total cut complexes of graphs*, arXiv:2209.13503, in particular Section 5, Table 3 (2022 preprint; revised 2024).

[2] H. Chandrakar, N. R. Hazra, D. Rout and A. Singh, *Topology of total cut complexes and cut complexes of grid graphs*, arXiv:2408.07646 (first posted August 14, 2024).

[3] M. Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365 (first posted February 11, 2026).

[4] A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427 (first posted February 24, 2026).
