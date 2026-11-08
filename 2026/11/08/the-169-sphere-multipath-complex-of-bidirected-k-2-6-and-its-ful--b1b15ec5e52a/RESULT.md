# The 169-sphere multipath complex of bidirected \(K_{2,6}\) and its full \(\mathfrak S_6\)-character

## Finding
Let \(D=\overleftrightarrow{K}_{2,6}\) be the complete bipartite digraph with both orientations on every edge, and \(X(D)\) its ordinary multipath simplicial complex. Its vertices are the directed arcs, and its faces are directed-edge sets whose components are simple directed paths or isolated vertices. Then
\[|X(D)|\simeq\bigvee^{169} S^3.\]
The natural action of the leaf-permutation group \(\mathfrak S_6\) on rational third homology is the following **complete** decomposition into irreducible Specht modules:
\[
\widetilde H_3(X(D);\mathbb Q)\cong
2S^{(4,2)}\oplus2S^{(4,1,1)}\oplus S^{(3,3)}\oplus4S^{(3,2,1)}\oplus
2S^{(3,1,1,1)}\oplus2S^{(2,2,2)}\oplus3S^{(2,2,1,1)}\oplus S^{(2,1,1,1,1)}.
\]
These summands have total dimension \(169\). The complete character, indexed by cycle type \(\mu\) of a leaf permutation, is:

| Cycle type \(\mu\) | Trace on \(\widetilde H_3\) |
| :-- | --: |
| \((6)\) | 1 |
| \((5,1)\) | -1 |
| \((4,2)\) | 1 |
| \((4,1,1)\) | 1 |
| \((3,3)\) | 1 |
| \((3,2,1)\) | -1 |
| \((3,1,1,1)\) | -5 |
| \((2,2,2)\) | 1 |
| \((2,2,1,1)\) | 1 |
| \((2,1,1,1,1)\) | -7 |
| \((1,1,1,1,1,1)\) | 169 |

## Assumptions and scope
The digraph has two hub vertices \(h_0,h_1\), six leaf vertices \(u_0,\ldots,u_5\), and precisely the arcs \(h_a\to u_i\) and \(u_i\to h_a\), for \(a=0,1\), \(0\le i\le5\). There are no loops and no edges between two hubs or two leaves. A multipath is an arc set in which every vertex has in- and outdegree at most one and **no directed cycle**. The complex is not the ordinary matching complex of the underlying undirected graph. Homotopy and homology are integral unless a coefficient field is displayed. The Specht modules are over \(\mathbb Q\).

## Proof
**Exact face model.** Index the \(24\) arcs in four blocks of length six: \(e_i=(h_0,u_i)\), \(e_{6+i}=(h_1,u_i)\), \(e_{12+i}=(u_i,h_0)\), and \(e_{18+i}=(u_i,h_1)\), for \(0\le i<6\). Every arc has exactly one hub endpoint, while each hub can support at most one incoming and one outgoing selected arc. Thus every face has at most four arcs. A subset is a face exactly when the source labels are pairwise distinct, the target labels are pairwise distinct, and the resulting partial successor map has no directed cycle. Complete enumeration from this definition gives the augmented face counts, by cardinality \(0,1,2,3,4\),
\[(1,24,192,600,600).\]

**Acyclic discrete-Morse certificate.** Start with the set \(F\) of all augmented faces, including the empty face. In the fixed arc order \(0,1,\ldots,23\), for each arc \(e\), and each currently unmatched face \(s\) listed by increasing cardinality and lexicographically, match \(s\) with \(s\cup\{e\}\) whenever \(e\notin s\) and both faces are still unmatched. Remove both faces and continue. The standalone program `verify_k2_6.py` generates **all** these faces and pairs directly from the preceding graph definition, checks every pair is a genuine codimension-one incident pair, then orients the entire augmented Hasse diagram downwards except for reversed matched incidences. A topological-sort exhaustion of all \(1417\) augmented faces and all \(4608\) cover relations proves that this finite directed graph has no directed cycle. This explicitly verifies Forman's acyclicity condition, not just a rank computation. The algorithm yields exactly \(624\) matched pairs and \(169\) unmatched faces, **all** of cardinality four. Its canonical matching-pair digest is
`4b74f6d6352facf63b8331aea1dcf5cd2247daa557581d0c58e868280595c03a`.

