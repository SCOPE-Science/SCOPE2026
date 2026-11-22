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

# Reproducible verification

Run `python verify.py` with Python 3.10+ and SymPy. The script computes the symbolic derivative of the exact expected absorption time, verifies the quartic optimization identity, confirms the leading and first finite-size asymptotic coefficients, and constructs full labelled graph generators without using the lumped system to derive their answers.

For each of six core sizes, it checks four different internal-core edge structures and three rational reset rates. It additionally checks the nonzero Laplace transform from independently built full generators for three core sizes, four internal graphs, and two rational rates. In total, 96 exact rational comparisons passed, alongside the general symbolic identities. The source itself does not depend on external data or other files.

The unbounded-size proof is the strong lumpability plus polynomial sign argument in `RESULT.md`; finite exact tests do not certify statements over all graph sizes by themselves. No independent external audit has been performed.
