# Review of the even-base partition leading-bit theorem

## Correctness — PASS

The extraction recurrence for \(b_m(m^rn-1)\) is exact. The Faulhaber/Bernoulli denominator estimate proves the crucial nonstandard lemma that \(T_m\) preserves \(\mathbb Z_2[x]\) for all even \(m\). It follows by induction that the normalized extraction polynomial is congruent to the identity modulo \(2^{\nu_2(m)}\). Convolution with the ordinary partition series gives the claimed integer divisibility and depth-invariant parity, and the multiplier-one case proves equality in the valuation. The standalone direct-recursion checker verified 500 finite cases and 40 sharp valuation witnesses, without relying on the polynomial proof. The infinite assertion is symbolic, not extrapolated.

## Originality — PASS on inspected evidence

Rødseth and Sellers (2001) give the even-base divisibility bound, but not the all-depth sharpness at the all-ones indices or the normalized first-bit convolution. Żmija's March 2024 preprint provides a broader divisibility framework, but its stated modulus is not the exact parity formula. A closely related later result treats the first nonzero base-\(m\) digit for odd bases coprime with six; its full mathematical text explicitly excludes even bases. A separate full-text result concerns exactly four branches of fixed depth three; it does not determine the arbitrary-depth leading-bit profile. The precise normalization, equivalence and stronger-coverage comparisons have been inspected. Residual risk is hidden or unindexed prior coverage, not an identified theorem that already states this law.

## Value — PASS

The mathematical problem is motivated by the older universal even-base congruence: is its modulus sharp and can one determine the first nonvanishing bit? Exact sharpness for all even bases and unbounded depths, together with a stable parity profile for every multiplier, gives a structural answer rather than a routine numerical check. The result determines an infinite class of exact valuations and converts massive-index congruence calculations into short convolutions.

## Limitations

Only one normalized binary digit is determined, and the theorem does not cover odd bases or colored partitions. Full research priority and infinite-proof correctness have not been checked by an independent mathematician.

Self-review: passed. Independent audit: not yet performed.
