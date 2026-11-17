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

## Reproducibility
`python verify.py` runs a self-contained standard-library verifier. It evaluates 1,000 moment-preserving band profiles from 100 fixed angles and ten band widths each, verifies three analytic consequences at each pair, and checks the limiting ratio. It prints `VERIFY_OK` with 3,000 finite checks.

The proof in `RESULT.md` is the source of the infinite-dimensional conclusions. The numerical checks do not establish general optimality, high-frequency non-stability, or the sharp exponent. The dual-potential identity, quadratic-form sign, rearrangement inequality, band interaction calculation, and oscillatory construction are all laid out analytically.

## Limits
The sharp exponent concerns the \(L^1\) distance for ordered curvature-radius profiles. It does not imply \(L^1\) stability without curvature ordering. The universal cubic coefficient is valid but not asserted sharp. Historical priority is provisional. Independent audit not performed.
