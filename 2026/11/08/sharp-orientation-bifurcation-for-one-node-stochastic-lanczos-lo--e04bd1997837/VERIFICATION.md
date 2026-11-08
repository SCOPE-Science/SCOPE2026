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

# Verification of the exact rank-one logarithmic SLQ orientation claim

The analytic proof is in `RESULT.md`, including definitions, fixed-\(q\) minimization, exact polynomial derivative and the sharp threshold comparison. The supporting script `verification/check.py` requires Python 3 and SymPy 1.14.0 (see `requirements.txt`). Run from the extracted document root:

```bash
python verification/check.py
```

The recorded run in `verification/run_output.txt` reports **45,867 passing exact symbolic/rational assertions**, independently recomputing the normalized four-sign identity, \(P(z)\) factorization and derivative, the endpoint difference polynomial, and broad finite rational/integer test families. The verification run is reproducible and checks the script against the embedded mathematical formulas. It is not a complete computational enumeration of continuous parameters; general correctness rests on the self-contained algebraic proof.

This verification does not establish publication novelty, generalization to other spectra, distribution-free accuracy, or independent scientific certification.
