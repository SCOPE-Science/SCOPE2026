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

# Reproducibility checks and exact scope

Use `python3 verify_gaussian_design.py` (Python 3.10+, standard library only). A direct execution of the packaged script completed with:

`PASS: 78817 independent numerical formula/competitor/boundary checks`

The script independently inverts the noisy two-by-two observation covariance and compares it to the rational formula, evaluates many alternative allocations and reflected locations across varying length-scales, target scales and budgets, includes omitted-channel cases, checks the exact critical regime, and numerically inspects the square-root onset. The numeric tests are finite and not a proof of global optimality, originality, or the asymptotic law. The proof is the analytic algebra and strictly signed derivatives in RESULT.md, which cover every continuous admissible choice in the restricted mirror-location family.

Neither the independent mathematical audit nor a comprehensive historical publication-priority audit has been performed. There is no theorem here for two freely asymmetric sites, more observations, unequal precision costs or unknown kernel parameters.
