# Assessment of the ternary tortoise second-moment law

## Correctness (C): PASS

The operator is defined for all finite words with maximum-letter splitting, including empty words. Binary output fertilities are obtained by allocating the initial zero block across two input zero blocks. An exact split convolution gives the first ternary block's fertility, and all later binary blocks contribute multiplicatively. The disjoint decomposition by numbers of maximal letters yields the rational series with no boundary omissions. Its dominant pole is simple, positive and strictly smaller in modulus than every other pole. Two independent programs confirm all length-at-most-nine ternary fibers, all binary split kernels through length twelve, and coefficient identities through degree eighty. This is a proof for all lengths, not an infinite inference from the finite checks.

## Originality (O): PASS against inspected comparisons

Defant--Kravitz establish the map and fertility methods. Campbell--Rampersad consider subword complexity of sorted/equivalent words, primarily over a binary alphabet. These results do not supply the **global square-summed ternary preimage counts** or entropy rate in their inspected relevant sections. Related published output-language formulas identify which fibers are positive, not their second moment. Search comparisons on tortoise fertility, collision moments, Rényi entropy and the specific cubic denominator did not surface an equivalent. However, prior work may contain an unindexed second-moment specialization.

## Value (V): PASS

The number of obtainable outputs misses the distribution of how often different inputs collide. The first three-symbol case has genuine weighted binary-block interactions, but an exact rational collision enumerator and explicit exponential rate. Its entropy rate is a natural operational statistic for information loss under deterministic string sorting, not a routine value substitution in a support-count formula.

## Sources and residual risks

The primary texts are *Stack-sorting for Words*, arXiv:1809.09158 (definition and fertility sections), and *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811 (2026 methods and results on subwords/equivalence). The general fertility framework might allow deriving this special case with substantial algebra, but no inspected theorem already states or dominates the global ternary second moment. Independent external priority verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
