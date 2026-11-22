# The complete vertex-puncture homotopy profile of the Petersen three-robust clique complex

## Finding

Let \(P=\mathrm{KG}(5,2)\) denote the Petersen graph with vertices the ten two-element subsets of \([5]=\{0,1,2,3,4\}\), two vertices adjacent precisely when they are disjoint. Its three-robust clique complex is
\[
K=\mathrm{Cliq}_3(P)=\{\sigma\subseteq V(P):\alpha(P[\sigma])\leq2\}.
\]
For every \(v\in V(P)\), define the induced deletion \(D_v=K[V(P)\setminus\{v\}]\) and the simplicial link \(L_v=\operatorname{lk}_{K}(v)\). Then
\[
K\simeq\bigvee^9 S^3,\qquad
D_v\simeq\bigvee^4 S^3,\qquad
L_v\simeq\bigvee^5 S^2.
\]
Moreover, the inclusion \(D_v\hookrightarrow K\) induces a *split integral monomorphism*
\[
0\longrightarrow \mathbb Z^4\xrightarrow{\ (i_v)_*\ }\mathbb Z^9
\longrightarrow\mathbb Z^5\longrightarrow0
\]
on third reduced homology. Consequently the image is primitive (the quotient is torsion-free), with precisely four surviving classes and five lost classes for every single-vertex puncture. The ambient rank-nine statement alone follows from known total cut results; the new contribution is the full local profile and the integral inclusion map.

## Assumptions and scope

Only finite, abstract simplicial complexes and integral reduced homology are involved. The link contains the empty face, but the verifier enumerates nonempty faces for Morse matching; this does not change the realization or reduced homology. All distances and graph adjacency are those of the original ten-vertex Petersen graph. The deletion is an induced subcomplex, **not** the three-robust complex of a graph in which edges have been added or distances changed.

The vertex set is ordered lexicographically as
\[
01,02,03,04,12,13,14,23,24,34,
\]
where each two-digit symbol represents a two-element subset, and the distinguished vertex for finite verification is \(v=01\). Every graph automorphism induced by a permutation of \([5]\) preserves disjointness. Such permutations act transitively on these ten vertices, so one computed deletion and link suffices for all \(v\).

## Proof

**Exact simplex enumeration.** A nonempty set \(\sigma\) of vertex labels is a face of \(K\) if and only if every three-element subset \(\tau\subseteq\sigma\) contains at least one adjacent pair in \(P\). The verifier builds all ten vertices, thirty directed adjacency incidences, all 120 candidate triples, and exhaustively checks all \(2^{10}-1=1023\) nonempty subsets. It produces precisely \(232\) faces, with \(10,45,90,75,12\) faces in dimensions \(0,1,2,3,4\). Deleting the vertex \(01\) leaves \(159\) nonempty faces; the link, defined from precisely those faces containing \(01\), has \(72\) nonempty faces.

**Discrete Morse certificate.** The accompanying self-contained `verify_petersen_robust_puncture.py` specifies a deterministic algorithm that, on each of the three complete face sets, either pairs an active upper cell with its unique active codimension-one boundary face or marks a minimum-dimensional remaining face critical. Selection ties are resolved deterministically with a fixed seed over sorted cell tuples. These operations are not assumed to give an acyclic matching: the verifier explicitly reconstructs *every* codimension-one Hasse cover and orients matched covers upward and all other covers downward. A full topological-sort traversal certifies there is no directed cycle and that every face is either in exactly one pair or critical.

The independently checked totals are:

| Complex | Nonempty faces | Hasse covers | Morse pairs | Unpaired critical faces |
|---|---:|---:|---:|---|
| \(K\) | 232 | 720 | 111 | one dimension-0 cell; nine dimension-3 cells |
| \(D_{01}\) | 159 | 471 | 77 | one dimension-0 cell; four dimension-3 cells |
| \(L_{01}\) | 72 | 168 | 33 | one dimension-0 cell; five dimension-2 cells |