The empty face is matched to the first arc vertex. Discarding the empty face and declaring that vertex critical gives a matching on the ordinary (unaugmented) complex with one critical zero-cell and \(169\) critical three-cells and no other critical cells; this remains acyclic because it is a restriction of the verified directed graph. Forman's discrete Morse theorem gives a CW model with one zero-cell and \(169\) three-cells. Every attaching map of a three-cell to the single point of the lower skeleton is null; the model is a wedge of \(169\) three-spheres. This proves the claimed **integral homotopy type**.

**Full symmetry character.** Permutations of the six leaves preserve the digraph and act simplicially on \(X(D)\). For a permutation \(g\in\mathfrak S_6\), the trace on oriented simplicial \(k\)-chains is the signed count of \((k+1)\)-arc faces fixed setwise by \(g\): the sign is the parity of the induced reordering of that face. Since the homology is concentrated in degree three, the reduced Lefschetz trace formula gives
\[
\operatorname{tr}(g\mid\widetilde H_3)=1-\sum_{k=0}^{3}(-1)^k\operatorname{tr}(g\mid C_k).
\]
Enumerating faces fixed by each of the eleven conjugacy-class representatives gives the character table above. The standalone program `character_k2_6.py` reconstructs these eleven signed trace counts directly from the faces, computes all \(\mathfrak S_6\) irreducible characters with the Murnaghan--Nakayama rim-hook rule, and takes the exact class-size-weighted inner products. It checks nonnegative integral multiplicities, full character orthogonality, reconstruction at all eleven classes, and total dimension \(169\), yielding the displayed Specht decomposition.

## Verification
Run `python3 verify_k2_6.py` and `python3 character_k2_6.py` with Python 3 standard library; no third-party packages or datasets are needed. The first program enumerates all \(1417\) augmented faces, verifies all \(624\) matched pairs and all \(4608\) Hasse incidences, performs a complete acyclicity test, and independently computes boundary ranks over \(\mathbb F_2\) and \(\mathbb F_3\). Both fields give ranks \((1,23,169,431)\) in successive augmented chain dimensions and reduced Betti numbers \((0,0,0,169)\). The second program calculates all eleven conjugacy-class traces and Specht multiplicities and verifies the symmetric-group character orthogonality equations. Their recorded exact output is `check.txt`; the integer homotopy conclusion relies on the exhaustive acyclic matching, not on the finite-field ranks alone.

## Relationship to prior work
Caputi, Collari, and Smith introduced a study of multipath complexes of **bidirectional paths and cycles** in their January 9, 2026 preprint [1], giving connectivity and homology results and explicit homotopy questions for those families. The bidirected complete bipartite graph \(\overleftrightarrow K_{2,6}\) is not one of those paths or cycles. The earlier paper of Caputi, Collari, Di Trani, and Smith [2] treats complete bipartite digraphs with an **alternating one-way orientation** for Euler characteristics; its hypothesis is not the bidirected graph studied here. Nearby calculations of the same bidirected family at the distinct long-part sizes four and five give Moore-space summands; those results do not determine the six-leaf case, its torsion behavior, or its symmetric-group character. Other published multipath results for bidirected trees do not cover the four-cycles in this graph. These comparisons motivate the first six-leaf case as a boundary beyond the known low-width Moore-space examples.

## Limitations
The result is an **exact finite case**, not a proof for all \(\overleftrightarrow K_{2,m}\) and not a stability theorem. The homotopy equivalence is nonequivariant: the displayed representation describes the rational action on homology, not an equivariant homotopy splitting. The character does not classify the integral \(\mathfrak S_6\)-lattice. The proof uses an exhaustive finite acyclic-matching certificate; it does not establish a closed-form matching for arbitrary widths. Independent review has not been performed.

## References
[1] L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670, first submitted 2026-01-09, https://arxiv.org/abs/2601.05670 .

[2] L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, first submitted 2022-08-09, https://arxiv.org/abs/2208.04656 .

[3] R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete Morse equivalence used for the finite certificate).
