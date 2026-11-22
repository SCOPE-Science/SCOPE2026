# Scientific review

## Correctness

PASS. The center-phase representation partitions every starting position and provides exact geometric probability weights for each center value. A valuation witness separates all different quartets, and the four explicit local signatures permit exhaustive within-quartet aggregation; the table of mass multiplicities, together with the counts of two-, three-, and four-center quartets, gives the result for all alphabet sizes and lengths. Lengths one and two are handled directly. The two replayed programs check the finite exact phase model and the literal finite-prefix frequencies independently; the infinite proof does not rely on those finite tests. Risk: hand enumeration of quartet collisions is a critical short finite lemma, made explicit in the proof and reproducible in the code.

## Originality

PASS on the compared literature, without claiming global priority certification. The closest indexed dyadic factor theorem gives unweighted counts and collision classes for powers-of-two lengths, not weighted frequencies, while Bell–Burnett–Schulz provide a universal level-count upper bound, not this exact model's distribution. Bognini–Ammar describe kernel and gap factorizations; Balková studies the distinct generalized Thue–Morse substitution. The statement is not a disguised corollary of a general bound or a restatement of factor count. Search and full-content comparisons are documented in AUDIT.json. Residual risk: an older unindexed period-doubling factor-frequency computation may contain an equivalent formula.

## Value

PASS. Distinct-factor counts fail to measure the probability of a randomly selected position producing each factor. This theorem determines every atom and multiplicity of the length-dependent factor distribution for all \(q,n\); it identifies a sharp change at \(3L/4\) and characterizes binary equifrequent lengths exactly. These are natural information-theoretic statistics of a widely studied automatic sequence, not a one-off small enumeration.

Self-review: passed. Independent audit: not yet performed.
