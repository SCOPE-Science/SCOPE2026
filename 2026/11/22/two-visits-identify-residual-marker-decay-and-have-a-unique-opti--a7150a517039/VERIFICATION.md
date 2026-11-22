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

For reproducibility, run `python3 check.py` using Python 3 and its standard library. The checker evaluates all four binary history probabilities, reconstructs the parameters by exact rational arithmetic for a grid of rational \((\psi,\alpha,a_t,q)\), and independently forms the Fisher matrix from category gradients at \(q=1\). It reports `PASS exact_fraction_checks=1296 numeric_checks=2415` and a numerical optimal gap of 22.912756169443 at the stated example parameters. All exact rational checks passed on the packaged code; finite numeric tests do not prove the general theorem. The full proof establishes global identifiability and unique local D optimality on the expressly stated open domain. No independent validation was performed. The residual-marker decay law, within-site conditional independence and perfect-detection optimum are mathematical assumptions, not empirically certified field conditions.