By the acyclic-matching theorem of discrete Morse theory, each finite complex is homotopy equivalent to a CW complex with precisely its displayed critical cells. A CW complex with a single zero-cell and only positive-dimensional cells of one fixed dimension at least two is a wedge of spheres in that dimension, because each attaching sphere maps into the singleton zero-skeleton. This establishes all three stated homotopy types integrally. An independent unsigned boundary-matrix computation over \(\mathbb F_2\) in the verifier also finds reduced Betti ranks \(9,4,5\) in degrees \(3,3,2\) respectively, providing a consistency check, not a substitute for the integer homotopy argument.

**Inclusion and primitivity.** For any simplicial complex with vertex \(v\), the star is the cone \(v*L_v\) and
\(K=D_v\cup(v*L_v)\), with intersection \(L_v\). Thus the pair \((K,D_v)\) has
\[
\widetilde H_j(K,D_v;\mathbb Z)\cong\widetilde H_{j-1}(L_v;\mathbb Z).
\]
Since \(L_v\simeq\bigvee^5 S^2\), the relative homology is concentrated in degree three with rank five. The long exact sequence for the pair, and the vanishing of \(\widetilde H_2(D_v;\mathbb Z)\), reduce in degree three to
\[
0\longrightarrow\widetilde H_3(D_v;\mathbb Z)\longrightarrow
\widetilde H_3(K;\mathbb Z)\longrightarrow\widetilde H_2(L_v;\mathbb Z)
\longrightarrow0.
\]
All groups are free abelian of the stated ranks; in particular the free quotient \(\mathbb Z^5\) makes the inclusion primitive, and the sequence splits as a sequence of abelian groups. No canonical or symmetry-equivariant splitting is asserted.

## Verification

Run `python3 verify_petersen_robust_puncture.py` using standard Python 3. The program requires no external libraries and prints the exact lines in `verify_expected.txt`. It checks: the Kneser graph construction; the complete simplex predicate; all nonempty faces of full, deletion, and link; every Morse pair and its codimension-one incidence; all face disjointness and critical counts; every Hasse cover; global directed acyclicity; and independent \(\mathbb F_2\)-boundary ranks. Every finite numerical statement used in the proof is either reconstructed or asserted on those fully reconstructed objects. The proof of vertex-uniformity and the integral short exact sequence is symbolic, not inferred from finite sampling.

## Relationship to prior work

Filakovský introduced and systematically studied \(k\)-robust clique complexes in a February 2026 preprint, proving sphere-wedge results for square-sequence graphs, which are bipartite. The nonbipartite Petersen graph is not in that scope. Kim and Lew earlier called the same simplicial construction the bounded-independence-number complex; their general work concerns collapsibility estimates, not the exact Petersen deletion/link/inclusion groups.

Bayer and collaborators introduced total cut complexes, which are combinatorial Alexander duals of robust clique complexes. A published calculation of the Petersen total three-cut complex yields nine four-spheres; it supplies (by Alexander duality) the already-known rank nine in degree three of \(K\), but gives no direct computation of \(D_v\), \(L_v\), or the integral inclusion morphism. These local groups and their primitive inclusion are the claimed new information, not the ambient rank.

## Limitations

This is a ten-vertex, one-puncture, vertex-transitive classification. Nothing is proved for two simultaneous punctures, other Kneser graphs, or all cubic graphs. The homology inclusion is split only as an abelian-group extension; no explicit integral equivariant splitting or homotopy retraction is asserted. Exhaustive finite combinatorial verification establishes the three homotopy types but does not establish comprehensive publication priority. An equivalent unindexed result may exist.

## References

1. M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first public version 2026-02-11, https://arxiv.org/abs/2602.11365.
2. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, first public version 2022-09-27, https://arxiv.org/abs/2209.13503.
3. M. Kim and A. Lew, *Complexes of Graphs with Bounded Independence Number*, arXiv:1912.12605, first public version 2019-12-29, https://arxiv.org/abs/1912.12605.
4. *The Petersen total \(3\)-cut complex is a wedge of nine \(4\)-spheres*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-petersen-total-3-cut-complex-is-a-wedge-of-nine-4-spheres--f242ea5e9ffb.
5. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
