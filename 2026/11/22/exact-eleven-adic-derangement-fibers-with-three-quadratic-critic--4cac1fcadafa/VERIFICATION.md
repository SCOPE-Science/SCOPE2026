---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The falling-factorial summands converge uniformly since every 11 consecutive factors give at least one factor of 11. Finite partial sums are integral polynomials and one-Lipschitz, so the limit is one-Lipschitz as well. For jets of fixed order j, a coefficient removes at most j factors from each product, so the coefficient sum converges integrally and substitution T=11t gives a restricted series. The truncation at index 32 suffices for constants modulo 1331, linear coefficients modulo 121 and quadratic coefficients modulo 11: every omitted term originally contains at least three divisible factors. At n>=0 the series terminates and equals (-1)^n D_n, by the recurrence; each class modulo 11^k occurs once at each parity in the stated block. The regular branches become unit-affine isometries after normalization by 11. The singular scaled series divided by 121 reduces coefficientwise to a quadratic with a nonzero quadratic coefficient, hence a unique critical center by Hensel. Translation and division by the square of the translated variable leaves a restricted series congruent to u_a. Its ratio to u_a has a restricted square root 1 mod 11 by the binomial series, yielding a linear isometry plus an 11-divisible Lipschitz correction; lifting gives an exact bijective coordinate. This proves E as exactly eleven lifts of each square root, including the modulus-one case. The square count follows by halving an even valuation and lifting the two unit square roots (or divisibility by 11^ceil(m/2) at zero). The regular signed images already cover all seven target balls, and taking a critical value proves unbounded fibers. The claim uses a complete period, not least period. Independently python3 /workspace/replay_independent.py 2 computed modular jets by nested Horner, recovered all three critical rows including gamma=(121,1090,1050) mod 1331, and compared every fiber at k=1..5 from recurrence and direct square histograms (maxima 6,26,48,125,246). This bounded reproduction checks the certificate and consistency, not the infinite theorem; the frozen k=6 run is recorded, not asserted here as independently replayed.

## originality

PASS

The credited general interpolation, congruence period and lifting tools are not new. The supported distinct result is the evaluated prime-eleven image and full signed all-depth index-fiber law with three quadratic branches; the strongest compared same-object result at seven is regular, and the closest same-prime fiber result is for a different sequence. No compared primary result or catalogue statement gives the same critical and regular data for derangements at eleven.

## value

PASS

For classical derangements, specifying the entire prime-power representation count is more informative than a congruence or an image alone. At eleven, critical fibers become unbounded without opening new target balls; that contrast with the compared regular seven-adic case motivates the exact invariant and the parity-aware three-sheet count. This is neither a least-period result nor a claim for general primes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
