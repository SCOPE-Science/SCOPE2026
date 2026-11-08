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

# Reproduction and limits

With Python 3 and the SymPy and NetworkX packages installed, run `python verify_cactus.py` in the directory containing the attached standalone checker. The checker calculates block measures and block-resistance integrals from the supplied edge lists, derives the candidate extrema, and separately computes exact continuous Green diagonals from finite-element Kirchhoff matrices with the correct quadratic bubble-energy term. It tests rational points on edges and the rational critical points of cycle envelopes, including a non-antipodal unique optimizer on a graph of three circles.

Observed results from the packaged checker:

```
EXACT_INDEPENDENT_KIRCHHOFF_GREEN_COMPARISONS_PASSED 264
ALL_CACTUS_BLOCK_ENVELOPE_CHECKS_PASSED
```

The proof in `RESULT.md` establishes the general theorem without relying on this finite sample. In particular, tested exact rational values are not exhaustive over arbitrary cactus topologies or all positive real edge lengths. The centered kernel is an energy Riesz representer, and the universal reduction uses block-cut resistance additivity plus strict convexity/concavity of the derived potentials. No independent audit has been performed.
