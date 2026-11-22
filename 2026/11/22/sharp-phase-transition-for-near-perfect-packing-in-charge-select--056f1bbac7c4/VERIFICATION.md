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

Execute `python3 CHECK.py` with Python 3 and no third-party dependencies. It verifies the exponent minimization recursion for a finite range of rod counts and biases, checks leading constants for two and three rods, and evaluates separately the central and edge three-rod placement integrals by independent numerical quadrature. These are reproducibility checks, not an exhaustive search of infinitely many rod counts or a substitute for the analytical proof.

The proof uses an exact first-placement partition, beta-integral asymptotics, positivity of all contribution constants, and rooted-tree edge counting. It does not require an external certification environment.

The primary model is sourced to arXiv:2608.28289v1. The published source's later finite-shell sections were inaccessible when originality was reviewed; this is a priority-risk limitation rather than a correctness qualification. Independent review has not been performed.
