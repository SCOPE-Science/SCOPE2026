---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Gale evenness identifies facets with k-edge cycle matchings; the omitted vertices in gaps g_i contribute matching rank Σfloor(g_i/2). Circular marked-gap compositions yield the exact coefficient n/s times binomial sum, including empty and simplex boundaries. For fixed k, overlapping adjacent-deletion edge selections vanish in factorial moments at scale q≈n^-1/2, yielding Poisson(c²); lower and upper tails proved by union bound and disjoint-edge binomial domination. Independently enumerated Gale facets, all 2^n candidate transversals and size counts for every admissible k with n=3..10; matched coefficients. Actual verify.py inspected.

## originality

PASS

The full facet-hitting size enumerator for all n>=2k+1 and fixed-k Poisson deletion window go beyond the well-known minimal transversal number and count. Geometric facet-to-cycle-matching correspondence, circular gaps and factorial-moment proof establish a useful new distribution. Prior generic Poisson approximation is credited rather than treated as new.

## value

PASS

A complete size distribution for facet-hitting sets is a natural strengthening of minimum transversal numbers, and the sharp random-deletion survival window contrasts random versus optimum hitting sets. The exact enumerator and Poisson limit are structurally motivated, not arbitrary finite slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
