# Seven temporal clocks and two longest-period symmetry types in the Clebsch excitation automaton

## Finding

On the 16-vertex, degree-five Clebsch graph (the folded five-cube), synchronous threshold-one, three-color Greenberg–Hastings dynamics has **exactly seven eventual least periods**. Among the \(3^{16}=43,046,721\) labelled initial configurations, the primitive temporal cycle counts are:

| Least period \(\ell\) | Number of primitive cycles | Number of periodic configurations |
|---:|---:|---:|
| 1 | 1 | 1 |
| 3 | 859,552 | 2,578,656 |
| 4 | 970 | 3,880 |
| 7 | 11,040 | 77,280 |
| 10 | 15,360 | 153,600 |
| 13 | 9,600 | 124,800 |
| 16 | 2,400 | 38,400 |

Thus the periodic set has exactly \(2,976,617\) labelled states, and the remaining \(40,070,104\) states are transient. Every state enters a temporal cycle in at most **eleven updates**. The bound is attained by exactly **11,520** initial states, all subsequently following a period-three orbit. The complete table of all 48 nonempty pairs (first-periodic-entry time, eventual least period) appears in `temporal_classes.csv`.

The full graph automorphism group has order \(1920\). Acting on primitive temporal cycles modulo time translation, it partitions the **2,400 primitive period-sixteen cycles into exactly two symmetry classes**, of sizes **480** and **1,920**; stabilizer orders are respectively four and one. The **9,600 period-thirteen cycles** form precisely five symmetry classes, each of size \(1920\), with trivial stabilizers. Every period-thirteen cycle excites each vertex exactly four times per period; every period-sixteen cycle excites each vertex exactly five times per period.

## Assumptions and scope

Let \(V=\mathbb F_2^4\), represented by the integers \(0,\ldots,15\) with binary XOR denoted by \(\oplus\). Let \(S=\{1,2,4,8,15\}\). Two distinct vertices are adjacent exactly when their XOR belongs to \(S\). This defines the degree-five folded five-cube, not its ten-regular complementary graph sometimes also called the Clebsch graph.

A configuration is \(x\in\{0,1,2\}^{V}\). The synchronous map \(F\) is given at every vertex \(i\) by
\[
(Fx)_i=\begin{cases}
1,&x_i=0\text{ and some neighbor of }i\text{ has color }1,\\
0,&x_i=0\text{ and no neighbor has color }1,\\
2,&x_i=1,\\
0,&x_i=2.
\end{cases}
\]
A *primitive temporal cycle* is a directed orbit of the map \(F\) with least positive period \(\ell\), counted once regardless of its starting state. The *first-periodic-entry time* is \(\tau(x)=\min\{t\ge0:F^t(x)\text{ belongs to a directed cycle}\}\). All counts concern labelled configurations, with graph automorphisms quotienting only the separately stated symmetry classification.

## Proof

