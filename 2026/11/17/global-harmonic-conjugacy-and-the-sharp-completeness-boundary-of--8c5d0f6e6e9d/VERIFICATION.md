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

# Verification of analytic identities

Execute `python checker.py` with Python 3, SymPy, and NumPy. The included checker verifies Lie-derivative identities for the inverse-radius oscillator, the angular equation, conservation of the rational integral, and the exact integral/oscillator-radius relation. Representative numerical reconstructions check consistency of the inverse coordinates with the original vector field, and direct numerical formulas check the limiting finite lifespans. The recorded successful output was `QUADRATIC_TORUS_HARMONIC_CONJUGACY_CHECK_OK`.

The infinite-time classification and blow-up assertions are proved analytically using the exact conjugacy, circular-arc geometry, and Taylor expansions, rather than by numerical enumeration. No independent audit or external certification has been performed.
