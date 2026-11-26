---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The local distributional-variation quotient excludes endpoint jumps and constants. Integrating the normalized Legendre basis over (s,1) gives the stated Q_s, so the finite-measure jump representation makes the norm precisely max_s integral |Q_s|. Checked reflection, the center integral, the signs of the endpoint/vertex values for |s|<=1/4, and the discriminant formula for integrating between the two roots. Squaring the comparison there is legitimate (both sides nonnegative); the strict certificate away from s=0 follows from the positive coefficients. The coefficient derivative bounds 56,16,8 give the asserted global bridge 3/32 on each covering interval. Independently reproduced the kernel and near-center polynomial positivity and used a separate exact chord bound for the absolute quadratic on 32 x-panels at all 300 s-centers, with maximal upper bound 907901415279699/536870912000000 < 17/10. Replay: /workspace/independent_exact_checks.py, cubic_legendre(). The resulting bound is <9/5 away from the center range and the midpoint value exceeds 9/5. No inference from a numerical sample.

## originality

FAIL

The distinct indexed record 50de2eabbe22 explicitly states the same sharp variation norm of the real cubic Legendre L² projector and the midpoint equality, and also states uniqueness up to constants and scaling. This is verified statement-level coverage, not a title match or an inference from a date. The catalog identifier has a later date than the frozen item's, but no inference of historical precedence, dependence or attribution is made in either direction. No separate mathematical claim of this frozen result survives the exact overlap.

## value

FAIL

The underlying sharp constant is meaningful for low-degree spectral truncation, but its explicit finding is already duplicated in the checked corpus, including equality at the central step. This record does not isolate a distinct useful invariant, extension or result about the certificate itself. This is not a rejection on grounds of small degree or computer-assisted proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
