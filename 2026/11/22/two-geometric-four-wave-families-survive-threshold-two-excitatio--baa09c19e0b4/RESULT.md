# Two geometric four-wave families survive threshold-two excitation on the Clebsch graph

## Finding

On the five-regular sixteen-vertex Clebsch graph, synchronous **three-state Greenberg–Hastings excitation with a two-neighbor activation threshold** has exactly one equilibrium, the all-rest configuration, and exactly **90 primitive temporal four-cycles**, with no other recurrent periods. Among the \(3^{16}=43{,}046{,}721\) labelled initial configurations, exactly \(58{,}920\) eventually oscillate and the remaining \(42{,}987{,}801\) become all-rest. The 90 temporal four-cycles form precisely **two** graph-automorphism classes:

| Wave geometry | Primitive four-cycles | Basin size per primitive temporal orbit | Total basin population |
|:--|--:|--:|--:|
| Four parallel affine two-flats | 30 | 676 | 20,280 |
| Alternating pairs of two distinct affine two-flat directions | 60 | 644 | 38,640 |

Each four-cycle uses all sixteen vertices, partitioned into four disjoint phase sets of four vertices each; every vertex is excited exactly once in four updates. Each phase set is a four-point affine two-flat in \(\mathbb F_2^4\). In the 30 parallel cycles all four phase sets share a direction subspace; in the 60 twisted cycles the two opposing pairs of phase sets have different direction subspaces.

Every configuration becomes periodic within a **sharp seven updates**, and the global map obeys
\[
 F^{11}=F^7,\qquad F^{10}\ne F^6.
\]
The exact first-periodic-entry census is:

| First periodic-entry time | Eventual period 1 | Eventual period 4 |
|---:|---:|---:|
| 0 | 1 | 360 |
| 1 | 65,535 | 5,400 |
| 2 | 3,178,531 | 53,160 |
| 3 | 10,245,950 | 0 |
| 4 | 15,448,184 | 0 |
| 5 | 10,086,320 | 0 |
| 6 | 3,812,880 | 0 |
| 7 | 150,400 | 0 |
| **Total** | **42,987,801** | **58,920** |

## Assumptions and scope

The graph's vertex set is \(V=\mathbb F_2^4\), represented by the sixteen integers \(0,\ldots,15\). Its five Cayley generators are \(S=\{1,2,4,8,15\}\); vertices \(u\) and \(v\) are adjacent if and only if their bitwise XOR lies in \(S\). This is the five-regular folded five-cube, *not* its ten-regular complement, which is also sometimes called a Clebsch graph.

Each configuration assigns to each vertex one of the states 0 (rest), 1 (excited), 2 (refractory). Simultaneous updating is given by
\[
(Fx)_v = \begin{cases}
 1,&x_v=0\text{ and at least two neighbors of }v\text{ have state }1,\\
 0,&x_v=0\text{ and fewer than two neighbors have state }1,\\
 2,&x_v=1,\\
 0,&x_v=2.
\end{cases}
\]
A *primitive temporal orbit* is a directed periodic cycle counted once, not once for every phase. Its basin consists of all initial configurations eventually entering that orbit, including the periodic configurations. The *first periodic-entry time* of \(x\) is the minimum nonnegative integer \(t\) for which \(F^t(x)\) is periodic. Only in the separate geometric census are temporal cycles identified under graph automorphisms.

## Proof

**Exact transition representation.** If \(E\) and \(R\) denote the disjoint subsets of excited and refractory vertices, let
\[
 A(E)=\{v\in V: |(v\oplus S)\cap E|\ge2\}.
\]
The map is exactly
\[
 (E,R)\mapsto\big(A(E)\setminus(E\cup R),\ E\big).
\]
Every vertex is in exactly one of \(E,R,V\setminus(E\cup R)\); hence the disjoint pairs form exactly \(3^{16}\) possible configurations. The attached `clebsch_threshold2_a.cpp` recursively enumerates these pairs, uses a table of \(A(E)\) for all \(2^{16}\) excited sets, and directly follows every orbit until it first reaches zero or repeats a state. It reports zero unresolved trajectories, and counts first-entry times and canonical individual temporal orbits. It detects the 90 four-cycles and records their basin populations.

**Independent complete functional-digraph calculation.** The attached `clebsch_threshold2_b.cpp` uses a different state encoding,
\[
 \operatorname{index}(x)=\sum_{v=0}^{15}x_v3^v,
\]
and calculates each vertex's neighbor count directly rather than using the first program's activation table. It constructs all \(3^{16}\) directed successor edges, removes indegree-zero states, and identifies every residual directed cycle. Exactly \(43{,}046{,}360\) states are peeled, leaving \(361\) periodic states: one fixed point and ninety disjoint four-cycles. Reverse traversal of the removed vertices assigns every transient state its first-entry time and terminal temporal cycle. This second method reproduces the entire table above and the complete basin-size spectrum:
\[
 1\times42{,}987{,}801,\qquad 60\times644,\qquad 30\times676.
\]
In particular, \(F^7(x)\) is periodic for every initial state \(x\), with every period dividing four. Therefore \(F^{11}=F^7\). The explicit initial state with excited mask `54784` and refractory mask `0` reaches the zero state for the first time at update seven, witnessing the sharpness and \(F^{10}\ne F^6\). The two algorithms use different enumeration, transition, and cycle-detection representations; all assertions are exact integer operations.

