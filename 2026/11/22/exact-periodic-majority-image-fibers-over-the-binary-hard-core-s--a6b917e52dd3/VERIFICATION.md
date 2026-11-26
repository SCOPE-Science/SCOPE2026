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

Under cyclic hard core, a received 1 is exactly the midpoint of the input pattern 101. On the integer periodic extension, split between successive received ones a distance g apart: the two forced inner input ones occur at offsets 1 and g−1. They coincide for g=2; g=1 or 3 is incompatible with hard core and g=4 forces an extra received 1. For g≥5 the intervening input gaps must all be at least 3, and any ordered decomposition of g−2 into such gaps works. The intervening segments and the compulsory gap-2 pairs at the received ones exhaust the source, also for a lone received 1. At n=1 the only legal source is zero; at n=2 the two one-sites give distinct nonzero outputs by the repeated-neighbor convention. The number of decompositions is one only for residual lengths 0, 3, 4 and 5. With no received ones, the unique closed distance-state walk of each admissible word gives tr(T^n); the all-zero path stays in the saturated state and the characteristic polynomial t³−t²−1 gives the listed recurrence. Marking a received one yields n/k times the k-gap composition coefficient with no primitivity assumption. Each gap series is positive with gcd of exponents one, so the only dominant pole is its simple positive root of G=1; the logarithmic derivative has leading coefficient one. Independent bounded enumeration through n=10 checked every fiber and both count series, including n=1,2; the all-n claims rest on the bijection and formal series, not enumeration. The frozen checker was inspected, not executed.

## originality

PASS

The supported distinction is the product for each hard-core-source fiber and the evaluated restricted image and singleton spectra. The closest singleton and cyclic image papers solve different counting problems over the full binary shift. This is a best-of-knowledge conclusion, not a priority determination.

## value

PASS

This is a natural local decoder with a standard exclusion constraint. The result answers both whether a received cycle is possible and exactly how ambiguous it is, including a nontrivial zero-word exception. It distinguishes exponential growth of singleton outputs from exponential decay of their fraction among attainable outputs, with explicit rates. The constructive factorization is more useful than an unevaluated transfer-matrix method or a table of small cycles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