The finite-state assertions are an exhaustive, exact computational theorem. There are no sampled or omitted states. Encode each configuration as the integer
\[
E(x)=\sum_{i=0}^{15}x_i3^i\in\{0,1,\ldots,3^{16}-1\}.
\]
The C program `clebsch_census.c` implements the stated local rule directly, constructs the successor of each of these \(43,046,721\) integers, and records all indegrees in the finite functional digraph. It recursively removes indegree-zero vertices. Each removed vertex is transient; the remaining directed graph has indegree and outdegree one at every vertex and is therefore a disjoint union of cycles. Traversing each remaining cycle gives its exact least length and number. Reversing the removal order assigns every removed state its terminal cycle length and entry time (one plus its successor's entry time). The resulting exact integer accumulations give the table above and `temporal_classes.csv`. Integer and array-size guards in the program turn unexpected path or period lengths into explicit failure rather than truncating them.

The separate program `clebsch_walk.c` does not use the indegree-peeling algorithm. Its successor rule uses precomputed excited/refractory bit masks and a binary-contact mask table. It classifies states by memoized forward trajectories, explicitly detects each first repeated state and back-propagates terminal period and entry time. All 55 cycle/class records of this independent *implementation* agree exactly with `clebsch_census.c`; this is a same-author computational cross-check, **not** an independent audit. The program also exports the minimum integer representative of each period-thirteen and period-sixteen temporal cycle, so no cycles of those lengths are omitted from symmetry analysis.

For the automorphism claim, the five connection vectors have the single relation that their sum is zero. Every permutation of the five vectors extends to an invertible linear map of \(\mathbb F_2^4\); together with translations this gives \(16\cdot5!=1920\) distinct graph automorphisms. Conversely, any graph automorphism fixing zero permutes its five neighbors. Since any nonneighbor of zero is uniquely determined by the two common neighbors it shares with zero, this permutation determines the whole automorphism. Thus these are all graph automorphisms.

`clebsch_symmetry.py` checks that all \(1920\) affine maps are distinct and preserve every edge, then uses four neighboring transpositions of the five connection vectors and four basis translations to generate their action. It canonically replaces an image of a temporal cycle by the minimum encoded state in that cycle. Exact orbit traversal of all \(9,600\) period-thirteen and \(2,400\) period-sixteen cycle representatives yields respectively five orbit sizes of \(1920\), and orbit sizes \(480\) and \(1920\). Since the eight generators generate the full group, these are the complete symmetry orbits, not a subgroup partition. An additional enumeration of all \(1920\) affine maps confirms stabilizer orders and phase shifts for representatives of both period-sixteen types. `clebsch_phase.py` checks the stated excitation count at each of the sixteen vertices on every one of the \(12,000\) cycles of periods thirteen and sixteen.

## Verification

The two different full-state algorithms each process the entire state set of size \(43,046,721\) and produce exactly the same primitive cycle census and each of the 48 nonzero entry-period populations. Their total populations are \(43,046,721\), and the first-periodic-entry-time distribution sums correctly. The sharp entry time eleven is witnessed by the nonempty class of \(11,520\) states. The symmetry computation accounts for every primitive cycle of lengths thirteen and sixteen, and verifies the actual graph action before computing its orbits. Source codes, saved output tables, cycle-representative lists, and the symmetry and phase verifiers are included as standalone files.

A reader can reproduce with a C11 compiler and Python 3, for instance by compiling and running both C programs in the directory containing the source files, then executing `clebsch_symmetry.py`, `clebsch_phase.py`, and `clebsch_stabilizers.py`. The exhaustive first program needs approximately 650 MiB of working memory. This is an exact finite proof conditional on faithful execution of the supplied transparent programs, not a machine-checked formal theorem or external certification.

## Relationship to prior work

Greenberg–Hastings excitation and refractory dynamics are established models, not proposed here. Fisch, Gravner, and Griffeath (1993) study metastability in lattice versions of the model. Gravner, Lyu, and Sivakoff (first publicly posted 2016) prove a broad finite-graph criterion for eventual synchronization and characterize the common excitation activity using a maximization over directed cycles (their Theorem 3). Their general theorem applies to this graph and controls qualitative long-time behavior, but does not tabulate the exact primitive temporal cycle numbers, transient-entry populations, or automorphism-orbit splitting of period-sixteen cycles calculated here.

The Clebsch graph and its folded-five-cube interpretation are classical; no graph construction or automorphism-group discovery is claimed. The claim is the exact temporal and equivariant census for the specified excitable dynamics. Earlier enumerations on other graphs or different local rules do not imply these exact labelled counts. Literature searches found no equivalent Clebsch-specific census, which is not a proof of historical uniqueness.

## Limitations

The claim is specific to the three-color, threshold-one model on the sixteen-vertex, degree-five folded cube. It does not assert the same periods or populations for other folded cubes, for the complement Clebsch graph, for different excitation thresholds, or for the cyclic cellular automaton rather than Greenberg–Hastings dynamics. Full enumeration is a finite proof and does not supply a closed-form family theorem. Historical-priority searches cannot rule out an unindexed, unpublished, or differently named prior enumeration. Independent human or formal validation has not been performed.

## References

- R. Fisch, J. Gravner, D. Griffeath, *Metastability in the Greenberg-Hastings Model*, arXiv:patt-sol/9303005, publicly submitted 1993-03-23. https://arxiv.org/abs/patt-sol/9303005
- J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first public preprint 2016-10-24; *Annals of Applied Probability* 28 (2018), 3324–3357, doi:10.1214/17-AAP1350. https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf
- E. W. Weisstein, *Clebsch Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/ClebschGraph.html (identification of the sixteen-vertex, five-regular folded cube).
