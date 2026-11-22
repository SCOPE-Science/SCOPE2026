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

# Reproduction and proof limits

Run `python3 CHECK.py` with Python 3 and no third-party packages. The script uses exact rational arithmetic and verifies the explicit continuant determinants, the derivative quartic for the stated rational bias, seven direct rational absorbing-walk linear systems, four rational isolating signs, the five-member Sturm chain's variations at the two endpoints, and the exact endpoint inequality used in the uniform sign bound. Its output reports the tested identities and the exact Sturm variation difference.

The entire parameter interval \(0<\varepsilon\le3/50\) is proved analytically by the sign formulas, the upper bound \(g(\varepsilon)\le g(3/50)<8\), and continuity. The finite verifier does not enumerate this continuum. All denominator positivity is proved from finite transient reversible substochastic matrices, not numerical conditioning tests. The two-root conclusion for \(\varepsilon=1/20\) is a Sturm-theorem consequence, and the root brackets are exact. The cited monotonicity theorems are the external premise of the one-valued lower-bound argument. No independent audit has been performed.
