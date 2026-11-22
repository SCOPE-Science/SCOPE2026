# Six affine thirteen-waves and a sharp contact-threshold collapse on the Paley graph of order thirteen

## Finding

Let \(G\) be the Paley graph on \(\mathbb Z/13\mathbb Z\), with edges between two distinct vertices precisely when their difference belongs to the quadratic-residue set \(Q=\{1,3,4,9,10,12\}\). Write \(F_\theta\) for synchronous three-state Greenberg–Hastings excitation with contact threshold \(\theta\): state \(1\) becomes \(2\), state \(2\) becomes \(0\), and state \(0\) becomes \(1\) exactly when at least \(\theta\) neighbors are in state \(1\), otherwise remaining \(0\).

**Exact threshold-two dynamics.** For \(\theta=2\), the only primitive temporal periods are \(1,3,13\). There is one fixed configuration (all zero), exactly \(2288\) primitive three-cycles, and exactly **six primitive thirteen-cycles**. Their immediate periodic populations are respectively \(1,6864,78\). Every one of the \(3^{13}=1{,}594{,}323\) initial configurations enters a periodic orbit within \(14\) updates, and the bound is attained by precisely \(624\) configurations. Thus
\[
F_2^{53}=F_2^{14},\qquad F_2^{52}\ne F_2^{13}.
\]
The complete eventual basin populations are \(1{,}498{,}799\) for the fixed point, \(88{,}114\) for the primitive three-cycles together, and \(7410\) for the thirteen-cycles together. Each of the six thirteen-cycles has an individual basin of exactly \(1235\) initial configurations.

**Geometric thirteen-waves.** The recurrent thirteen-periodic set is precisely the orbit of one explicitly specified configuration under the \(78\) affine graph symmetries \(i\mapsto ai+b\), where \(a\in Q\) and \(b\in\mathbb Z/13\mathbb Z\). With coordinates in order \(0,1,\ldots,12\), that configuration is the word `0000002221110`. The update translates it three positions, and its affine images form six distinct traveling-wave cycles with six distinct speeds from \(Q\).

**Threshold-three collapse.** For \(\theta=3\), every initial configuration reaches the all-zero equilibrium within \(4\) updates, sharply; exactly \(101{,}062\) initial states require four updates. In particular \(F_3^4\) is the constant zero map but \(F_3^3\) is not. This is a critical half-degree threshold on the six-regular graph, not a consequence of a strict half-degree contraction bound.

## Assumptions and scope

The graph is the undirected simple \(13\)-vertex quadratic-residue circulant, not the directed cyclic or Paley tournament. Every vertex has exactly six neighbors, explicitly \(i\pm1,i\pm3,i\pm4\pmod{13}\). Vertices and colors are labelled; no symmetry quotient is taken in state or orbit counts. All states belong to \(\{0,1,2\}^{13}\). A primitive temporal cycle is an orbit counted once modulo time translation, while the basin of one cycle counts all states eventually entering that cycle, including its periodic members. The first periodic-entry time \(\tau(x)\) is the least nonnegative \(t\) for which \(F^t(x)\) is periodic. The fixed-point extinction time is the least \(t\) at which the whole configuration is zero.

## Proof

**Finite exhaustive state reduction.** Encode each configuration as the integer
\[
E(x)=\sum_{i=0}^{12}x_i3^i\in\{0,\ldots,3^{13}-1\}.
\]
The graphs in `graph/paley13_t2.txt` and `graph/paley13_t3.txt` give, for every vertex, the complete sorted list of its six neighbors; the second source program independently constructs these neighbors from \(Q\) instead. Both programs implement the stated update, with integers only, on every one of the \(3^{13}\) possible encodings for each threshold.

The first program, `verification/census_detail.cpp`, follows each unclassified state forward until it either meets a previously classified state or repeats a state in the current path. A first repetition closes a directed cycle; the number of states before the repetition gives its least period, and backward propagation along each path gives every transient state's first periodic-entry time, terminal period, and cycle-basin identifier. The second program, `verification/paley13_peel.cpp`, separately constructs all successor edges and indegrees, repeatedly removes zero-indegree vertices, enumerates the cycles remaining in the functional digraph, and propagates period, depth, and basin identifiers in reverse removal order. Every finite functional digraph consists exactly of cycles with rooted in-trees feeding them; consequently either algorithm exhausts every state and counts cycles without duplication. The independent algorithms agree on all entry-time/period cells and all individual-basin size multiplicities, not only on totals.

For threshold two they both give the three primitive-cycle counts \((1,2288,6)\) for periods \((1,3,13)\), maximal depth \(14\), and nonempty terminal depth-fourteen class of size \(624\). The basin computation gives \(6\) thirteen-cycle basins of size \(1235\), one equilibrium basin of size \(1{,}498{,}799\), and \(2288\) three-cycle basins (their exact size multiplicities appear in the full output). For threshold three, cycle enumeration leaves only the zero fixed point; the nonempty depth-four class is of size \(101{,}062\), proving the sharp four-step extinction cutoff. As all states have been exhausted, these results are finite, exact claims, not extrapolations from a sample.

