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

Run `python verify.py` in a Python environment with SymPy and NumPy installed. The verifier checks the finite trace formula symbolically; exact path-matrix inversions for all ordered pin pairs on path lengths 2 through 9 with a rational gain; the derivative, curvature, mixed derivative, critical-point elimination and special crossover; the complete 20-gap rational comparisons on the 21-vertex path for three gains; and numerical agreement between five long finite paths and the cubic continuum root.

The asserted general results are justified by the mathematical proof in `RESULT.md`, not merely by successful tests. Finite exhaustive comparisons establish only the specified 21-vertex example. Numerical approximations are not used to establish all-size convergence or uniqueness. No independent audit or formal proof-assistant certification has been undertaken.
