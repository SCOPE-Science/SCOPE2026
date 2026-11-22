# Self-review

## Correctness — PASS
The local truth table, persistent-wall lemma, erosion of each interior block, and the two distinct boundary rules reconstruct the complete basin-membership criterion for every path length at least three. The odd-run generating function counts all possible first/last colors without double counting; algebraic extraction gives the parity-dependent Lucas and Fibonacci forms and Binet asymptotics. A standalone functional-graph implementation and a separate run-word recognizer agree on each of 524,280 labelled initial states at lengths 3 through 18, and the rational coefficients match the closed formulas through length 100. Finite checks are corroboration rather than the all-length proof.

## Originality — PASS, qualified
Inokuchi and Sato (2000), Section 3.35, already establish Rule 178 fixed-boundary two-cycle membership, a Fibonacci recurrence for the total number of two-cycle attractors, and the sharp maximum transient. Those prior theorems and local erosion claims are explicitly excluded from the proposed contribution. Their inspected results do not enumerate the basin of the unique fully alternating attractor. The published cyclic Rule 178 entry-time treatment has different boundaries and counts entry shells rather than this orbit's basin. The published sequential path treatment has a different update schedule with universal extinction. Kuhlman et al. prove a general period bound, and Fukś supplies individual-iterate formulas; none of the inspected presentations states the boundary-specific initial-language classification together with its exact rational basin population and parity asymptotics. Unindexed equivalent work remains a residual risk. These are claim/implication comparisons, not title-only comparisons.

## Value — PASS
The fully alternating two-cycle is a canonical extreme spatial-pattern attractor among exponentially many Rule 178 two-cycles. Determining how many initial conditions select that specific attractor—not merely how many recurrent states exist—gives a natural basin statistic. The theorem identifies boundary-induced forbidden even runs, establishes an exact regular-language count and a nontrivial parity correction to its Fibonacci/Lucas asymptotic, and proves that this oscillator has exponentially vanishing selection probability despite almost all states eventually oscillating. The precise invariant is motivated without requiring a general theorem on every individual basin.

## Scope and residual risks
No uniqueness or largest-basin assertion is made. The 2000 primary paper has relevant wall-erosion lemmas; although its explicit statements do not contain this basin count, an older unindexed derivation may do so. The general infinite-line Rule 178 iterate formula provides strong background information from which additional basin results might be derived. No independent scientific audit has occurred.

Self-review: passed. Independent audit: not yet performed.
