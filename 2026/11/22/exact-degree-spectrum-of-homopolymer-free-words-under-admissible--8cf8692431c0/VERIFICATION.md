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

# Reproducibility and limits

Run `python3 checker.py` with standard Python 3. The script independently constructs every proper source word and tests its legal adjacent swaps, computes the profile-based distribution, and uses a separate polynomial transfer dynamic program. It tests \(q=3\) for lengths 3–9, \(q=4\) for lengths 3–7 and \(q=5\) for lengths 3–6, checking support, isolated and top multiplicities, and totals. Its terminal marker is `ALL_CHECKS_PASSED`.

The all-length claim rests on the explicit second-neighbor proof and symbolic transfer reduction in RESULT.md. Finite enumeration cannot certify infinitely many parameter values. The exact missing penultimate degree follows from a proved double-loss argument, not a computational absence. This package has undergone self-review only; independent audit has not been performed.
