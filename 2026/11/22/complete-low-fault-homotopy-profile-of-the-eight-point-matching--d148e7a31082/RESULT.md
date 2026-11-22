# Complete low-fault homotopy profile of the eight-point matching complex

## Finding

Let \(K_8\) be the simple complete graph on \(\{0,1,\ldots,7\}\). For any graph-edge fault set \(F\subseteq E(K_8)\) with \(|F|\leq 3\), let \(\mathcal M(K_8-F)\) be its **ordinary matching complex**: vertices are surviving graph edges and a simplex is a collection of pairwise vertex-disjoint surviving graph edges. Then, for every such \(F\),
\[
\mathcal M(K_8-F)\simeq\bigvee^{b(F)} S^2,
\]
with the following complete classification by isomorphism type of the graph formed by the faulty edges (isolated vertices are ignored):

| Number of faults | Fault graph | \(b(F)\) |
|---:|---|---:|
| 0 | empty | 132 (previously known) |
| 1 | \(K_2\) | 116 |
| 2 | \(P_3\) (incident pair) | 100 |
| 2 | \(2K_2\) (disjoint pair) | 102 |
| 3 | \(K_{1,3}\) (star) | 84 |
| 3 | \(K_3\) (triangle) | 84 |
| 3 | \(P_4\) (three-edge path) | 86 |
| 3 | \(P_3\sqcup K_2\) | 88 |
| 3 | \(3K_2\) | 90 |

Equivalently, writing \(q(F)\) for the number of unordered pairs of **disjoint faulty edges** in \(F\), all nine counts are governed by the compact rule
\[
b(F)=132-16|F|+2q(F)\qquad (|F|\leq3).
\]
In particular, two faults of different incidence types leave different numbers of integral two-spheres; three faults first permit a triangle, and the star and triangle have the same sphere multiplicity despite being nonisomorphic.

## Assumptions and scope

The graph is fixed to eight labeled vertices, with no loops or multiple edges. Exactly the ordinary edge-matching simplicial complex is meant, not a higher matching complex, perfect-matching extendibility complex, or a complex of graph vertices. The table is exhaustive only for \(0\leq |F|\leq3\). All homotopy types are integral, with no torsion. No infinite-order extension or classification for four or more faulty edges is asserted.

## Proof

**Exhaustion of fault shapes.** A simple graph of at most three edges, ignoring isolated vertices, belongs to one of the nine displayed classes. With three edges the only possibilities are three disjoint edges, a two-edge path plus a disjoint edge, a four-vertex path, a three-edge star, and a triangle. On eight vertices each representative is realized and vertex relabeling induces a simplicial isomorphism of matching complexes.

**Why the numerical profile has this form.** Inclusion-exclusion over the faulty graph edges in the alternating face sum gives the contribution of one forbidden edge as the reduced Euler characteristic of the ordinary matching complex on six remaining vertices, which is \(-16\); a disjoint forbidden pair contributes the reduced Euler characteristic of the four-vertex matching complex, which is \(2\); a disjoint forbidden triple contributes that of the two-vertex matching complex, which is \(0\). A pair of incident edges cannot simultaneously lie in a matching, so contributes nothing as a pair. Since \(|F|\leq3\), this proves \(\widetilde\chi=132-16|F|+2q(F)\). The ensuing acyclic matching, not this Euler calculation alone, proves the space has no lower or higher homotopy cells.

**Explicit finite discrete-Morse construction.** For each row take the canonical faulty-edge representatives below, with unordered endpoints written in increasing order:

- \(K_2:\ \{01\}\); \(P_3:\ \{01,02\}\); \(2K_2:\ \{01,23\}\).
- \(K_{1,3}:\ \{01,02,03\}\); \(K_3:\ \{01,02,12\}\); \(P_4:\ \{01,12,23\}\).
- \(P_3\sqcup K_2:\ \{01,02,34\}\); \(3K_2:\ \{01,23,45\}\).

Enumerate all matchings (including the empty matching), represent each as a bitmask of its edge set in lexicographic order, and apply sequential toggling: for each surviving graph edge \(e\), pair every **as-yet-unpaired** face \(\sigma\) not containing \(e\) with \(\sigma\cup\{e\}\) whenever both are present and unmatched. This defines explicit disjoint codimension-one pairs. All cover relations are enumerated; reversing each matched cover and directing all other covers upward gives an acyclic directed graph in each of the nine cases. Thus it is a complete acyclic discrete vector field on the augmented face poset.

