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

# Reproducible mathematical checks

Run `python verify.py` with Python 3 and the `sympy` package. The script symbolically reconstructs the quartic field, checks all three exact time-reversing reflections on the neutral hyperplanes, verifies the published equilateral Floquet numerator specializations, proves algebraic cancellation of the weighted sum, and checks all six explicit sign patterns. Expected line: `VERIFY_OK exact_reflections=3 exact_skew_cancellation=1 all_six_sign_patterns=6`.

These checks do not establish historical novelty or constitute independent certification. The global-in-radius claims are established by the strict algebraic sign inequalities and the standard reversible periodic-orbit lemma in the proof, not by finite sampling. No external auditing has been performed.
