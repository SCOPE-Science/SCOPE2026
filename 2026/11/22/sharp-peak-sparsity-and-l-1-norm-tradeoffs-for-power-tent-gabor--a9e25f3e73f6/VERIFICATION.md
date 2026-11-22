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

The proof establishes the statement for every real exponent \(r>0\), every modulation \(0<\beta\le1/2\) and every feasible peak cap; it uses the exact two-site duality relation, the pointwise constrained extremizer and integral differentiation. The code `checker.py` independently checks finite instances and asymptotic algebra only as supplementary evidence. Execute `python checker.py` from the directory containing this file and the checker.

Observed run: 9,913 rational exact linear-program fiber comparisons, 46 independent integral/closed-form comparisons and 36 support comparisons passed. No computer experiment is offered as a proof for continuously many parameters. The large-cap formula is already a consequence of unrestricted dual theory; the novel claim is the constrained interpolation and its boundary analysis. Independent mathematical audit was not performed.
