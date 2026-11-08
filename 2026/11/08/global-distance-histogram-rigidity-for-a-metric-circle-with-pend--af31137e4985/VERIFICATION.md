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

# Verification

The primary mathematical evidence is the derivation from ordered point-pair arclength, exact formula (2), one-sided density limits, and the signed-measure peeling induction (3) in `RESULT.md`. The theorem is not an enumeration claim.

Reproduce finite checks with `python verify.py` using Python 3, NumPy and SciPy. The check was actually run with output:

`VERIFY_OK exact_reconstructions=960continuity_collision_cases=3 direct_pairs=350000max_cdf_discrepancy=0.000782`

The script checks 960 randomly generated *exact rational* configurations (arm counts 1–8) with exact arithmetic for the atomic inverse and near-zero formulas, three collision/jump checks, and seven numerical CDF comparisons with an independently constructed direct metric-graph point-pair simulation. All arm and circle lengths are positive in the verifier. Numerical integration and Monte Carlo are not infinite proofs. A direct self-review was conducted; independent validation was not performed.

Scope exclusions: finite samples do not provide the exact density discontinuity or distributional derivative; no numerical stability or nonparametric statistical recovery theorem is claimed. Other graph topologies are outside the injectivity statement.
