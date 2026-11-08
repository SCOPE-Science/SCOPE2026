# Mixed-dimensional integral homotopy of \(\operatorname{Ind}_2(Q_4)\)

## Finding

Let \(Q_4\) be the four-dimensional cube graph. Let \(X=\operatorname{Ind}_2(Q_4)\) be its second independence complex: a vertex subset is a face exactly when all connected components of its induced subgraph have at most two vertices. Then

\[
X\simeq\left(\bigvee^{16}S^3\right)\vee S^4.
\]

Consequently \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^{16}\), \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z\), and \(\widetilde H_i(X;\mathbb Z)=0\) for all other degrees. The wedge decomposition is integral and is stronger than a calculation of Betti numbers.

## Assumptions and scope

Label the sixteen vertices by the integers \(0,1,\ldots,15\), interpreted as binary words of length four. Two distinct vertices \(u,v\) are adjacent precisely when \(u\mathbin{\mathrm{xor}}v\) is a power of two. This is the Cartesian product of four copies of the two-vertex complete graph and is also isomorphic to the Cartesian square of a four-cycle. A face is a vertex subset whose induced graph has maximum degree at most one. In this triangle-free graph that is equivalent to avoiding every three-vertex path as a (not necessarily induced-edge-maximal) subgraph; it is the devoid complex \(D(Q_4;P_3)\) of [1]. The assertions are for this specific graph, not for all hypercubes.

## Proof

**Explicit finite face model.** At each of sixteen vertices there are \(\binom{4}{2}=6\) distinct unordered pairs of neighbors. The resulting 96 three-element sets are all the minimal nonfaces: any selected induced component with three or more vertices contains a selected vertex with two distinct selected neighbors. Enumerating all \(2^{16}\) vertex masks, or equivalently testing avoidance of these 96 triples, gives the complete face vector including the empty face:

\[
(f_{-1},f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7)
=(1,16,120,464,964,960,440,80,10).
\]

**Finite acyclic matching.** Work in the nonempty face poset and retain the singleton \(\{0\}\) unmatched. For pivot vertices \(v=0,1,\ldots,15\), in increasing numerical order of face masks, pair each as-yet-unmatched face not containing \(v\) with its \(v\)-extension if the extension is a face and remains unmatched. There are 1,513 pairs, with critical cells in dimensions \(0,3,4,5\) in multiplicities \(1,17,6,4\). Orient each Hasse edge downward except matched ones, which are oriented upward. A complete topological sort of all 13,568 covering relations on all 3,054 nonempty faces verifies that this matching is acyclic.

**Five certified Morse cancellations.** Repeatedly choose two critical cells in consecutive dimensions connected by exactly one directed alternating gradient path, reverse its matching directions, and check acyclicity of the entire resulting Hasse digraph. Such cancellations preserve the homotopy type of the associated Morse CW complex. The five cancellations, written as (dimension of upper cell, upper integer mask, lower integer mask, length in downward path edges), are

\[
(5,26904,10328,2),\ (5,26916,10340,2),\ (5,38424,5272,2),
\]
\[
(5,38530,37442,2),\ (4,49442,49158,2).
\]

The exhaustive path enumerator certifies uniqueness at the moment of each cancellation, not just a nonzero boundary coefficient; the acyclicity test is repeated after each reversal. The final matching contains 1,518 pairs and leaves precisely one vertex, sixteen three-cells and one four-cell. In particular it has no critical one-, two-, or five-cells.

**Integral attaching map.** Orient every face by increasing vertex labels. Compute the signed Morse differential by recursively replacing every matched lower face with the signed combination of the other codimension-one faces of its paired upper face. This integral recursion gives a zero coefficient on **every** critical three-cell in the boundary of the sole critical four-cell. The three-skeleton of the Morse CW model is therefore a wedge of sixteen three-spheres. The attaching map of the four-cell lies in \(\pi_3(\bigvee^{16}S^3)\cong H_3(\bigvee^{16}S^3;\mathbb Z)\cong\mathbb Z^{16}\) by Hurewicz; its coordinate degrees are precisely those signed boundary coefficients. They all vanish, so the attaching map is nullhomotopic. Attaching the four-cell adds a single \(S^4\), proving the claimed integral wedge decomposition.

## Verification

The complete standalone program `verification/verify_morse.py` constructs the cube and both equivalent face predicates, examines all vertex masks, constructs the initial matching, certifies all Hasse relations, enumerates the unique gradient paths, reverses each path, checks the new directed graph for acyclicity, and computes the final signed integral Morse differential. It reports `ALL_CHECKS_PASS`; its exact output is in `verification/morse_output.txt`. The independent program `verification/verify_mod2.py` builds faces from forbidden triples and row-reduces all ordinary simplicial boundaries over \(\mathbb F_2\); its reduced Betti numbers are \(16\) in degree three and \(1\) in degree four, and zero otherwise. It reports `INDEPENDENT_MOD2_CHECKS_PASS` in `verification/mod2_output.txt`. This field computation is a consistency check, not a replacement for the integral Morse proof.

Run, from the root of the extracted package, `python3 verification/verify_morse.py` and `python3 verification/verify_mod2.py` (Python 3.9 or later; standard library only).

## Relationship to prior work

Taylan's 2015 paper [1] introduced the more general notion of devoid complexes, developed matching-tree techniques, and determined the \(P_3\)-avoiding complexes for forests, paths, and cycles. It does not state this result for the Cartesian four-cube, which is neither a forest nor a cycle. The later higher-independence treatment [2] covers complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect rooted trees. None of those families includes the four-regular cube graph. Known results for the **ordinary** independence complex of \(Q_4\), which forbids every selected edge, do not determine the strictly larger \(P_3\)-avoiding complex. The exact mixed-dimensional integral homotopy type proved here is not a Betti-number corollary of those earlier descriptions.

## Limitations

This is a finite, exact result for \(Q_4\), not a classification of \(\operatorname{Ind}_2(Q_d)\) for arbitrary \(d\). No group-equivariant homotopy type or higher-dimensional persistence statement is established. The proof relies on exhaustive but reproducible finite computations plus standard discrete Morse and Hurewicz theorems. An equivalent unindexed or unpublished prior result remains possible; no independent mathematical audit has been performed.

## References

[1] D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, first made public 2015-01-27; especially Definitions 3.8, Theorems 3.10, 3.14, 5.2. https://arxiv.org/abs/1501.06754

[2] P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first submitted 2020-01-15; especially Theorems 3.5, 3.8, 4.6, 5.6. https://arxiv.org/abs/2001.05448
