# A sharp two-flip geodesic defect for the proper bicolorings of the ternary projective plane

## Finding

Let \(\mathcal H\) be the line hypergraph on the thirteen points of \(\operatorname{PG}(2,3)\), with its thirteen four-point lines. A proper named bicoloring is a map \(c:P\to\{0,1\}\) taking both values on each line. Let \(\mathcal F\) be the graph with these colorings as vertices, where adjacent colorings differ at exactly one point. Let \(h(c,c')\) denote Hamming distance and \(d(c,c')\) shortest path length in \(\mathcal F\).

**Theorem (exact flip defect).** The graph \(\mathcal F\) is connected and cubic, has \(468\) vertices and \(702\) edges, and is self-centered with radius and diameter \(13\). For **every** pair of proper bicolorings,
\[
 d(c,c')-h(c,c')\in\{0,2\}.
\]
There are exactly \(26,208\) unordered distinct pairs with defect two and \(83,070\) with defect zero. Thus every pair can be connected by a valid recoloring sequence with at most two moves more than the number of points on which it differs, and the additive two is attained. The complete joint metric census is:

| Hamming distance | Shortest flip distance | Unordered pairs |
|---:|---:|---:|
| 1 | 1 | 702 |
| 2 | 2 | 1404 |
| 3 | 3 | 2808 |
| 4 | 4 | 5616 |
| 4 | 6 | 2808 |
| 5 | 5 | 11232 |
| 5 | 7 | 5616 |
| 6 | 6 | 14040 |
| 6 | 8 | 10296 |
| 7 | 7 | 16848 |
| 7 | 9 | 7488 |
| 8 | 8 | 16848 |
| 9 | 9 | 8424 |
| 10 | 10 | 2808 |
| 11 | 11 | 1404 |
| 12 | 12 | 702 |
| 13 | 13 | 234 |

Every coloring has the same flip-distance sphere sizes \((1,3,6,12,24,48,72,96,116,68,12,6,3,1)\), at distances \(0,1,\ldots,13\). Its unique vertex at distance \(13\) is its global color complement. The color classes in any proper bicoloring have sizes six and seven.

## Assumptions and scope

The thirteen points are the one-dimensional subspaces of \(\mathbb F_3^3\); each nonzero triple is normalized so that its first nonzero coordinate is \(1\), then the normalized point list is sorted lexicographically. For each normalized nonzero covector \(a\), its line is \(L_a=\{p:a\cdot p=0\pmod 3\}\). This produces a simple \(2\!\!-\!\!(13,4,1)\) block design: exactly thirteen four-point lines and exactly one line through any point pair. Named colors matter: a coloring and its complement are different vertices. A flip changes one point's color and may be used only when all thirteen lines remain nonmonochromatic. There is no allowance for simultaneous swaps or temporarily improper states. Claims apply only to this finite configuration, with no assertion for other projective planes or general hypergraphs.

## Proof

**Full exact finite certificate.** An unambiguous independent construction starts from the integer masks of thirteen normalized points and thirteen lines. Define \(M=2^{13}-1\) and, for each line \(L\), let \(m_L\) be its four-bit-position indicator mask. A coloring mask \(b\in\{0,\ldots,M\}\) is proper **if and only if**
\[
 \forall L:\quad 0<(b\mathbin{\&}m_L)<m_L.
\]
The comparison is valid because \(b\mathbin{\&}m_L\) is a submask of \(m_L\): it excludes exactly the empty and full line intersections. Therefore enumerating the \(8192\) integers gives all colorings without omissions. Single-point flips are precisely \(b\mapsto b\mathbin{\oplus}2^i\) for \(0\le i<13\), accepted only if the target again satisfies every line test. This constructs every edge exactly once if counted from both endpoints and divided by two. It produces \(468\) colorings, exactly \(234\) of weight six and \(234\) of weight seven; every one has degree three, so there are \(468\cdot3/2=702\) edges.

