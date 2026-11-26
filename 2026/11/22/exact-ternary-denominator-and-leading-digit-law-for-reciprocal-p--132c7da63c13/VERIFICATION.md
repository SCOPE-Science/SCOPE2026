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

For n prime to 3 the geometric difference quotient gives U_n/n congruent to (-1)^(n-1); tripling n multiplies U_n by exactly 3 times a unit congruent to 1, since a^m=(-1)^m(1+3t) gives the factor 3(1+3t+3t^2). This proves both the term valuation and its normalized unit. Scaling the finite prefix by 3^(hr) kills all lower layers. At n=3^r the surviving unit is 1, and at n=2·3^r it is -2=1 mod 3. The d surviving terms therefore give d, nonzero for d=1,2, including r=0 and at jumps N=3^r. This proves the denominator and digit for all stated a,h,N. The a=4 example is outside the theorem; at N=2 it violates integrality under the claimed r=0 normalization. The supplied finite tests were inspected, not run or used as proof.

## originality

PASS

The inspected prior statements concern real inverse tails, term valuations, or fibers of individual terms. None covers the exact joint finite-prefix valuation and normalized digit across the stated bases and powers. The elementary term valuation by itself does not resolve the tie between two maximal-depth summands.

## value

PASS

The exact reduced denominator at 3 and the next unit digit are natural arithmetic invariants of finite reciprocal prefixes. The uniform no-cancellation result is useful precisely when two summands attain the minimal valuation, a regime where the analogous ordinary harmonic power sums can cancel. It gives both invariants for every positive power and permitted base without computing the large reduced fraction. Its contribution is elementary and prime-specific, not a general theory of reciprocal sums.

The dated certificate retains the supplied scientific assessment, sources and limitations.
