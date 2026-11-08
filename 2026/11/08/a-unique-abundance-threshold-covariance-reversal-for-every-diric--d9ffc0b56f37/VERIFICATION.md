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

## Repeatable checks
Run `python verify.py` in a Python 3 environment with SciPy installed. The script performs 690 exact rational checks (660 beta-binomial covariance identities and 30 exact zero checks), 150 direct quadrature and sign checks across non-integer powers, and 20 high-order limiting checks, for a total of 860. Output observed: `PASS 860 checks`.

The analytic proof in RESULT.md establishes the full parameter domains; finite exact checks, floating quadrature and numerical root-finding are corroboration only. The numerical tests use finite power 300 and do not prove the infinite-power limit. No external audit or formal proof assistant result is asserted.
