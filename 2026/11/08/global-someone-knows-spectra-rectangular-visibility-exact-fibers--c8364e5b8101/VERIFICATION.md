---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible verification

Run `python3 check.py` with Python 3 and no third-party dependencies. The checker directly evaluates the original modal disjunction using the coordinate-equivalence accessibility relation and compares it with the projection-closure characterization. It enumerates every subset of every nonempty subteam of the \(2\times2\), \(2\times3\), \(3\times3\) and \(2\times2\times2\) cubes: **844 teams and 27,050 truth events**. It checks closed-set fiber inversion independently and verifies complete full-product event spectra for \((1,2),(2,2),(2,3),(3,3),(2,2,2),(2,2,3)\).

Selected exhaustive full-product checks: \((2,2)\) has 10 observations from 16 valuations; \((2,3)\) has 22 observations from 64 valuations; \((2,2,2)\) has 28 observations from 256 valuations; \((2,2,3)\) has 64 observations from 4,096 valuations, and its maximally invisible events have cardinality 9 and multiplicity 36. Reproduction output terminates with `ALL_CHECKS_PASSED`.

The code is a finite diagnostic only. The full theorem uses the written arguments about projection closure, Möbius inversion, inclusion-exclusion and graph covers. NP-hardness invokes the standard three-dimensional-matching theorem, not a computational experiment. No formal proof assistant or independent certification is claimed.
