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

# Reproduction instructions

Use Python 3 and SymPy 1.14. From this directory run `python verify.py`. The script is stand-alone, uses no network requests, and terminates with assertion errors on any failed comparison.

The script performs nine independent exact-rational infected-subset calculations for the six-edge witness, exact symbolic verification of its rational probability, strict derivative and crossover, and complete generation of graph isomorphism representatives. Every connected simple graph with at most four vertices, and every connected five-vertex simple graph with at most five edges, is represented. Graphs without triangles have no triadic-rate dependence. The seven remaining graph types produce 129 exact rational target-order comparisons; each has a zero or coefficientwise one-signed numerator after clearing its positive rational denominator. No floating-point Monte Carlo sample is used as proof. Finite graph enumeration does not establish claims for any larger graph.

The displayed race decomposition provides a proof independent of the computation for the five-vertex formula. The finite enumeration establishes the stated small-order absence of reversal, not any unbounded-graph statement. Independent scientific validation has not been performed.
