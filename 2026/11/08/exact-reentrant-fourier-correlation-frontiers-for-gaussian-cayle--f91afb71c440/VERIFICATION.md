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

The source of reproducible finite checks is `verify.py`. It requires Python 3 and `mpmath`; execute `python verify.py` in the directory containing it. The contemporaneous deterministic output is `verify_output.txt`: 151 checks passed. These checks compare numerical Gaussian integration to independently derived erfc formulae for the first two modes, reproduce the three roots numerically, and test the exact Chebyshev identity on a finite grid. Only the analytic proof in `RESULT.md` establishes global root uniqueness, exact sign intervals, and statements for all Fourier indices. No independent scientific audit has been performed.
