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

# Mathematical verification and limits

The fixed-set classification is proved analytically in `RESULT.md` by support invariance and the unique positive square-root of an operator congruence. The derivative eigenvalue bound and both endpoint obstructions are algebraic, not extrapolated from finite examples.

`python CHECK.py` runs exact rational tests for spectral projector selections, a genuinely off-diagonal stationary state at repeated coupling eigenvalue, unstable omitted active modes, two rational points across the sharp scalar stability boundary, and all two-active-mode pairs on a rational parameter grid. It returned `PASS: spectral subsets, off-diagonal degenerate fixed states, stability and sharp boundary`. The tests check examples but do not constitute proof for arbitrary dimensions. Neither global basin classification nor claims for nonsymmetric coupling are verified.

Self-review: passed. Independent audit: not yet performed.
