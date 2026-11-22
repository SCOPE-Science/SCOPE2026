# One-failure power domination of the four-cube: five optimal geometries and a relocation divide

## Finding

Let \(Q_4\) be the binary four-cube, with vertex set \(\mathbb F_2^4\). A **one-failure power-dominating set** is a subset \(S\) of *distinct* sensor locations such that \(S\setminus\{v\}\) power dominates \(Q_4\) for every \(v\in S\), without deleting the vertex or its incident graph edges. Then:

1. The minimum size of such an \(S\) is exactly \(4\), and there are exactly \(376\) minimum sets.
2. Put an auxiliary edge between two cube words exactly when their Hamming distance is \(3\). A four-set \(S\) is one-failure power dominating **if and only if** its auxiliary induced subgraph is \(2K_2\), \(P_4\), or \(C_4\). The respective counts are \(160\), \(192\), and \(24\). These split into five orbits under the ordinary cube automorphism group: three \(2K_2\) types of sizes \(48,96,16\), one \(P_4\) type of size \(192\), and one \(C_4\) type of size \(24\).
3. Under *token jumping*, replacing one selected vertex by any unselected vertex while preserving the one-failure requirement and size four, the \(376\) optima form a connected graph with \(2496\) edges, degrees \(12,14,16\) on the three induced-subgraph classes, radius \(5\), and diameter \(6\). Under *token sliding*, requiring the removed and inserted locations to be adjacent in the original cube, all \(376\) optima are isolated.

## Assumptions and scope

The underlying graph is the fixed simple labelled graph \(Q_4\) with vertices the sixteen four-bit words; the coordinate indexing in the verification scripts is \(0,\ldots,15\), with an edge \(uv\) when \(\operatorname{popcount}(u\oplus v)=1\). There is at most one sensor at a vertex. Failure removes one sensor, **not** a graph vertex. Given a surviving set \(A\), power domination begins by observing the closed neighborhood \(N[A]\). Thereafter, whenever an observed vertex has exactly one unobserved neighbor, that neighbor is observed; repeat until no new vertices can be observed. A set succeeds precisely when all sixteen vertices are observed. At least one failure is considered even for a singleton set. The auxiliary graph defined by Hamming distance three is *not* the graph on which sensors propagate or slide.

## Proof

**1. The complete two- and three-sensor test.** The full cube automorphism group consists of all translations and coordinate permutations. It is transitive on unordered pairs of a given Hamming distance. Directly applying the stated observation and propagation rule to \(\{0000,v\}\), for \(v=0001,0011,0111,1111\), gives respective terminal observed-set sizes \(8,8,16,10\). Thus an unordered pair power dominates exactly when its Hamming distance is three (there are \(32\) such pairs).

For unordered triples, the sorted multiset of their three pairwise Hamming distances determines their orbit under the same group: after translating one vertex to zero, the two remaining support sizes and their overlap determine a coordinate-permutation orbit. There are six types. For each, the following table gives a representative, orbit size, and terminal observed-set size obtained by explicit neighborhood propagation.

| Pairwise distances | Representative decimal vertex labels | Triples | Terminal observed vertices |
|---|---|---:|---:|
| \((1,1,2)\) | \((0,1,2)\) | 96 | 11 |
| \((1,2,3)\) | \((0,1,6)\) | 192 | 16 |
| \((1,3,4)\) | \((0,1,14)\) | 64 | 16 |
| \((2,2,2)\) | \((0,3,5)\) | 64 | 11 |
| \((2,2,4)\) | \((0,3,12)\) | 48 | 11 |
| \((2,3,3)\) | \((0,3,13)\) | 96 | 16 |

These counts sum to \(\binom{16}{3}=560\). In each successful type at least one pair has distance three; in each unsuccessful type none does. Hence **a three-vertex set power dominates exactly when it contains a distance-three pair**. The table can be regenerated without assuming this conclusion by the direct forcing checker, which processes every one of the \(560\) triples.

**2. Geometry and sharp optimum.** Let \(H\) be the graph on the same sixteen words, joining pairs at distance three. Its edges always join opposite parity classes, so \(H\) has no triangle. Any putative one-failure three-set would have to leave a power-dominating pair after each of three deletions, forcing a triangle in \(H\), which is impossible. A one-failure four-set \(S\) requires every triple of \(S\) to contain an edge of \(H\); equivalently \(\alpha(H[S])\le2\). Since \(H\) is triangle-free, the only induced four-vertex graphs with independence number at most two are \(2K_2\), \(P_4\), and \(C_4\). The stated examples show this condition is attainable.

The four weight-three vectors \(1111\oplus e_i\), \(i=1,2,3,4\), form a basis of \(\mathbb F_2^4\): the linear map \(T(x)=x\oplus(\operatorname{parity}(x))1111\) satisfies \(T^2=\mathrm{id}\) and sends weight-one differences exactly to weight-three differences. Hence \(H\cong Q_4\). The ordinary cube has \(32\) edges and \(24\) four-cycles. A \(P_4\) is uniquely determined by a middle edge and an ordered choice of distinct additional directions at its endpoints, giving \(32\cdot3\cdot2=192\) induced \(P_4\)'s. The number of unordered disjoint edge pairs is \(\binom{32}{2}-16\binom{4}{2}=400\). Each \(P_4\) contributes one such pair and each \(C_4\) two, leaving \(400-192-2\cdot24=160\) induced \(2K_2\)'s. Thus \(160+192+24=376\).

