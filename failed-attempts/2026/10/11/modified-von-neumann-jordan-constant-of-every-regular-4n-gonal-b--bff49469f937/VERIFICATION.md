---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Inradius-one polygon norms satisfy ||z||_N<=||z||_2; unit vectors have Euclidean radius at most sec(pi/N). Parallelogram identity gives universal quotient <=sec²(pi/N). Adjacent vertices at ±pi/N realize equality because both x+y and x-y lie on orthogonal facet-normal rays when 4 divides N. Independently recalculated norm quotients for N=4,8,12,20,40; all agree. The proof is infinite-family analytic.

## originality

FAIL

Decisive prior coverage: the published Resultary theorem on the skew von Neumann–Jordan constant for the SAME entire real regular 4n-gonal family already establishes supremum over t in [0,1] equals sec²(pi/(4n)) AND that the maximum is attained at t=1. Its t=1 is exactly Cprime_NJ. This stronger theorem mathematically implies the entire audited result, not merely sample values.

## value

FAIL

The surviving exact value, maximizing pair and asymptotic are mechanically implied by the published stronger whole-family skew theorem; no independently uncovered structural or quantitative fact remains. Correctness alone cannot make a fully covered special case valuable as a new research result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
