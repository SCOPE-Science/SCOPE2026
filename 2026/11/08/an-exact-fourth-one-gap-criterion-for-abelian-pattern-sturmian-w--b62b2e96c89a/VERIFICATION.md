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

Run `python verify_prefix.py` from the directory containing this file. The checker constructs the graph directly from each list of sums and uses a disjoint-set union cycle test; it does not implement the residue-chain proof.

The inspected code checked all \(7920\) pairs \(3\le M\le90\), \(1\le t\le90\), including \(6895\) acyclic graphs. Each acyclic case was also tested after three successive additions of a support value greater than twice the previous maximum. These finite checks corroborate the theorem but cannot certify its infinite quantifiers.

The infinite proof depends on the direct graph argument in RESULT.md and on Theorem E of arXiv:2609.28059 for the equivalence between acyclic incidence graphs and Abelian pattern Sturmian words. No independent audit has been performed.
