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

## Reproducibility
The formulas can be tested by running `python verify.py` with SymPy and SciPy. Checks include exact symbolic derivative and reconstruction identities, four angular quadrature checks for each of four example rectangles, and five positive target ratio reconstructions, including examples approaching both sharp boundaries. The proof's general quantifiers do not depend on finite sampling.

## Limits
No arbitrary-precision computer algebra output substitutes for the self-contained positive-density facet-normal reduction or global monotonicity argument. Classical-priority coverage remains incomplete; no independent audit has been performed.
