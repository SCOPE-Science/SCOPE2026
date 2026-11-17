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
# Verification and boundaries

Run `python3 check.py` with Python 3 and its standard library. This uses two independent routes. First, every one of the \(4^q\) choices of edge directions for \(2\le q\le8\) is tested by Kahn's directed-acyclic-graph algorithm; the resulting half-signed-degree coordinates produce exact integer exponents \(2\|v\|_2^2\). These counts are matched coefficient-by-coefficient against the closed multinomial expression. A second purely integer combinatorial check compares total counts, both extreme values, their multiplicities and exact rational means for all \(2\le q\le150\).

Observed output: `K2Q_RADIAL_PASS independently_enumerated_dimensions=2..8 independently_enumerated_vertices=19166 symbolic_dimensions=2..150`.

These checks are finite. The full-dimensional theorem rests on the acyclic-orientation characterization, a direct norm computation, strict convexity, multinomial sampling, and standard central limit and delta methods. The analytic central limit theorem is not established by the finite computation.

Self-review: passed. Independent audit: not yet performed.
