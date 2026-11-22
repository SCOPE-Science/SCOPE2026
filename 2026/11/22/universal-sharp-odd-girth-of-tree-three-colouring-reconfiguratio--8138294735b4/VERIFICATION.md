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
# Reproducible checks

Run `python3 verify.py` with Python 3 and the standard library. It checks all labelled trees with one through five vertices (146 in total), the entire labelled three-colouring reconfiguration graphs and their exact move sets, the predicted connectedness, numbers of edges, parity and shortest odd closed walks, and the legal three-sweep \(3n\)-step witness from each colouring. Four representative tree shapes at each of six and seven vertices are also tested.

The checker is an independent finite corroboration of the integer-height proof, not an exhaustive verification at unbounded order. An even-order graph has no odd cycle; the parity-expanded shortest-odd-closed-walk breadth-first searches test precisely this finite claim. Publication history comparisons remain subject to unindexed sources.
