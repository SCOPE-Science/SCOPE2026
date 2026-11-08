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

# Verification and limits
The analytic argument is self-contained in `RESULT.md`: regenerative equilibrium-age formula, the unique critical ratio root, explicit concave majorant, Jensen and equality cases, and the infimum construction. The standalone `verify_envelope.py` requires Python 3 and SciPy and checks independent Gaussian quadrature against the closed form, the root residual and tangency, and mixed-clock bounds across parameter values. A local run passed 430 finite numerical assertions. These tests are not an independent proof of the infinite-dimensional variational claim and do not certify historical originality. The small-reset-period extremizing family approaches its supremum but is never equal to it. No independent audit has been performed.
