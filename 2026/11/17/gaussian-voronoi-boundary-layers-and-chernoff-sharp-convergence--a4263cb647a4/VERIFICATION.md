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

# Reproducibility and scope

Run `python3 verify_atomic_durrmeyer.py` with Python 3.9 or later. The script needs only the standard library. The executed checks include exact rational stochasticity, detailed balance, and nonnegative principal minors for three rational sites and degree 1 through 21; adjacent KL crossover identities; six critical Gaussian-window comparisons at degree 1000; and exponential-scale diagnostics for degrees 100, 200, 400 and 800. All these checks passed in the reviewed run. They are finite diagnostics; the claim's universal quantifiers depend on the analytical proof in `RESULT.md`.

The sharp norm claim is a \(\Theta\) estimate, not an assertion that any normalized coefficient converges. Independent verification remains not performed.
