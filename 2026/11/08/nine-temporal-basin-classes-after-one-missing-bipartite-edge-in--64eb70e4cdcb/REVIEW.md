# Scientific review

## Correctness — PASS

The single missing edge distinguishes exactly two vertices; the ordinary vertices in each shore have identical neighborhoods. For a fixed labelled coloring, each initially occupied ordinary color class therefore evolves identically, so tracking one representative of each such class is information-preserving for exact labelled return times. Two nonempty supports, two distinguished colors and their tracked representatives define only 441 signatures. The explicit four-tuple transition is fully specified in RESULT.md. Exact finite iteration produces the nine-class support coefficient table, and inclusion–exclusion supplies the weight for each labelled assignment. The proof checks that classes which merge remain separately tracked; hence the abstract and labelled entry times coincide. Independent direct adjacency-based enumeration covers 1,185,921 configurations from 25 graph sizes, and the support computation checks all 441 signatures and the total population. The proof's unlimited graph-size quantification follows from the reduction, not extrapolation of finite graph tests. The maximum transient is attained on every permitted graph by a displayed four-step state sequence.

## Originality — PASS, qualified

The CCA rule and the general circulation criterion for synchronization are established in Gravner–Lyu–Sivakoff (arXiv:1610.07320, 2016-10-24); their Theorem 3 already implies the diameter bound for synchronizing configurations. That general statement does not enumerate the nine first-entry classes or classify every nonsynchronizing orbit for a single-edge-deleted complete bipartite graph. Related exact treatments of intact complete bipartite graphs and of complete bipartite graphs with a whole perfect matching removed are on different parameter families and do not imply the stated one-edge formulas for every shore-size pair. Search of relevant published records, aliases, parameter families and primary literature found no statement which dominates the precise claim. A possible unindexed equivalent remains a historical-priority risk, so this is a reasoned originality assessment rather than a proof of absolute priority.

## Value — PASS

A single-edge perturbation of a highly symmetric dense bipartite graph introduces an exactly counted maximal-delay consensus layer, while leaving a tractable mixture of fixed, three-cycle and four-cycle attraction basins. The theorem quantifies both periodic and transient behavior for the entire two-parameter family; the nine exact labelled populations are strictly more informative than generic circulation/synchronization criteria or a numerical graph census. The special-case path, dense bipartite and nontrivial four-cycle regimes all arise from the same classification, offering a reusable method for one-defect network dynamics.

## Sources and limitations

Gravner, Lyu, Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (read full accessible text, including Theorem 3, finite-graph statements and examples). The first public version is dated October 24, 2016. The related intact-family and full-matching-deletion calculations are comparison cases, not premises of the proof. Searches cannot exclude work absent from indexed sources. No external or independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
