# Exceptional excitation clocks survive line-graph expansion of two generalized Petersen graphs

## Finding
Let \(H_1=GP(5,1)\) be the pentagonal prism and \(H_2=GP(5,2)\) be the Petersen graph. On the fifteen-vertex simple line graphs \(L(H_i)\), use synchronous three-state Greenberg–Hastings excitation with one-contact threshold. For each least period \(p\), let \(O_i(p)\) count primitive temporal orbits (time shifts identified, vertices and states labelled). The **complete recurrent orbit census** is

| Least period \(p\) | \(O_1(p)\) | \(O_2(p)\) |
| --- | ---: | ---: |
| 1 | 1 | 1 |
| 3 | 195250 | 220810 |
| 4 | 80 | 60 |
| 5 | 6 | 30 |
| 7 | 100 | 0 |
| 8 | 0 | 60 |

No other primitive periods occur. In particular, *all* the non-three primitive orbit counts for the two line graphs **agree, period by period, with the previously determined counts on their ten-vertex base graphs**, despite the addition of five dynamical sites. The agreement is asserted for these two pairs only, not for arbitrary line graphs.

The exact sharp maximum first-periodic-entry times are \(17\) on \(L(H_1)\) and \(12\) on \(L(H_2)\), attained by exactly \(80\) and \(1200\) initial states, respectively. Every maximum-depth state eventually has least period three. Both line graphs have \(3^{15}=14,348,907\) states. The eventual-period basin sizes, including recurrent states, are

| Eventual period | \(L(H_1)\) | \(L(H_2)\) |
| --- | ---: | ---: |
| 1 | 292287 | 277077 |
| 3 | 13208940 | 13229250 |
| 4 | 714720 | 201240 |
| 5 | 45780 | 536580 |
| 7 | 87180 | 0 |
| 8 | 0 | 104760 |

For geometric orbit classes, additionally quotient primitive temporal orbits by the *full* graph-automorphism group of the line graph. The non-three geometric classes have orbit-size partitions as follows (numbers in parentheses are the sizes of the classes in primitive temporal orbits):

| Graph | Period four | Period five | Long exceptional period |
| --- | --- | --- | --- |
| \(L(H_1)\) | \(10,10,10,10,20,20\) | \(2,4\) | five classes each of size \(20\) at period seven |
| \(L(H_2)\) | one class of size \(60\) | one class of size \(30\) | one class of size \(60\) at period eight |

Thus the Petersen-line graph has exactly one spatial type at **each** exceptional period, whereas the prism-line graph has thirteen exceptional geometric types altogether.

## Assumptions and scope
For \(k\in\{1,2\}\), define \(H_k=GP(5,k)\) on labelled vertices \(u_i,v_i\) indexed by \(i\in\mathbb Z/5\mathbb Z\), with fifteen undirected edges \(u_i u_{i+1}\), \(u_i v_i\), \(v_i v_{i+k}\). Each \(H_k\) is connected, cubic and triangle-free. Its line graph has one distinctly labelled vertex per edge of \(H_k\); two line-graph vertices are adjacent exactly when their corresponding original edges share an endpoint. Each line graph is simple, connected, four-regular and has fifteen vertices.

