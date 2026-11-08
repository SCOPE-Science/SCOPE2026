# Scientific review: paired-leaf random-walk cover time

## Correctness — PASS

The exact law follows from the two-site excursion outcomes (untouched petal complete with probability \(1/2\), partial petal complete with probability \(3/4\)), rate-one Poisson splitting among \(m\) petals, and the resulting single-petal survival \(2e^{-3u/4}-e^{-u}\). Wald's identity converts the number of completed excursions into jump time, with the final-hub-return correction of exactly two expected jumps. The asymptotic expansion is derived by comparing to maxima of shifted exponentials, with an integrable dominating function and a gamma integral. The exact rational sum, petal recurrence, and independent full visited-set Markov equations agreed on all reported tests. Both finite identities and the limiting coefficient follow by proof, not merely numerical pattern.

## Originality — PASS on examined evidence, provisional

The closest broad source is Zlatanov–Kocarev's 2009 cover-time distribution formula for arbitrary graphs, which does not supply the specialized friendship-graph sharp fractional-power correction. Aldous–Fill's 1994 treatment explicitly obtains the star coupon-collector result, but not the paired-star comparison. Published mathematical-result records contain related work on mixing on spiders, cover times for different processes, and edge metric dimension of friendship graphs; the compared scientific claims neither state nor imply the \(m^{2/3}\) coefficient here. Risk: an unindexed prior windmill calculation may exist; no global priority certification is claimed.

## Mathematical value — PASS

The comparison isolates the quantitative gain of adding a perfect matching among star leaves. The leading asymptotic cover times agree, but the improvement has an unexpected nonintegral exponent and an explicit gamma coefficient, providing a reproducible sharp benchmark for a natural infinite graph family. This is not a renaming of the coupon-collector leading term nor an arbitrary small graph table. Its significance is in resolving the first nonzero scale and constant; it does not claim a universal network optimization rule.

Self-review: passed. Independent audit: not yet performed.
