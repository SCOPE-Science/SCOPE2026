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

# Reproducibility of the four-color bipartite temporal census

With Python 3, from the root of this package:

```sh
python scripts/verify_supports.py
python scripts/verify_vertices.py
```

The first command independently regenerates all 225 initial nonempty tagged-support pairs, their exact first-entry/least-period classifications, the ten \(4\)-by-\(4\) coefficient matrices, and the surjection-weighted checks for selected shore sizes. The finite classification is also fully enumerated in `checks/support_catalog.tsv`. The second command uses explicit neighbour lists on ten labelled complete bipartite graphs and exhaustively checks 92,752 labelled initial colorings. It agrees with all weighted class counts, including all 65,536 configurations of \(K_{4,4}\).

Captured results from the supplied programs are in `checks/support_check.log` and `checks/vertex_check.log`. The computations prove the finite 225-case classification as a reproducible exhaustive certificate; the universal graph-size conclusion additionally uses the mathematical reduction and onto-coloring argument in `RESULT.md`. Exhaustion of the listed small graphs by itself proves no all-size statement. An independent audit has not been performed.
