# Spectral rigidity and isolated equilibria in Clebsch majority dynamics

## Finding

Let \(C\) be the five-regular Clebsch graph: its vertices are the sixteen words \(\mathbb F_2^4\), and \(u\) and \(v\) are adjacent when \(u\oplus v\in\{1,2,4,8,15\}\), interpreting words as four-bit integers. On every labelled binary configuration, let \(F\) update all vertices simultaneously to the strict majority of their five neighbors. Then

\[
\boxed{F^6=F^4,\qquad F^5\ne F^3.}
\]

There are exactly **142 fixed configurations** and **1,165 primitive temporal two-cycle orbits**, and no other recurrent periods. The sharp maximum first-periodic-entry time is four. All 140 nonconstant fixed configurations have exactly eight occupied vertices, induce three same-color and two opposite-color neighbors at every vertex, and have **singleton attraction basins**. The only fixed points with nontrivial attraction basins are the all-zero and all-one states, each attracting 12,333 initial configurations.

The first-entrance census of all \(65{,}536\) labelled configurations is:

| First periodic-entry time | Eventual period one | Eventual period two |
| ---: | ---: | ---: |
| 0 | 142 | 2,330 |
| 1 | 2,616 | 14,720 |
| 2 | 11,264 | 23,680 |
| 3 | 8,864 | 0 |
| 4 | 1,920 | 0 |
| Total | 24,806 | 40,730 |

The complete primitive-attractor basin spectrum (basin size **per temporal orbit**, followed by number of such orbits) is:

| Temporal period | Basin size | Number of orbits |
| ---: | ---: | ---: |
| 1 | 1 | 140 |
| 1 | 12,333 | 2 |
| 2 | 2 | 40 |
| 2 | 4 | 240 |
| 2 | 8 | 480 |
| 2 | 10 | 120 |
| 2 | 42 | 240 |
| 2 | 462 | 40 |
| 2 | 1,218 | 5 |

Primitive two-cycles flip exactly 8, 10, 12, or 16 vertices, in respective orbit counts 160, 240, 720, and 45. Under the full 1,920-element graph automorphism group, the 142 fixed states form **four** spatial classes of sizes 1, 1, 20, and 120, and the 1,165 temporal two-cycles form **ten** spatial classes, hence **fourteen geometric recurrent classes** in total. Explicit representative masks and all geometric-class sizes are in `recurrent_classes.csv`.

## Assumptions and scope

The graph is the *five-regular* Clebsch/Greenwood–Gleason graph, equivalently the four-cube with one antipodal matching added. This must not be confused with the complementary ten-regular graph sometimes also called the Clebsch graph. Vertex labels are four-bit words from 0 through 15; a configuration is an integer mask \(x\) from 0 through 65,535, whose bit \(v\) is the opinion at vertex \(v\). The update has no ties or self-neighbors and is exactly

\[
F(x)_v=\mathbf1\!\left\{\sum_{h\in\{1,2,4,8,15\}}x_{v\oplus h}\ge3\right\}.
\]

A primitive temporal orbit is counted once, even if it contains two different configurations. No quotient is imposed on these orbit counts by graph automorphisms or global color reversal. The first periodic-entry time is the least \(t\ge0\) for which \(F^t(x)\) belongs to a recurrent orbit. An attraction basin includes the recurrent orbit itself.

## Proof

**Spectral restriction on fixed states.** The Cayley characters \(\chi_a(v)=(-1)^{a\cdot v}\) diagonalize the adjacency matrix \(A\) of \(C\). If \(j\) is the Hamming weight of \(a\), its eigenvalue is \(4-2j+(-1)^j\). Hence the adjacency spectrum is \(5\) once, \(1\) ten times, and \(-3\) five times. If an equilibrium has \(k\) vertices in its minority color, then \(1\le k\le8\), and every minority vertex has at most two opposite-color neighbors. Consequently its cut has at most \(2k\) edges. The adjacency-spectrum bound, obtained by splitting its indicator vector into the constant eigenspace and its orthogonal complement with largest eigenvalue \(1\), gives

\[
|\partial U|\ge\frac{(5-1)k(16-k)}{16}=\frac{k(16-k)}4.
\]

For \(1\le k<8\), the lower bound exceeds \(2k\), a contradiction. At \(k=8\), both bounds equal 16. Every vertex therefore has exactly two neighbors of the opposite opinion and three of its own. Equivalently, if the configuration is encoded as a sign vector \(s\in\{-1,+1\}^{16}\), then \(As=s\). Conversely any sign vector satisfying \(As=s\) is a fixed configuration. Thus the nonconstant fixed configurations are **exactly** the sign vectors in the adjacency eigenvalue-one subspace, and all are balanced. Their exact number, 140, is established by the finite complete certificate below; the two constant configurations are the other two fixed points.

**Exact complete functional graph.** Set

\[
B(v)=\sum_{h\in\{1,2,4,8,15\}}2^{v\oplus h},\quad F(x)=\sum_{v=0}^{15}2^v\,\mathbf1\{\operatorname{popcount}(x\mathbin{\&}B(v))\ge3\}.
\]

