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

The analytic theorem is proved from subgradient KKT conditions, explicit flux evolution inside fused blocks, and data constructed by KKT inversion when a prescribed flux exceeds its permitted edge penalty. The limiting-flux inequalities are sufficient for every data signal; a strict violated inequality yields data with a nontrivial interval of fusion followed by separation.

`check_cycle.py` is a dependency-free exact-rational checker. Executing `python check_cycle.py` checks 16 regularization-level KKT certificates in the two explicit counterexamples, a stable nonconstant triangle, and 1,700 finite sampled positive mass/penalty profiles exhibiting the specified local minimum obstruction. All included tests passed. Sampled checks do not establish infinitely many cases, and no independent audit has been performed.
