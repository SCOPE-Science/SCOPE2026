# Petersen-specific period doubling between cyclic and refractory excitation dynamics

## Finding

Two standard three-color, synchronous threshold-one automata can assign different *eventual least periods* to the same initial coloring, even though they have the same long-term synchronization-versus-activity classification. This discrepancy occurs in a controlled comparison of the two ten-vertex cubic generalized Petersen graphs. Let \(p_C(x)\) and \(p_H(x)\) be the eventual least periods of cyclic cellular automaton (CCA) and Greenberg–Hastings (GHM) evolution, respectively. Every one of the \(3^{10}=59049\) labelled initial colorings has the following exact joint classification:

| Graph | \((p_C,p_H)\) | Number of initial colorings |
| --- | --- | ---: |
| Pentagonal prism \(GP(5,1)\) | \((1,1)\) | 8409 |
| | \((3,3)\) | 2460 |
| | \((4,4)\) | 38430 |
| | \((5,5)\) | 2190 |
| | \((7,7)\) | 7560 |
| Petersen graph \(GP(5,2)\) | \((1,1)\) | 7839 |
| | \((3,3)\) | 4500 |
| | \((4,4)\) | 5040 |
| | \((5,5)\) | 27270 |
| | \((8,4)\) | **4800** |
| | \((8,8)\) | 9600 |

All omitted joint-period classes are empty. Thus periods agree pointwise on \(GP(5,1)\), whereas exactly \(4800\) initial states of \(GP(5,2)\) undergo an eight-to-four **eventual-period collapse** when the CCA rule is replaced by GHM; there are no other mismatches. These 4800 colorings form exactly **40 orbits of size 120** under the full Petersen graph automorphism group \(S_5\). In particular, none is fixed by a nontrivial spatial automorphism.

## Assumptions and scope

For \(k\in\{1,2\}\), the graph \(GP(5,k)\) has labelled vertices \(u_i,v_i\), indexed by \(i\in\mathbb Z/5\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+k}\). Both graphs are connected, cubic, and have ten vertices and fifteen edges. A configuration assigns each vertex a color in \(\{0,1,2\}\). For the *CCA* rule, a vertex of color \(c\) changes to \(c+1\pmod3\) exactly when some neighbor currently has color \(c+1\pmod3\), and otherwise remains at \(c\). For the *GHM* rule, colors \(1\to2\to0\) advance unconditionally, whereas \(0\to1\) occurs exactly when a neighbor currently has color 1. All updates are simultaneous. The eventual least period is the least positive period of the terminal temporal cycle, after an arbitrary finite transient. States and counts retain the specified vertex labels, without quotienting by temporal phase or spatial symmetry unless stated explicitly.

## Proof

**Complete finite functional-graph reduction.** Encode \(x\) as \(s=\sum_{i=0}^4x(u_i)3^i+\sum_{i=0}^4x(v_i)3^{i+5}\), a bijection from all initial configurations to integers \(0\) through \(59048\). For each of the two graphs and two update rules, `verification/verify_graph.py` constructs *every* transition and its indegree. Remove indegree-zero vertices in a queue, recursively. No removed vertex lies on a directed cycle. Conversely every remaining vertex lies on a directed cycle: a noncyclic component of a finite functional graph has a directed source of indegree zero after all upstream sources are removed. Enumerate the remaining directed cycles, assign their lengths, then process removed states in reverse removal order, assigning each the period of its successor. This proves the period assignments for the complete finite state space, not a sample or extrapolation. The computed exact joint table is recorded in `verification/verify_graph_output.json`.

**Independent complete reconstruction.** The separately written C++ checker `verification/verify_trajectories.cpp` constructs both graphs and local maps independently. For *each* of the 59049 configurations on *each* graph, it applies Floyd's tortoise-and-hare algorithm to recover both eventual least periods and both entry times, without using indegrees or the Python transition table. Its complete joint counts match each entry above (`verification/verify_trajectories_output.txt`). Thus two different exhaustive orbit algorithms and two different update implementations yield the same complete finite proof. The unique mismatch type is \((p_C,p_H)=(8,4)\), with exactly 4800 states on the Petersen graph.

