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

Run `python3 verify.py` using standard-library Python 3. The script tests the exact moment formulas for all listed finite orders, directly checks the beta normalization, and numerically reconstructs perimeter and area from both the circular-angle and chord-gap formulas. It also carries out a seeded conditional simulation for the scaled chord-loss variance, which approaches the theoretical target \(5\pi^6/8\). Sample-based checks cannot certify the infinite-sample central limit theorem.

The analytical proof does not invoke the simulation: it uses the uniform Dirichlet density, exact Dirichlet power moments, deterministic Taylor remainders and the classical iid central limit theorem applied to normalized exponential spacings. Some early publication full text is inaccessible, so priority comparison is necessarily qualified. Independent mathematical validation is not performed.
