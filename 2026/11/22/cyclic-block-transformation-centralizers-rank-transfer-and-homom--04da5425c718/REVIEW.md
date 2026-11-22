# Self-review

## Correctness — PASS

The exact domain is the cyclic block-character transformation monoid on \(m\ge1\) two-element blocks. An idempotent necessarily has zero character, with each block either identity or a constant. The four local intertwining cases have rank polynomials \(2z+2z^2,z,2z,z+z^2\); multiplying by the precise source/target-type counts gives the claimed \(2^a z^m(1+z)^{m-2d_k}\). The formula is independent of the arbitrary constant values. The cyclic transfer matrix has eigenvalues \(z+2\) and \(z\), producing the stated totient sum. Divisor-order bounding proves the asymptotic commuting probability and conditional binomial law. Exact programmatic enumeration checks every commuting pair for block counts one through five, every type pattern through seven for the three cutoffs, and the known strictly homometric pair at eight. The finite checks do not replace the all-parameter proofs.

## Originality — PASS relative to inspected sources

Sarkar–Singh, arXiv:2310.19414v1, Proposition 3.9, already characterizes idempotents of the general character-restricted partition-preserving semigroup; it does not present this character-indexed centralizer rank polynomial or the global divisor transfer. Their 2024 bijective-character paper addresses Green's relations and unit-regularity. Araújo–Konieczny, *Centralizers in the Full Transformation Semigroup*, Corollary 5.2, already gives the general digraph-based commutation criterion for idempotents; the derived local rank enumeration and cyclic shift/reflection collisions are additional, and general membership is not claimed new. Jedrzejewski–Johnson, *The Structure of Z-Related Sets*, already records the eight-point homometric pair; only its explicit monoid-centralizer application is assessed. Searches of relevant research records for cyclic-block/wreath transformation centralizers and cyclic autocorrelation showed no equal/stronger rank-refined claim. Closest indexed claims concern permutation-centralizer retraction ranks, unrelated wreath-product generating rank, and labelled group-set commuting retractions, without the cyclic-character centralizer census. A general character-restricted centralizer formula hidden in older work remains the principal priority risk.

## Value — PASS

The complete composition-centralizer rank spectrum is a natural monoid invariant for every idempotent of an infinite family, rather than a single numerical sample. The result quantifies commuting probability with an exponential rate and explicit finite-error estimate, proves a conditional rank law, and identifies the exact earliest small-degree failures of unindexed/shift-indexed fingerprints. The homometry connection explains a structural loss of identifiability. The natural boundary is fixed two-element block size; no claim about larger blocks is made.

## Residual limitations

The paper's framework and the 2013 full-transformation membership criterion are substantial premises, not contributions. The original 2013 homometric pair is credited. Source inspection and similarity search cannot rule out every unindexed historical theorem. Direct checker coverage is finite, and no external audit has been performed.

Self-review: passed. Independent audit: not yet performed.
