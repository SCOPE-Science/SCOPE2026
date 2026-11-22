# Two degree-matched tournaments separate into exclusive four- and twenty-three-step majority clocks

## Finding
Let \(P_{23}\) be the quadratic-residue Paley tournament and \(C_{23}\) the clockwise carousel tournament, both on the labelled vertex set \(\mathbb Z/23\mathbb Z\). Apply simultaneous strict binary majority to every vertex's eleven out-neighbors. Then the **complete** recurrent dynamics on \(P_{23}\) consists of the two unanimous fixed states and exactly **3,542 primitive temporal four-cycles**, with no other least periods. On \(C_{23}\) it consists of the same two unanimous fixed states and exactly **12 primitive temporal twenty-three-cycles**, with no other least periods. Thus the two regular tournaments have equal order and out-degree but **disjoint nontrivial temporal period sets**.

Of the \(2^{23}=8,388,608\) labelled binary initial configurations, \(69,828\) on \(P_{23}\) eventually reach four-cycles and \(8,318,780\) reach unanimity; the corresponding numbers on \(C_{23}\) are \(3,906,412\) reaching twenty-three-cycles and \(4,482,196\) reaching unanimity. The exact oscillator-basin probabilities are \(69,828/8,388,608\) and \(3,906,412/8,388,608\), respectively. The sharp maximum first-periodic-entry times are **ten** and **four** synchronous updates.

The identities of maps on the *entire* configuration spaces are, sharply,
\[
F_P^{14}=F_P^{10},\qquad F_C^{27}=F_C^4,
\]
while \(F_P^{13}\ne F_P^9\) and \(F_C^{26}\ne F_C^3\).

## Assumptions and scope
Both tournaments have vertices \(i\in\mathbb Z/23\mathbb Z\). The Paley arcs are \(i\to i+d\) for \(d\in Q=\{1,2,3,4,6,8,9,12,13,16,18\}\), the eleven nonzero quadratic residues modulo 23. The carousel arcs are \(i\to i+d\) for \(d\in\{1,2,\ldots,11\}\). All additions are modulo 23. As \(-1\) is a nonresidue mod 23, each orientation has one directed edge between every pair, with out-degree eleven.

For either out-neighborhood \(N^+(i)\) and initial binary vector \(x\in\{0,1\}^{23}\), the synchronous update is
\[
F(x)_i=\mathbf 1\!\left\{\sum_{j\in N^+(i)}x_j\ge6\right\}.
\]
No tie arises because each out-degree is odd. Encode a configuration by the nonnegative integer \(\sum_{i=0}^{22}2^ix_i\); bit zero is vertex zero. A *primitive temporal cycle* is a distinct set of states lying on one closed orbit, not an oriented graph cycle. The *first periodic-entry time* is the least \(t\ge0\) for which \(F^{t+p}(x)=F^t(x)\) for some \(p\ge1\), and its period is the minimal such positive \(p\).

## Proof
The claim is an exact finite-state theorem, proved by a complete traversal of two explicitly defined deterministic maps, not by statistical sampling. Each map has precisely \(2^{23}\) states. The two standalone source programs compute its complete functional directed graph using **different** update and orbit-classification implementations.

Program `code/exhaustive_peel.cpp` computes a 23-bit successor from the population counts of eleven bit masks, builds indegrees, and repeatedly peels states with zero remaining indegree. The remaining vertices are *exactly* those on directed cycles, because each has one successor and all non-cycle branches disappear. It traverses each unvisited remaining component to assign its actual primitive cycle length. Processing all peeled vertices in reverse deletion order assigns each the length and first-entry distance of its successor plus one. This proves exhaustiveness of every counted period, depth and basin. The program enumerates each integer \(0\le x<2^{23}\).

Independently, `code/exhaustive_paths.cpp` calculates each successor using eleven individual shifted-bit tests (rather than population-count masks) and follows as-yet-unclassified orbits until meeting a previously classified state or detecting a repetition on its own path. It assigns each new cycle its measured primitive length and each predecessor its recursive entry depth. This second enumeration also visits the entire integer interval and gives exactly the same full depth-by-period table as the first, without using any saved results from it. The programs' full outputs are contained in `data/peel_output.txt` and `data/paths_output.txt`.

The resulting cycle counts are \(2\) length-one and \(3542\) length-four cycles for \(P_{23}\), and \(2\) length-one and \(12\) length-twenty-three cycles for \(C_{23}\). The entire entry-time distribution is shown below, including zero entries only by omission. The maximal entry times are ten and four; because all eventual periods divide four and twenty-three respectively, these tables imply the displayed global iterate identities. For sharpness, state encoding `23807` on \(P_{23}\) first reaches its fixed point at step ten, and encoding `171551` on \(C_{23}\) first reaches its fixed point at step four. Further, encoding `15611` is on a primitive four-cycle on \(P_{23}\), while `63` is on a primitive twenty-three-cycle on \(C_{23}\); direct iterations from these states are independent sanity checks of the two period counts.

