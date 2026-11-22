# Scientific review: entropy–variance reversal

## Correctness

**PASS.** The definitions are restricted to bilateral mixing binary shifts forbidding the two specified length-\(2k\) words for every integer \(k\ge2\). Exact weighted border identities yield distinct implicit Perron pole equations. Differentiation proves the two rational variance formulas, and finite-length reverse-complement symmetry gives exact half means. The uniform large-modulus bound, the \(k=2,\dots,7\) exact rational root certificates, and the classical entropy overlap inequality complete the proof. The finite coefficients and small-modulus computations were verified with `check.py`; the infinite parameter range is proved analytically.

## Originality

**PASS within inspected sources.** Bóna, Maga and Richey (2026), https://arxiv.org/abs/2606.06655, formulate the relevant weighted border generating function and first-moment letter-frequency comparisons. Their equality of the means for `1100` and `1010` is already known. Chandgotia, Marcus, Richey and Wu, https://arxiv.org/abs/2409.09024, and Guibas–Odlyzko provide the corresponding entropy/overlap framework. Neither inspected full text states the opposite strict ordering of second derivatives for every \(k\ge2\), or its asymptotic leading gap. The known generating function makes the quantity computable but does not itself give the uniform sign proof. Residual priority risk is a possible unindexed equivalent result.

## Value

**PASS.** The entropy of a single-word shift measures combinatorial freedom, whereas the variance measures long-range digit-count fluctuations. These two natural balanced forbidden-word families have exactly the same first moment, but the all-parameter entropy and variance orderings point in opposite directions. The new strict comparison and its explicit asymptotic decay identify a meaningful structural distinction between no self-overlap and maximal alternating self-overlap.

## Limits and references

The finding does not claim to optimize variance over all forbidden words, establish independent external certification, or extend to arbitrary forbidden lists. Main sources are Bóna–Maga–Richey (2026), Chandgotia–Marcus–Richey–Wu (2024 preprint), and Guibas–Odlyzko (1981). Exact small-modulus certificates and independent finite generating-function tests are in `check.py`.

Self-review: passed. Independent audit: not yet performed.