**Geometric identification.** Let \(w\) be the configuration with ordered color word `0000002221110`. Substituting in the local rule gives \((F_2w)_i=w_{i-3}\) for every \(i\pmod{13}\). Therefore its temporal orbit contains thirteen distinct translated states and has least period thirteen. Every affine permutation \(i\mapsto ai+b\) with \(a\in Q\) preserves adjacency, because it multiplies each nonzero difference by another quadratic residue. These permutations commute with the synchronous update. The \(78\) affine images of \(w\) are pairwise distinct, as is confirmed by the direct finite permutation check in `verification/verify_package.py`. They are all period-thirteen states; direct orbit enumeration partitions them into exactly six cycles of thirteen states. Because the exhaustive graph census proves there are only \(6\cdot13=78\) period-thirteen states altogether, this construction accounts for **every** such state. The six individual basin sizes agree both directly and, as a consistency consequence, by affine transitivity.

## Verification

With a C++17 compiler and Python 3, run `python3 verification/verify_package.py` from the directory containing this document. The script rebuilds two separate C++17 executables, reads both graph specifications, recomputes all \(3^{13}\) transitions for both thresholds using different algorithms, compares every joint entry-period histogram cell and every basin-size multiplicity, validates all stated numbers and sharpness witnesses, and independently generates the \(78\) affine wave images and checks their actual dynamical transitions. Recorded deterministic outputs are `verification/paley_t2_census.txt`, `verification/paley_t3_census.txt`, `verification/paley_peel_output.txt`, and `verification/verify_package.out`. The complete threshold-two joint table appears in the recorded output, not merely in this summary. No external dependencies beyond a C++17 compiler and Python's standard library are needed.

The finite-state proof is conditional on executing and trusting the supplied programs and finite arithmetic; it is not a formal proof certificate or an independent external audit. The geometric wave construction itself is independently checkable by substitution.

## Relationship to prior work

Durrett and Griffeath's 1993 study established threshold-range excitable cellular automata in a spatial-lattice setting; its available archival abstract does not give the present graph-specific finite census. Gravner, Lyu and Sivakoff (2016 preprint, 2018 publication, inspected §§1–2 and main results) analyze three-state excitation on arbitrary graphs at the **one-neighbor** threshold, rather than contact thresholds two and three. Doba's 2018 full-text treatment also expressly assumes activation from **at least one** excited neighbor. Neither result directly implies the listed higher-contact primitive periods, basin populations, or sharp clocks.

Published finite-graph induced-density and above-half-degree extinction criteria imply extinction for some sparse/high-contact regimes, but the induced edge density of this six-regular graph is exactly \(3\), so the **strict** density condition is inconclusive at threshold three and false at threshold two; the above-half-degree contraction requires threshold **greater** than three. A published half-degree result forbids immediately primitive three-cycles here at threshold three because thirteen is not divisible by three, but does not rule out all other periods or determine the four-step cutoff. Previously published Clebsch and Heawood excitation censuses address different graphs and/or thresholds. Earlier Paley-graph binary-majority classifications concern a different state set and update rule. Searches for the exact graph, its circulant aliases, waves, orbit counts, threshold parameters, and basin sizes found no matching prior census. These comparisons do not establish definitive historical priority.

## Limitations

The exact claims concern only this explicitly labelled Paley graph of order thirteen and thresholds two and three. No inference is made for larger Paley graphs, arbitrary six-regular graphs, other refractory lengths, randomized rules, or directed tournaments. The finite census and geometric construction are complete for the specified model; the source-priority search is not exhaustive of unindexed literature. The 1993 primary paper was accessed via its archival abstract rather than its full document. Independent mathematical validation has not been performed.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first publicly submitted 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (publicly posted 2016-10-24), https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf.
3. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, *Complex Systems* 27 (2018), https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf.
4. *A densest-subgraph threshold and finite excitation budget for three-state graph dynamics*, published mathematical finding (2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-densest-subgraph-threshold-and-finite-excitation-budget-for-th--352367f51e91.
5. *Half-degree rigidity and a sharp contact-threshold collapse on squared cycles*, published mathematical finding (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-half-degree-rigidity-and-a-sharp-contact-threshold-collapse-on-s--7c3fe196f42d.
6. *Sharp logarithmic extinction clocks above the half-degree excitation threshold*, published mathematical finding (2026-11-17), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-logarithmic-extinction-clocks-above-the-half-degree-excita--661b1e5fd561.
7. *Paley graph*, quadratic-residue definition and \(13\)-vertex example, https://en.wikipedia.org/wiki/Paley_graph.