## Verification
All counts below are for *labelled initial states*, not equivalence classes modulo a tournament automorphism. A row means first periodic entry at the specified update and eventual minimal period as specified.

**Paley tournament**:

| First entry | Period | Number of initial configurations |
|---:|---:|---:|
| 0 | 1 | 2 |
| 0 | 4 | 14,168 |
| 1 | 1 | 556,140 |
| 1 | 4 | 29,854 |
| 2 | 1 | 4,746,326 |
| 2 | 4 | 9,108 |
| 3 | 1 | 2,061,996 |
| 3 | 4 | 8,602 |
| 4 | 1 | 628,958 |
| 4 | 4 | 4,048 |
| 5 | 1 | 174,064 |
| 5 | 4 | 3,036 |
| 6 | 1 | 89,562 |
| 6 | 4 | 1,012 |
| 7 | 1 | 33,902 |
| 8 | 1 | 16,192 |
| 9 | 1 | 10,626 |
| 10 | 1 | 1,012 |


**Carousel tournament**:

| First entry | Period | Number of initial configurations |
|---:|---:|---:|
| 0 | 1 | 2 |
| 0 | 23 | 276 |
| 1 | 1 | 1,375,952 |
| 1 | 23 | 2,302,576 |
| 2 | 1 | 2,427,880 |
| 2 | 23 | 1,556,548 |
| 3 | 1 | 617,504 |
| 3 | 23 | 47,012 |
| 4 | 1 | 60,858 |


The Paley table totals \(8,388,608\); its two period-basin totals are \(8,318,780\) and \(69,828\). The carousel table independently totals \(8,388,608\); its basin totals are \(4,482,196\) and \(3,906,412\). Compiling the two source files separately with `g++ -std=c++17 -O3 -mpopcnt code/exhaustive_peel.cpp -o exhaustive_peel` and `g++ -std=c++17 -O3 code/exhaustive_paths.cpp -o exhaustive_paths`, then executing them, reproduces the recorded counts exactly. No random seeds, third-party libraries, external files, or omitted datasets are required.

The result demonstrates a finite-order dynamical difference between the two specific canonical orientations. It does **not** establish any analogous statement for all regular tournaments, all Paley primes, or all carousel orders.

## Relationship to prior work
Benjamini, Chan, O'Donnell, Tamuz and Tan [1] discuss the symmetric/undirected majority setting, for which every orbit becomes a fixed point or a two-cycle. Their undirected hypothesis excludes both tournaments here and cannot imply these length-four and length-twenty-three attractors. Jørgensen [2] describes Paley tournaments within normally regular directed graphs, but does not count binary majority orbits.

Nakar and Ron [3] analyze **centered** radius-\(r\) binary majority automata on one-dimensional cyclic rings. The carousel update here is related to their centered radius-five rule \(M_5\) by the exact change of formulation \(F_C=S^6M_5\), where \(S\) is one-site cyclic shift; therefore their structural results may constrain possible carousel waves. Their classification of eventual centered fixed points/two-cycles does not state the above labelled \(23\)-site carousel basin histogram, nor the Paley comparison. This distinction matters: merely naming the network a tournament does not make the carousel an unrelated update rule.

The closest examined published graph-specific majority census [4] covers Paley tournaments on \(3,7,11,19\) vertices, including primitive four- and nineteen-cycles at order 19. Its complete proof and tables do not address order 23 or the two-tournament comparison. The general absence of two-cycles on tournaments and consensus-only fixed-point behavior on regular tournaments are prior results, and are not claimed as innovations here. The new contribution is the *complete order-23 contrast*, including its exact attraction proportions and sharp transients.

## Limitations
This is a full finite enumeration at one vertex count, not an infinite-family theorem. The correctness check consists of two independent implementations and exact complete state traversal, not external mathematical validation. The priority comparison covered accessible published full text and indexed mathematical findings, but equivalent unindexed historical numerical studies may exist; broader theoretical treatments of directed majority and the shifted radius-five cellular automaton could potentially imply some counts after additional work. No inference about a measure on tournaments, asymptotic probability, or universal period prohibition is made.

## References
[1] I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, publicly posted 2014-05-11. https://arxiv.org/abs/1405.2486

[2] L. K. Jørgensen, *Normally Regular Digraphs*, arXiv:1410.8424v1, publicly posted 2014-10-30. https://arxiv.org/abs/1410.8424

[3] Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv:2205.08972v1, publicly posted 2022-05-18. https://arxiv.org/abs/2205.08972

[4] *A forbidden two-clock and the Paley-19 revival of majority oscillations*, full result, proof and census posted 2026-11-17. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-forbidden-two-clock-and-the-paley-19-revival-of-majority-oscil--13a06d889156
