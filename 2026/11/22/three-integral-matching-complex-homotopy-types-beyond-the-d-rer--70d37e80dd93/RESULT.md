# Three integral matching-complex homotopy types beyond the Dürer graph

## Finding
For \(n\in\{7,8,9\}\), the ordinary matching complexes of the generalized Petersen graphs \(G_n=\operatorname{GP}(n,2)\) have these **exact integral homotopy types**:
\[
\begin{aligned}
\mathcal M(G_7)&\simeq\bigvee^{28}S^4,\\
\mathcal M(G_8)&\simeq\bigvee^2S^4\vee\bigvee^{16}S^5,\\
\mathcal M(G_9)&\simeq\bigvee^{42}S^5.
\end{aligned}
\]
The middle complex has nonzero reduced integral homology in two adjacent degrees, while the two neighbors are single-dimensional wedges. All three are torsion-free. These assertions are about the ordinary graph-edge matching complex, not the two-independence complex or perfect-matching complex.

## Assumptions and scope
For each listed \(n\), define \(G_n\) on vertices \(u_i,v_i\), with \(i\in\mathbb Z/n\mathbb Z\), and exactly the \(3n\) undirected graph edges \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), and \(\{v_i,v_{i+2}\}\). The graph is simple and cubic. Its matching complex has one simplicial vertex for each graph edge; a face is any subset of graph edges with pairwise disjoint endpoints. There are no extra restrictions (in particular, a face need not be extendable to a perfect matching). All conclusions are nonequivariant integral homotopy statements for the three finite graphs only.

Represent the graph vertices as integers \(i\) and \(n+i\). Lexicographically sort the \(3n\) undirected graph edges, and encode a simplex by a bitmask specifying its selected edges; this determines graph construction, orientations, and every certificate in `verification/verify.py`.

## Proof
**Exhaustive face set.** Recursive search on increasing graph-edge indices adds an edge precisely when neither of its endpoints is occupied. This produces each matching exactly once. The augmented face counts (including the empty face) for \(n=7,8,9\) are respectively \(3418,10990,34880\), so the nonempty counts are \(3417,10989,34879\).

**Acyclic discrete-Morse matching.** Begin with the complete augmented face poset. For each graph-edge index \(j\) in increasing order, pair every then-available lower face not containing \(j\) with its upper face obtained by adding \(j\), whenever both are available. Remove all stage pairs, then continue to the next \(j\). A directed Hasse graph has every unmatched covering relation oriented toward the smaller face and every matched relation reversed. Complete topological sorting processes every augmented face and verifies acyclicity. The matching counts are respectively \(1693,5477,17404\), and the numbers of checked covering relations are \(14329,52712,187857\).

The empty simplex is matched with one zero-dimensional simplex. Removing only this pair (and ignoring the empty face as a geometric CW cell) produces one critical vertex and does not create a directed cycle because the empty simplex then has no outgoing Hasse arrows. The remaining positive-dimensional critical-cell multiplicities are
\[
\begin{array}{c|cc}
n&\text{degree}&\text{number of critical cells}\\\hline
7&3,4&2,30\\
8&4,5&11,25\\
9&5,6&57,15.
\end{array}
\]
No other critical cells occur.

**Exact integral Morse boundaries.** Orient simplex vertices by increasing graph-edge index. For each matched codimension-one relation \(a\subset b\), its simplicial incidence coefficient is \(\pm1\). The `down` recurrence in the verifier explicitly expands every gradient path over the integers: project a critical lower-dimensional cell to itself; project a matched upper cell to zero; and solve the matched upper boundary relation for each matched lower cell using its unit incidence coefficient. The recurrence is finite because the complete matching is acyclic. Applying this projection to the oriented simplicial boundary of every critical upper cell yields the exact integer Morse differential. No sampled or modular computation is substituted for this differential.

The only nontrivial matrices are of sizes \(2\times30\), \(11\times25\), and \(57\times15\). Integral row and column elimination, using **only pivot entries \(\pm1\)** and recording a zero residual matrix, yields respectively \(2,9,15\) unit factors. Consequently the remaining critical degrees have ranks
\[
\begin{array}{c|cc}
n&\text{lower degree}&\text{upper degree}\\\hline
7&0&28\\
8&2&16\\
9&42&0.
\end{array}
\]
Each surviving integral homology group is free; all other positive-degree groups vanish.

