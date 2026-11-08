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

# Verification record

The analytic steps in `RESULT.md` are sufficient for arbitrary finite connected graphs and nonempty anchor sets; the included `verify_graph_kaczmarz.py` checks exact identities only for the finite labelled-graph census up to five vertices.

Run `python3 verify_graph_kaczmarz.py` using the standard library. The expected result is `VERIFY_OK 23169 cases; unique 6891 nonunique 16278`. Arithmetic uses pairs of exact rationals for \(\mathbb Q(\sqrt2)\); no floating-point tolerance substitutes for equality.

The checker verifies normalization and the eigenvector identity for one explicitly constructed shortest-path-forest optimum, confirms the distance inequality, and evaluates the uniqueness criterion. It is not an exhaustive enumeration of all optimal probability laws, and it is not an external certification. The flow-face equivalence and uniqueness in all graph orders rely on the proof in `RESULT.md`. Unindexed prior art remains a possible originality limitation.