The standalone program `k8_near_complete_verify.py` independently constructs the faces from graph edges, enumerates every pair, checks all codimension-one incidences, and topologically sorts the **entire** directed Hasse graph to certify absence of a closed gradient path. Its result is: the empty face participates in exactly one pair; every other unpaired face is a **three-edge matching**, i.e. a two-simplex; the numbers of such faces are exactly \(132,116,100,102,84,84,86,88,90\), in table order. The augmented empty-to-vertex pair may be omitted, producing one critical vertex and the listed critical two-simplices without creating a cycle (the now-unmatched empty face has no incoming Hasse arrows, and all other orientations are unchanged). Forman's finite discrete-Morse theorem gives a CW homotopy model with one zero-cell, no one-cells, \(b(F)\) two-cells, and no cells of higher dimension. Every attaching map of a two-cell into the sole zero-cell is constant, yielding precisely the stated wedge of two-spheres, without integral torsion.

**Independent face-count check.** The complete list of face-count vectors \((f_0,f_1,f_2,f_3)\) in table order is
\[
\begin{aligned}
 &(28,210,420,105),\ (27,195,375,90),\ (26,180,330,75),\
 &(26,181,336,78),\ (25,165,285,60),\ (25,165,285,60),\
 &(25,166,291,63),\ (25,167,297,66),\ (25,168,302,68).
\end{aligned}
\]
For each, the independent Euler characteristic check \(b=f_0-f_1+f_2-f_3-1\) agrees exactly with the Morse critical-cell count. For instance, disjoint two-edge faults permit one two-edge matching containing both missing graph edges in the complete reference complex, while incident faults do not; this accounts for the first different corrections in their face vectors. These Euler checks alone would not establish the homotopy type; the exhaustive acyclic matchings do.

## Verification

Run `python3 k8_near_complete_verify.py` in Python 3, requiring no external packages. The program enumerates all \(1+28+378+3276=3683\) fault sets of sizes zero through three to verify the orbit signatures, and separately verifies the nine representatives. It confirms all face vectors; the full augmented Hasse digraph is checked for acyclicity, with 316, 286, 256, 260, 226, 226, 230, 234, and 237 matched pairs, respectively. The independent Euler check agrees with the critical-face count in every case. The program terminates with `PASS` only if every check holds. It is a finite exhaustive certificate, not an inference from sampled cases.

## Relationship to prior work

Mondal, Mukherjee, and Saha establish the intact \(\mathcal M(K_8)\simeq\bigvee^{132}S^2\) (Example 3.3); this is background, not a new claim. Their theorem concerns complete graphs and does not give the distinct noncomplete fault-orbit table above. Bayer, Jelić Milutinović, and Vega study polygonal line tilings and give the standard deletion/link cofiber sequence; their graph-family results do not cover these dense near-complete graphs. Existing general split-injectivity results about integral matching homology under edge additions do not by themselves classify the damaged spaces up to homotopy or determine this incidence-sensitive nine-row profile. The new content is exactly the complete \(\leq3\)-fault homotopy table with an acyclic finite certificate; the elementary inclusion-exclusion Euler rule is used to organize the table, not presented as a separate novel theorem.

## Limitations

The result is a finite eight-vertex classification; its strength is orbit completeness through the first possible three-edge cycle, not an asymptotic or all-order theorem. The code checks the full combinatorial Morse certificate; no formal proof assistant or independent audit was involved. An unindexed equivalent published table or deduction has not been excluded, and novelty is assessed against the explicitly inspected sources and indexed comparisons.

## References

1. A. Mondal, S. Mukherjee, K. Saha, *Discrete Morse theory and the topology of matching complexes of complete graphs*, arXiv:2303.07054 (first available 2023-03-13), merged into arXiv:2305.02973; published as *Topology of matching complexes of complete graphs via discrete Morse theory*, DMTCS 26:3 (2024), Example 3.3. https://arxiv.org/pdf/2305.02973
2. M. Bayer, M. Jelić Milutinović, J. Vega, *General polygonal line tilings and their matching complexes*, arXiv:2211.12559 (first available 2022-11-22), especially Section 2 (deletion/link tools) and Section 3 (scope). https://arxiv.org/pdf/2211.12559
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete-Morse CW theorem).
