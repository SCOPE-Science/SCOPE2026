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

The standalone `verify.py` checks connected domination by closed-neighborhood coverage and induced connectivity, then checks inclusion-minimality by deleting each selected vertex. For the finite graphs checked, this agrees with direct family reconstruction from all labelled trees using Prüfer sequences.

Actual execution: `VERIFY_OK exhaustive_n=3..6 checked_nonempty_subsets=2131004 minimal_counts=3:6,4:36,5:320,6:3750 generated_n7=54432 membership=PASS minimality=PASS formula=PASS`.

The program exhaustively tests all nonempty subsets for \(3\le n\le6\), with vertex counts \(6,10,15,21\). At \(n=7\) it checks each generated set against the definition but does not test all \(2^{28}-1\) nonempty subsets. All infinite-size statements follow from the written combinatorial proof, not from the experiments. No independent audit was performed.
