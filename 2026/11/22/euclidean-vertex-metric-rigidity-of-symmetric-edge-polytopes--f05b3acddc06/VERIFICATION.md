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

The theorem concerns exact standard-coordinate signed edge-incidence roots. Its proof is given in `RESULT.md`; none of the following finite tests is used as a substitute for Whitney's theorem or for the all-graphs inner-product identity.

Run from the directory containing these embedded files:

```sh
python3 sep_metric_reconstruction_check.py
```

The script uses Python's standard library only. It computes exact integer squared distances from independently formed coordinate differences, identifies unique antipodes, reconstructs line-graph adjacency from the four shells, and compares directly to source-edge incidence. It exhaustively checks all labeled simple graphs of orders 2--5 (discarding empty edge sets), plus 601 deterministic masks on six vertices. It separately tests triangle/claw ranks 2 and 3, distinguishes a four-vertex path from a three-leaf star, and tests near-boundary errors with absolute value less than one. The checker reports:

```
SEP_METRIC_RECONSTRUCTION_EXACT_PASS
graphs_tested 1694
Whitney_exception_dimensions 2 3
squared_distance_shells (2, 4, 6, 8)
```

An additional graph-atlas comparison of 1245 graphs with edges, up to seven graph vertices, recovered the corresponding line graphs from the same exact metric-shell rules. That calculation was performed separately; the standalone checker is the package-replayable finite test.

**Critical infinite step.** For any distinct undirected graph edges, the dot product of their signed incidence roots is zero if and only if they are disjoint, and otherwise has absolute value one. Whitney's connected line-graph isomorphism theorem then leaves only triangle/claw, resolved by the rank of the centered six-point distance matrix. This is the complete mathematical proof, not a computational inference.

**Limits.** No claim about arbitrary weighted roots, unlabeled distance *histograms*, missing measurements or independently verified priority is made. The metric-noise guarantee is for a complete table whose entrywise squared-distance errors are strictly less than one.
