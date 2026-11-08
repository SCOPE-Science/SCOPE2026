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

# Reproduction and verification

The analytic proof uses only the parity of the \(2\)-adic valuation and a complete case distinction on the odd part of each proposed period. It is independent of exhaustive enumeration.

With Python 3, execute `python3 verify.py`. This program constructs \(p(n)\) directly from integer arithmetic, checks every candidate square period \(1\le d\le128\) and start \(0\le a\le2048\), validates the dyadic periods and mandatory location/length restrictions, checks all dyadic square blocks through scale \(13\), and computes shortest repetition-factorization widths for the first ten explicit witnesses using independent finite dynamic programming. All comparisons are exact integer operations. It prints a terminal `VERIFY_OK` line only when all assertions pass.

Verified output: `VERIFY_OK squares_checked= 5518 max_start= 2048 max_period= 128 block_scales= 13`.

The checker is a finite diagnostic. Proof of the general result is supplied by the two valuation-mismatch lemmas, the dyadic-square identity, and the strict endpoint growth inequality. No infinite certificate or independent mathematical audit is asserted. The exact minimum number of factors for arbitrary scales and arbitrary factors remains undetermined.
