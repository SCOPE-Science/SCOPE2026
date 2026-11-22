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

The included standard-library script `checker.py` proves strict numerical interval bounds for the explicit \(L=D=1\), \(a=3\), \(x=1/100\), \(r=100\) witness using exact rational Taylor interval arithmetic, confirms the weak-derivative rational expression, and checks resolvent-integral agreement numerically. To run: `python3 checker.py`. These computations are ancillary; the global statement is established analytically through renewal, Dynkin's formula, the killed Green kernel and a two-step limit. No independently audited formal proof or complete literature novelty guarantee is claimed.
