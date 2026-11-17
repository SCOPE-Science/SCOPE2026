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

# Verification notes

The theorem uses the intrinsic shortest-path metric on two vertices connected by at least three positive-length edges with a uniquely shortest link. The proof in `RESULT.md` gives a complete partition of the product space into same-edge transit triangles and distinct-edge transit rectangles. All formulas are exact; no finite check is offered as proof for infinitely many length choices.

The standalone Python standard-library script `verify.py` re-computes the event by independently enumerating simple path lengths. It compares the exact formula against midpoint quadrature and independently generated arclength-uniform endpoint pairs for eight length vectors involving 3–7 edges; each numerical quadrature uses a 230×230 grid for every ordered edge pair and 80,000 Monte Carlo pairs per configuration. The script checks the sharp fixed-length inequality and equality shapes. A second run of 650,000 independent conditioned-coordinate proposals verifies the three barycentric coordinate means of the same-edge simplex against \(1/3\), and the distinct-edge rectangle coordinate means against \(1/2\). Expected sampling error is accounted for by the stated tolerances in executable assertions.

Run with `python verify.py`; successful completion prints `PARALLEL_GEODESIC_COMPLETE_EDGE_TRANSIT_CHECKS_OK 8`.

No randomized test establishes universal correctness, nor has any independent external mathematical audit been performed. The nearest literature studies spectral gaps and continuous mean distance on related metric graphs, with possible future historical comparison needed for exact complete-edge routing formulas.
