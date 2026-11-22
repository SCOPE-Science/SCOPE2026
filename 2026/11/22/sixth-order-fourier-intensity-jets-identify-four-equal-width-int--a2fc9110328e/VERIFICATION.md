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

# Reproducibility and limits

Run `python CHECK.py` with Python 3 and SymPy. This reproduces the six-distance polynomial identities, eliminated cubic, strict-monotonicity expressions, direct sixth-order intensity coefficients, a distinct lower-jet collision and 500 rational parameter checks. The recorded message is `FOUR_INTERVAL_SIXTH_JET_CHECKS_PASSED`.

The universal conclusion is based on the analytic inequalities and algebraic proof in RESULT.md, not the finite checks. In particular no computer algebra output by itself certifies an exhaustive search over real interval lengths. Sources listed in RESULT.md were compared by mathematical implication; the full motivating preprint remains uninspected. No independent mathematical validation has been performed.
