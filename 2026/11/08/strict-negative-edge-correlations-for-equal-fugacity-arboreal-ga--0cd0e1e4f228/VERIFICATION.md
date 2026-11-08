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

Run `python3 verify.py` in the same directory as the theorem files. No third-party Python modules or external data are required. The checker computes the three formal Rayleigh differences with exact sparse bivariate integer-polynomial arithmetic, proves identity with the explicitly positive coefficient tables as a finite algebraic calculation, then independently enumerates all weighted forest configurations on 12 small graphs (four sizes times three fugacities). Each graph-and-fugacity configuration tests the partition function, one-edge probability and three two-edge probabilities, totaling 60 exact rational equalities. The program prints its own success results and aborts on a failed assertion.

The mathematical verification of the unbounded family is the forest structural classification and the polynomial factorization in the proof, not the finite enumeration. The checker does not independently establish historical originality, infer arbitrary edge-weight negative correlation, or perform an external audit.
