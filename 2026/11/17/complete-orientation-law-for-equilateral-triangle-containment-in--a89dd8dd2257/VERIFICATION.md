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

# Reproducibility and scope of verification

Run `python3 CHECK.py` with a standard Python 3 installation. The program builds the twelve original vertex-pair linear constraints instead of relying on the theorem's hexagon formulas. It clips an enclosing square against each halfplane to reconstruct the actual similarity-factor polygon and independently checks its area and farthest-vertex radius against the exact expressions. It also directly evaluates translated-fit feasibility over a deterministic grid of orientations and compares quadrature and 48 threshold probabilities with the analytic distributions.

The recorded invocation completed without assertion failure and printed twelve PASS rows followed by `PASS 12 shapes, 48 distribution comparisons, 12 independent polygon computations`. The analytic proof in `RESULT.md`, not a finite numerical regression or an external proof system, supplies the universal quantifiers and the sharp optimization statements. The numerical tolerances are documented in the checker; no rounding is asserted to prove strict inequalities across all real parameters. Boundary configurations are covered in the algebraic case analysis of the proof.

The public source and provenance references in `RESULT.md` are descriptive citations only; this verification does not imply independent mathematical validation, formal certification, or any unperformed external check.
