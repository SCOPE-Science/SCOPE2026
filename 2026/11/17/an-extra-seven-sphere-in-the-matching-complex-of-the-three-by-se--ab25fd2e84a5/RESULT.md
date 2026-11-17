# An extra seven-sphere in the matching complex of the three-by-seven cylinder

## Finding
Let \(G=P_3\square C_7\) be the Cartesian product of the three-vertex path and the seven-cycle. Its **ordinary matching complex** \(\mathcal M(G)\), whose simplices are sets of pairwise vertex-disjoint graph edges, has the integral homotopy type
\[
\boxed{|\mathcal M(P_3\square C_7)|\simeq\bigvee^{58}S^6\vee S^7.}
\]
In particular, its only nonzero reduced integral homology groups are \(\widetilde H_6\cong\mathbb Z^{58}\) and \(\widetilde H_7\cong\mathbb Z\), with no torsion. The high-dimensional summand distinguishes this periodic seven-column strip from the rectangular three-by-seven grid, whose matching complex is known to be \(\bigvee^{55}S^6\). No assertion about the homology map induced by adding periodic edges is needed or made.

## Assumptions and scope
The graph is simple and undirected. Its vertex set is \(\{0,1,2\}\times\mathbb Z/7\mathbb Z\). Each \((r,c)\) is adjacent horizontally to \((r,c+1)\) (modulo seven); each \((r,c)\), for \(r=0,1\), is also adjacent vertically to \((r+1,c)\). No edge wraps in the three-vertex path coordinate. There are exactly 21 vertices, 21 horizontal edges and 14 vertical edges, hence 35 graph edges.

Order graph vertices by the integer \(7r+c\), order each graph edge by its sorted endpoint pair, and order all 35 graph edges lexicographically. A simplex is the 35-bit integer recording a subset of the graph edges with disjoint endpoint sets. The empty simplex is included only in augmented enumeration. This finite, ordinary simplicial complex is the sole object classified; all homology and homotopy assertions use integer coefficients or geometric realization.

## Proof
**Complete face census.** Iterate over the ordered 35 edges, branching between not using an edge and using it if both endpoints are unoccupied. Each edge subset has a unique branch sequence, and every branch retained is a matching, so the algorithm enumerates the complete augmented face family without sampling. In cardinalities zero through ten, the face counts are exactly
\[
(1,35,511,4060,19222,55867,99085,103231,58310,15267,1274),
\]
a total of 356,863 augmented faces. The reduced Euler characteristic is 57.

**Complete acyclic discrete-Morse matchings.** Encode an explicit permutation of the 35 edge indices as the sequence
`34,22,17,32,7,28,33,19,1,14,29,12,25,20,9,27,3,13,6,26,8,30,10,11,23,24,15,18,21,4,0,2,16,31,5`.
Starting with the entire face set, at each index pair every remaining face omitting that graph edge with the face obtained by adding it, provided both are still available, and remove all such pairs before processing the next index. Exactly 178,361 pairs are formed. Orient each of the 2,303,210 Hasse cover relations **upwards on the matched pairs and downwards otherwise**. Direct Kahn topological sorting visits all 356,863 augmented faces. Thus the entire gradient digraph, not a sample of its paths, is acyclic.

Exactly 99 unpaired six-dimensional faces and 42 unpaired seven-dimensional faces remain; there are no other augmented critical faces. The empty face was paired with one vertex. Deleting the empty face and that single pair yields an ordinary acyclic discrete-Morse matching with exactly one critical vertex, 99 critical six-cells and 42 critical seven-cells, and no cells of dimensions one through five or above seven.

**Exact signed attaching map.** Orient each simplex by the increasing order of its graph-edge indices. For a face \(a\) of dimension six paired upwards with a face \(b\) of dimension seven, its projection into the critical six-chain group is obtained by solving the unit relation \(\partial b=0\):
\[
R(a)=-[\partial b:a]^{-1}\sum_{t\prec b,\ t\ne a}[\partial b:t]R(t).
\]
For a critical six-face \(c\), put \(R(c)=c\); for a six-face paired *downwards* with a five-face, put \(R(c)=0\). Acyclicity makes this recursion well founded. The integral Morse boundary of each critical seven-face \(f\) is \(\sum_{a\prec f}[\partial f:a]R(a)\). This is the signed algebraic Morse differential, retaining all integer coefficients and orientations.

The complete resulting integer boundary is the 42-row, 99-column matrix included as `proof/morse_boundary_A_42x99.csv` (rows are ordered critical seven-faces and columns ordered critical six-faces). Applying only integer row and column operations at coefficients \(+1\) or \(-1\) yields precisely 41 unit pivots and a completely zero remaining 1-by-58 block. Thus, integrally, the differential has Smith invariants \(1\) repeated 41 times and no other nonzero invariants. This proves the reduced homology groups asserted above.

