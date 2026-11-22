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

# Verification record

The exact proof uses modular cycle sums, elementary prime valuations, Möbius inversion, and Jordan-totient counting. These are mathematical deductions; no external proof certificate is asserted.

To reproduce finite checks, run `python3 checker.py`. It requires only the Python 3 standard library. It exhaustively checks 1,484 primitive-target/modulus/stride cases, independently enumerates 81,090 finite preimage fibers, and enumerates all possible target words for 95 additional distribution comparisons. Its tested cases are finite and do not alone prove the all-parameter formulas.

This document records no independent validation. No separate human or external mathematical audit has been performed.
