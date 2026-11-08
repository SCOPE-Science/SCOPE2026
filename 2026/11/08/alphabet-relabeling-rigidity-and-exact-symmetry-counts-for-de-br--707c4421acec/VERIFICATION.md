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
# Reproducibility

With Python 3 and only its standard library, run `python3 VERIFY.py` and `python3 CROSSCHECK.py` from the directory containing the companion scripts. In the checked package both completed successfully, producing `VERIFY_OK` and `CROSSCHECK_OK` respectively.

`VERIFY.py` directly enumerates and checks all order-two de Bruijn cycles at alphabet sizes 2, 3 and 4; counts all order-one cycles in the stated examples; and constructs correctly relabeling-invariant order-two de Bruijn cycles at alphabet sizes 2, 6 and 10. `CROSSCHECK.py` independently counts every cyclic Euler circuit in the quotient directed labeled multigraph for 1, 2 and 3 symbol pairs, obtaining 1, 72 and 20,736,000; it also checks the voltage criterion on a rectangular integer parameter grid. Both programs operate with exact integer arithmetic.

These are finite independent checks. The all-parameter nonexistence and enumeration claims follow from the mathematical proof, including its graph quotient, monodromy calculation, BEST theorem, and directed matrix-tree calculation. They are not extrapolations from computation. This package contains no independent scientific or historical-priority audit.
