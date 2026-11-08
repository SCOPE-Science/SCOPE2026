# Self-review

## Correctness
**PASS.** Every query-positive branch of a permutation assignment fixes a complete row and column, giving the sharp universal \(n-1\) upper bound. The eight-leaf tree on the four-by-four board is a finite certificate reproduced by the standalone checker. The induction uses two mutually exclusive edges in one row and the precise rank of the two residual forbidden matchings. The last-deletion case removes two forbidden diagonal entries per positive edge. The static comparison is separately proved by Hall's theorem, including the three-row obstruction and two-row swap cases.

## Originality
**PASS, within the actual comparisons made.** A prior claim for derangements already determines their complete *static* shattering complex and VC dimension, so that part is not presented as new. Exact online ranks for all deletion sizes are a logically separate, stronger claim not implied by static VC data, derangement counts, or the general online closure bounds inspected. The closest inspected sources concern perfect-matching enumeration, alternate permutation-order shattering, or general learning theory. Broader work under alternate assignment-identification language remains a residual priority risk.

## Value
**PASS.** The result identifies an exact sharp phase transition from static to adaptive capacity under one forbidden assignment edge and the precise small-order exceptions. Its induction gives explicit adversarial mistake trees rather than only a counting estimate, and it completely classifies the matching-deletion family with a natural discrete restriction parameter.

## Limitations
No result is asserted for arbitrary forbidden bipartite subgraphs, and no independent expert examination has been performed. The finite computations are supporting checks of the unrestricted proofs. Historical identification under other nomenclature is a residual risk.

Self-review: passed. Independent audit: not yet performed.
