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

Finite exact-rational checks: run `python3 verify.py` from the file directory. The checker derives the finite completion-time distribution by independent dynamic programming, tests its geometric generating function, verifies the continuous-time beta-binomial masses and their normalization, and checks the exact one-half atom at zero. For n=2 through 7, a 350-step truncation leaves less than 1e-10 tail probability for the completion clock. The proof, not the numerical truncation, establishes the uniform all-n, all-q result. The bound is sufficient, not claimed optimal.
