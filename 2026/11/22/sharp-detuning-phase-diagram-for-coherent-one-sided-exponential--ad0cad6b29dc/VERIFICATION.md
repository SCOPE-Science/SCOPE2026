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

# Verification notes

The complete proof appears in `RESULT.md`, Steps 1–5. The Zak symbol is a uniformly convergent geometric sum on each open unit cell; its rational denominators remain nonzero and bounded uniformly for every fixed admissible window. The exact phase criterion is an equality of nonnegative absolute values. A zero reached only in the limit as \(x\uparrow1\) still forces an essential lower frame bound of zero. The two detuning regimes are exhaustive, and all boundary cases are included in the proof.

Run `python verify_detuning.py` using Python 3 and no third-party packages. The script independently compares the phase minimum with sampled values, tests every frame and nonframe parameter chamber, recovers exact Zak zeros numerically, and cross-checks the infinite geometric-series symbol against a finite 200-term sum at several parameters. The test passed 497 supplementary assertions. These finite checks are diagnostics, not a proof of claims for all real parameters.

No independent audit or external validation has been performed. Historical-priority assessment is provisional and is not a certification.
