# Complementary Petersen dynamics: matched excitation basins and 118 geometric wave classes on the triangular graph

## Finding

On the ten-vertex triangular graph \(T(5)=L(K_5)=J(5,2)\), the synchronous three-color cyclic cellular automaton (CCA) and three-state Greenberg–Hastings model (GHM), both with contact threshold one, assign **the same eventual least temporal period to each of the \(3^{10}=59{,}049\) labelled initial colorings**. Their only eventual least periods are one and three. Precisely \(3{,}399\) configurations eventually become fixed and \(55{,}650\) eventually enter a primitive three-cycle, for each model. Every one of the \(30{,}240\) immediately primitive-three-periodic configurations is common to both models, and the two maps act identically on this common recurrent subset. Thus both systems have exactly \(10{,}080\) primitive temporal three-cycle orbits, but different fixed states and transient clocks.

For an initial configuration \(x\), write \(T(x)\) for the minimum number of updates needed to reach a periodic state and \(p(x)\) for the eventual least temporal period. The **complete joint census** of \((T(x),p(x))\), with no quotienting by graph automorphisms, is:

| Entry updates \(T\) | CCA: period one | CCA: period three | GHM: period one | GHM: period three |
|---:|---:|---:|---:|---:|
| 0 | 3 | 30,240 | 1 | 30,240 |
| 1 | 2,916 | 20,370 | 1,023 | 6,700 |
| 2 | 480 | 5,040 | 1,133 | 8,470 |
| 3 | 0 | 0 | 1,082 | 8,560 |
| 4 | 0 | 0 | 160 | 1,680 |
| **Total** | **3,399** | **55,650** | **3,399** | **55,650** |

Both bounds are sharp: every CCA state is periodic by the second update and every GHM state by the fourth. The CCA has three monochromatic fixed configurations and the GHM has only its all-zero fixed configuration. Furthermore the complete graph automorphism group is \(S_5\), and the \(10{,}080\) common primitive-three temporal cycles form **exactly 118 spatial symmetry orbits**, with the following orbit-size multiplicities:

| Number of temporal cycles per spatial orbit | Number of spatial orbits |
|---:|---:|
| 15 | 2 |
| 20 | 3 |
| 30 | 7 |
| 60 | 49 |
| 120 | 57 |

The graph is the *complement* of the Petersen graph. On the Petersen graph the two automata have a documented class of \(4{,}800\) colorings with unequal eventual least periods (eight under CCA, four under GHM). The present complete classification therefore identifies a canonical complement with exact pointwise period agreement, shared three-cycle wave geometry and markedly different transient time laws.

## Assumptions and scope

Index the ten vertices lexicographically as the two-element subsets \(v_0=(0,1),v_1=(0,2),v_2=(0,3),v_3=(0,4),v_4=(1,2),v_5=(1,3),v_6=(1,4),v_7=(2,3),v_8=(2,4),v_9=(3,4)\) of the five-element set \(\{0,1,2,3,4\}\). Two distinct vertices are adjacent exactly when their corresponding subsets **intersect**. Each vertex has degree six. A labelled configuration \(x\) assigns each vertex a color in \(\{0,1,2\}\), and all sites update simultaneously. Under CCA, a vertex at color \(c\) advances to \(c+1\pmod3\) if it has a neighbor of that successor color, and otherwise holds its color. Under GHM, a site advances \(1\to2\to0\) unconditionally, while \(0\to1\) requires a neighbor of color one. No randomization, refractory delay variation, tie-breaking, rotation quotient or threshold change is involved.

Here \(T(x)=\min\{t\ge0:F^t(x)\text{ belongs to a directed temporal cycle}\}\), and \(p(x)\) is the least positive return period of that cycle. The two functions \(F\) have their model-specific meanings. A temporal cycle is identified modulo time origin; an additional *spatial symmetry orbit* identifies such temporal cycles under graph automorphisms. The main pointwise comparison uses exactly the same initial color assignment for both models.

## Proof

**1. Complete finite-state algorithm.** Encode each state by \(e(x)=\sum_{i=0}^{9}3^i x(v_i)\). This is a bijection onto the integers \(0,\ldots,59{,}048\). The standalone source `verification/census.py` constructs, using the explicit adjacency and rules above, the complete list of \(59{,}049\) successors separately for the two automata. Each vertex in this finite functional digraph has one outgoing arrow. Repeatedly remove every vertex with indegree zero, recording the deletion order; the remaining vertices are *exactly* the directed cycles. Indeed every noncyclic in-tree has a removable source and removing all such sources cannot remove a vertex of a directed cycle. Traverse each surviving cycle to determine its exact least period, give its vertices entry time zero, and then process the deleted vertices in reverse order. A deleted vertex has entry time one more than its successor and the same eventual least period. This is an exhaustive classification of the entire graph, not a partial trajectory sample.

The resulting exact integers are tabulated in `data/census.json`, and give precisely the joint census displayed above. The CCA cycle census consists of three fixed states and \(10{,}080\) primitive three-cycles; GHM has one fixed state and \(10{,}080\) primitive three-cycles. Comparing the two arrays of eventual periods entry by entry shows equality for every \(e(x)\), proving the stated *pointwise* identity. The largest nonzero entry time equals two for CCA and four for GHM, with positive populations at both cutoffs, proving sharpness.