**Witness and spatial symmetry.** The Petersen graph is isomorphic to \(KG(5,2)\), whose vertices are the ten two-subsets of five points and edges join disjoint pairs. For the chosen vertex order, the two-subsets are

`(0,1), (2,3), (0,4), (1,2), (3,4), (2,4), (1,4), (1,3), (0,3), (0,2)`.

Every permutation of the five points is an automorphism, yielding 120 distinct automorphisms. Conversely a maximum independent set of four vertices in \(KG(5,2)\) is necessarily the star of pairs containing one fixed point: a pairwise-intersecting family of two-subsets without a common point has at most three members. The five stars therefore recover the five underlying points intrinsically, so every graph automorphism embeds into \(S_5\); the entire group has order 120. The checker `verification/verify_symmetry.py` enumerates all 120 actions, verifies adjacency preservation and computes their orbits on precisely the 4800 discrepant configurations. All 40 orbits have size 120, establishing the geometric refinement.

For an explicit exceptional coloring, in the vertex order above take `1210210000` (base-three integer 421 with the leftmost displayed trit at \(u_0\)). It starts on a primitive eight-cycle under CCA, but enters a primitive four-cycle after two steps under GHM. Both complete orbit finders verify this witness.

## Verification

From the directory containing the embedded `verification` folder, run `python3 verification/verify_graph.py` and compare its JSON output to `verification/verify_graph_output.json`. Compile using `g++ -std=c++17 -O2 verification/verify_trajectories.cpp -o verify_trajectories`, run `./verify_trajectories`, and compare to `verification/verify_trajectories_output.txt`. Finally run `python3 verification/verify_symmetry.py` and compare to `verification/verify_symmetry_output.txt`. These tests are deterministic, use integer arithmetic, require no datasets, and exhaust all \(2\cdot3^{10}\) initial configurations in both update implementations. The two max-first-periodic-entry pairs, CCA/GHM, are \((6,8)\) on the prism and \((4,6)\) on the Petersen graph; these are auxiliary checks rather than a general-family assertion.

## Relationship to prior work

Gravner, Lyu, and Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs* (arXiv:1610.07320v1, 2016), define the two models and relate synchronization/activity to cycle circulation. Their general activity criterion is consistent with this example, but it does not determine the eventual *least temporal period* for each coloring of these particular graphs, nor the joint table above. The published *Exact recurrence and basins on the two ten-vertex generalized Petersen graphs* determines the Greenberg–Hastings census on these graphs alone: our GHM marginal totals agree exactly, but the published marginal does not distinguish the 4800 CCA-eight/GHM-four colorings. The published *Matched eventual periods but different transient clocks for three-state excitable dynamics on bicliques* proves a pointwise equality of eventual periods for complete bipartite graphs. Neither graph here is bipartite, and the Petersen result establishes a natural boundary to extrapolating that coincidence to arbitrary cubic graphs. No stronger covering joint-period classification was identified in the inspected sources; historical priority remains qualified.

## Limitations

This is an **exact finite** classification only for \(GP(5,1)\) and \(GP(5,2)\), and does not assert the same behavior for all generalized Petersen graphs or other regular graphs. It counts eventual least periods, not equality or containment of entire attractor cycles. The proof of the finite census is exhaustive computation with two inspectable, complete implementations rather than a compact symbolic case split. The spatial-orbit refinement is also finite exhaustive enumeration after identifying the full automorphism group. No independent mathematical audit has been performed. Possible unindexed earlier exact joint-period computations remain a historical-priority risk.

## References

1. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first publicly posted 2016-10-24, https://arxiv.org/abs/1610.07320 . See the definitions and Theorem 3; author-hosted full text: https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf .
2. *Exact recurrence and basins on the two ten-vertex generalized Petersen graphs*, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-recurrence-and-basins-on-the-two-ten-vertex-generalized-pe--7d4c1d4df82a/RESULT.md .
3. *Matched eventual periods but different transient clocks for three-state excitable dynamics on bicliques*, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-matched-eventual-periods-but-different-transient-clocks-for-thre--29320e9e89df/RESULT.md .
