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

# Verification details

The standard-library checker `artifacts/check.py` independently constructs the independent-set incidence indicator, its full exact integer Walsh transform, the Fourier multiplier support and the inverse transform for two complete groups: \(m=1\) with \(8\) elements, and \(m=2\) with \(1024\) elements. At \(m=1\), it confirms three missing frequencies, rank five and range-projection endpoint norm \(7/4\). At \(m=2\), it confirms 405 missing frequencies, rank 619 and norm \(7397/512\). It also evaluates the proved formula at \(m=3\) as \(39965296585/67108864\), with no complete enumeration of that dimension. Run `python artifacts/check.py` at the package root. The correctness proof is algebraic for every \(m\ge1\); these finite tests are reproducibility checks only. No external independent audit has been performed.
