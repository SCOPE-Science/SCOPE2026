---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Every nonnegative unit flow on the DAG splits into 0-to-n paths, and each zero–one path incidence vector is extreme by its coordinates. The squared metric counts the arcs in exactly one path. For an independent generating-function derivation, split each ordered pair at the successive shared visited vertices. A primitive block is a shared edge of length 1 or 2, or a divergent/rejoining span k>=2: the initial short/long choice has two orders, intermediate single visits must alternate until rejoining, and the paths use k+1 differing edges. Thus the primitive series is t+t^2+2z^3t^2/(1-zt). Taking sequences of blocks and removing the empty one gives the stated rational series. In the record's transfer the state 11 reaches every state and has a loop, and all states return to it for positive z. The starting vector is nonnegative, not strictly positive as described, but its scalar product with a strictly positive Perron vector is positive, as is the terminal pairing. Primitivity and local analytic continuation justify the separated exponential term; implicit differentiation gives the specified log derivatives, and the Taylor limit and square-root delta method give both positive variances. The endpoint case n=1 contributes the single diagonal pair. Independently verified full distributions for n=1..12 using long-edge subsets and short-edge coverage, and the cubic log derivatives by symbolic arithmetic; replay record3() in /workspace/branches/frozen_metric_replay.py. No supplied script was executed. Finite enumeration only corroborates the all-n proof.

## originality

PASS

The uncontracted zigzag graph, path correspondence and Fibonacci counts are known. Exact Fibonacci-cube distances and the same-date path Hansen polynomials do not count short-edge disagreement or the ordering of adjacent long-edge disagreements and do not yield the claimed generating function and CLT constants. Bounded priority assessment only.

## value

PASS

The elementary path labels hide a different intrinsic edge-coordinate metric. The renewal/transfer law gives the complete finite distribution in a canonical infinite family and quantifies nondegenerate fluctuations both in squared distance and in ordinary Euclidean distance. Neither the Fibonacci vertex census nor its binary graph metric supplies this information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
