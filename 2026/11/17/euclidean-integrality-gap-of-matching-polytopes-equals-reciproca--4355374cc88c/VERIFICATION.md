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
# Reproducibility

Use Python 3.11 or later with `networkx`, `numpy`, and `scipy` installed. From a directory containing both scripts, execute `python verify.py` and `python exhaustive_graphs.py`. The second script imports helpers from the first. No network calls or precomputed data files are required.

The exact rational test verifies the Cauchy–Schwarz certificates for all fractional half-cycle packings and matchings in each selected graph, tests every vertex degree bound and every odd-set matching inequality, and verifies the claimed squared distance by rational arithmetic. The numerical check is an independent quadratic-programming fit of the nearest matching-polytope point using SLSQP and the full small-graph Edmonds halfspace representation. A Euclidean vector error tolerance of \(2\times10^{-5}\) is used for these numerical comparisons. The all-five-vertex-graph test inspects 1,024 labeled graphs, encompassing 12,287 fractional vertices. The programs' successful markers are:

```
MATCHING_HAUSDORFF_PASS packs=157 vertices=518 independent_QP=85
FIVE_NODE_GRAPH_EXHAUSTIVE_PASS graphs=1024 vertices=12287 packs=2687
```

The programs are finite experiments and do not prove universal claims, which instead follow from the classical half-integral vertex theorem, Cauchy–Schwarz, the explicit averaging construction, and convexity. In particular, the tests are not exhaustive for graphs with six or more vertices. The NP-completeness assertion uses the established triangle-partition problem; no complexity proof library or randomized solver is needed.
