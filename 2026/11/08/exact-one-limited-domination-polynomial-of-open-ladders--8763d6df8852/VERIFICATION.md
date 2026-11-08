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

# Reproducibility of the exact algebraic certificate

Run `python3 artifacts/verify.py` using Python 3.10 or newer. The script uses no third-party packages, numerical tolerance, or network access. All coefficients are exact integers.

It constructs a sixteen-state transfer for the original local domination predicate. It verifies the complete monic degree-sixteen polynomial identity for the transfer matrix over integer polynomials, checks the first sixteen residuals of the claimed order-five recurrence, and compares all five numerator coefficients. Since the polynomial matrix identity implies a degree-sixteen recurrence on each residual, sixteen zero initial residuals certify all later residuals by induction. Thus this is a finite exact certificate of the unrestricted rational identity, not a finite extrapolation.

The program also independently enumerates every labelled vertex subset for open ladders of lengths two through eight, computing the capacity and domination conditions directly and matching the entire coefficient array. It tests minimum-set counts at additional finite lengths. These checks are corroborative and not substitutes for the symbolic matrix identity or the general combinatorial minimum-set proof.

Observed output:

```
EXACT_MATRIX_POLYNOMIAL_IDENTITY_OK dimension=16 degree=16
EXACT_ORDER_FIVE_RECURRENCE_OK first_16_residuals_and_annihilator
EXACT_RATIONAL_NUMERATOR_OK degrees_t=0..4
DIRECT_SUBSET_ENUMERATION_OK n=2..8
MINIMUM_PATTERN_AND_COUNTS_OK n=2..79
VERIFY_OK
```

The proof requires neither unprovided datasets nor random experiments. No independent audit has been performed, and priority in all historical publications is not certified.
