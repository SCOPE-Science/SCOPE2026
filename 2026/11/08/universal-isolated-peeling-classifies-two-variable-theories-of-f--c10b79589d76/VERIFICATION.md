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

## Reproducible finite check

Run `python verification/verify.py` using Python 3.10+ and NetworkX 3.x, from the directory containing this document. The embedded `verification/output.txt` is the exact expected stdout, including `PASS`.

The procedure constructs the entire zero-/one-/two-pebble state space for the 1253 unlabeled simple graphs in the NetworkX atlas through order seven, including the empty graph. Equality and adjacency are explicitly represented in the atomic initial partition. It repeatedly refines every state by *both* possible pebble-replacement successor-color sets, until stable, and checks that the resulting graph-level classes agree exactly with the signed-peeling signatures. It also independently checks the minimum-order coefficients against a recurrence for the rational series.

The 55 classes include the empty graph, which lies outside the theorem's stipulated nonempty domain. The 54 nonempty classes and the minimum-representative counts through order seven agree with the theorem.

This is an exhaustive finite atlas test, **not** an infinite proof or an independent audit. The full theorem uses the permanent pebble-game argument supplied in RESULT.md. Numerical agreement cannot certify historical priority.
