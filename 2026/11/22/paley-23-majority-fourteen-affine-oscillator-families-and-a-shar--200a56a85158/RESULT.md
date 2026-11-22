# Paley-23 majority: fourteen affine oscillator families and a sharp ten-step consensus tail

## Finding
On the canonical quadratic-residue Paley tournament on twenty-three labelled vertices, synchronous strict out-neighbor binary majority has exactly two fixed configurations and **3,542 primitive temporal four-cycle orbits**, with no other recurrent periods. Every one of its \(2^{23}=8{,}388{,}608\) initial configurations is periodic after at most ten updates, and the cutoff is sharp: precisely \(1{,}012\) configurations first become periodic at step ten, all entering consensus. Equivalently, its global map \(F\) satisfies
\[
\boxed{F^{14}=F^{10},\qquad F^{13}\ne F^9.}
\]
The entire four-cycle population splits into fourteen disjoint classes under the order-\(253\) affine symmetry group of the quadratic-residue tournament. Each class contains exactly \(253\) temporal orbits, so each orbit has trivial stabilizer in that group. Every four-cycle is **half-complementary**:
\[
\boxed{F^2(x)=\mathbf1-x\quad\text{for every primitive four-periodic configuration }x.}
\]
The all-state attraction-basin total is \(69{,}828\) for four-cycles and \(8{,}318{,}780\) for consensus; each of the two unanimous equilibria attracts exactly \(4{,}159{,}390\) configurations. Under uniform initialization, the probability of eventual oscillation is precisely \(17{,}457/2{,}097{,}152\). The final-entry shell has four full affine orbits of \(253\) initial configurations each, paired into two pairs by global bit complementation.

The complete first-periodic-entry census, stratified by eventual least temporal period, is:

| First entry time | Period one | Period four |
|---:|---:|---:|
| 0 | 2 | 14,168 |
| 1 | 556,140 | 29,854 |
| 2 | 4,746,326 | 9,108 |
| 3 | 2,061,996 | 8,602 |
| 4 | 628,958 | 4,048 |
| 5 | 174,064 | 3,036 |
| 6 | 89,562 | 1,012 |
| 7 | 33,902 | 0 |
| 8 | 16,192 | 0 |
| 9 | 10,626 | 0 |
| 10 | 1,012 | 0 |

The fourteen class representatives (minimum phase encoding) and their **individual four-cycle basin sizes** are:

| Representative | Four-cycle orbits in class | Basin per four-cycle |
|---:|---:|---:|
| 15611 | 253 | 6 |
| 20431 | 253 | 12 |
| 22511 | 253 | 6 |
| 23167 | 253 | 22 |
| 30571 | 253 | 4 |
| 38395 | 253 | 10 |
| 44671 | 253 | 30 |
| 56699 | 253 | 6 |
| 61177 | 253 | 6 |
| 61263 | 253 | 22 |
| 73455 | 253 | 20 |
| 81641 | 253 | 64 |
| 105851 | 253 | 58 |
| 105971 | 253 | 10 |

The size-\(253\) affine classes of initial states attaining the sharp ten-update delay have minimum encodings \(23807,32675,61245,103805\). Complementation swaps the first with the second and the third with the fourth; it preserves each of the fourteen four-cycle classes.

## Assumptions and scope
Let the vertex set be \(\mathbb Z/23\mathbb Z\), and let the nonzero quadratic residues be
\[
Q=\{1,2,3,4,6,8,9,12,13,16,18\}.
\]
Orient an arc \(i\to j\) when \(j-i\pmod{23}\in Q\). Every vertex has exactly eleven outgoing arcs and no self-loop. A configuration is \(x\in\{0,1\}^{23}\), and the synchronous update rule is
\[
F(x)_i=\mathbf1\!\left\{\sum_{q\in Q}x_{i+q}\ge6\right\}.
\]
No tie occurs because each local neighborhood has eleven vertices. A configuration has first-periodic-entry time \(\tau(x)\) equal to the smallest \(t\ge0\) such that \(F^{t+k}(x)=F^t(x)\) for some positive integer \(k\); its eventual least period is the smallest such \(k\) at \(t=\tau(x)\). All initial states are labelled; a temporal orbit groups its phases, but rotations or affine relabellings are **not** identified when counting the \(3{,}542\) primitive orbits.

