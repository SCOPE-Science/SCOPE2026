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

# Verification notes

The mathematical proof applies to all integers \(b,n\ge2\) using a published Apéry-representative lemma and explicitly proved recurrences. `CHECKER.py` is a standalone pure-Python 3 verification aid and needs no nonstandard dependencies. Executing `python CHECKER.py` succeeded on 26 parameter pairs, comparing the predicted length histogram against direct additive-semigroup membership and separately verifying every Apéry representative with Dijkstra shortest paths. Exactly 8,585 maximal missing-integer intervals were checked. The maximal multiplicity tested was \(R_n=511\); no computational finite range is presented as exhaustive for arbitrary parameters. Published antecedents and outstanding access/prior-publication risks are given in RESULT.md.