Parallel \(2K_2\)'s in \(H\cong Q_4\) have transverse separation two or three, giving respectively \(4\cdot12=48\) and \(4\cdot4=16\) sets; the other \(96\) have nonparallel edges. The types are invariant under cube automorphisms and are each a single orbit: the claim follows either by moving their edge directions and displacements using coordinate permutations and translations, or by the exhaustive orbit checker. Representative decimal labels, in the original cube, are \((0,1,6,7)\), \((0,1,6,14)\), \((0,1,14,15)\), \((0,1,6,11)\), and \((0,3,13,14)\), in that five-type order.

**3. Exact relocation.** For the \(376\) four-sets classified above, construct the token-jump adjacency graph by testing each of the \(4\cdot12\) possible one-for-one replacements; a replacement is accepted if and only if the resulting four-set has one of the three allowed auxiliary induced-subgraph forms. This is a finite exhaustive algorithm with no search heuristic. Both supplied verifiers reconstruct all \(376\) states independently, enumerate these candidate moves, and perform breadth-first search from every state. The undirected jump graph has \(2496\) edges. Its unordered-pair distance histogram for distances \(1,2,3,4,5,6\) is \(2496,13536,29520,22992,1932,24\), summing to \(\binom{376}{2}\). Consequently it is connected, has radius five and diameter six; \(328\) states have eccentricity five and \(48\) have eccentricity six. All candidate jumps corresponding to an original cube edge fail the membership test, so the token-slide graph has no edges. The short exhaustive procedures and expected exact counts appear in the attached checkers, rather than relying on logs as proof.

## Verification

Compile and run `verify_direct.cpp` with `c++ -std=c++17 -O2 verify_direct.cpp -o verify_direct && ./verify_direct`; run `verify_structural.py` with `python3 verify_structural.py`. The first program evaluates propagation independently on **every** one of the \(2^{16}=65536\) vertex subsets, tests all single-sensor deletions, and checks optimal relocation paths. The second constructs the distance-three graph directly, enumerates four-subsets, their five symmetry orbits and the same relocation graph, without calling or implementing the power-domination propagation routine. Both exit with an assertion failure on a mismatch, and require no nonstandard libraries. Their distinct methods agree on the shared finite claims. The computed full one-failure cardinality polynomial (not required for the classification proof) is

\[
376z^4+3328z^5+7832z^6+11440z^7+12870z^8+11440z^9+8008z^{10}+4368z^{11}+1820z^{12}+560z^{13}+120z^{14}+16z^{15}+z^{16}.
\]

## Relationship to prior work

Dean, Ilic, Ramirez, Shen and Tian (2011) proved the unprotected power domination number \(\gamma_P(Q_4)=2\) through their exact power-domination result on power-of-two-dimensional cubes. The general concept of vertex-fault-tolerant power domination predates the present result (Pai, Chang and Wang, 2010); the 2023 work of Bjorkman and Conrad distinguishes distinct-location faults from sensor-multiset defects and develops broad bounds. Bjorkman, Conrad and Flagg (2023) develop the multiset variant for complete bipartite and block graphs, not the distinct-location four-cube classification. Bjorkman and collaborators (2026) study reconfiguration of *ordinary* minimum power domination; their general framework does not identify the robust optima here. The present assertions concern the complete distinct-location one-failure optimum geometry and its two different relocation rules; they do not claim that power domination or one-failure robustness are new notions.

## Limitations

The theorem is confined to the finite graph \(Q_4\), one failed sensor, and distinct sensor locations. It does **not** characterize higher-dimensional hypercubes, multiset sensor allocations, two or more failures, or relocations passing through larger nonoptimal intermediate sets. Reconfiguration paths under jumping preserve the four-sensor budget and robustness at each step. The proof uses small exhaustive computations for the triple-orbit closure table and exact relocation distances. Independently authored mathematical review and complete publication-priority clearance have not been performed.

## References

- N. Dean, A. Ilic, I. Ramirez, J. Shen and K. Tian, *On the Power Dominating Sets of Hypercubes*, 14th IEEE International Conference on Computational Science and Engineering (2011), DOI: https://doi.org/10.1109/CSE.2011.211 ; accessible full text: https://kjtian.github.io/PDSHypercube.pdf .
- K.-J. Pai, J.-M. Chang and Y.-L. Wang, *Restricted power domination and fault-tolerant power domination on grids*, Discrete Applied Mathematics 158 (2010), 1079–1089, https://doi.org/10.1016/j.dam.2010.03.001 .
- B. Bjorkman and E. Conrad, *Introduction to Robust Power Domination*, first publicly posted May 22, 2023, https://arxiv.org/abs/2305.13430 .
- B. Bjorkman, E. Conrad and M. Flagg, *An Introduction to PMU-Defect-Robust Power Domination: Bounds, Bipartites, and Block Graphs*, December 12, 2023, https://arxiv.org/abs/2312.07377 .
- B. Bjorkman et al., *Power Domination Reconfiguration*, La Matematica 5, article 8 (2026), https://doi.org/10.1007/s44007-025-00187-5 .
