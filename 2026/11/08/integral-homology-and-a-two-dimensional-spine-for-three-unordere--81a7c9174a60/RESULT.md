# Integral homology and a two-dimensional spine for three unordered points on the Petersen graph

## Finding

Let \(P\) be the Petersen graph, realized as a one-dimensional CW complex. For the unordered configuration space
\[
B_3(P)=\{\{x_1,x_2,x_3\}\subset|P|:\ x_i\ne x_j\text{ for }i\ne j\},
\]
there is an explicit finite collapse onto a two-dimensional CW subcomplex. Its integral homology is
\[
H_i(B_3(P);\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^6\oplus\mathbb Z/2\mathbb Z,&i=1,\\
\mathbb Z^{25},&i=2,\\
0,&i\ge3.
\end{cases}
\]
The degree-one group is included for completeness and is already determined by established general results. The specifically new claims are the exact free rank in degree two for this canonical nonplanar graph and the constructive two-dimensional spine.

## Assumptions and scope

The graph has vertices \(0,\dots,9\). Its 15 edges consist of an outer pentagon \(\{i,i+1\}\) (indices modulo five), five spokes \(\{i,i+5\}\), and an inner five-point star \(\{5+i,5+(i+2)\}\). Graph edges are unit topological intervals; neither a metric constraint nor a discretization of the particle positions appears in the definition of \(B_3(P)\). Particles are unordered and must remain distinct.

Subdivide each of the 15 original graph edges once, giving \(25\) vertices and \(30\) edges. Distinct essential (degree-three) vertices are separated by at least two new edges. Every non-nullhomotopic loop has at least ten new edges because the original Petersen graph has girth five. With three particles, the stable-equivalence theorem of Prue–Scrimshaw, Theorem 3.2, applies: the unordered discrete cubical configuration model is homotopy equivalent to \(B_3(P)\). This theorem is the topological bridge between the finite cell computation and the continuous configuration space.

## Proof

A \(k\)-dimensional cubical cell of the discrete model consists of \(k\) distinct open edges with pairwise disjoint closures together with \(3-k\) distinct vertices outside all chosen edge endpoints. For \(0\le k\le3\), exhaustive enumeration gives the cell vector
\[
(c_0,c_1,c_2,c_3)=(2300,7590,8190,2880).
\]
The accompanying self-contained `verify.py` constructs these cells directly, repeats their counting independently from the edge selections, and computes every signed cubical boundary. With edge coordinates ordered increasingly, its lower endpoint has sign \((-1)^{j+1}\) and upper endpoint has sign \((-1)^j\) in zero-based coordinate \(j\). For every \(2\)- and \(3\)-cell it checks \(\partial^2=0\) using exact integer arithmetic.

Consider a cubical face with exactly one currently remaining codimension-one coface. This face and its unique coface form a genuine free face–cell pair, so both may be removed by an elementary collapse, retaining homotopy type. The verifier deterministically applies this rule \(7260\) times, including removal of all \(2880\) original three-cells. The surviving subcomplex has cell vector
\[
(1297,3210,1933,0),
\]
and every retained cell has its entire boundary retained. In particular the space has a two-dimensional CW spine, not merely vanishing third homology.

The surviving one-skeleton is connected. A spanning tree has \(1296\) edges. Contracting it to a point is a homotopy equivalence and yields \(1914\) one-cells and \(1933\) two-cells. Their exact integer degree-two boundary matrix has \(1914\) rows, \(1933\) columns and \(4605\) nonzero entries. Applying explicit unimodular row and column eliminations at entries of absolute value one isolates \(1907\) unit invariant factors. The residual matrix has seven rows and 26 columns; all eight remaining nonzero entries occupy a single row and have absolute value two. Its only nonzero Smith invariant is two. Thus the full Smith form has nonzero factors
\[
\underbrace{1,\ldots,1}_{1907\text{ factors}},\quad 2,
\]
and \(\operatorname{rank}\partial_2=1908\). Since the contracted CW spine has a single vertex and no cells of dimension three, the cellular groups give
\[
H_1\cong\mathbb Z^{1914-1908}\oplus\mathbb Z/2\mathbb Z,
\qquad H_2\cong\mathbb Z^{1933-1908}.
\]
All dimensions above two vanish. The Euler characteristic cross-check is \(2300-7590+8190-2880=20=1-6+25\).

All reductions are finite exhaustive exact computations on specified graph cells. In particular, no modular-rank inference, floating-point assumption, or timeout is treated as an integral homology proof.

## Verification

Run `python3 verify.py` using Python 3 and its standard library only. It reproduces all face counts, verifies both boundary-square identities, exhaustively performs the free-face collapses, constructs the spanning-tree quotient, and carries out the complete integer unit-pivot reduction. The included `verification_output.txt` records the expected stdout, ending with `ALL_CHECKS_PASS`. A primitive residual row of entries \(\pm2\) distinguishes cyclic two-torsion from a field-only Betti-number computation.

## Relationship to prior work

Prue–Scrimshaw (2009, arXiv:0909.5511) provides the configuration-space equivalence used here, without this Petersen computation. Ko–Park (2011, arXiv:1101.2648) gives general graph-braid first-homology methods: the degree-one summand is not claimed as new. An–Drummond-Cole–Knudsen (2017, arXiv:1708.02351) gives a more general homological chain framework. Maciążek–Sawicki (2019, DOI:10.1007/s00220-019-03583-5) analyzes graph configuration homology and reports data for other particle numbers on the Petersen-family graphs (in its Table 2, the ten-vertex member occurs for four and six particles), but that table does not state the three-particle integer group computed here. The closest general product-cycle statement, Maciążek–Sawicki Theorem 12, gives generation in degree two under a single high-valence-vertex hypothesis; it does not supply independent relations or the numerical rank \(25\), and the Petersen graph has no vertex of degree greater than three. No inspected general result supplies the explicit collapse certificate. Published calculations for three particles on the Heawood and Pappus graphs concern different graphs; a previously recorded two-particle Petersen result concerns a different configuration space. Matching those broader or neighboring results to the present claim requires an implication, not merely similar nomenclature.

## Limitations

This establishes only integral homology and existence of the indicated two-dimensional CW spine, not the full homotopy type, the integral cohomology ring or the action of the Petersen automorphism group. The degree-one result is not a novelty claim. It does not classify three-particle configurations on other cubic graphs or other particle numbers. A targeted literature and mathematical-record comparison did not find the precise degree-two group and collapse, but cannot establish definitive publication priority; equivalent unindexed treatments remain possible. Independent mathematical audit has not been performed.

## References

- P. Prue and T. Scrimshaw, *Abrams's Stable Equivalence for Graph Braid Groups*, first public preprint 2009-09-30, arXiv:0909.5511, https://arxiv.org/abs/0909.5511, especially Theorem 3.2.
- K. Ko and H. Park, *Characteristics of Graph Braid Groups*, first public preprint 2011-01-13, arXiv:1101.2648, https://arxiv.org/abs/1101.2648.
- B. An, G. Drummond-Cole and B. Knudsen, *Subdivisional Spaces and Graph Braid Groups*, arXiv:1708.02351, https://arxiv.org/abs/1708.02351.
- T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, Communications in Mathematical Physics 371 (2019), 921–973, https://doi.org/10.1007/s00220-019-03583-5, Tables 1–2 and Sections 4–5.
- B. An and B. Knudsen, *On the Second Homology of Planar Graph Braid Groups*, arXiv:2008.10371, https://arxiv.org/abs/2008.10371; its planar hypotheses exclude the Petersen graph.