Encode each configuration by the integer \(\sum_{i=0}^{22}2^ix_i\), with vertex zero the least significant bit. The affine transformations \(i\mapsto si+a\), for \(a\in\mathbb F_{23}\) and \(s\in Q\), form a group of order \(23\cdot11=253\). They preserve the directed graph and commute with \(F\). Bit complementation \(x\mapsto\mathbf1-x\) also commutes with \(F\), because the local majority has odd arity.

## Proof
**Fixed points.** Both unanimous words are fixed. If a nonunanimous fixed configuration has \(s\) vertices in state one and \(t\) in state zero, every vertex in either class must have at least six outgoing neighbors in its own class. Each induced class is a tournament, so double counting its internal arcs gives \(s(s-1)/2\ge6s\) and \(t(t-1)/2\ge6t\). Therefore \(s,t\ge13\), contradicting \(s+t=23\). Hence there are exactly two fixed configurations.

**Exhaustive finite functional graph.** The first standalone implementation, `verification/census.cpp`, generates the eleven-neighbor masks from the squares modulo twenty-three. It computes one successor for **each** integer state from zero through \(2^{23}-1\). Its in-degree queue removes precisely the nonrecurrent vertices, since a vertex survives the queue if and only if it lies on a directed cycle of this finite functional graph. The remaining vertices are traversed into disjoint temporal cycles, without truncation. Reading removed vertices in reverse queue order gives their exact first-entry times, eventual periods, and the identity of the attracting cycle. Counting those identities yields every basin size. This constructive finite algorithm yields exactly two cycles of length one and \(3542\) cycles of length four; the complete first-entry census is the table above. In particular, the largest first entry is ten and its population is \(1012\).

**Independent iterate calculation.** `verification/iterates.cpp` reconstructs the quadratic-residue neighbor masks differently: it tests Euler's criterion \(d^{11}\equiv1\pmod{23}\) for each nonzero difference. It builds \(F\), then \(F^2\) and \(F^4\), and separately iterates every original binary state to each time \(t\) from zero through ten. It checks whether each image is fixed by \(F^4\), distinguishes one-cycles from four-cycles, and explicitly rejects a two-periodic nonfixed point. Every initial state passes the four-return test by step ten but not all pass at step nine. Consequently, on the **entire** finite configuration set, \(F^{14}=F^{10}\), while \(F^{13}\ne F^9\). This independently excludes all periods other than one and four, verifies the sharp bound, and independently reproduces every cell of the displayed census.

**Affine symmetry and basins.** The transformations \(i\mapsto si+a\) preserve the set of outgoing quadratic differences. Their actions therefore commute with the update and map temporal orbits and their complete basins bijectively. `verification/classes.py` reads the full list of cycle representatives and basin sizes generated by `census.cpp` and independently rebuilds the local rule to verify each representative is a genuine four-cycle. For each unclassified temporal orbit, it explicitly applies all \(253\) affine transformations, reducing the resulting configurations to the minimum of their four temporal phases. These generated sets are pairwise disjoint and cover all \(3542\) four-cycle orbits. The resulting classes have size \(253\) each, with the fourteen basin sizes stated above. Their total attraction population is
\[
253(6+12+6+22+4+10+30+6+6+22+20+64+58+10)=69{,}828.
\]
The checker also verifies \(F^2(x)=\mathbf1-x\) for every listed canonical orbit representative; commutation with \(F\) extends this to all phases. It verifies that complementation preserves every one of the fourteen affine classes. Finally it partitions all \(1012\) depth-ten initial states under the same group into four classes of size \(253\) and computes their two complement-pairings. These are exhaustive calculations on explicitly given finite sets, not statistical estimates.

