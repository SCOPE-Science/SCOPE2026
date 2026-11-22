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

# Reproduction and boundaries

Run `python3 verify.py` with Python 3. The program requires no dependencies beyond the standard library. It constructs exact rational rotation coordinates via a tangent half-angle parametrization, then evaluates the objective and its normal equations over discrete offset laws using exact fractions. A separate numerical grid checks the sign of the frequency derivative, and exact fraction identities check the small-step coefficient. The script also checks a discrete nonuniform offset law having the uniform distribution's mean and variance.

The mathematical proof of the unique optimum, exact residual, angular folds and all-laws fourth-order criterion is written in `RESULT.md`. A finite suite of arithmetic checks supports the absence of transcription mistakes, but is neither an exhaustive test over distributions nor a substitute for proof.

The asserted fold is for the fitted angular coefficient alone. Full-data identifiability, stochastic noise sensitivity, finite-sample optimizer fluctuations and nonlinear-model effects have not been assessed. The coincidence with the established fourth-order compact-difference Fourier symbol is explicitly acknowledged in the mathematical discussion.
