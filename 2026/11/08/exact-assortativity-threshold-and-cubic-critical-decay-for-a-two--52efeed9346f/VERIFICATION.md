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

# Reproduction and verification

The standalone `verify.py` uses exact symbolic arithmetic in Python 3 with SymPy. Run `python verify.py` in the same directory as this document. Its successful output is `VERIFY_OK`.

The script constructs the published polynomial SIS dynamics, the two-class Perron vectors, the nonzero stable eigenvalue, the projected quadratic coefficient, the quadratic center-manifold correction, and the full cubic coefficient. Each claimed rational expression is checked by symbolic simplification to zero. It also checks the derivative signs' *formulae* and the exact endpoint, neutral-mixing, and zero-assortativity identities; inequalities themselves follow from explicit positive coefficients and positive denominators on the declared parameter interval.

The analytic argument requires the irreducible Perron eigenvalue to be simple; it is for \(-1\le r<1\). Standard local center-manifold theorems then justify the amplitude equation and its stable transverse contraction. The calculated polynomial signs provide an infinite-parameter proof; finite numerical simulations are neither needed for nor substituted for the theorem. The conclusion is local and deterministic and no external independent verification has been performed.
