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

# Verification
The independently written `VERIFY.py` tests equations (1)–(4) by direct enumeration of all strict orderings of the complete-graph edge weights for vertex counts 2 through 5, producing exact histograms for the associated nearest-neighbor mapping. It also uses exact rational binomial inversion to check coefficient nonnegativity and normalization, factorial moments, mean, variance, and Fano factor through 50 vertices. The stored, extracted script was executed and returned `VERIFY_OK 923 assertions`. No external modules, input datasets, or network services are required to reproduce these checks.

The proof of the infinite family is analytic. The finite checker is a reproducibility test, not an exhaustive infinite certificate. The assumption that an unordered edge has one shared weight is essential; independent directional weights define a different model. Independent audit has not been performed.
