# The second Spence (45,12,3,3) graph is a critical-group witness against the cubic tritangent graph

## Finding

Let \(B\) be the graph given by the **second** adjacency matrix in Edward Spence's catalogue for parameters \((45,12,3,3)\). Its 3-primary graph critical group is
\[
 K(B)_{(3)}\cong (\mathbb Z/3)^8\oplus(\mathbb Z/9)^3\oplus(\mathbb Z/27)^{16}.
\]
It requires 27 generators. This makes \(B\) an explicit cospectral witness against the integral critical group of the cubic-surface tritangent-plane graph, whose 3-primary critical group requires 29 generators. The graphs have identical adjacency spectra and the same spanning-tree number \(3^{62}5^{23}\).

The full invariant factors for \(B\) are
\[
 K(B)\cong (\mathbb Z/3)^4\oplus(\mathbb Z/15)^4\oplus(\mathbb Z/45)^3\oplus(\mathbb Z/135)^{16}.
\]
The contribution is the identified witness and the exact 3-primary comparison, not an independent priority claim for the tritangent baseline or for the 5-primary factors.

## Objects and normalization

The tritangent graph \(T\) has as vertices the 45 tritangent planes of a smooth cubic surface over an algebraically closed field of characteristic zero. Vertices are adjacent when their planes contain a common line on the surface. This is the point graph of \(GQ(4,2)\). For a connected graph with integral Laplacian \(L\), the critical group is \(\operatorname{tors}(\operatorname{coker}L)\), equivalently the cokernel of a reduced Laplacian. The notation \(K_{(p)}\) denotes the Sylow \(p\)-subgroup. These are graph groups, not Picard groups of a cubic surface.

## Proof

**Graph inputs.** On the blowup of the plane at six general-position points, let \(E_i\) denote the exceptional classes, \(L_{ij}=H-E_i-E_j\), and \(Q_i=2H-\sum_{k\ne i}E_k\). The 45 unordered tritangent triples are the 30 \(\{E_i,L_{ij},Q_j\}\) with \(i\ne j\), and the 15 \(\{L_{ab},L_{cd},L_{ef}\}\) indexed by partitions into three pairs. Indeed anticanonical triples have degrees in \(H\) either \((0,1,2)\) or \((1,1,1)\); coefficient comparison gives these two lists. Each listed effective divisor sums to \(-K\), hence is an anticanonical plane section. Connecting triples with a common line supplies the canonical adjacency matrix. The companion `spence_second.txt` is the sequence of binary rows 46–90 when binary rows in Spence's 78-matrix file are counted starting at one (other lines ignored). Direct checks of degree, symmetry and common-neighbor counts give parameters \((45,12,3,3)\) for both matrices.

**Common spectral data and 5-part.** For either adjacency matrix \(A\), \(A^2=9I+3J\), so the adjacency eigenvalues are \(12,3,-3\) with multiplicities \(1,20,24\) (using the trace). The Laplacian \(L=12I-A\) has eigenvalues \(0,9,15\) with the same respective multiplicities. The matrix-tree theorem gives \(9^{20}15^{24}/45=3^{62}5^{23}\). On the lattice of degree-zero vertex vectors, the identity \(L(24I-L)=135I-3J\) becomes \(L(24I-L)=135I\). Hence the 5-part of the critical group is elementary abelian of rank 23 for every graph with these parameters.

**Graph-specific 3-part of the witness.** Delete one vertex of \(B\). For the resulting 44-by-44 reduced Laplacian, exact row and column reduction over \(\mathbb Z/3^9\mathbb Z\) gives valuation counts \(0:17,1:8,2:3,3:16\). To replay the reduction, at each pivot use a nonzero entry of least valuation \(v\) in the active submatrix, swap it into position, and clear its column and row by dividing their entries by \(3^v\) and using the inverse of the pivot unit modulo \(3^{9-v}\). These operations lift to invertible elementary operations over the local ring; no active pivot saturates the modulus. The counts sum to 44 and the valuation sum is 62. The accompanying calculation gives the same counts using deleted vertices 0, 9 and 20. Together with the common 5-part, pairing the sorted primary valuations gives the stated invariant factors for \(B\).

**Geometric comparison baseline.** Let \(N\) be the 27-by-45 line–plane incidence matrix. The bipartite Levi graph has Laplacian with diagonal blocks \(5I_{27},3I_{45}\) and off-diagonal blocks \(-N,-N^{\mathsf T}\). Since \(N^{\mathsf T}N=3I+A_T\), eliminating \(5I\) over \(\mathbb Z_{(3)}\) identifies its cokernel there with that of \((12I-A_T)/5\). Thus the 3-primary factors \((\mathbb Z/3)^{10}\oplus(\mathbb Z/9)^5\oplus(\mathbb Z/27)^{14}\) follow also from the exact Levi graph determination in [3]. The divisor-class matrix does not depend on the choice of smooth cubic surface in the specified characteristic. These factors, independently reproducible by the same reduced-Laplacian computation on \(T\), require 29 generators, unlike \(B\). The 5-part is common to both, so their integral critical groups are not isomorphic and neither are the graphs.

## Verification

In the directory with the accompanying `verify_tritangent.py` and `spence_second.txt`, run `python3 verify_tritangent.py`. These unchanged companions check the tritangent enumeration and both complete strongly regular matrices, and reproduce their exact reduced determinants and local factors for three roots of each graph. The expected terminal line is `CUBIC_TRITANGENT_CRITICAL_GROUP_COMPARISON_OK`. The reproduction is a finite certificate on two specified graphs, not a census of critical groups over all 78 catalogue entries.

## Relationship to existing results

The graph enumeration in [2] and the matrix file [1] specify the allowable graphs, not the exact 3-primary factors of the second matrix. The same-date Levi graph statement [3] is a different graph calculation but, by the displayed local reduction and the common 5-part, it also supplies the tritangent group's exact factors; no within-day precedence is assumed. Theorem 3.3 of [4] applies at 3 with the nonzero eigenvalues ordered \(15,9\), of valuations 1 and 2, respectively. For the second matrix's 3-rank \(17\) it restricts the positive valuation counts to either \((7,5,15)\) or \((8,3,16)\); the graph-specific calculation selects the latter. The general theorem therefore does not force the claimed group from the parameters or even from the 3-rank alone. The parameter-based 5-part is not new. Priority is limited to the explicit witness comparison to the best of available evidence; no complete catalogue of critical groups or universal priority claim is made.

## References

1. E. Spence, *Strongly Regular Graphs*, [catalogue](https://www.maths.gla.ac.uk/~es/srgraphs.php), [binary matrices for (45,12,3,3)](https://www.maths.gla.ac.uk/~es/SRGs/45-12-3-3).
2. K. Coolsaet, J. Degraer and E. Spence, *The Strongly Regular (45,12,3,3) Graphs*, Electron. J. Combin. 13 (2006), R32, [§5 and Table 2](https://eprints.gla.ac.uk/12858/1/12858.pdf).
3. *Integral critical group of the cubic-surface line–tritangent Levi graph*, [record 616774bc1c5b](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-integral-critical-group-of-the-cubic-surface-line-tritangent-lev--616774bc1c5b).
4. J. E. Ducey et al., *Critical group structure from the parameters of a strongly regular graph*, J. Combin. Theory Ser. A 180 (2021), [arXiv:1910.07686](https://arxiv.org/abs/1910.07686), §3.
