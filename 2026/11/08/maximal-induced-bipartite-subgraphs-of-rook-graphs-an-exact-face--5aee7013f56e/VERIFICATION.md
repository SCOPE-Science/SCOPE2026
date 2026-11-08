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

# Reproducible finite checks

Run `python3 verify_rook_bipartite.py` in a directory containing the standalone script. Only the Python 3 standard library is needed. For every vertex subset of each rook graph of order at most sixteen in the tested parameter list, the verifier reconstructs the induced graph, two-colors every component, checks the independent degree-capacity test, and tests one-vertex extensions for inclusion-maximality. Two larger boards are enumerated via the capacity test already exhaustively compared with graph bipartiteness on all smaller test boards. The predicted facet counts come from an exact rational coefficient recurrence for the path/cycle exponential generating function.

Verified cases: \((m,n)=(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5)\). The script prints the full per-case coefficients and concludes:

`VERIFY_OK cases=11 examined_subsets=1419088 bipartite_sets=59904 maximal_sets=6506 GF=PASS classification=PASS`

The finite results confirm the proposed formula for the named instances, not for all integers. The all-parameter proof appears in RESULT.md, including a direct necessity/sufficiency argument and explicit labeled component counts. No external independent audit has been performed.
