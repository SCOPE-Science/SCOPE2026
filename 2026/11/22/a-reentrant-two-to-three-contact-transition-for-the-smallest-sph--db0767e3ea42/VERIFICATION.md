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

# Reproducibility and bounds

The theorem is established for all real \(\eta>0\), \(0<L\le\pi\) by the exact reduction and inequalities in `RESULT.md`. It is not a finite enumeration. The standalone `VERIFY.py` requires only standard Python 3 and performs deterministic checks of the center, enclosing radius and contacts at 96 parameter pairs and boundary points, plus 115,296 helix-distance tests and 11,616 center comparisons. It evaluates strict-crossing bisections and one-sided derivative limits, printing `HELIX_ENCLOSING_BALL_REENTRANT_CHECKS_OK` when the checks succeed.

To reproduce, save `RESULT.md` and `VERIFY.py` in the same directory and run `python3 VERIFY.py`. The checker is supplementary: its finite sampling does not establish continuous maximization, uniqueness, logarithmic concavity or absence of additional contacts; those require the analytic proof in `RESULT.md`. It uses approximate floating point arithmetic and does not purport to give a computer-certified infinite proof.

No independent mathematical or historical-priority validation has been performed. Scope is one angular turn and positive pitch. Historical priority is provisional.
