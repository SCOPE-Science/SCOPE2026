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

# Verification

Run `python3 checker.py` with Python 3.9 or later; no third-party dependencies are required. The checker carries out exact rational exhaustive binary-cut checks on all widths for primes \(3,5,7,11,13\), exact rational multilevel-input tests, and finite checks of arc witnesses. The results are independent numerical corroboration, not an infinite certification. The all-prime assertion relies on the complete proof in RESULT.md, including a published prime-cyclic majorization theorem.

Expected terminal markers: `EXACT_ALL_PRIME_BINARY_CUTS_PASS 119628`, `EXACT_RATIONAL_MULTILEVEL_CHECKS_PASS 6240`, `ARC_FORMULAS_AND_BALANCED_EXTREMIZERS_PASS`, `ALL_PRIME_BOXCAR_GINI_CHECKS_PASS`.
