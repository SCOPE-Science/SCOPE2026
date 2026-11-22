# Scientific review: minimum domination on cycles

## Correctness — PASS
The claim is the complete shattered-support polynomial of the minimum-cardinality dominating sets of a simple cycle, for all integer orders \(n\ge3\). Every minimum solution has \(\lceil n/3\rceil\) vertices and selected-to-selected clockwise gaps of lengths one, two or three. The total deficit from length-three gaps is exactly zero, one or two according to \(n\bmod3\). An arc between prescribed positive queries requires at least its nonnegative residue deficit. Zero-deficit arcs rigidly select every third vertex. This proves that unlisted pair/triple residue types and all larger supports have a missing trace. Conversely, eight explicit witnesses on the seven-cycle and complete two-query seed supports on the four- and five-cycles lift to every admissible support by inserting three vertices into any edge while adding one selected vertex. The coefficient counts are rooted cyclic-gap compositions. The separate brute-force checker enumerated 44,544 supports through 22 vertices and checked 1,420 specific lifts through 15 vertices. Enumeration corroborates, but does not replace, the unrestricted proof.

## Originality — PASS, with historical-priority qualification
Hernández-Gómez and coauthors (2020) [1] already give the complete minimum-dominating-set classification of cycles, including residue cases and orbit descriptions. This result credits that work and adds the full binary-coordinate trace/shattering classification, exact support polynomial, and gap-deficit lifting and missing-label arguments. Brewster, Mynhardt and Teshima (2023) [2] analyze the distinct minimum *independent* domination reconfiguration problem. The closest published-finding corpus cycle record [3] treats **inclusion-minimal** dominating sets and finite adaptive shattering, not the minimum-cardinality class; another [4] treats minimum independent dominating sets of **paths**. The original sources were inspected for statements and implications, not only searched by title. No inspected result directly gives the all-order stated polynomial. A later or differently named equivalent result remains a genuine priority risk.

## Value — PASS
The scalar domination number and the counts of optimum solutions do not answer which collections of vertex labels are simultaneously independently realizable. This theorem answers the full incidence-trace question for an infinite classical family, identifies a sharply bounded rank-three shattering complex, and shows a period-three transition between VC dimensions one, two and three. A residue-only decision criterion and explicit all-face counts can be used without enumerating the optimal solutions. These are motivated structural consequences of optimal domination, not arbitrary finite parameter slices.

## Scope and limitations
The distinction between minimum and inclusion-minimal domination is essential. No theorem about all dominating sets, online shattering, or other graph families is claimed. The full primary descriptions of minimum solutions are acknowledged as prior. Historical originality is qualified by unindexed possible equivalents, and the polynomial has not had an independent mathematical audit.

## References
1. J. C. Hernández-Gómez et al., *Transitivity on Minimum Dominating Sets of Paths and Cycles*, *Symmetry* 12 (2020), 2053, https://doi.org/10.3390/sym12122053, published 2020-12-11.
2. R. C. Brewster, C. M. Mynhardt, and L. E. Teshima, *The i-Graphs of Paths and Cycles*, arXiv:2303.08190v1, https://arxiv.org/html/2303.08190v1.
3. *The first minimal-domination cycle gap: complete five-query traces and a vertex-transitive amplification*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-first-minimal-domination-cycle-gap-complete-five-query-trace--84ef6ec729bc.
4. *A periodic shattering law for minimum independent dominating sets of paths*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-periodic-shattering-law-for-minimum-independent-dominating-set--ab94895bb7a2.

Self-review: passed. Independent audit: not yet performed.
