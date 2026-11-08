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

# Reproducible mathematical checks

Run `python3 verify.py` using Python 3's standard library. The program constructs all labeled trees from Prüfer codes for orders 2 through 8. It computes the number of leaves, deletes each edge to calculate the smaller-side vertex count, and accumulates all first and mixed moments as exact integers. It compares them with the exact rational formulas and verifies the pendant/non-pendant covariance signs. It also checks the strict rational inequality of the formula for every nontrivial split size at all orders 4 through 150.

A completed execution found 280,392 enumerated trees and 11,014 successful exact assertions. The values for orders 2 and 3 are boundary diagnostics; the theorem's strict positivity of the pendant covariance begins at order 4. The checks do not establish an infinite theorem; that requires the Cayley/Prüfer conditioning and analytic inequality supplied in `RESULT.md`. No randomized sampling, external dependencies or external validation service is needed for reproducibility.

Scientific limits: finite enumeration cannot rule out historical publication; no independence or stochastic-order conclusion is tested or claimed.
