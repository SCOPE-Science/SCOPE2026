# Assessment of the exact idempotent generating-tuple count

## Correctness — PASS
The unrestricted formula follows from two explicit structural lemmas. The idempotent parametrization is proved by induction using \([P,P^2-P]=0\), so no characteristic-dependent division is hidden. The generator test follows from the semisimple diagonal quotient, adjacent rank-two quotients, and lifting diagonal matrix units in the generated algebra. Independent literal finite-field matrix enumeration checks all ordered tuples in four small cases; the given code also verifies the higher polynomial specializations coefficient-by-coefficient in formal polynomial arithmetic. Computational checks supplement, not replace, the algebraic proof.

## Originality — PASS (provisional)
Kelarev, van der Merwe and van Wyk (1998) established the minimal generator number and the hypercube construction. The full accessible paper was compared, and its existence theorem is credited. Gargate and Gargate (2020) enumerate *individual* potent matrices. Kolegov (2025) counts unrestricted matrix tuples generating finite incidence rings. None of these inspected results supplies the idempotent-conditioned ordered-tuple count or its nonadjacent Hamming weights; neither existence nor unrestricted generation probabilities imply the proposed count by direct specialization. Kolegov (2024) gives minimum idempotent-generator numbers in greater generality, but only its abstract could be inspected, leaving priority risk. A still-unidentified broader enumerative identity may dominate this claim.

## Value — PASS
The enumeration determines a natural counting/probability invariant for every finite field, dimension, and number of idempotent generators. It refines a classic sharp minimum-generator theorem quantitatively and integrates algebra generation with weighted hypercube paths. The nonadjacent weights show that mere existence or local adjacent constraints do not determine the multiplicities.

## Limitations
The result is for ordered tuples and the standard upper triangular chain algebra, not conjugacy classes, other incidence posets or nonfield base rings. Historical priority is provisional and independently unverified. The 2024 full text remains a specific inaccessible comparison.

Self-review: passed. Independent audit: not yet performed.