A state \(x\) labels each line-graph vertex by \(0\) (resting), \(1\) (excited) or \(2\) (refractory). All labels update simultaneously under \(F\): \(1\mapsto2\), \(2\mapsto0\), and \(0\mapsto1\) precisely when at least one open neighbor currently has label \(1\); otherwise \(0\mapsto0\). There is no stochasticity or random tie-breaking. The first entry time \(t(x)\) is the least \(t\ge0\) for which \(F^t(x)\) is periodic; \(p(x)\) is its eventual least period. The number of distinct primitive temporal orbits of length \(p\) equals \(\#\{x:t(x)=0,p(x)=p\}/p\).

All counts concern exactly these two labelled finite graphs, with no assertion for arbitrary generalized Petersen parameters or larger families. No color permutations are identified: the three states have different dynamical roles.

## Proof
**Step 1 (exact finite encoding).** List the fifteen base edges by the five outer edges, five spokes and five inner edges, in increasing \(i\) order within each block. Represent each labelled state by the unique integer \(s=\sum_{j=0}^{14}x_j3^j\) in \(\{0,\ldots,3^{15}-1\}\). The finite update is computed directly using the defined edge intersections and three explicit local cases; all 15 line-graph degrees are asserted to equal four. This representation covers *every* labelled configuration once and makes no symmetry reduction before the complete temporal classification.

**Step 2 (functional-graph exactness).** Every map on a finite set has a unique decomposition into disjoint directed cycles and their incoming rooted in-trees. `verification/classify.cpp` considers every integer state from zero through \(3^{15}-1\). On an unvisited trajectory, it marks each newly encountered state active, and stops at either an already completed state or one in the active path. In the latter case, the section of the active path starting at the first repetition is exactly one directed cycle. It assigns that cycle's length as the exact least period and time zero to its vertices. It then processes the remaining transient path backward, assigning to each predecessor its successor's eventual period and one plus its successor's entry time. A completed state is never reclassified. Induction on processed paths proves that the procedure returns exactly \(p(x)\) and \(t(x)\) for **every** state. There are no sampling, rounding or unbounded-search assumptions.

Running this exhaustive procedure gives the recurrent, basin and entry-depth numbers in `verification/counts_1.txt` and `verification/counts_2.txt`. Its `--reps` option prints one representative of every primitive cycle of length at least four; these exact lists are `verification/reps_1.txt` and `verification/reps_2.txt`. The cycle lists contain respectively \(186\) and \(150\) representatives, equal to the sums of the exceptional temporal-orbit counts. Division of the number of period-\(p\) recurrent configurations by \(p\) gives the first table. Each eventual-period basin table sums exactly to \(3^{15}\).

**Step 3 (independent exact enumeration).** `verification/check_independent.cpp` builds successor arrays directly from the adjacency lists, increments exact indegrees, and deletes vertices of indegree zero using a queue. A vertex lies on a directed cycle if and only if it survives this pruning: the deleted vertices cannot be recurrent, and any finite noncyclic in-tree has a zero-indegree leaf. It traverses the remaining cycles, computes their exact lengths and processes the deleted states in reverse order to recover first-entry distances. This is a separate implementation and a different classification algorithm, not a replay of the first algorithm's stored arrays. Its complete period/entry distributions match the corresponding 46 and 37 nonzero rows of the first program, for the full \(3^{15}\) states on each graph.

**Step 4 (full spatial symmetry).** Because \(H_k\) is triangle-free and cubic, each triangle in \(L(H_k)\) is exactly the three edges around one original vertex: three pairwise intersecting edges in a triangle-free graph must have a common endpoint. Thus the ten distinct triangular cliques of \(L(H_k)\) recover the ten base vertices. Every line-graph vertex lies in exactly two such cliques, recovering its base edge. Consequently, every automorphism of the line graph induces an automorphism of \(H_k\), and conversely every base automorphism induces a line automorphism. Therefore the groups coincide. The plain-Python program `verification/check_symmetry.py` enumerates all adjacency- and nonadjacency-preserving base-vertex permutations by complete backtracking and obtains group orders \(20\) and \(120\).

That program also checks that each supplied representative truly has its claimed least period, canonically minimizes it over all time shifts, and applies every induced line-graph automorphism followed by temporal canonicalization. The resulting group orbits partition **all** exceptional cycle representatives and have exactly the listed sizes. Since the representative lists were generated by the exhaustive classifier, this is an exact geometric classification, not a sample of symmetry types.

**Step 5 (comparison).** The prior ten-vertex \(GP(5,1)\)/\(GP(5,2)\) classification reports primitive orbit counts \((80,6,100)\) for periods \((4,5,7)\) and \((60,30,60)\) for periods \((4,5,8)\), respectively. The directly established line-graph rows above agree with these period by period. The period-three populations instead increase from \(150\) to \(195250\), and from \(80\) to \(220810\), respectively. This proves the stated exceptional-period conservation for the two named graph pairs without claiming a general line-graph conservation law.

## Verification
Compile from the `verification` directory with `g++ -std=c++17 -O3 classify.cpp -o classify` and `g++ -std=c++17 -O3 check_independent.cpp -o check_independent`. For each \(k\in\{1,2\}\), run `./classify k` and `./check_independent k`. Compare the respective printed period/entry tables with `counts_k.txt`: the independent program prints precisely the same complete period/entry histogram in a different format. Run `./classify k --reps` and compare its output byte-for-byte with `reps_k.txt`. Finally run `python3 check_symmetry.py`; it uses only the Python standard library and verifies the full automorphism-group sizes, all exceptional phase-cycles and all geometric orbit partitions. The two compiled programs each reconstruct all \(28,697,814\) state transitions across the two graphs independently. No external certificate server, random seed or numerical approximation is required.

## Relationship to prior work
Gravner, Lyu and Sivakoff (2016, first arXiv submission 2016-10-24) establish general Greenberg–Hastings oscillation and synchronization criteria through circulation of initial colorings; their Theorem 3 does not give these fifteen-vertex line-graph orbit multiplicities, entry times, or symmetry classes. A published exact census for the original ten-vertex \(GP(5,1)\) and \(GP(5,2)\) graphs already determines their periods seven versus eight, their primitive exceptional orbit counts, and their much shorter entrance cutoffs of eight and six. The present result does **not** reclaim those original-graph counts: it directly classifies two different fifteen-vertex transition maps, observes the exact conservation of non-three counts under the line-graph operation in these instances, and detects substantially changed basins and transient depths.

A separate published line-graph study identifies proper three-edge-colorings with primitive three-cycles under **two-contact** excitation on cubic line graphs. That result concerns a different local threshold and cannot supply threshold-one primitive periods four, five, seven and eight, or their full basins. Exact excitation censuses on other individual symmetric graphs (including the twelve-vertex cuboctahedron, itself the line graph of the cube) concern different graphs and do not determine the present two cases. Targeted searches for generalized Petersen line-graph one-contact orbit enumerations and any stronger line-graph period-conservation theorem did not identify an equivalent indexed statement; this is not proof of priority.

## Limitations
This is a complete finite, reproducibly exhaustive theorem for two specific graphs, **not** a general claim that all connected cubic graphs preserve non-three excitation orbits under line-graph expansion. A potential general mechanism for the striking observed equalities is not established. Although the code verifies the complete finite state spaces and all relevant group actions, independent external mathematical audit has not been performed. Unindexed, inaccessible or differently formulated historical work may cover the same computations. The full historical literature cannot be exhaustively excluded by search; no conclusion about causal effects of Hamiltonicity, girth or graph degree is warranted.

## References
1. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first public version 2016-10-24, https://arxiv.org/html/1610.07320v1, especially the precise GHM update and Theorem 3.
2. *Exact recurrence and basins on the two ten-vertex generalized Petersen graphs*, published computational result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-recurrence-and-basins-on-the-two-ten-vertex-generalized-pe--7d4c1d4df82a, `RESULT.md`.
3. *Tait colourings as primitive-three excitation on cubic line graphs, with a constant-six seam law*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-tait-colourings-as-primitive-three-excitation-on-cubic-line-grap--c4fb511b080a, `RESULT.md`; different threshold and period scope.
