# Integral two-torsion in \(\mathcal F_2\) distinguishes the Shrikhande and rook graphs

## Finding
Let \(S\) be the Shrikhande graph and \(R\) the four-by-four rook graph. Their second forest-filtration complexes have **different complete reduced integral homology**:

\[
\widetilde H_i(\mathcal F_2(S);\mathbb Z)\cong
\begin{cases}
\mathbb Z^9\oplus\mathbb Z/2,&i=4,\\
\mathbb Z^6,&i=5,\\
\mathbb Z^{36},&i=6,\\
0,&\text{otherwise},
\end{cases}
\qquad
\widetilde H_i(\mathcal F_2(R);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{33},&i=5,\\
\mathbb Z^{72},&i=6,\\
0,&\text{otherwise}.
\end{cases}
\]

In particular, \(\mathcal F_2(S)\) has genuine integral two-torsion, whereas \(\mathcal F_2(R)\) is torsion-free. Both reduced Euler characteristics equal \(39\). The graphs have the same strongly regular parameters and spectrum, so these finer topological invariants are not determined by those graph parameters or by the Euler characteristic.

## Assumptions and scope
The vertex set of each graph is \((\mathbb Z/4\mathbb Z)^2\), ordered lexicographically and encoded by \(4a+b\), with \(a,b\in\{0,1,2,3\}\). In \(R=K_4\square K_4\), distinct vertices are adjacent precisely when they share a coordinate. In \(S\), adjacency is defined by the six differences \(\pm(1,0),\pm(0,1),\pm(1,1)\), where the final signs are correlated. Both definitions give simple graphs with sixteen vertices, degree six, and exactly two common neighbors for each pair of distinct vertices. Their adjacency spectra coincide.

For a finite graph \(G\), the complex \(\mathcal F_2(G)\) consists of all vertex subsets \(U\subseteq V(G)\) for which the induced graph \(G[U]\) is acyclic and has maximum degree at most two. Equivalently, every component of \(G[U]\) is a path or an isolated vertex. The empty subset is included as the unique face of dimension minus one. All homology is ordinary reduced simplicial homology over the integers. No coefficient localization or quotient by graph automorphisms is taken.

## Proof
First, enumerate **all** \(2^{16}=65,536\) subsets for each graph. A subset is retained exactly when no edge creates a cycle under union-find and no induced vertex degree exceeds two. Independently, a component-search predicate confirms that the induced edge count plus the number of components equals the number of selected vertices, together with the same maximum-degree bound. The two exhaustive tests agree on every subset. The resulting face counts in dimensions \(-1,0,1,2,3,4,5,6\) are, respectively,

\[
\begin{array}{c|rrrrrrrr}
 &-1&0&1&2&3&4&5&6\\\hline
R&1&16&120&528&1392&2160&1728&576\\
S&1&16&120&528&1408&2064&1424&384.
\end{array}
\]

For either complex, perform a lexicographic acyclic matching on its augmented face poset. At each vertex position in ascending order, pair every as-yet unmatched face omitting that position with its union with the position whenever both are present. In decreasing order, repeat independently. Both pairings are explicit in `verify.py`, and the program checks their **complete** directed Hasse graphs for acyclicity, orienting every unmatched incidence downward and every matched incidence upward. Thus each matching gives an integral algebraic Morse reduction: every reversed pivot has incidence \(\pm1\).

For \(R\), both matching orders have \(3,204\) pairs; the \(32,608\) face incidences are all checked. Their critical cells number \(4,37,72\) in dimensions \(4,5,6\), respectively, and none elsewhere. The reduced integral Morse boundary \(\partial_5\) has shape \(4\times37\), Smith invariant factors \(1,1,1,1\), and rank four. The boundary \(\partial_6\), of shape \(37\times72\), is zero. Therefore the only reduced groups are free of ranks \(33\) in degree five and \(72\) in degree six.

For \(S\), both orders have \(2,934\) pairs, and all \(29,024\) incidences are checked. Their critical cells number \(22,19,36\) in dimensions \(4,5,6\), respectively, and none elsewhere. Here the integer boundary \(\partial_5\) has shape \(22\times19\) and Smith normal form with twelve unit factors and **one factor of two**. In particular it has integer rank thirteen. The boundary \(\partial_6\), of shape \(19\times36\), is zero. Consequently \(H_4\) is the cokernel of \(\partial_5\), namely \(\mathbb Z^9\oplus\mathbb Z/2\); \(H_5\) is its free kernel of rank \(6\); and \(H_6\cong\mathbb Z^{36}\). There are no other critical groups, so every other reduced homology group is zero.

The signed boundary calculations use the increasing vertex order to orient each simplex. The Morse differential replaces a matched lower face by the negative of the other terms of its paired upper-face boundary, divided by its unit incidence. Acyclicity makes this alternating-path recurrence terminate, and it preserves the integral chain-homotopy type. The exact integer Smith computations therefore prove the claimed integral groups rather than merely matching rational or mod-two Betti numbers.

## Verification
`verify.py` regenerates both graphs; verifies all \((16,6,2,2)\) common-neighbor tests; compares two exhaustive forest predicates; constructs both pivot-order matchings; checks each complete Hasse orientation for cycles; generates and checks the signed Morse boundaries; computes exact Smith normal forms over \(\mathbb Z\); and independently computes **all** reduced mod-two simplicial boundary ranks on the original unreduced complexes. The mod-two reduced Betti ranks are \((0,0,0,0,0,33,72)\) for \(R\) and \((0,0,0,0,10,7,36)\) for \(S\). These match the universal-coefficient predictions from the integral groups, including the two extra mod-two dimensions associated with the single torsion summand.

The certificate `MATRICES.json` records both integral Morse boundary systems, critical cell counts, Smith diagonals, and full mod-two checks. With Python and SymPy installed, run `python verify.py --check-certificate MATRICES.json`. The expected output is `verification_output.txt`; its last line is `FOREST_LEVEL_TWO_SHRIKHANDE_ROOK_INTEGRAL_CERTIFICATE_PASS`. The certificate replay and the recorded output were checked for exact agreement.

## Relationship to prior work
Carnero Bravo [1] defines the forest filtration and studies paths, cycles, cactus graphs, joins, and selected products. The inspected sections and full-document searches do not supply the level-two integral homology of the present pair. Brouwer and Van Maldeghem [2] establish the two nonisomorphic strongly regular graphs with these shared parameters and their explicit construction; graph-spectral or adjacency-matrix Smith invariants in that reference do not determine the integral homology of these induced-vertex-set complexes.

A previously recorded computation for the same pair concerns **two-independence complexes**, equivalent to the *first* forest stage \(\mathcal F_1\). Its sphere-wedge homotopy types do not imply the new level-two integral groups: faces containing induced paths on three or more vertices enter at the second stage, and the acyclicity requirement is independent of the prior stage's degree bound. Neighborhood, Čech, and cut-complex calculations on the same graphs likewise use different face predicates, with no known chain equivalence that would imply this result. The precise torsion in level two was not found in the inspected literature.

## Limitations
This is an exact finite calculation for two sixteen-vertex graphs. It does **not** classify the homotopy types or attaching maps of the complexes, show that the torsion produces a Moore-space wedge summand, describe induced maps between forest-filtration stages, determine symmetry representations, or prove a theorem for all strongly regular graphs. Absence of an equivalent result from the inspected sources is evidence for originality, not a proof that unindexed literature contains none. The integer computations require the stated SymPy dependency; no independent external audit is claimed.

## References
1. Andrés Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first posted 25 July 2023; sections 1, 3, and 4. https://arxiv.org/abs/2307.13271
2. Andries E. Brouwer and Hendrik Van Maldeghem, *Strongly Regular Graphs*, §10.6, Chapter 10, 2022. https://homepages.cwi.nl/~aeb/math/srg/rk3/srgw.pdf
