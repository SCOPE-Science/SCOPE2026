# Exceptional one-contact excitation persists under line-graph expansion of the pentagonal prism and Petersen graph

## Finding

For the synchronous, one-contact, three-state Greenberg–Hastings rule, the primitive temporal orbit counts at every least period **other than three** are unchanged by taking the line graph of either the pentagonal prism or the Petersen graph. On the two line graphs, the nonconstant exceptional orbits fall into thirteen geometric classes for the prism and just one class at each of the three exceptional periods for the Petersen graph. These are exact comparisons for these two graph pairs, not a conservation law for line graphs generally.

Let \(H_1=GP(5,1)\), \(H_2=GP(5,2)\). For each of the four graphs the complete primitive temporal orbit counts, with time shifts identified but sites and states labelled, are:

| Least period | \(H_1\) [2] | \(L(H_1)\) | \(H_2\) [2] | \(L(H_2)\) [3] |
| --- | ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 1 | 1 |
| 3 | 150 | 195250 | 80 | 220810 |
| 4 | 80 | 80 | 60 | 60 |
| 5 | 6 | 6 | 30 | 30 |
| 7 | 100 | 100 | 0 | 0 |
| 8 | 0 | 0 | 60 | 60 |

There are no other least periods. The base counts are those of [2]. The labelled Petersen-line orbit counts, basin counts and entry-depth census are also reported for threshold one in [3]; their reproduction here serves as a benchmark for the comparison, not as a separate new census of that graph.

The sharp maximum first-periodic-entry time on the prism line graph is \(17\), attained by exactly \(80\) states; its Petersen-line counterpart is \(12\), attained by \(1200\) states [3]. In both cases the deepest states enter three-cycles. The eventual-period basin populations, inclusive of recurrent states, are:

| Eventual period | \(L(H_1)\) | \(L(H_2)\) [3] |
| --- | ---: | ---: |
| 1 | 292287 | 277077 |
| 3 | 13208940 | 13229250 |
| 4 | 714720 | 201240 |
| 5 | 45780 | 536580 |
| 7 | 87180 | 0 |
| 8 | 0 | 104760 |

The full line-graph automorphism group partitions primitive temporal orbits of each nonconstant exceptional period into the following geometric classes. Entries are class sizes measured in primitive temporal orbits.

| Graph | Period four | Period five | Long exceptional period |
| --- | --- | --- | --- |
| \(L(H_1)\) | \(10,10,10,10,20,20\) | \(2,4\) | five classes of size \(20\) at period seven |
| \(L(H_2)\) | one class of size \(60\) | one class of size \(30\) | one class of size \(60\) at period eight |

## Assumptions and scope

The ten base vertices are \(u_i,v_i\), with indices in \(\mathbb Z/5\mathbb Z\). The fifteen undirected edges are \(u_i u_{i+1},u_i v_i,v_i v_{i+k}\) for \(k\in\{1,2\}\). Each base graph is connected, cubic and triangle-free. Its line graph is simple, connected and four-regular, with edges of the base graph as its fifteen sites; sites are adjacent exactly when their corresponding base edges meet.

A configuration labels each site by \(0\) (rest), \(1\) (excited) or \(2\) (refractory). Updates are simultaneous: \(1\mapsto2\), \(2\mapsto0\), while \(0\mapsto1\) if at least one open neighbor is excited and otherwise \(0\mapsto0\). First-periodic-entry time is the least \(t\ge0\) for which \(F^t(x)\) is periodic, and eventual period is that state's least period. No quotient by colour permutations is taken.

## Proof

**Exhaustive labelled classification.** Order the fifteen base edges by outer edges, spokes and inner edges, each in increasing \(i\). Encode configurations by \(s=\sum_{j=0}^{14}x_j3^j\) for \(0\le s<3^{15}\), so each state occurs exactly once. Neighbors are computed by checking whether the base edges share an endpoint. The update applies the three local cases to the input digits, not the partially updated state. The code checks that all fifteen neighbor sets have size four.