More strongly, the discrete-Morse CW model has a single vertex, 99 six-cells and 42 seven-cells, so its six-skeleton is \(\bigvee^{99}S^6\). Because \(\pi_6(\bigvee^{99}S^6)\cong\mathbb Z^{99}\) by Hurewicz, the seven-cell attaching homotopy classes are **fully** determined by the integral signed differential. Unimodular basis operations are realizable by self-homotopy equivalences of the sphere bouquet and changes of seven-cell generators. The 41 unit entries cancel 41 six/seven-cell pairs up to homotopy; the remaining seven-cell attaching class has zero degree vector and is nullhomotopic. The CW model is therefore precisely \(\bigvee^{58}S^6\vee S^7\), establishing the whole integral homotopy type.

**Independent Morse sequence.** To avoid relying on a unique combinatorial reduction, the verifier also applies a second, different explicit 35-edge permutation. It produces 178,362 pairs, 98 critical six-cells and 41 critical seven-cells, checks all 2,303,210 covers for acyclicity again, and produces 40 integral unit pivots followed by a zero 1-by-58 block. This independently reproduces the same homotopy classification.

## Verification
From the directory containing this report, run `python3 proof/verify_cylinder.py` with Python 3.10 or newer, using only the standard library. This program reconstructs the graph, every face, both full Morse matchings, both complete acyclicity topological sorts, both signed gradient-path matrices, and the integer unit-pivot reductions. It also compares the first generated matrix entry by entry with the separately embedded `proof/morse_boundary_A_42x99.csv`. All checks are exact. The verified standard output is in `proof/verification_output.txt`. No previous-run log, external data file, random sample or floating-point computation is required.

The finite exhaustive checks suffice because the classification concerns exactly one finite complex. They do not prove a uniform pattern for other cycle lengths. The derived Hurewicz and cellular attaching-map steps above are needed to upgrade integral homology to homotopy; a Smith-form computation alone would not establish a sphere wedge.

## Relationship to prior work
Chauhan, Sharma and Shukla, first publicly posted September 23, 2026, study matching complexes of rectangular three-by-\(n\) Cartesian grids, \(P_3\square P_n\), establishing connectivity and homology-vanishing results. The seven-column **cylinder** here has three wraparound edges absent from those rectangular graphs. In available published full text, the exact rectangular seven-column result is \(\mathcal M(P_3\square P_7)\simeq\bigvee^{55}S^6\), with 32 rather than 35 graph edges and without any seven-dimensional homology. Another published finite classification determines the pentagonal cylinder \(\mathcal M(P_3\square C_5)\simeq\bigvee^{24}S^4\vee\bigvee^3S^5\); it does not give a length recurrence or cover the heptagonal cylinder. The 2021 Goyal–Shukla–Singh paper concerns rectangular grids as well and was subsequently withdrawn with an error notice. The polygonal-line-tiling and outerplanar matching-complex literature does not yield these two Betti multiplicities for the multirow cyclic cylinder. Search comparisons found no covering exact computation, but this does not prove bibliographic uniqueness. The complete 2026 rectangular-grid preprint was not accessible for appendix inspection, which remains a priority risk.

## Limitations
The theorem is for the **single graph** \(P_3\square C_7\), not all cylinders, tori, rectangular grids or graph matching complexes. Neither a general periodicity formula nor an inclusion-induced homology map nor an equivariant homology representation is claimed. The finite proof is internally reproducible but has not been independently audited. Potential unindexed equivalent calculations and the inaccessible full 2026 paper remain originality risks.

## References
1. P. Chauhan, A. Sharma and S. Shukla, *Homology of matching complexes of 3-by-n grid graphs*, arXiv:2609.27366v1, first public September 23, 2026, https://arxiv.org/abs/2609.27366.
2. *Mixed-dimensional matching-complex homotopy on the pentagonal three-row cylinder*, public research record, November 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-mixed-dimensional-matching-complex-homotopy-on-the-pentagonal-th--da8762498878/RESULT.md.
3. *The matching complex of the three-by-seven grid is a wedge of 55 six-spheres*, public research record, November 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-matching-complex-of-the-three-by-seven-grid-is-a-wedge-of-55--88cca1c89c8d/RESULT.md.
4. S. Goyal, S. Shukla and A. Singh, *Matching complexes of 3-by-n grid graphs*, *Electron. J. Combin.* 28 (2021), P4.16, withdrawn, https://arxiv.org/abs/2106.09915.
5. R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145.
