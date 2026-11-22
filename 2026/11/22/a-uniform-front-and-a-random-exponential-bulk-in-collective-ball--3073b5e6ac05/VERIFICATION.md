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

# Reproduction and limits

Use Python 3 and run `python3 checker.py`. No third-party packages or network services are required. The checker uses a fixed seed, exact quadrature, independent direct excursion samples and duration-weighted stationary samples. It verifies the reciprocal-maximum formula at two particles, three return-time survival probabilities, several weighted stationary uniform-front cases, and the limiting exponential-mixture exceedance law with a positive variance.

The checker is a finite numerical consistency test. It does not certify all populations or the limit as the population grows. The proof in `RESULT.md` explicitly establishes the recurrence threshold by renewal theory, the stationary law by time occupation, and the large-population result by extreme-value concentration, total variation and empirical-measure convergence. No external mathematical certification or independent audit was performed.
