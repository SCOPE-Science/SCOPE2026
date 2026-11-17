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

Run `python3 checker.py` with Python 3 and no nonstandard dependencies. It computes unperturbed Lagrange values, the exact one-node-update formula, and the independent nodal-product formula, then verifies partition of unity and finite parameter cases. It also numerically solves the strictly concave one-variable optimization and samples degrees from 100 to 7000. The checker passed 195 finite diagnostic assertions.

These checks cannot establish an infinite-degree asymptotic or historical priority. The mathematical proof is in RESULT.md: exact finite-degree identities (1)–(3), uniform harmonic-tail expansion (7), global localization (9), and a strict-concavity uniqueness argument. Numerical examples illustrate the asymptotic but converge slowly because of the degree-independent additive term. Independent audit remains not performed.
