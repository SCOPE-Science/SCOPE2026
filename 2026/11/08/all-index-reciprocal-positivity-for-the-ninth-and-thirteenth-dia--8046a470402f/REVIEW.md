# Scientific review: ninth and thirteenth diagonal Padé reciprocal positivity

## Correctness — PASS
The claim is fully quantified for precisely two rational Padé denominators. `positivity_certificate.py` verifies a disjoint exhaustive Rouché localization for every root, a strictly negative real-root derivative, all nonreal root moduli strictly above the real one, certified derivative/modulus residue bounds, and strictly positive finite recurrence coefficients. The exact tail inequalities become effective at indices 44 and 105. A partial finite enumeration does not stand in for an infinite proof: it is explicitly complemented by the geometric residue majorant. All tests and constants have been replayed locally; independent validation has not occurred.

## Originality — PASS, with historical-priority risk
Fasi–Higham (2019), Conjecture 3.2, introduces the sign question, and Scardino (arXiv:2610.39051v1, 2026), Theorem 8.2, proves *conditional eventual* positivity while explicitly leaving the diagonal case open. Neither supplies all-index results at the specified two degrees. Earlier degree-3, degree-5 and degree-7 findings have different polynomial denominators and do not imply ninth/thirteenth degree. Targeted reciprocal-series, reverse-Bessel, and Padé searches did not identify a covering theorem. Historical novelty remains qualified by the possibility of unindexed equivalent work.

## Value — PASS
These degrees are standard choices in the scaling-and-squaring matrix exponential (Al-Mohy–Higham 2009, Algorithms 3.1 and 5.1), with degree thirteen particularly important for scaling. The complete coefficient signs close a natural finite but mathematically significant section of a published open conjecture and permit the positivity-dependent auxiliary forward-error bound for these two orders. There is no claim that these signs alone certify algorithmic accuracy or total speedup.

## Limitations and closest literature
The result does not settle other odd diagonal degrees, off-diagonal denominators, or implementation rounding errors. The closest literature is Fasi–Higham, *An Arbitrary Precision Scaling and Squaring Algorithm for the Matrix Exponential*, 2019; Scardino, *On a positivity conjecture of Fasi and Higham for Padé approximants to the matrix exponential*, arXiv:2610.39051v1, 2026; and Al-Mohy–Higham, *A New Scaling and Squaring Algorithm for the Matrix Exponential*, 2009.

Self-review: passed. Independent audit: not yet performed.
