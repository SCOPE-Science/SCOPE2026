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

# Reproducibility and proof checks

Invoke `python VERIFY.py` with Python 3 and its standard library. Its exact-arithmetic transfer test checks the matrix identity \( (R-I)(R-I/3)^2=0 \) and times \(3,4,5\); these imply the published all-time one-density formula once the cited finite-state transfer representation is accepted. Direct local-window enumeration independently verifies each mean-decrease fraction for times \(1,2,3,4\): respectively \(16/243,17/729,2/243,19/6561\). All 27 lifted local truth-table entries are tested, as are the 64 protected words with both run lengths from 2 through 9. Two implementations traverse every initial state on rings of lengths 3 through 10, giving exact agreement and global fixation.

The probabilistic upper and lower bounds and the expectation estimate are proved in `RESULT.md` for arbitrary lengths; finite enumeration is corroboration rather than an extrapolated proof. The cited source's full preimage language equivalence is a published input, not independently certified by the finite checks. No independent external audit has been performed.
