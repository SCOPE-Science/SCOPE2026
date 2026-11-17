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

## Scope of verification

The exact finite certificate is `verify_graph_bv_heat.py`. Run with `python3 verify_graph_bv_heat.py`, requiring only the Python 3 standard library.

Its successful execution checks all 40 allowed small-cycle leaf-attachment patterns, all 3,064 associated nontrivial cuts, the equality between cut formula and a separately evaluated directional derivative, 48 explicit long-cycle witnesses, 16 excluded pentagon attachment patterns, 165 bridge-cut identities, and a Lipschitz-vs-edge-variation separating witness.

The program is exhaustive only for the explicitly bounded small-cycle cases, not for all finite graphs. The unrestricted cut criterion and the arbitrarily large unicyclic obstructions require the symbolic arguments given in `RESULT.md`; their validity does not follow from finite experiments. Publication-priority equivalence outside the inspected sources is unproved. Independent mathematical audit has not been performed.