To verify **all** distances, run breadth-first search from each of the \(468\) vertices using these exact neighbors. Each search reaches all \(468\) vertices. For each unordered pair \(\{b,b'\}\) compute \(h(b,b')=\operatorname{popcount}(b\mathbin{\oplus}b')\) and tabulate the search distance. The complete table above is asserted exactly in `check_projective.py`, including the exclusion of any discrepancy except zero or two. Its entries add to \(\binom{468}{2}=109278\). The total defect-two count equals \(2808+5616+10296+7488=26208\). The searches also explicitly check the common distance-sphere sequence, connectivity, the maximum distance \(13\) and the complement as **the unique** vertex at that distance from every starting state. Hamming distance gives a lower bound because a point can change only once per move, and parity forces any excess to be even. Exhaustive verification of the stated table proves the upper bound as well, without sampling or unjustified extrapolation.

**Second independently encoded certificate.** The cyclic Singer difference set \(\{0,1,3,9\}\subset\mathbb Z/13\mathbb Z\) generates all lines as its thirteen translates. The C++ program `check_singer.cpp` verifies the \(2\!\!-\!\!(13,4,1)\) property and constructs its coloring/flip graph independently. It also implements an explicit bijection from the sorted field-coordinate points into Singer indices and checks that the two incidence-line lists agree exactly, so the second enumeration addresses the same plane rather than merely another abstract incidence structure. A fresh enumeration and \(468\) breadth-first searches recompute the entire joint distance table, defect totals, uniform distance spheres, and connectivity. The results match the Python certificate exactly.

## Verification

Run `python3 check_projective.py` and `c++ -O2 -std=c++17 check_singer.cpp -o check_singer && ./check_singer` from the extracted artifact directory. Neither needs third-party modules. Both assert all main claims and print the complete pair table; the captured outputs are `check_projective.out` and `check_singer.out`. Each program was executed from its actual source path, and the captured outputs were compared to the expected results. Exhaustive computation is justified here by the finite \(8192\)-mask universe and full \(468\)-source graph traversal, not by testing selected representatives.

## Relationship to prior work

The definition of proper two-coloring as forbidding monochromatic hyperedges appears in Mishra and Pal (2015), whose full open text treats extremal counts of properly colored hyperedges in arbitrary uniform hypergraphs, not recoloring-path distances on the ternary projective-plane line system. The static geometry of minimal nontrivial blocking sets of \(\operatorname{PG}(2,3)\) is classical. A prior public exact result, *The six-regular exchange graph of minimum nontrivial ternary projective blocking sets* (2026), proves that the \(234\) six-point blocking sets admit a connected six-regular **one-point replacement** graph with diameter six; their static count and exchange diameter are **not** claimed new. The present graph is different: it includes both six- and seven-point color classes and allows **one point to flip** per move, changing the size parity. Its sharp pairwise Hamming-distance defect bound and exact \(26208\) obstructed-pair census do not follow from the cited exchange graph's regularity, diameter or one-source shell counts alone. The published *A blocking-set obstruction to shortest oval exchanges in \(\operatorname{PG}(2,3)\)* (2026) considers exchanges between four-point ovals, not the current two-coloring states; its unrelated obstruction count \(1638\) cannot imply the present defect census. The later small-plane blocking-set classification paper (2022) was accessible in abstract but not full text, leaving a specific priority risk.

## Limitations

The central geodesic assertion rests on two complete, reproducible finite enumerations, not a general structural formula for other plane orders. It does not assert novelty of the 234 six-point blocking sets or the minimum-blocking-set exchange graph. A previously unindexed full treatment of the binary recoloring graph or an equivalent 2-colorability solution graph might imply the exact pair metric. The full 2022 paper on small Desarguesian blocking sets was not materially inspected, so its possible coverage remains a residual historical risk. No independent scholarly validation has been performed.

## References

1. T. K. Mishra and S. P. Pal, *An extremal problem in proper \((r,p)\)-coloring of hypergraphs*, arXiv:1507.02463, first public 2015-07-09, https://arxiv.org/abs/1507.02463.
2. *The six-regular exchange graph of minimum nontrivial ternary projective blocking sets*, public mathematical record (2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-six-regular-exchange-graph-of-minimum-nontrivial-ternary-pro--2ff15d411d81.
3. *A blocking-set obstruction to shortest oval exchanges in \(\operatorname{PG}(2,3)\)*, public mathematical record (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-blocking-set-obstruction-to-shortest-oval-exchanges-in-operato--b513166e882c.
4. K. Coolsaet, A. Botteldoorn, and V. Fack, *Classification of minimal blocking sets in small Desarguesian projective planes*, Journal of Combinatorial Designs 30 (2022), 561–580, https://doi.org/10.1002/jcd.21842.
