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

# Reproducible checks and limits

`python verify.py` uses the Python standard library only and enumerates all permutations through nine named parameters. Two different implementations of the type statistic agree through size six. A second exhaustive search counts orientations of Hamilton cycles of the path square through size ten. The program's exact output is stored in `verification_output.txt`. This is a finite reproducibility check, not a proof at unbounded size.

The general proof in RESULT.md establishes all sizes by prefix-set parity, a unique crossing cycle, elimination of fixed vertices, and an induction proving the square of a path has a unique Hamilton cycle. A prior-work comparison inspected the Cameron and Linman–Pinsker primary texts and a separate oligomorphic-profile source; unlocated equivalent formulations remain a historical-risk qualification. No independent audit is represented here.
