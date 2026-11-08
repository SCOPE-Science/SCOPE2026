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

The standalone verification script `verify_rook.py` can be executed with Python 3 and no external packages. It constructs the original labelled rook graphs without referring to any structural component decomposition, enumerates vertex subsets, checks induced maximum degree at most one, and checks maximality through every unselected vertex. It compares the resulting exact cardinality counts with the proposed formula.

Observed result:

`VERIFY_OK instances=17 vertex_subsets=1419214 dissociation_sets=9778 maximal_sets=1467 all_coefficients=PASS single_vertex_extensions=PASS`

The tested dimensions are all \(1\le m\le4\), \(m\le n\le6\), with \(mn\le20\). The finite computation does not certify infinite parameter ranges. The mathematical proof relies on a unique component decomposition and a complete coverage/maximality argument. Independent mathematical audit has not been performed.