## Verification
Run `g++ -std=c++17 -O3 verification/census.cpp -o census` and `./census > verification/census.out` from the package root; then run `python3 verification/classes.py`. Independently compile and run `g++ -std=c++17 -O3 verification/iterates.cpp -o iterates` and `./iterates > verification/iterates.out`. No third-party libraries or network calls are required. The embedded output files are recorded runs, not substitutes for their source programs. The first program examines all \(8{,}388{,}608\) inputs and computes exact functional-graph classes. The second examines the same entire finite state space by a different algorithm, using Euler's criterion rather than an explicitly accumulated residue set, and agrees on every entry-time and period cell. The geometric-class verifier checks all \(3542\) individual cycles and all \(1012\) last-depth configurations. For the code-level results, the expected success markers are `INDEPENDENT_ITERATES_OK` and `AFFINE_BASIN_CLASS_OK`. Both checks were rerun from extracted package files after assembling the result.

## Relationship to prior work
The mathematically closest published finite classification, *A forbidden two-clock and the Paley-19 revival of majority oscillations*, shows that the preceding quadratic-residue Paley tournament on nineteen vertices has \(342\) primitive four-cycle orbits **and** \(18\) primitive nineteen-cycle orbits, with sharp maximal entry time seven; it only treats orders \(3,7,11,19\). It therefore does not imply the order-twenty-three phenomenon: the complete disappearance of non-four long cycles, fourteen affine families with their individual basin sizes, and the ten-step last layer. The established universal prohibition of two-cycles on tournaments is consistent with this result, but alone does not classify four-cycles, basins, or transient depth.

Jørgensen's *Normally Regular Digraphs*, section 1, constructs Paley tournaments as doubly regular tournaments and supplies structural graph properties, but no binary-majority temporal census. Benjamini, Chan, O'Donnell, Tamuz and Tan's majority-dynamics theorem explicitly assumes **undirected** graphs and cannot prohibit four-cycles on this directed tournament. The separately published homotopy classification of the same Paley-23 out-neighborhood complex has the same quadratic-residue graph and its order-253 affine action, but studies topological homology rather than nonlinear opinion trajectories; it implies none of the stated temporal counts. The historical general work of Goles on automata networks has a relevant abstract but no full-text comparison was obtained; it remains a priority risk. The full original statement and source material used for each comparison are identified in the review.

## Limitations
This is a complete, exact **finite** classification for one natural twenty-three-vertex directed network, not a theorem that all Paley tournaments or all doubly regular tournaments have only one- and four-period states. No asymptotic law in tournament order is asserted. Neither the particular graph's topology nor the finite calculations alone establishes a new general constraint on longer cycles; the main contribution is the sharp natural-order boundary and the symmetry-resolved full functional-graph census. A previously unknown or unindexed identical classification may exist. The finite proof is conditional only on the supplied exhaustive enumerations and their faithfully specified implementation; it does not classify other orders.

## References
1. L. K. Jørgensen, *Normally Regular Digraphs*, arXiv:1410.8424v1, first public 2014-10-30, section 1 on Paley tournaments. https://arxiv.org/abs/1410.8424 .
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first public 2014-05-11; Theorem 1.1 applies to undirected graphs. https://arxiv.org/abs/1405.2486 .
3. E. Goles Ch., *Dynamics of Positive Automata Networks*, *Theoretical Computer Science* 41 (1985), 19–32, https://doi.org/10.1016/0304-3975(85)90057-X (abstract inspected; complete paper unavailable for comparison).
4. *A forbidden two-clock and the Paley-19 revival of majority oscillations*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-forbidden-two-clock-and-the-paley-19-revival-of-majority-oscil--13a06d889156 .
5. *The Paley-23 out-neighborhood complex: a mixed sphere wedge and affine homology character*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-paley-23-out-neighborhood-complex-a-mixed-sphere-wedge-and-a--d2e37276ff47 .
