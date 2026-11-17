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

# Reproduction and limits

Run `python CHECKER.py` in a Python environment with NumPy. The checker reports `OK: 72 exact-rational cases and 3 asymptotic probes`; the exact-rational cases validate matrix determinants, positivity/rank of individual symmetric parts, the parallel-sum inverse and resolvent identities, and both squared singular-value expressions. The three numerical probes verify the predicted leading orders along an approaching diagonal path. The companion mathematical proof in `RESULT.md` supplies the universal parameter and asymptotic statements and directly handles the singular multivalued relation. Finite sampling does not establish any universal fact on its own.

Primary-source statements were compared at the level of hypotheses and implications. The classical linear paramonotonicity criterion and nonexpansiveness of monotone resolvents are treated as previously known, not independently discovered. Numerical findings are not claimed as an independent mathematical audit.
