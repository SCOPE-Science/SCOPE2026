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

The exact forward shadowing theorem is proved analytically in `RESULT.md`. The only computational supplement is `verify.py`, using rational input parameters and rational errors. It tests 840 finite pseudo-orbit prefixes and 12 near-fixed-point defect identities. These finite tests do not prove assertions quantified over infinite pseudo-orbits.

Run `python verify.py` in the same directory with Python 3 (standard library only). The script prints `VERIFY_OK exact_rational_finite_prefixes 840 adversarial_fixed_points 12` on success.

In the main proof, verify independently that (i) \(\mu-\delta>1\) prevents return from the contracting branch, (ii) \(x_N<k+\delta\) permits selection of a matching exact entry point, (iii) the backward error is a convex combination of the two sharp inverse-slope bounds, and (iv) constant pseudo-orbits near each fixed point give the separate lower obstructions. Nothing about independent mathematical verification is asserted.
