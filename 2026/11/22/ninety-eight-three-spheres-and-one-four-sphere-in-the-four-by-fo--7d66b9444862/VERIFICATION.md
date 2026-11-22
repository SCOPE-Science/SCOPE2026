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

# Exact standalone verification

Run with Python 3 in this directory:

```sh
python3 verify.py
python3 modp_check.py
```

Both programs use only the standard library. `verify.py` exhaustively constructs every permitted vertex subset in the four-by-four rook graph from graph-metric forbidden triples and independently through the equivalent bipartite-star-forest representation. It checks the entire face list, matching size, every Hasse relation, complete directed acyclicity, the critical-cell distribution, and the signed **integer** Morse boundary from the critical four-cell. Boundary signs depend on the ordinal position in the ordered simplex. The exact result is zero, after 191 integer unit substitutions. The critical-cell CW structure is one zero-cell, ninety-eight three-cells and one four-cell; its final attaching map is nullhomotopic.

`modp_check.py` independently computes the complete simplicial boundary ranks and Betti vectors over the fields with 2, 3 and 5 elements; these tests supplement rather than replace the exact integer Morse attachment calculation. The recorded complete outputs of both commands are in `verification_output.txt`.

These checks certify only the explicitly finite sixteen-vertex domain of the claim. Independent mathematical audit has not been performed.
