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

## Reproducible checks
Run `python3 checker.py` from the extracted artifact directory (only Python standard library required). The checker evaluates all graph integrals analytically through piecewise linear minima, checks the closed hub formula and two-edge circle degeneracy, tests the strict gap inequality with positive prescribed length profiles, and compares against independent midpoint quadrature over actual shortest-path alternatives. It executes 22,000 parameter-position cases across 800 graph configurations with two through nine edges, including repeated edge lengths, and 24 quadrature comparisons. The actual successful marker is `PARALLEL_GRAPH_ARCLENGTH_MEDIAN_OK 22000 max_bound_excess 8.882e-16 max_midpoint_error 1.212e-07`.

## Limits
Finite computation corroborates formulas at tested instances; the theorem for every positive real length vector rests on the analytical proof, not the checker. Independent external proof and historical-priority audits have not been conducted.