**From integer degrees to homotopy type.** Each Morse CW complex has a single zero-cell and cells in exactly two adjacent dimensions \(d,d+1\), with \(d\ge3\). Its \(d\)-skeleton is a wedge of \(d\)-spheres. Since \(\pi_d(\bigvee S^d)\cong H_d(\bigvee S^d;\mathbb Z)\), each attaching map is determined by its signed integer degree vector. The unit-pivot row and column transformations correspond to homotopy equivalences of the wedge and elementary changes in attaching cells. Each pivot therefore cancels one \(d\)- and one \((d+1)\)-cell homotopically; the zero residual means all remaining upper cells attach trivially. The displayed integral sphere-wedge equivalences follow.

## Verification
Run `python3 verification/verify.py` with Python 3.10 or later. The verifier uses only the standard library. It independently generates each graph, checks degrees and edge counts, exhaustively enumerates matching faces, constructs both ascending and descending edge-order discrete-Morse matchings, checks every directed face-poset covering relation for acyclicity, and computes exact signed integral Morse boundaries and unit-only reductions. An independent direct simplicial chain-rank calculation over \(\mathbb F_2\) agrees with each lower/upper multiplicity for the ascending reductions. The same routine additionally checks the already-known \(n=6\) Dürer case as a control; that control is not a newly asserted result. The expected output is in `verification/expected.txt` and ends in `ALL EXACT CHECKS PASS`.

## Relationship to prior work
The ordinary matching complex of \(\operatorname{GP}(5,2)\), the Petersen graph, was previously identified as \(\bigvee^5S^2\vee\bigvee^5S^3\). The ordinary matching complex of \(\operatorname{GP}(6,2)\), the Dürer graph, was previously identified as \(\bigvee^{22}S^3\). **Neither prior classification is new here.** The nearest published four-case classification for \(\operatorname{GP}(n,2)\) with \(n=6,7,8,9\) concerns the *two-independence complex on graph vertices*, whereas the complexes calculated here consist of pairwise disjoint *graph edges*. There is no object-preserving implication between those claims. Other published ordinary matching-complex calculations concern graphs such as \(\operatorname{GP}(12,5)\), not these three \(\operatorname{GP}(n,2)\) parameters.

The general sphere-wedge theorem for matching complexes of forests does not apply: each graph here contains cycles. The published matching-complex theorem for outerplanar graphs likewise does not cover these graphs: a nonempty cubic graph cannot be outerplanar, since finite outerplanar graphs have a vertex of degree at most two. Equivalently, \(\mathcal M(G_n)=\operatorname{Ind}(L(G_n))\), but a result for ordinary independence complexes of \(G_n\) (as opposed to its line graph) is not a result about \(\mathcal M(G_n)\). Source searches and source-content comparisons found no implication establishing the present three types; this does not prove global priority.

## Limitations
This is an exact complete classification of three consecutive natural finite graph parameters, not a universal formula for all \(n\). No equivariant representation, recurrence, shellability statement, or periodicity is claimed. Reproducible finite exhaustive calculations prove these finite cases; they do not prove statements beyond them. Unindexed or inaccessible coincident calculations remain possible. No independent external mathematical audit has been performed.

## References
1. *Four intermediate higher-independence homotopy types in the generalized Petersen family*, public mathematical record dated 2026-10-25, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-four-intermediate-higher-independence-homotopy-types-in-the-gene--1c34d1c9107e/RESULT.md.
2. *The Dürer matching complex: an integral sphere wedge and its full dihedral character*, public mathematical record dated 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-d-rer-matching-complex-an-integral-sphere-wedge-and-its-full--29af2a0878b2/RESULT.md.
3. *Integral homotopy type of the Petersen graph matching complex*, public mathematical record dated 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-integral-homotopy-type-of-the-petersen-graph-matching-complex--134e2131d746/RESULT.md.
4. R. Pandey, *Parity-Dependent Real-Rootedness in Independence Polynomials of Generalized Petersen Graphs*, arXiv:2601.03293v1, initially posted 2026-01-05, https://arxiv.org/abs/2601.03293 (background on the graph family, not a matching-topology result).
5. M. Bayer, M. Jelić Milutinović, and J. Vega, *Matching complexes of outerplanar graphs are contractible or wedges of spheres*, arXiv:2411.04601, https://arxiv.org/abs/2411.04601 (inapplicable outerplanarity hypothesis).
6. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete-Morse foundations).
