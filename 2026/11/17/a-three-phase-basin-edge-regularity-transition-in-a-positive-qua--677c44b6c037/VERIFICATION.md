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

# Verification of basin-edge regularity

The analytic proof in `RESULT.md` derives the exact two-dimensional homogeneous decomposition and radial cocycle, then checks three separate small-composition regimes using a first-exit index. The geometric-series derivative at \(1<\lambda<2\), the exact resonance factor \(1/\log 2\), and the lower/upper power bounds for \(2<\lambda<4\) are proof assertions, not output inferred from finite numerical trials.

Run `python3 check_boundary.py` with Python 3.11+ and its standard library. The checker uses exact rational arithmetic for two mass/composition identities, high-precision decimal evaluation for the radial functional equation and endpoints, and shrinking-composition sequences for three benchmark cases. A passing run prints `QUADRATIC_MAP_ENDPOINT_REGULARITY_CHECK_OK`.

The finite computations are consistency tests. They do not certify all real parameters, prove convergence of the infinite series, or justify a leading constant in the superresonant case. The proof supplies those results or explicitly withholds them. No independent audit or external mathematical certification has been performed.
