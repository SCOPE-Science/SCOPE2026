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

# Verification instructions and scope

Execute `python checks/verify.py` with Python 3 and no third-party packages. A normal run ends with `ALL_CUBIC_TWO_CAP_SPECTRAL_CHECKS_OK`. The script derives the four polynomial cap-energy ratios by rational integration of associated Legendre factors; compares all coefficients with the stated formulas; verifies all six factored eigenvalue gaps, the trace, the exact resonance values, and rational representatives of the strict-ordering intervals; and independently checks twelve numerical integrations.

The exact polynomial identities together with positivity of the factored expressions prove the universal comparisons for every cutoff in \(0<t<1\). The numerical integrations and finitely many sampled cutoffs are consistency checks only. The implementation does not certify the absence of earlier equivalent papers, the geometry of unequal caps, or arbitrary-degree Slepian concentration. Independent external audit has not been performed.
