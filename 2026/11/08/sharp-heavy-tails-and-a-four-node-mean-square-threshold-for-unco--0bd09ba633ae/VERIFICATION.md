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

## Reproduction

Run `python check.py` with Python 3, NumPy installed. The recorded deterministic run uses the explicitly set pseudorandom seed in the checker. The program performs 9,859 assertions, including exact rational checks of the moment equations and orthogonal-minimum-norm identity for node counts 2–8, an independent floating-point least-squares comparison, finite conditional-noise variance identities, and Monte Carlo estimates of the predicted tail exponent and constant for sizes 2–4. `check_output.txt` contains the actual output.

## Proof-versus-computation boundary

The checker is supportive but not a proof of the asymptotic tail, its density dependence, or the infinite-moment threshold. These conclusions require the exact mean/centered-variable Jacobian, dominated convergence and the tail-integration argument in `RESULT.md`. Monte Carlo tail estimates are intentionally approximate; the program asserts only agreement within a finite-sample tolerance. Independent audit has not been performed.
