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

# Reproducible checks

Run `python verify.py` with a standard Python 3 interpreter in the directory containing this document and the verifier. No internet access or third-party dependencies are required. The verifier is standalone and does not import the proof conditions into its allocation-enumeration routine.

The executed checks passed: all complete allocations were examined independently on each of 791 positive integer multiset valuation profiles (good counts one through five; each singleton value from 1 to 7); 600 seeded positive rational-valued profiles were additionally compared; both explicit gain/loss witnesses were confirmed; exact `fractions.Fraction` arithmetic reproduced both joint probability tables from the ordered-spacing Laplace identities.

The mathematical proof covers all strictly positive real-valued profiles with four or five goods. The finite-profile checks do not certify arbitrary real inputs, and the probability computations depend on the stated independent continuous distribution assumptions. No claim about larger instances or arbitrary random laws is tested here.
