# Self-review: temporal basins in three-state excitation on a pendant clique

## Correctness — PASS

The mathematical domain is every labelled graph obtained from a clique on \(r+1\) vertices, \(r\ge2\), by attaching \(s\ge1\) leaves at one fixed clique hub, with synchronous three-state Greenberg–Hastings updates. The claim is a complete ten-class distribution of initial states by entry time \(t\in\{0,1,2,3,4\}\) and least eventual period \(p\in\{1,3\}\), plus identical five-layer basin populations for each primitive three-cycle.

The quotient by the hub state and the two nonempty occupied-color supports is exact because each initially monochromatic vertex class with an identical neighborhood evolves identically. The update on all 147 support signatures and its finite coefficient matrix is stated explicitly in the proof; `code/verify_signatures.py` checks the full finite case analysis. The separate forced leaf trajectory against a rainbow clique cycle gives the individual basin layers \((3,2^s-1,3^s-1,3^s-1,3^s-2^s)\). The nonoscillatory coefficient matrix, multiplied by the exact numbers of surjections onto each occupied-color support, yields the five fixed-point entry formulas. Together they exhaust \(3^{r+s+1}\) labelled states. The positive last three-cycle layer for every \(s\ge1\) makes the four-step upper bound sharp.

`code/verify_direct.py` evolves 392,040 labelled states on 20 actual graphs, with separate graph adjacency and no use of the support quotient; it also verifies individual periodic-orbit basins. Both programs were executed from the packaged sources; their observed outputs are saved in `checks/verification_output.txt`. Finite enumeration is a complete argument only for the 147-state quotient, whose exact relationship to arbitrary labelled configurations is proved, not inferred statistically. All claimed infinite-parameter formulas follow from the exact recurrence, leaf clock, and surjection identities.

## Originality — PASS, qualified

The closest primary text is Gravner–Lyu–Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (2016-10-24), the full HTML text of which was inspected, including the update definition, the finite-graph theorems and proof, and its references. Its general finite-graph characterization already accounts for the qualitative dichotomy of fixation and persistent excitation. This qualitative dichotomy is **not** claimed as new. The compared results do not state the complete exact ten-class entrance distribution on pendant cliques, nor the equal per-cycle basin sizes and precise five-layer profile.

Accessible preceding scientific claims concern either the same dynamics on friendship or complete multipartite graphs, or different rules on pineapple and tree-grafted clique graphs. Those claims are not generally equivalent to the exact labelled entrance counts for Greenberg–Hastings excitation on a pendant clique. Published-record searches and web searches using the graph family, rule, orbit entries, aliases and parameter expressions found no stronger statement that entails this complete profile. This is evidence of no identified overlap, not a guarantee of novelty. The 1978 origin paper was available as bibliographic reference only; an unindexed or inaccessible equivalent remains a risk.

## Mathematical value — PASS

The invariant is natural: for an excitable system on a canonical clique-with-leaves family, the exact basin partition resolves not merely whether a state eventually oscillates but precisely when it enters a specified primitive orbit. The exact five-layer orbit-by-orbit distribution is independent of the number of core vertices and is sharply different from the extinction layer structure. The resulting conditional three-way large-leaf limit provides a robust parameter law. These statements are motivated by temporal propagation through hub-attached leaves and supply more than an unmotivated small instance or a routine application of the general circulation criterion.

## Limitations and closest literature

The finding is confined to three-state synchronous one-neighbor excitation, a single hub for all leaves, and \(r\ge2,s\ge1\). The qualitative fixation/oscillation partition was previously known by general circulation theory. Historical-priority comparisons remain bounded by accessible sources and possible unindexed or privately circulated equivalents. No independent expert audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
