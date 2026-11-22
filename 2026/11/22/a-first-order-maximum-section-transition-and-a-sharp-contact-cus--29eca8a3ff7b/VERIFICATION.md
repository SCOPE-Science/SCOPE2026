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

# Reproduction and verification scope

Run `python checker.py` with Python 3 in this directory. No third-party dependencies are required. The recorded run completed 91 deterministic checks. The script checks the closed circular-segment area against direct numerical integration of section widths, tests the predicted cap deficit at multiple resolutions, confirms selected vertical-area ties and inequalities on both sides of the global transition, checks the Haar contact inverse, and tests the \(s\to\infty\) expansion. Exact proofs of all real-parameter and limiting statements, including existence of the global critical aspect ratio and nonuniqueness-neutral phase classification, are in RESULT.md. Finite computation is not a proof of an infinite claim.

No independent mathematical audit or formal proof assistant verification has been performed. The variational characterization of the critical aspect ratio is rigorous, but the displayed decimal approximation is not interval certified. Historical priority is not independently certified.
