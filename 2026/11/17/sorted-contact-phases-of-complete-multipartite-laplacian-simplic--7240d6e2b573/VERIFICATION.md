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

# Reproducibility and verification

Run `python check_multipartite_laplacian.py` with Python 3; there are no third-party dependencies. It constructs full integer Laplacian matrices, evaluates the rational center and optimality weights, and checks every proposed distance and contact exactly.

Observed output: `MULTIPARTITE_LAPLACIAN_BALL_PASS exact_profiles=272 large_profiles=50 distinct_active_levels=8 boundary_profiles=1`. The explicit tripartite examples include the all-contact/zero-certificate-weight boundary.

An additional, separate SciPy SLSQP minimax run optimized unrestricted ambient ball centers for five class-size triples. Each converged to the predicted squared radius; the largest displayed center discrepancy was about 1.2e-7. This numerical test is optional and is not required for the checker.

The unrestricted mathematical proof is the exact convex combination of contact vertices plus the weighted variance identity in `RESULT.md`. The finite enumeration and numerical optimizer are not infinite proofs. No independent audit has been performed.
