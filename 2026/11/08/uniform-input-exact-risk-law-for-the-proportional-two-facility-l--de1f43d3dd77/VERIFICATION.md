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

# Verification details

Run `python3 verification/checker.py` after extracting the self-contained files. It implements rational polynomial operations and exact finite-profile enumeration using Python's standard library only. The exact checks verify the two moment numerator polynomials at sufficient rational inputs (five for degree at most four, seven for degree at most six), the normalization of the selected-second-site kernel on small profiles, the exact conditional expected cost against direct allocation enumeration, the rational second-moment integral, and the local endpoint expansions. It also checks the numerical first-moment expression and selected limiting constants.

The uniform empirical convergence and limit theorem are analytic; finite tests are supporting checks, not an exhaustive infinite-population certificate. The near-endpoint constants apply to the limit law with the population limit taken first. The approximation denominator is the unrestricted optimal two-median cost, not the best report-constrained pair.

Self-review: passed. Independent audit: not yet performed.
