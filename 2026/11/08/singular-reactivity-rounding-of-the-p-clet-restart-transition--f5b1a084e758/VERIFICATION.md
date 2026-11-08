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

# Verification record

Run `python3 verify.py` using the supplied standalone standard-library program. In the checked execution it reported `PASS: 1591 deterministic bounded checks`. The checks compare the exact derivative numerator with the Taylor-coefficient identity, assess the derivative signs and sampled minima, and test the predicted fixed-parameter and double-scaling limits.

The tests include finite grids only. The strictly increasing derivative quotient and asymptotic root convergence are established in the proof in `RESULT.md`, not through this program. The cited source of the base resolvent is arXiv:2609.22527v1; the perfect-absorber Péclet transition is established in arXiv:1811.08239. This document does not claim independent verification, a formal proof assistant certificate, or a result for any model outside the stated assumptions.
