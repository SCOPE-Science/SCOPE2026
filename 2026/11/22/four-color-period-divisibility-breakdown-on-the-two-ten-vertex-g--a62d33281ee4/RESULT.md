# Four-color period-divisibility breakdown on the two ten-vertex generalized Petersen graphs

## Finding

Let \(C\) be the synchronous four-color cyclic successor-contact automaton and \(H\) the synchronous four-state threshold-one Greenberg–Hastings excitation automaton. Start both from the **same** coloring on each of the labelled cubic graphs \(GP(5,1)\) (the pentagonal prism) and \(GP(5,2)\) (the Petersen graph). Across all \(4^{10}=1{,}048{,}576\) possible initial colorings on **each** graph, their joint eventual least periods \((p_C,p_H)\) have the exact counts below.

| \((p_C,p_H)\) | \(GP(5,1)\) | \(GP(5,2)\) |
|:--|--:|--:|
| \((1,1)\) | 419936 | 402496 |
| \((1,4)\) | 197380 | 24360 |
| \((1,5)\) | 12900 | 155880 |
| \((4,1)\) | 14930 | 1020 |
| \((4,4)\) | 340090 | 22560 |
| \((4,5)\) | 6100 | 21900 |
| \((5,1)\) | 1900 | 25620 |
| \((5,4)\) | 37200 | 43680 |
| \((5,5)\) | 12980 | 351060 |
| \((6,1)\) | 80 | 0 |
| \((6,4)\) | 5080 | 0 |

Every unlisted ordered pair has zero states. Each column sums to \(1{,}048{,}576\). On the prism exactly \(275{,}570\) initial colorings have unequal periods, and exactly \(258{,}660\) have \(p_H\nmid p_C\); on the Petersen graph the corresponding counts are \(272{,}460\) and \(245{,}820\). Thus **the four-color system violates pointwise inter-model period divisibility on both canonical cubic graphs**. The previously established three-color theorem \(p_H\mid p_C\) on every finite graph does not extend unchanged to four colors.

The two automata also have distinct sharp first-periodic-entry maxima, in CCA/GHM order: \((11,8)\) on the prism and \((11,11)\) on the Petersen graph. These are auxiliary consequences of the same complete finite classification, not asymptotic predictions.

## Assumptions and scope

For \(k\in\{1,2\}\), let \(GP(5,k)\) have vertices \(u_i,v_i\), \(i\in\mathbb Z/5\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+k}\) for every \(i\). There are ten vertices and fifteen distinct undirected edges. Colors are \(0,1,2,3\); updates are simultaneous and use only neighbors, with no loops or threshold-two rule.

At a vertex of color \(c\), the cyclic successor-contact rule advances to \(c+1\pmod4\) if at least one neighbor currently has that successor color, otherwise retaining \(c\). The Greenberg–Hastings rule advances \(1\to2\to3\to0\) unconditionally, and a resting vertex \(0\) changes to \(1\) precisely when at least one neighbor is currently in state \(1\), otherwise retaining \(0\). Both are deterministic maps on the full set of labelled configurations.

The eventual least period \(p_T(x)\) of a map \(T\) at an initial state \(x\) is the length of its unique terminal directed cycle. The first-periodic-entry time \(\tau_T(x)\) is the least nonnegative \(t\) for which \(T^t(x)\) already lies on that directed cycle. No quotient by time shifts or spatial automorphisms is taken in any table.

## Proof

**1. Exhaustive finite reduction.** Encode a configuration uniquely by
\[
s(x)=\sum_{i=0}^4 x(u_i)4^i+\sum_{i=0}^4x(v_i)4^{i+5},\qquad 0\le s(x)<4^{10}.
\]
For either \(k\) and either update rule, its entire functional graph therefore has exactly \(2^{20}\) labelled states. The source `compare.cpp` builds each of the fifteen edges from the explicit \(GP(5,k)\) formula; for every encoded state, it evaluates each of the ten local rules against the three neighbors, recording a unique integer successor. Every state is visited, not sampled.

**2. Complete cycle classification.** `compare.cpp` traces each as-yet-unclassified state along successors until it meets a previously visited state. If that state belongs to the current trace, the suffix is a directed cycle: mark its least period as the suffix length and its entry time as zero. Working backwards from the cycle (or from an earlier classified state) assigns the same least period and an entry time one higher than its successor. Every finite functional graph is a disjoint union of rooted in-trees feeding directed cycles, so the algorithm classifies *every* state and recovers both invariants exactly. It produces the joint table and the two sharp maxima in `compare.out`.

**3. Independent full reconstruction.** The separately implemented `verify_indegree.cpp` constructs the prism directly as the Cartesian product \(C_5\square K_2\), and the Petersen graph in another vertex ordering as the disjointness graph \(KG(5,2)\). It constructs successors using base-four digit arrays rather than the first program's bit operations, then performs indegree-zero elimination. Exactly the directed-cycle vertices remain; identifying cycles and processing the eliminated states backwards produces the same periods and entry times. Its joint table (`verify_indegree.out`) matches `compare.out` for both graphs. Consequently this does not assume the table or rely on a single graph encoding or orbit-finding algorithm.

**4. Divisibility and a concrete boundary witness.** Sum exactly those table cells satisfying \(p_H\nmid p_C\): on \(GP(5,1)\) these are \((1,4),(1,5),(4,5),(5,4),(6,4)\), totaling \(258{,}660\); on \(GP(5,2)\) they are \((1,4),(1,5),(4,5),(5,4)\), totaling \(245{,}820\). Every other observed pair has \(p_H\mid p_C\). The difference between these totals and the unequal-period counts arises from unequal pairs where \(p_H=1\).

