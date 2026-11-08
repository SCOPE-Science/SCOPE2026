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

# Verification record

The general result is proved algebraically in `RESULT.md`: positivity and invertibility of the base matrix, a direct rank-one equilibrium identity, strict quadratic curvature on the centered opinion space, and minimization of a positive quadratic on a half-open fractional-linear interval. No finite computer experiment is used as proof of an infinite assertion.

## Reproduction

Run `python3 verify.py` with Python 3 and no third-party dependencies. The verifier uses exact fractions for the graph Laplacians, stubbornness coefficients, innate opinions, inverses, and polarization–disagreement objectives; it independently solves the FJ systems rather than assuming the candidate rank-one identity. It tests 540 connected graphs with orders two through seven, eight selected-node coefficients per graph, and sampled scalar-optimality inequalities. Its observed output is:

```
VERIFY_OK configurations=540 exact_assertions=12831 three_vertex_minimizer=1/3
```

The exact three-vertex checks include the rational function for polarization–disagreement, its derivative identity, the unique optimum \(t=1/3\), and comparisons with the low- and high-resistance limits. The finite tests cannot prove absence of undiscovered equivalences in the literature, correctness for all graphs on their own, or any independent certification.
