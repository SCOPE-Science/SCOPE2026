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

Execute `python3 VERIFY.py` from this directory. It uses only `fractions` and `itertools`, creates exact rational inverses for four cubic test graphs, checks the stochastic and inverse identities, enumerates all sign cuts for these finite examples and checks the recovered sharp curvature and extremizers. The output ends with `ALL_EXACT_CHECKS_PASSED` if successful.

The checker is a finite consistency test, not a substitute for the general algebraic proof. The external cubic MAX CUT hardness theorem is cited rather than mechanically reproduced. The inferred numerical conditioning bound and the all-dimension rounding proof are analytical. Full-text originality comparison for the 1990 norm-maximization paper remained unavailable, and no independent validation has occurred.
