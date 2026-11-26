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

The normalized monomial basis gives a single forward shift: projecting z^(n+2) times conjugate(z) multiplies z^(n+1) by (n+2)/(n+3). Squaring the resulting weight gives (n+1)/(n+2)+2x(n+1)/(n+3)+y(n+1)(n+2)/(n+3)^2. Subtracting at adjacent indices recovers A_k, B_k and C_k over the stated positive denominator, while the initial diagonal entry is automatically nonnegative. This reasoning does not divide by a weight and covers zero weights. Consecutive line differences are positive slope increments times x−X_k. The X_k are strictly ordered and tend up to −5/8, so telescoping settles every finite maximum and monotone convergence settles the unattained limiting regime, including its left endpoint. Completing the square gives the stated centers and radii. The positive-coefficient formula for Y_k−X_k² shows that every switch lies in the physical domain, and the nonzero change in slope gives a corner on each sign of the imaginary part. The accumulation points follow from Y_k→1/2. On the real line the cubic numerator in k has all coefficients nonnegative in the two allowed closed ranges; outside them either its constant term (through t=−1) or its leading cubic term is negative. Thus both real endpoints are included and the intermediate range is genuinely excluded.

## originality

PASS

Credit the prior fixed-angular-degree criterion with the entire infinite family of tests and hence the individual disk inequalities. The distinct content is the explicit evaluated envelope, the proof that infinitely many of those disks make genuine exposed arcs and corners, and the exact real slice. Related sufficient conditions and the superficially similar radial-perturbation model do not give this geometry.

## value

PASS

It is a natural first nonharmonic perturbation of the Bergman shift, and the explicit envelope turns an infinite test into an exact phase diagram. Infinitely many exposed circles show that no finite truncation of the original commutator tests can capture the complex region; their corner accumulation and the simpler reentrant real slice explain the geometry that the general criterion leaves implicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