These are finite integer formulas. The standalone `verify_finite_dynamics.py` constructs the **entire** functional graph with exactly \(2^{16}=65{,}536\) vertices, removes all noncyclic states by exact indegree pruning, and walks every remaining directed cycle. It then propagates the primitive period, first-entry depth and temporal-orbit representative backwards along the removed vertices. Integer assertions check all stated totals and basin sizes, and the pointwise identity \(F^6=F^4\). Independently, `verify_independent_symmetry.py` calculates the update by direct neighbor-bit sums, tests six successive iterates at **every** initial state, classifies the first periodic entry, and checks the 142 fixed states against \(As=s\) and their singleton basins. Both reproduce the same period-refined entrance table and 1,307 primitive temporal orbits. Since every one of the finite possible initial configurations is tested, no infinite extrapolation is involved.

**Sharpness.** The explicitly checkable trajectory of decimal configuration masks

```text
431 -> 1163 -> 292 -> 1024 -> 0 -> 0
```

has first periodic entry exactly at time four. Thus \(F^5\ne F^3\), while the full census proves \(F^6=F^4\).

**Spatial classification.** A graph automorphism is determined by its image of vertex zero (16 choices) and by a permutation of its five neighbors. Conversely any permutation of the five connection vectors \(1,2,4,8,15\) extends uniquely to an invertible linear map, because any four form a basis and their sole nontrivial relation is that all five sum to zero. Composing with translations gives \(16\cdot5!=1{,}920\) graph automorphisms. Distinct automorphisms are determined by zero and its neighborhood: all other vertices are distinct pairwise sums of the five neighbors and are thereby forced. The independent symmetry verifier checks all 1,920 affine maps, and generates their action on temporal-orbit representatives using eight explicit generators. Its complete disjoint orbit partition yields the four fixed and ten two-cycle spatial classes in `recurrent_classes.csv`. The CSV also records the basin size shared by every representative in each class.

## Verification

The following standalone programs require only Python 3's standard library, and should be executed in the directory containing them:

```sh
python3 verify_finite_dynamics.py > full_dynamics_output.json
python3 verify_independent_symmetry.py > independent_symmetry_output.txt
```

The two corresponding output files are included. They contain their complete assertion-checked summary and geometric-class table. The first uses a bit-mask transition and indegree-pruning functional-graph analysis; the second uses direct neighbor-bit sums and forward trajectories, independently deriving the symmetry orbit partition. Both examine all 65,536 starting states. `recurrent_classes.csv` is the immutable 14-class summary of the independently computed orbit table. No probabilistic sampling or unverified machine algebra is used.

## Relationship to prior work

Goles and Olivos (1980) proved eventual period at most two for finite symmetric threshold systems, an earlier theorem **fully acknowledged** here. Benjamini and collaborators (first public preprint 2014-05-11) investigate convergence and unanimity on infinite unimodular and random graphs, not this exact folded-cube census. Kaaser, Mallmann-Trenn and Natale (2015 preprint) establish general complexity and voting-time bounds, not this graph-specific four-step sharp cutoff. Agur, Fraenkel and Klein (1988) exactly enumerate fixed strings for self-inclusive radius-one majority on **cyclic binary words**; their full eight-page paper does not concern the Clebsch graph.

The directly comparable published four-cube majority census has 702 fixed configurations, 885 temporal two-cycle orbits, and thirty geometric recurrent classes, versus 142, 1,165, and fourteen here. Adding the antipodal matching changes the degree from four (tie retention) to five (no ties); this is a genuinely different update graph, and those four-cube numbers alone do not imply the present census. Previously published Heawood and dodecahedral exact majority censuses concern distinct graphs and yield no direct reduction to Clebsch dynamics. The spectral characterization of all nonconstant equilibria and their singleton basins distinguishes the present calculation.

## Limitations

This is a complete finite theorem for the specified labelled sixteen-vertex graph, not an all-dimensional theorem for folded cubes, arbitrary strongly regular graphs, or random/asynchronous updates. The 140 count and the singleton-basin assertion are verified by complete exact enumeration, whereas the balanced-eigenvector characterization is independently proved by the spectrum and cut bound. The verified first-public-date field records the day-resolved 2014 majority-dynamics preprint; earlier classical work exists, but no day of its original first public circulation was established. Although targeted published-record, database, and full-text comparisons identified no equivalent Clebsch-specific census, an unindexed older calculation cannot be excluded. No independent external mathematical audit has been performed.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first posted 2014-05-11, https://arxiv.org/html/1405.2486v1 .
3. D. Kaaser, F. Mallmann-Trenn, E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1 (2015), https://arxiv.org/abs/1508.03519 .
4. Z. Agur, A. S. Fraenkel, S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics 70 (1988), 295–302, lawful full text: https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf .
5. E. W. Weisstein, *Clebsch Graph*, MathWorld, https://mathworld.wolfram.com/ClebschGraph.html .
6. *Thirty geometric recurrent classes and a sharp four-step clock for majority dynamics on the four-cube*, publicly available exact finite classification, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-thirty-geometric-recurrent-classes-and-a-sharp-four-step-clock-f--c8cd34678da7 .
7. *A two-step majority projection and exact attraction basins on the Heawood graph*, publicly available exact finite classification, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-two-step-majority-projection-and-exact-attraction-basins-on-th--8cd2964a9d93 .
