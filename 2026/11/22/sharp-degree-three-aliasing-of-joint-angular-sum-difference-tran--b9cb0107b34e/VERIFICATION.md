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

Execute `python verify.py` in an environment with Python 3 and SymPy. The script checks exact trigonometric identities and moment integrals, the simultaneous half-period cancellation, the allowed frequency parity and degree-three onset, and the positive-dependence formulas. It was executed successfully with SymPy 1.14.0.

The proof of the full joint pushforward and its necessity is analytic (two inverse sheets and Fourier uniqueness); no finite search is asserted to establish the infinite statement. The trigonometric-minimality assertion follows from the complete finite list of possible two-coordinate modes below degree three, which the checker also enumerates. Strict positivity follows for the stipulated open parameter range. Exact test-power equality follows from equality of finite-dimensional product laws, not simulation.

The actual empirical-rank APIT procedure uses the original sample to estimate margins, so this package deliberately does not claim that its finite-sample distribution is identical under the constructed alternative. Historical-priority review of the entire literature and independent mathematical certification have not been performed.