**2. Common recurrent wave geometry.** The complete transition enumeration finds exactly \(30{,}240\) period-three states at entry time zero for either rule, with precisely the same integer state indices. It additionally compares the two successors of each such state and finds them identical. Independently of orbit classification, `verification/census.py` checks for all \(59{,}049\) colorings the equivalent local characterization: a coloring belongs to this common recurrent subset **if and only if** every vertex has at least one neighbor carrying the successor color. Necessity and sufficiency of the forward implication are also transparent from the definition: when this holds, every site advances by one color at each time, so all neighboring color differences are preserved and the same condition holds at each of the three updates; these are exactly common primitive-three cycles. The converse for the entire graph is established by exhaustive comparison, not asserted for arbitrary graphs. Thus all \(30{,}240\) common states are partitioned into \(30{,}240/3=10{,}080\) temporal cycles, with identical transitions in both models.

**3. Independent complete orbit reconstruction.** The standalone `verification/independent.cpp` constructs the adjacency from pair-intersection tests and the two local rules using a separate C++ implementation. For each of the \(59{,}049\) initial states, for each model, it uses Floyd's tortoise-and-hare method to find the first cycle-entry time and the least period, without indegree pruning or reusing the Python successor table. It checks the complete joint census and the independent pointwise cross-model period table, with \(3{,}399\) period-one and \(55{,}650\) period-three initial states. This independently proves the finite enumeration conditional only on the displayed, inspectable integer algorithms.

**4. Complete spatial symmetry.** A clique in the triangular graph is an intersecting family of two-subsets of a five-set. Every intersecting family without a common point has size at most three: if two edges meet at a point, but a third misses that point, all further edges intersecting those three must lie among the edges of their triangle. Consequently the only cliques of size four are the five four-edge *stars* of the underlying \(K_5\), one at each base point. These five maximal cliques intrinsically recover the five base points; each triangular-graph vertex is the intersection of its two corresponding stars. Every graph automorphism therefore induces a unique permutation of the five stars, and conversely every permutation induces an automorphism. Hence \(\operatorname{Aut}(T(5))\cong S_5\), of order \(120\).

For each of the \(10{,}080\) primitive-three cycles take its smallest encoded state as canonical representative. `verification/symmetry.py` enumerates all \(120\) point permutations, verifies that each preserves adjacency, maps each representative and reduces its image modulo the three temporal phases. Group orbit enumeration visits **all** \(10{,}080\) representatives, producing the five orbit-size classes in the table and exactly \(118\) orbits. The complete canonical representative list and multiplicities are supplied in `data/symmetry.json`; the list also gives a finite certificate that every orbit has been accounted for. Every orbit size divides \(120\), as required by orbit–stabilizer. The weighted identity \(2(15)+3(20)+7(30)+49(60)+57(120)=10{,}080\) provides an independent consistency check.

## Verification

Run `python3 verification/check_all.py` from the directory containing `verification/` and `data/`, using Python 3 and a C++17 compiler. The command independently runs `verification/census.py`, `verification/symmetry.py` and the separately compiled `verification/independent.cpp`; the Python scripts also check the exact contents of `data/census.json` and `data/symmetry.json`. Each algorithm is deterministic and uses only finite integer operations, with no downloaded input or randomized sampling. The observed terminal markers are `CENSUS_ALL_59049_OK`, `SYMMETRY_ALL_10080_OK`, `INDEPENDENT_FLOYD_ALL_59049_OK` and `ALL_EXHAUSTIVE_CHECKS_OK`. These finite complete algorithms are the proof certificates; they do not certify any unexamined infinite-family statement.

## Relationship to prior work

Durrett and Griffeath originally analyzed the synchronous excitable-media families, including CCA and GHM, with emphasis on lattice spirals and threshold phenomena [1]. Gravner, Lyu and Sivakoff's general graph theorem [2] characterizes eventual synchronization using a conservative graph 1-form and expresses asymptotic excitation activity through maximal cycle integrals. The theorem supplies useful qualitative background but does not enumerate labelled temporal cycles, first-entry times or spatial symmetry classes for \(T(5)\); the full 2018 author-hosted text was consulted in particular around the model definitions and Theorem 3.

A published comparison of CCA and GHM on the *Petersen graph*, \(KG(5,2)\), exhibits exactly \(4{,}800\) initial configurations with period eight under CCA but four under GHM [3]. The present graph is its graph complement, so that result neither covers the present graph nor implies its matching period basins; the contrast motivates this exact classification. Published work proves pointwise eventual-period agreement for **complete bipartite** graphs [4], but \(T(5)\) has triangles and degree six, so that theorem does not imply the result. Another published finite classification concerns \(KG(6,2)\), which has fifteen vertices and different adjacency, not \(J(5,2)\) [5]. These are claim-to-claim comparisons; the searches cannot establish absolute historical priority against all unindexed tables.

## Limitations

The conclusions are **finite** and specific to this one labelled ten-vertex graph, three colors, contact threshold one, and synchronous updates. The group-orbit distribution is a finite complete classification, not a formula for all triangular graphs. Matching eventual period does not mean identical transient trajectories or identical fixed states. No classification is asserted for perturbed graphs or higher color counts. The graph-census and group-census theorems depend on complete, reproducible enumeration; they are not analytic closed-form all-size results. Although close primary results were compared, an older unindexed equivalent census cannot be ruled out. No independent external mathematical audit has been performed.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first public arXiv version 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first public 2016-10-24, https://arxiv.org/abs/1610.07320 ; author-hosted full 2018 text https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf .
3. *Petersen-specific period doubling between cyclic and refractory excitation dynamics*, published finite census, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-petersen-specific-period-doubling-between-cyclic-and-refractory--85df9829d668 .
4. *Matched eventual periods but different transient clocks for three-state excitable dynamics on bicliques*, published family classification, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-matched-eventual-periods-but-different-transient-clocks-for-thre--29320e9e89df .
5. *Exact excitation clocks and \(S_6\)-symmetry on the first triangular Kneser graph*, published finite census of \(KG(6,2)\), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-excitation-clocks-and-s-6-symmetry-on-the-first-triangular--df4858aabb3d .
