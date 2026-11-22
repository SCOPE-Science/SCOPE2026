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

# Reproducibility checks

The analytic proof in `RESULT.md` treats the complete unbounded harmonic basis and all finite spherical configurations. The exact certificate `EXACT_CHECK.py` separately reconstructs the rational squared links of the zonal heat multiplier at \(t=\log2\) and \(s=\log(13/5),\log3,\log5\).

Run `python3 EXACT_CHECK.py`. Its final line should be `All exact rational certificates passed.` All inequalities use Python rational arithmetic; there are no floating-point tolerances, random seeds, external input files or network dependencies.

The positivity upper certificates test all eight LDL pivots of the truncated squared operator in the appropriate parity. The lower certificates are a strictly negative two-by-two principal determinant and two strictly negative one-by-one tests. The discarded columns have Hilbert–Schmidt norm less than \(10^{-9}\) from a geometric bound uniform over the three cases, so finite tests imply the stated **strict infinite-operator inequalities**. The exact checker does not claim the total number or locations of all parity ties.

Independent mathematical validation is not reported or implied by these checks.