For example, on \(GP(5,2)\), the initial encoded state \(s=6\) has digit word `2100000000` in the order \((u_0,\ldots,u_4,v_0,\ldots,v_4)\). Its CCA sequence starts

```
2100000000 -> 2210001000 -> 2221002111 -> 2222112222 -> 2222222222
```

and stays fixed at the final all-two state. Its GHM sequence starts

```
2100000000 -> 3210001000 -> 0321002111 -> 0032113222
             -> 1003220333 -> 2100330000 -> 3210001000
```

and therefore enters a genuine five-cycle at its first update (the five displayed states beginning with `3210001000` are distinct and recur). Hence \(p_C(6)=1\) and \(p_H(6)=5\), a direct witnessed failure of divisibility. On the prism, \(s=2054\) similarly has \((p_C,p_H)=(1,5)\). `verify_witness.py` independently executes the displayed trajectories and verifies the two witnesses.

## Verification

Run the complete, self-contained standard C++17 checks with

```
g++ -O3 -std=c++17 compare.cpp -o compare && ./compare > current_compare.out
g++ -O3 -std=c++17 verify_indegree.cpp -o verify_indegree && ./verify_indegree > current_verify_indegree.out
python3 verify_witness.py
```

Compare the first two outputs byte for byte with `compare.out` and `verify_indegree.out`, respectively. Both implementations enumerate every one of \(4^{10}\) states for each graph and each map. The second checker differs in graph construction and orbit-finding method. `verify_witness.py` validates the two explicitly claimed five-cycle counterexamples directly from the local rules. Both period-table columns, marginal totals, entry-time maxima, and divisibility counts are recomputable from the included code; only standard compilers and the Python standard library are required.

## Relationship to prior work

The 1978 Greenberg–Hastings model and the explicit arbitrary-color CCA/GHM rules in Fisch–Gravner–Griffeath (1991) are prior theory. The latter concerns excitable wave behavior on two-dimensional lattices and does not give a matched-input table for either ten-vertex generalized Petersen graph. Gravner–Lyu–Sivakoff's full arXiv paper `1610.07320` establishes results for **three** colors on arbitrary finite graphs, but not the four-color joint-period table on either graph. A separately published three-color inter-model clock reconstruction proves \(p_H\mid p_C\) for **three-color** matched inputs, a conclusion falsified here for four colors; we do not claim that earlier theorem is false within its own scope.

The published exact three-color joint-period census of \(GP(5,1)\) and \(GP(5,2)\) gives a prism equality and a Petersen eight-to-four collapse, but does not determine the four-color population above. Another published result determines the **four-state GHM marginal** period and transient distributions on the Petersen graph; our GHM marginal agrees with that result exactly and is not claimed as new. Similarly, the prior four-state prism GHM census is respected. A published four-color GHM/CCA coincidence on complete tripartite graphs does not cover either generalized Petersen graph: the prism and Petersen have five-cycles, while complete tripartite graphs have a different edge structure and recurrent period classification. The new contribution here is the full **matched-initial-state, four-color joint-period classification** and the resulting sharp failure of three-color period divisibility on two canonical cubic graphs.

## Limitations

The result is finite and specific to these two graphs and four-color threshold-one synchronous rules. It does not establish the first possible graph size for period-divisibility failure, or a theorem about all cubic graphs. The exact tabulation is supported by fully exhaustive, independently implemented integer algorithms, not by a short general symbolic formula. The data do not assert that all time trajectories are related by a conjugacy. Relevant indexed records and selected primary full texts were examined, but this is not a guarantee against unindexed earlier equivalent calculations; no independent external audit has been performed.

## References

1. J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, SIAM Journal on Applied Mathematics **34** (1978), 515–523, DOI: https://doi.org/10.1137/0134040 (historical model; bibliographic record).
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, archival public preprint dated 1993-03-22, https://arxiv.org/abs/patt-sol/9303002 (archival scope and model background; full paper examined).
3. R. Fisch, J. Gravner and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, *Statistics and Computing* **1** (1991), 23–39, https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf (full accessible paper consulted for model definitions and graph scope).
4. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, posted 2016-10-24, https://arxiv.org/abs/1610.07320 (full 2016 preprint examined).
5. *Exact excitation clock reconstruction and period divisibility for three-color graph automata*, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-excitation-clock-reconstruction-and-period-divisibility-fo--6edafe27dc02 (published mathematical result; `RESULT.md` examined).
6. *Petersen-specific period doubling between cyclic and refractory excitation dynamics*, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-petersen-specific-period-doubling-between-cyclic-and-refractory--85df9829d668 (three-color graph-pair comparison; `RESULT.md` examined).
7. *Five-cycle survival and two four-cycle symmetry types in four-state Petersen excitation*, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-five-cycle-survival-and-two-four-cycle-symmetry-types-in-four-st--9ac3197a4c9b (four-state Petersen GHM marginal; `RESULT.md` examined).
8. *Four-state excitation on tripartite graphs: identical four-cycle orbits, different transients, and exact extinction*, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-four-state-excitation-on-tripartite-graphs-identical-four-cycle--6411c0882be0 (four-color comparison on a different graph family; `RESULT.md` examined).
