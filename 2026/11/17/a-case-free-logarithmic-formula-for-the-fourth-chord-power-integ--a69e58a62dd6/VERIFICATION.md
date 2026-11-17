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
# Reproducibility and limits
Run `python verify_chord_i4.py` with Python 3 and SciPy. Eight independent normal-angle/offset quadratures compared against the logarithmic formula; a further exact equilateral identity and three homogeneity identities were asserted. Every check passed in the original run, including near-degenerate and right triangles.

The analytical proof in RESULT.md establishes the all-triangle claim. Finite quadrature does not establish it and may lose precision at extreme near-degeneracy. Historical novelty is not independently certified. The code uses no external data or network.
