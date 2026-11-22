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

# Reproducible mathematical checks

Two standalone Python 3 programs use only the standard library. From a directory containing the extracted files, run:

```sh
python verify_visibility.py
python verify_bfs.py
```

`verify_visibility.py` constructs the twenty vertices and thirty edges of \(H(5,2)\) from subset inclusion; validates the geodesic-mask multiplicities; generates every feasible face by ordered insertion; validates both size polynomials and the two symmetry orbits; and compares all optimum jump/slide pairs with the stated Petersen line-graph model. Its expected final line is `VERIFY_OK`.

`verify_bfs.py` constructs \(GP(10,3)\) independently, exhausts the full \(2^{20}\)-mask universe using the hereditary pruning condition, and tests visibility by shortest-path BFS avoiding other chosen vertices. Its expected final line is `VERIFY_BFS_OK`. The two checks arrive at the same cardinality polynomial with different graph presentations and shortest-path predicates. The first proves the remaining structural statements by exhaustive finite comparisons.

The first implementation explores feasible masks only because infeasibility is hereditary; this pruning is logically exact. The second examines each ambient mask (and skips a subset only when a known infeasible predecessor exists), which again is exhaustive by heredity. Correctness of an infinite family is neither asserted nor inferred. Neither code execution nor this review is an independent scientific audit; publication priority is not certified.
