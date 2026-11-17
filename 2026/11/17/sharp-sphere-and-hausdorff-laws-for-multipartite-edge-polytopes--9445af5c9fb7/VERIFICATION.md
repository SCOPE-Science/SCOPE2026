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
# Verification and reproducibility

The exact-arithmetic program `checker.py` checks all positive integer partitions of totals from three through twelve that have at least two blocks. It constructs the graph's edge vertices and tests the derived squared smallest-ball radius and all contact classifications with rational fractions. It constructs the claimed nearest point for every forbidden edge vertex and checks both its exact squared distance and the nonnegative projection inner-product certificate against every permitted edge vertex. The recorded successful output is:

`MULTIPARTITE_EDGE_METRIC_EXACT_PASS profiles=258 contact_edges=8704 strictly_inner_edges=198 missing_vertex_projections=3150`

Run from this directory with `python checker.py` (standard library). The supplementary `numeric_checker.py` runs ten separately coded constrained numerical optimizations of the Euclidean minimum enclosing ball (NumPy and SciPy are required). Its output lists ten tested class profiles; it also checks rational-coordinate projection certificates by floating-point evaluation.

The formal proof in `RESULT.md` establishes the arbitrary finite graph theorem using only: (i) convex projection and a barycentric minimax lower bound; (ii) the rank-two hypersimplex identity for the feasible class sums; (iii) a strict-convexity/KKT calculation; and (iv) Cauchy--Schwarz plus equality conditions for the forbidden-vertex projections. Finite enumeration and numerical optimization are corroborating checks, not infinite certificates.

Priority has been reviewed against identified literature but not independently audited. No independent mathematical verification has been performed.
