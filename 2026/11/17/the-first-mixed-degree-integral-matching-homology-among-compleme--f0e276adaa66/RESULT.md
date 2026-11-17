# The first mixed-degree integral matching homology among complements of cycles

## Finding

Let \(C_n\) be the cycle on vertices \(0,1,\ldots,n-1\), and let \(G_n=\overline{C_n}\) be its simple graph complement. Let \(X_n=\mathcal M(G_n)\) be the simplicial complex whose vertices are edges of \(G_n\) and whose faces are pairwise vertex-disjoint collections of those edges. Among all \(3\le n\le9\), the first \(X_n\) with nonzero reduced integral homology in **two different nonnegative dimensions** occurs at \(n=9\). Precisely,

\[
\widetilde H_2(X_9;\mathbb Z)\cong\mathbb Z^{42},\qquad
\widetilde H_3(X_9;\mathbb Z)\cong\mathbb Z.
\]

Every other reduced integral homology group of \(X_9\) vanishes. For smaller nonempty cases, the nonzero reduced groups are \(\widetilde H_1(X_5;\mathbb Z)\cong\mathbb Z\), \(\widetilde H_1(X_6;\mathbb Z)\cong\mathbb Z^6\), \(\widetilde H_1(X_7;\mathbb Z)\cong\mathbb Z\), and \(\widetilde H_2(X_8;\mathbb Z)\cong\mathbb Z^{42}\). The realization \(|X_3|\) is empty and \(X_4\) is a simplex. The nine-vertex complex is therefore the first mixed-degree case in this natural graph family. All homology groups in the stated finite range are torsion-free.

## Assumptions and scope

All graphs are finite, simple, and labeled cyclically, with the pair \(\{i,j\}\) an edge of \(G_n\) exactly when its endpoints are not consecutive around the cycle. The scope is the complete finite interval \(3\le n\le9\), not an assertion concerning \(n\ge10\). Homology uses integer coefficients and standard reduced augmentation. For the empty realization at \(n=3\), the conventional augmented degree-minus-one group is excluded from the claim about nonnegative degrees. The top-dimensional faces have at most \(\lfloor n/2\rfloor\) matching edges.

## Proof

All cases are finite and exhaustively checked by exact integral chain computations using the supplied standalone `verify_antihole.py`. For each \(n\), enumerate every subset of edges of \(G_n\) by binary recursion: either exclude an edge, or include it only if neither endpoint has been used. A face with \(d+1\) chosen edges has dimension \(d\); orient it by increasing lexicographic edge index. For each oriented face \([e_0,\ldots,e_d]\), its chain boundary is

\[
\partial_d[e_0,\ldots,e_d]
 =\sum_{j=0}^{d}(-1)^j[e_0,\ldots,\widehat{e_j},\ldots,e_d].
\]

The exact enumerated face counts \((f_0,f_1,\ldots)\) and integer boundary ranks \((r_1,r_2,\ldots)\) are:

| \(n\) | Face numbers by dimension | Integral boundary ranks |
| --- | --- | --- |
| 4 | \((2,1)\) | \((1)\) |
| 5 | \((5,5)\) | \((4)\) |
| 6 | \((9,18,4)\) | \((8,4)\) |
| 7 | \((14,49,35)\) | \((13,35)\) |
| 8 | \((20,110,164,31)\) | \((19,91,31)\) |
| 9 | \((27,216,555,324)\) | \((26,190,323)\) |

The zero-edge case \(n=3\) is immediate. For every nonzero boundary matrix, the checker performs **only unimodular integer operations**: choose a coefficient \(\pm1\); use integer column additions to clear the pivot row, then integer row additions to clear the pivot column; and remove the resulting unit diagonal block. The source code implements these operations exactly, maintaining sparse row and column dictionaries. In every degree of every graph order, it reduces the full matrix to a zero residual after extracting exactly the ranks stated in the table. Therefore every nonzero Smith invariant factor of every boundary matrix equals \(1\); this conclusion is stronger than a field-rank computation and excludes all integral torsion.

For each \(d\ge1\), the rank of reduced homology is \(f_d-r_d-r_{d+1}\), taking missing ranks to be zero. In dimension zero, subtract the rank-one augmentation. Substitution gives the groups in the finding. For \(n=9\) specifically, \(f_2-r_2-r_3=555-190-323=42\), and \(f_3-r_3=324-323=1\). Every smaller nonempty graph order has homology supported in at most one positive degree, and \(n=4\) has no reduced homology. Thus nine is the sharp first mixed-degree order in the specified family. No inference from finite data to higher graph orders is made.

## Verification

Run `python3 verify_antihole.py` from the directory containing this file. The program has no third-party dependencies; it reconstructs every graph edge and simplicial boundary rather than loading precomputed matrices, and it verifies the entire finite interval with exact integer arithmetic. The recorded standard output is embedded in `verification_output.txt`. A second finite-field elimination over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) independently reproduced the nonzero Betti ranks for \(5\le n\le9\), but the integral proof does **not** rely on those field checks. The integral checker reports `ANTICYCLE_COMPLEMENT_INTEGRAL_BOUNDARIES_PASS`.

## Relationship to prior work

Björner, Lovász, Vrećica and Živaljević's foundational work studies chessboard complexes and matching complexes, including the connectivity of matching complexes of **complete graphs**. Shareshian and Wachs analyze integral torsion and homology of complete-graph and complete-bipartite matching complexes. These results motivate the integral, rather than rational, computation here. They do not determine the exact groups of the proper subcomplex obtained by deleting the nine cyclic edges from the complete graph. Different topological complexes on complementary cycles, such as three-cut complexes, do not imply this matching-complex computation. The claim is limited to the exact finite cutoff and does not claim a general recursive theorem.

## Limitations

The calculation certifies integral homology and the minimality of the mixed-degree occurrence through order nine. It **does not** prove that \(X_9\) has a wedge-of-spheres homotopy type; homology alone does not classify its higher attaching maps. It also does not determine the homology for \(n\ge10\), nor assert that the exact fact has never appeared in an unindexed computational table. An independent mathematical audit has not been performed.

## References

1. A. Björner, L. Lovász, S. T. Vrećica and R. T. Živaljević, “Chessboard Complexes and Matching Complexes,” *Journal of the London Mathematical Society* 49 (1994), 25–39, https://doi.org/10.1112/jlms/49.1.25 (published February 1, 1994).
2. J. Shareshian and M. L. Wachs, “Torsion in the Matching Complex and Chessboard Complex,” preprint first posted September 3, 2004, https://arxiv.org/abs/math/0409054.
