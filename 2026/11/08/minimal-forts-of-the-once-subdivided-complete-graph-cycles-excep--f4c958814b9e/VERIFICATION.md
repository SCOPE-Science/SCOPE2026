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

Run `python3 verify.py` with a standard Python 3 interpreter. The program uses no nonstandard dependencies.

It constructs the subdivision vertices and all adjacencies from the original complete graph, tests the fort condition directly, and enumerates inclusion-minimal forts by ascending cardinality. In contrast to an insufficient one-vertex-deletion test, its inclusion-minimality algorithm rejects any fort containing an already identified smaller fort.

The expected families are generated separately from undirected simple cycles, the complete original set, and each exceptional original-star complement. Full set equality and coefficientwise polynomial equality are asserted for all orders \(3\le n\le6\).

Observed final output:

`VERIFY_OK n=3..6 vertex_subsets=2131004 minimal_forts=264 exact_minimality=PASS polynomial=PASS`

The checks enumerate all \(2,131,004\) nonempty subsets in these four graphs, including \(2,097,151\) subsets at \(n=6\). This confirms finite instances only. The general classification and asymptotic statement are proved mathematically in RESULT.md. No independent audit has been performed.
