# Complete one-, two-, and three-edge-fault Morse homotopy profile of \(K_{3,3}\)

## Finding
Let \(K_{3,3}\) be the complete bipartite graph on shores \(A=\{0,1,2\}\) and \(B=\{3,4,5\}\). For each \(F\subseteq E(K_{3,3})\) with \(|F|\le3\), the ordinary simplicial Morse complex \(\mathcal M(K_{3,3}-F)\) has the exact **integral homotopy type** in the following exhaustive table. In this table \(\bigvee^k S^d\) denotes a wedge of \(k\) spheres, and \(\ast\) denotes a contractible space.

| Fault orbit | Representative deleted edges | Exact homotopy type |
|---|---|---|
| No edges (previously known) | none | \(\bigvee^{80}S^4\) |
| One edge | \(\{03\}\) | \(S^3\vee\bigvee^{17}S^4\) |
| Two incident edges | \(\{03,04\}\) | \(\bigvee^4S^3\) |
| Two disjoint edges | \(\{03,14\}\) | \(\bigvee^2S^3\vee\bigvee^2S^4\) |
| Three-edge star | \(\{03,04,05\}\) | \(\bigvee^8S^3\) |
| Three-edge path on four vertices | \(\{03,04,13\}\) | \(\ast\) |
| Two-edge path and disjoint edge | \(\{03,04,15\}\) | \(\bigvee^4S^3\) |
| Three disjoint edges | \(\{03,14,25\}\) | \(\bigvee^2S^3\vee\bigvee^2S^4\) |

Here \(03\) abbreviates the unordered graph edge \(\{0,3\}\), etc. In particular, the three-edge path is **the first possible contractible fault**: no fault set with at most two edges has a contractible Morse complex. The intact case is credited to an earlier computation, not asserted as a new discovery.

