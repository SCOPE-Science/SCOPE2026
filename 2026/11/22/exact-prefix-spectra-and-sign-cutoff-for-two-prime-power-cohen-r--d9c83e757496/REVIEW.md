# Scientific review: two-prime-power Cohen–Ramanujan prefix spectra

## Correctness — PASS

The exact Cohen divisor identity and multiplicativity imply that only indices divisible by \(H\) contribute. At each such index the sum is a product of two prime-power divisor factors, giving the stated closed prefix expression. Blocks of \(Q\) consecutive integers contain every residue modulo \(P\), which proves the spectrum and multiplicities. Because \(Q>P\), these bands are disjoint and the sign changes at the claimed sharp index. The proof treats the full-period endpoint, arbitrary prime exponents, and the least-period assertion separately. The independent divisor-formula checker passed 103 parameter tuples and 1,138,338 exact prefix comparisons. Remaining risk: independent human checking of the argument has not occurred.

## Originality — PASS with residual priority risk

The closest paper is Thomas–Namboothiri (arXiv:2312.07098, especially Theorem 3.4), which gives a *lower bound* for a maximal generalized Ramanujan partial sum. The present exact all-prefix spectrum, each fiber size, and sharp one-sign transition are not stated there. Kühn–Robles (arXiv:1311.2816) treat sums with the varying **modulus** as index; this does not imply the fixed-modulus prefix-spectrum classification. Namboothiri (arXiv:1708.04505) concerns restricted linear congruences and uses generalized Ramanujan sums without classifying these cumulative values. Accessible prior-record claims and semantic-database results do not present this exact finding. The classical divisor formula does encode every partial sum and makes this a short elementary derivation, so an earlier explicit statement outside the inspected works remains possible. No universal novelty claim is made.

## Mathematical value — PASS

The 2023 work directly raises the problem of maximum cumulative generalized Ramanujan sums, while the exact extremum for prime-power products of two distinct primes is not given by its generic lower bound. The full theorem yields considerably more than the extremum: exactly \(p^{2s}\) attainable values independently of the larger prime and both prime exponents, exact integer multiplicities, a uniquely located sign transition, and the exact least period. This is a natural exhaustive two-prime classification, useful as a concrete boundary case when more prime factors create substantially more intricate inclusion–exclusion effects. It is elementary and limited to two-prime support; no general theorem for arbitrary support is claimed.

Self-review: passed. Independent audit: not yet performed.
