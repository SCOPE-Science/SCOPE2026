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

# Verification and limits

The theorem's proof is analytic. Execute `python3 check_theta_inball.py` using Python 3 with only the standard library. The script checks exact rational potential norms and contact ranks independently using (i) integer feasible-value enumeration with a graph-connectivity test for tight edges at \(m=3,4,5\), and (ii) signed path-gradient words at \(m=3,\ldots,8\).

Expected terminal messages:

```
RAW_INTEGER_FEASIBLE_TIGHT_GRAPH_VERTICES_PASS models= 3 facets= 708
FULL_SIGNED_PATH_POTENTIAL_VARIANCE_AND_RANK_PASS models= 6 potentials= 19668
THREE_EDGE_GENERALIZED_THETA_INBALL_ALL_CHECKS_PASS
```

Exact finite verification is not a proof for every integer \(m\ge3\). The all-integer claim follows from connected tight-edge graphs, the bipartite parity argument, the centered-squared-norm identity, strict integer maximization, and the explicit rank computation in `RESULT.md`.