## Assumptions and scope
The underlying graph is the unfilled one-dimensional simplicial complex \(K_{3,3}-F\). A vertex of \(\mathcal M(G)\) is one incident vertex-edge pair \((v,e)\) in \(G\). A collection is a simplex when no vertex or edge is used in more than one pair and its induced arrows from \(v\) along \(e\) have no directed cycle (the graph form of Forman's closed-gradient-path condition). Equivalently, these simplices are partial orientations of rooted forests. This is neither the ordinary graph edge-matching complex nor the generalized or strong Morse complex. All coefficients and attaching-map conclusions are over the integers; there is no asymptotic or higher-fault claim.

## Proof
**Symmetry and exhaustiveness.** The automorphism group of \(K_{3,3}\) contains the \(72\) shore-preserving and shore-interchanging bijections \((\mathfrak S_3\times\mathfrak S_3)\rtimes C_2\). Its action on subsets of the nine edges of cardinality at most three has exactly the eight orbits displayed in the table. `verify.py` explicitly generates every automorphism, computes the orbit of each listed fault representative, and establishes that their union is all \(\sum_{j=0}^3\binom9j=130\) fault sets, rather than relying on a sampled classification.

**Exact face enumeration.** Order the surviving graph edges lexicographically and, for each, introduce both possible oriented incidences \((v,e)\) (one for each endpoint). Encode a face as a nonzero bitmask on these incidences. Enumerate all masks, keeping only those that use each vertex and edge at most once and induce no directed cycle. No face uses more than five incidences because six distinct tails in a finite six-vertex directed graph with an outgoing arrow at each vertex would contain a directed cycle. Therefore the finite enumeration is exhaustive.

**Acyclic face-poset matching.** For each fault orbit, `verify.py` fixes an explicit permutation of incidence indices. Process the indices in that order. At a pivot \(p\), pair each still-unmatched face \(\sigma\) omitting \(p\) with \(\sigma\cup\{p\}\), whenever both are currently unmatched faces. The verifier constructs every cover relation in the nonempty face poset, reverses exactly the paired cover relations and performs a full topological sort of the resulting directed Hasse graph. This certifies acyclicity, so Forman's matching theorem supplies a homotopy-equivalent CW complex with precisely the unmatched simplices as cells. Here are the independently reproducible exact counts:

| Fault orbit | Nonempty simplices | Paired face pairs | Critical cells by dimension |
|---|---:|---:|---|
| None | 1791 | 855 | \(c_0=1,c_4=80\) |
| One edge | 1023 | 502 | \(c_0=1,c_3=1,c_4=17\) |
| Two incident | 527 | 261 | \(c_0=1,c_3=4\) |
| Two disjoint | 575 | 285 | \(c_0=1,c_3=2,c_4=2\) |
| Three-star | 215 | 103 | \(c_0=1,c_3=8\) |
| Three-path | 271 | 135 | \(c_0=1\) |
| Path plus disjoint edge | 287 | 141 | \(c_0=1,c_3=4\) |
| Three disjoint | 319 | 157 | \(c_0=1,c_3=2,c_4=2\) |

**Integral attaching maps.** In every case the critical CW model has a single \(0\)-cell and no \(1\)- or \(2\)-cells. The only potentially nonzero cellular boundary is \(\partial_4:C_4\to C_3\). The program reconstructs the oriented simplicial boundaries and evaluates the signed gradient-path cancellation recurrence for *every* critical \(4\)-cell, with exact integer arithmetic, proving \(\partial_4=0\) in every case. Hence the \(3\)-skeleton is \(\bigvee^{c_3}S^3\); the integral Hurewicz isomorphism \(\pi_3(\bigvee^{c_3}S^3)\cong H_3(\bigvee^{c_3}S^3;\mathbb Z)\) makes each \(4\)-cell attaching map nullhomotopic. Consequently the whole complex is \(\bigvee^{c_3}S^3\vee\bigvee^{c_4}S^4\), with the tabulated ranks. When both counts vanish, it is contractible. This proves the homotopy types over \(\mathbb Z\), not merely field-homology ranks.

## Verification
The embedded `verify.py` is a standalone Python 3 program using only the standard library. Run `python3 verify.py`. It independently checks orbit coverage; enumerates all faces; reconstructs the face-poset matching; tests the whole oriented Hasse graph for cycles; checks the exact signed integer degree matrix \(\partial_4\); and computes mod-two homology from the original simplicial chain complex as a cross-check. Its final line is `PASS: all 130 fault sets covered by eight orbits; exact integral Morse certificates verified`. It uses no randomness and accepts no outside files or unpublished tables. The script contains the critical pivot orders, so the finite proof can be reproduced without relying on the result table.

## Relationship to prior work
The existing intact calculation *The Morse complex of \(K_{3,3}\) is a wedge of \(80\) four-spheres* determines only \(F=\varnothing\) and is credited as such. Its stated scope does not cover graph-edge faults. Scoville–Zaremsky's *Higher connectivity of the Morse complex* gives general connectivity bounds and discusses complete bipartite graphs in Example 4.6, but does not determine the damaged complexes. The strong-collapse and star-cluster approaches of Lin–Scoville / Donovan–Lin–Scoville and Donovan–Scoville concern other graph families or connectivity conditions; none of the inspected specific theorems determines this complete seven-orbit fault profile. The distinction between ordinary discrete Morse complexes and ordinary graph matching complexes is essential to the comparison.

## Limitations
This is a finite, complete fault classification for this single six-vertex base graph, not a theorem for all bicliques or more than three missing edges. The homotopy equivalences use an exact exhaustive discrete-Morse certificate; the program's verification is necessary to check the listed incidence orders and gradient cancellations. No statement about the behavior of inclusion-induced maps between different faults is claimed. Bibliographic searches and inspected accessible texts do not exclude an unindexed or differently phrased equivalent calculation. Independent expert validation has not been performed.

## References
1. M. Lin and N. A. Scoville, *Strong collapses of the Morse complex*, first public preprint of arXiv:1909.11440, 25 September 2019; developed into C. Donovan, M. Lin, and N. A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, https://arxiv.org/abs/1909.11440.
2. N. A. Scoville and M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481, https://arxiv.org/abs/2004.10481.
3. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780, https://arxiv.org/abs/2207.13780.
4. *The Morse complex of \(K_{3,3}\) is a wedge of \(80\) four-spheres*, previously published exact intact case, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-the-morse-complex-of-k-3-3-is-a-wedge-of-80-four-spheres--ada39e4b9bea/RESULT.md.
