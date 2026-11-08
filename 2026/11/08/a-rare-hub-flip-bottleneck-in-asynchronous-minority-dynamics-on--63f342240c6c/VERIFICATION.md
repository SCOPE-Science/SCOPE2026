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

# Reproduction and scope
The result concerns the self-inclusive minority update on \(F_m\) with uniform random single-vertex selection. Its proof is written in `RESULT.md`; the following tests independently check finite cases.

Run `python checks/check_scc.py` and `python checks/check_product.py` from the extracted package root. Both scripts require only the Python standard library. `check_scc.py` exhaustively builds state transitions on \(2^{2m+1}\) binary states and computes closed strongly connected classes for \(m=1,2,3,4\). `check_product.py` independently re-implements the update rule, exhaustively constructs the claimed recurrent states and their outgoing transitions for \(m=1,2,3,4,5\), and checks exact rational hub-flip probabilities. Original outputs are included alongside the scripts.

The scripts prove no infinite-parameter statement by themselves. The general correctness rests on the graph-product, energy-descent, reversible-uniform-measure, and stationary crossing arguments in the main proof. A matching mixing-time upper bound was not established. Independent external audit has not been performed.