`verification/classify.cpp` follows an unclassified state to the first repeat or the first state with a known classification. A repeat within the current path identifies exactly the cycle, with least period equal to the length of the repeated segment and depth zero on it. Propagation backward assigns each remaining path vertex its successor's least eventual period and one plus its distance to the cycle. Every state is assigned once. Thus a count of depth-zero states at least period \(p\), divided by \(p\), counts each primitive orbit once. Basin sizes are sums over all depths at fixed eventual period. This gives `verification/counts_1.txt` and `verification/counts_2.txt`, and one representative for every period-four-or-longer orbit in `verification/reps_1.txt` and `verification/reps_2.txt`.

`verification/check_independent.cpp` separately constructs the complete successor and indegree arrays. Repeated deletion of indegree-zero vertices eliminates exactly the noncyclic states: no member of a directed cycle can be deleted, and in a finite functional graph each incoming tree is ultimately deleted starting at its leaves. Traversing the remaining directed cycles gives their lengths, and reverse deletion order recovers transient distances. The two implementations agree in all 46 and 37 nonzero period/entry cells for the respective graphs. Each basin table totals \(3^{15}=14{,}348{,}907\). In particular, the nonzero entry cells at the sharp maxima are \((p,t,\mathrm{count})=(3,17,80)\) and \((3,12,1200)\).

**Full spatial quotient.** A line-graph triangle is exactly the clique of edges incident to a base vertex: three pairwise intersecting edges either share a vertex or form a base triangle, which is ruled out here. The ten distinct cliques recover the ten base vertices, and each site belongs to precisely the two cliques corresponding to its edge endpoints. Thus a line-graph automorphism induces a base automorphism and conversely. `verification/check_symmetry.py` enumerates all base automorphisms by adjacency-preserving permutation backtracking, yielding group orders \(20\) and \(120\). The program checks least periods of the listed representatives and identifies each time orbit by its minimal state encoding. Applying every induced site permutation, followed by the temporal minimization, partitions the exhaustive list and gives the geometric class sizes above.

**Comparison.** Compare the complete line-graph columns with the base columns of [2]. The equality includes all the periods absent from both graphs of a given pair, since the full census has no other periods. The large changes at period three and in first-periodic-entry depth distinguish exceptional-count preservation from preservation of the whole dynamics.

## Verification

In `verification`, compile `g++ -std=c++17 -O3 classify.cpp -o classify` and `g++ -std=c++17 -O3 check_independent.cpp -o check_independent`. For each \(k=1,2\), run `./classify k` and `./check_independent k` and compare their period/entry histograms with `counts_k.txt`. Compare `./classify k --reps` to `reps_k.txt`. Run `python3 check_symmetry.py` to verify the symmetry classes against these complete lists. Enumeration is exact and uses no sampling or numerical tolerances.

## Relationship to prior work and limitations

The earlier base-graph census [2] already determines the two distinct long periods, primitive counts, and sharp entry times \(8,6\) on the ten-site graphs. The separate Petersen-line study [3] treats all four thresholds and gives the same labelled threshold-one orbit, basin and entry data as used here. The contributions here are the complete one-contact prism-line classification, the exact non-three comparison on the two base/line pairs, and the exceptional geometric partitions on the line graphs. The same-day source [3] is cited for overlapping results without asserting an order of priority.

General circulation criteria [1, Theorem 3] describe synchronization and limiting excitation rates, not these counts or geometric partitions. The line-graph Tait-colouring result [4] uses a two-contact rule and period three, not these one-contact exceptional periods. No bijection between base and line-graph orbits is established and no conclusion about general line-graph preservation, degree, girth or Hamiltonicity is implied. The inspected literature cannot settle priority beyond the stated comparisons.

## References

1. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, [arXiv:1610.07320](https://arxiv.org/abs/1610.07320), Theorem 3.
2. *Exact recurrence and basins on the two ten-vertex generalized Petersen graphs*, [Resultary, 2026-11-02](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-exact-recurrence-and-basins-on-the-two-ten-vertex-generalized-pe--7d4c1d4df82a).
3. *Complete excitation and extinction censuses on the Petersen line graph*, [Resultary, 2026-11-22](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-complete-excitation-and-extinction-censuses-on-the-petersen-line--ccade4380bb4), threshold-one rows.
4. *Tait colourings as primitive-three excitation on cubic line graphs, with a constant-six seam law*, [Resultary, 2026-11-08](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-tait-colourings-as-primitive-three-excitation-on-cubic-line-grap--c4fb511b080a).