**Complete geometric classification.** The five nonzero generator vectors have the unique linear dependence that their XOR is zero. Hence each of their \(5!\) permutations extends to an invertible linear map of \(\mathbb F_2^4\), and translations give \(16\cdot5!=1{,}920\) graph automorphisms. There are no others: an automorphism fixing zero permutes its five neighbors, while each of the remaining ten vertices is uniquely determined by its two neighboring generators. The script `clebsch_threshold2_symmetry.py` constructs these 1,920 maps and verifies adjacency preservation, then canonically identifies a temporal cycle after each map and all four phase shifts. Applied to the complete 90-cycle list, this partitions the cycles into orbits of sizes 30 and 60, with individual basin sizes respectively 676 and 644.

For an explicit parallel example, the four successive excited sets are
\[
\{0,1,6,7\},\ \{8,9,14,15\},\ \{10,11,12,13\},\ \{2,3,4,5\}.
\]
For a twisted example they are
\[
\{0,1,10,11\},\ \{8,9,14,15\},\ \{6,7,12,13\},\ \{2,3,4,5\}.
\]
The script verifies the corresponding four states form legitimate cycles. For every phase set it checks that the XOR of the four vertices is zero, characterizing an affine two-flat, and compares the translated difference subspaces. The parallel class has one such direction; the twisted class alternates between exactly two distinct directions. The geometric cases exhaust every nontrivial periodic orbit rather than being selected examples.

## Verification

The finite theorem is reproducible with a standard C++17 compiler and Python 3. From a directory containing the attached standalone files:

```sh
g++ -std=c++17 -O3 -o clebsch_threshold2_a clebsch_threshold2_a.cpp
./clebsch_threshold2_a > clebsch_threshold2_a.log
g++ -std=c++17 -O3 -o clebsch_threshold2_b clebsch_threshold2_b.cpp
./clebsch_threshold2_b > clebsch_threshold2_b.log
python3 clebsch_threshold2_symmetry.py > clebsch_threshold2_symmetry.log
python3 clebsch_threshold2_crosscheck.py > clebsch_threshold2_crosscheck.log
```

The expected integer results and executed outputs are embedded in the four corresponding `.log` files. The cross-check tests equality of both independent full-state shell and basin tables, the total population, and the sharp seven-update entry. The symmetry script tests all 1,920 graph automorphisms against all 90 temporal cycles and checks the plane geometries. These computations are exhaustive *because the configuration space is finite*, not because samples of trajectories support an extrapolation.

## Relationship to prior work

Excitable-media cellular automata and their contact thresholds are classical, including Durrett and Griffeath's 1993 study of threshold-range behavior on lattices. Gravner, Lyu, and Sivakoff's graph-level synchronization characterization (first preprint 2016) assumes the standard **one-neighbor** three-state rule; it does not yield this two-contact graph-specific classification. The existing exact Clebsch excitation census for threshold one gives seven recurrent least periods \(1,3,4,7,10,13,16\) and \(2{,}976{,}617\) periodic configurations; the present threshold-two rule instead has only periods one and four and just \(361\) periodic configurations. The older result's explicit scope excludes alternative thresholds, so its counts do not imply the numbers here.

The five-regular Clebsch graph's affine folded-cube construction and symmetry group are classical. The specific new information is the complete dynamical and basin classification at threshold two and the separation of its 90 four-wave attractors into two geometrically distinct, unequally attractive classes. Exact computations for other regular, bipartite or strongly regular graphs have not been used to infer this census.

## Limitations

This is an exact **finite** classification for the specified graph, three colors and activation threshold two. It does not establish a theorem for arbitrary strongly regular graphs, arbitrary folded cubes, additional colors, or other thresholds. Complete exhaustive code provides a reproducible finite proof subject to faithful execution and the correctness of the displayed algorithms; it is not a formally machine-checked theorem or independent external validation. The literature comparison is a good-faith priority check, not proof that an equivalent unpublished or unindexed computation does not exist.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first publicly posted 1993-03-22, https://arxiv.org/abs/patt-sol/9303002 .
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first publicly posted 2016-10-24; open-access final paper, *Annals of Applied Probability* 28 (2018), 3324–3357, https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf .
3. *Seven temporal clocks and two longest-period symmetry types in the Clebsch excitation automaton*, published technical result on threshold-one dynamics, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-seven-temporal-clocks-and-two-longest-period-symmetry-types-in-t--69af5154ca1f .
4. E. W. Weisstein, *Clebsch Graph*, MathWorld, https://mathworld.wolfram.com/ClebschGraph.html .
