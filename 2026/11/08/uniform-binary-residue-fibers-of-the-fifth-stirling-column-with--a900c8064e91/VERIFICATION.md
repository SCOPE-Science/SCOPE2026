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

# Reproducibility and proof boundaries

Run `python3 verify.py` with an ordinary Python 3 interpreter. No packages or external data are required. The verifier independently builds the Stirling recurrence and checks the prediction for all residues modulo powers of two through exponent twelve, at three distinct windows per exponent. It also checks the exact inclusion-exclusion formula, half-index bijections, minimal-period witnesses, and the sharp preperiod counterexample for every tested nontrivial exponent.

Expected output:

```
VERIFY_OK levels=1..12 exact_fiber_counts=PASS both_parity_bijections=PASS shift_checks=49140 fiber_cells=24570 exponential_identity_checks=76 sharp_preperiod_checks=9 lower_columns=PASS
```

These checks are finite. For every exponent, the infinite theorem relies on the algebraic interpolation, exact 2-adic valuation identity for the difference of the two odd-base terms, and compactness of the 2-adic integers, as detailed in `RESULT.md`. Historical completeness and independent validation remain unverified.
