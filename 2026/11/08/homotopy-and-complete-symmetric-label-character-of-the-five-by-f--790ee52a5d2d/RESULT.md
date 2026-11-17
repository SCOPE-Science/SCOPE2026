# Ordinary homotopy splitting of the five-crown matching complex

## Finding

Let \(D_5=\{(i,j):1\le i,j\le5,\ i\ne j\}\) and let \(X=\mathcal M(D_5)\) be the simplicial complex of partial nonattacking rook placements on these twenty off-diagonal squares, equivalently the ordinary matching complex of the five-crown graph. Then
\[
\boxed{X\simeq S^2\vee\bigvee^{13}S^3.}
\]
This is an **ordinary, nonequivariant integral homotopy equivalence**. It strengthens the previously computed integral homology groups \(\widetilde H_2(X;\mathbb Z)=\mathbb Z\) and \(\widetilde H_3(X;\mathbb Z)=\mathbb Z^{13}\) by determining all three-cell attaching maps in an explicit Morse CW model.

The full rational \(S_5\times C_2\) character of this same complex is **prior work**, already published on 18 October 2026 and again on 1 November 2026. It is neither claimed as a new result here nor needed as an originality premise for the homotopy splitting. In particular, the pre-existing decomposition is \(\widetilde H_3(X;\mathbb Q)\cong (S^{(4,1)}\oplus S^{(3,2)})\boxtimes\mathbf1\oplus S^{(2,1,1,1)}\boxtimes\varepsilon\), and \(\widetilde H_2(X;\mathbb Q)\cong \mathbf1\boxtimes\varepsilon\).

## Assumptions and scope

Faces are unordered sets of distinct squares with no shared row or column. The complex has exactly five labels, with five diagonal squares forbidden. Every simplex is oriented by increasing lexicographic square order for integral chain calculations. No assertion about an equivariant homotopy splitting, other label counts, or a complete integral group-action lattice is made.

## Proof

**1. Explicit face and matching model.** In zero-based coordinates order the twenty off-diagonal squares lexicographically. Exhaustive generation of partial injections avoiding fixed points yields face counts \((1,20,130,320,265,44)\) by cardinalities zero through five, including the empty face. Apply the consecutive vertex-toggle matching to the still-unmatched face set, in the following zero-based vertex order:

`(19,9,10,17,16,3,11,14,4,8,0,7,2,6,1,15,18,5,13,12)`.

At each vertex, pair an available face not containing it with its one-vertex enlargement when that enlarged face remains available, and remove both from the unmatched set. Initially include the empty simplex; after matching, delete the augmented empty/vertex pair and declare that vertex a critical zero-cell. The ordinary matching has 382 pairs and leaves exactly one critical zero-cell, one critical two-cell and thirteen critical three-cells.

**2. Acyclicity certificate.** In the Hasse graph of the nonempty face poset, reverse every matched cover relation and orient every other cover downward. Exhaustive inspection gives 779 nodes and 2,500 cover relations. Topological sorting visits all 779 nodes, proving that no directed gradient cycle exists. This finite certificate can be reconstructed by the included `crown_d5_verify.py` (which also performs the character calculations used as background). A separate direct face/matching/DAG implementation reproduces the counts and complete acyclicity. The result is a valid acyclic Forman matching on this finite complex.

**3. Integral cellular structure and attaching maps.** Forman's discrete Morse theorem gives an ordinary CW model with exactly one cell in dimension zero, one in dimension two and thirteen in dimension three, and no other cells. Its two-skeleton is exactly \(S^2\). Let \(d:\mathbb Z^{13}\to\mathbb Z\) be the cellular differential of its three-cells. Exact characteristic-zero simplicial boundary ranks, using increasing square order, are \((1,19,111,208,44)\) in augmented chain degrees zero through four. They give \(\dim_{\mathbb Q}\widetilde H_2(X;\mathbb Q)=1\) and \(\dim_{\mathbb Q}\widetilde H_3(X;\mathbb Q)=13\); the independent earlier integral chain-contraction computation also gives the corresponding torsion-free integral groups. Therefore \(d\otimes\mathbb Q=0\). Since \(d\) is an integer matrix, \(d=0\) integrally.

Each attaching map of a three-cell is a map \(S^2\to S^2\). Its homotopy class is classified by its degree because \(\pi_2(S^2)\cong\mathbb Z\). The corresponding column of \(d\) is exactly that degree. Since all columns vanish, all thirteen attaching maps are nullhomotopic. Attaching thirteen three-cells trivially to the two-sphere produces the claimed wedge \(S^2\vee\bigvee^{13} S^3\).

## Verification and limitations

The bundled finite checker `crown_d5_verify.py` reconstructs all allowed faces, the matching and acyclic gradient graph; performs exact characteristic-zero boundary rank computations and the existing homology-character calculations. The numerical character computations are **corroboration of already known group representations**, not novelty. Independent checks reconstruct the 779-face complex, the full 382-pair matching and its acyclic gradient graph. The homotopy conclusion uses the explicit CW cell structure and degree classification; finite enumeration is exhaustive only for this particular twenty-vertex complex.

This correction withdraws any novelty claim for the complete \(S_5\times C_2\) characters or the integral homology ranks. The homotopy equivalence is the sole surviving new mathematical assertion. Historical work may still contain an equivalent homotopy calculation under a different description. The full Björner–Welker 1999 article could not be read through currently accessible institutional access, which remains a material publication-priority risk. No equivalence between an ordinary homology-group calculation and this explicit homotopy splitting has been assumed without the Morse analysis.

## References

- *Full \(S_5\times C_2\) homology characters of the five-crown matching complex*, 18 October 2026, https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-full-s-5-times-c-2-homology-characters-of-the-five-crown-matchin--223bbad446ab . Earlier complete rational character and rational homology, not a homotopy classification.
- *The full symmetric-group and transpose homology of the five-by-five diagonal-deleted chessboard*, 1 November 2026, https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-the-full-symmetric-group-and-transpose-homology-of-the-five-by-f--2c83cecae788 . Earlier integral homology and complete rational character, not a homotopy classification.
- J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054, Section 8, Table 8.1.
- A. Björner and V. Welker, *Complexes of Directed Graphs*, SIAM J. Discrete Math. 12 (1999), 413–424, doi:10.1137/S0895480198338724.
- R. Forman, *Morse Theory for Cell Complexes*, Adv. Math. 134 (1998), 90–145.
