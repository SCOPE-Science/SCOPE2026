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

The claim is a mathematical proof for every finite star with at least one leaf and all complex input pairs. The independent-audit channel is unperformed.

The accompanying `verify_star_l2.py` is executable with Python 3 and the standard library. Run `python3 verify_star_l2.py`; in the supplied package the execution printed `ALL CHECKS PASSED`, with 3,534 exact rational Gram identities, 280,270 exact rational domination comparisons, 22 positive-region witnesses, and 6,000 direct real/signed/complex pairs. The finite tests do not replace the universal proof; the proof of the global bound is the piecewise-linear branch and Perron comparison, and the proof of sharpness is an explicit open-cell singular direction. The checker's floating-point witness checks have finite precision and are corroborative only.

The prior-work comparison distinguishes single-input variation inequalities, two-input total-variation estimates, and strictly fractional asymptotics from the exact vertex-Hilbert-to-edge-Hilbert modulus. The bibliography search cannot prove the absence of an earlier equivalent theorem.
