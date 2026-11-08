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
# Reproducibility checks and limitations

Run `python3 verify.py` with Python 3 and no third-party dependencies. The exact-check program independently constructs the cyclotomic polynomial of order thirty, computes remainders for the first twenty monomials, and tests the explicit positive dual weights needed in the proof. It scans all \(1,048,576\) binary coefficient masks in the twenty-position window by Gray-code remainder updates, with exactly \(32\) divisible masks including the zero polynomial. It also confirms algebraic lifting and exact boundary examples through order \(480\). The run output is:

```
EXACT_DUAL_CERTIFICATE_OK [0, 0, 0, 0, 0, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 0, 0, 0, 0, 0]
BINARY_WINDOW_EXHAUSTIVE_OK masks= 1048576 divisible_including_zero= 32
DYADIC_LIFT_OK a= 1 n= 30 sharp_diameter= 20
DYADIC_LIFT_OK a= 2 n= 60 sharp_diameter= 40
DYADIC_LIFT_OK a= 3 n= 120 sharp_diameter= 80
DYADIC_LIFT_OK a= 4 n= 240 sharp_diameter= 160
DYADIC_LIFT_OK a= 5 n= 480 sharp_diameter= 320
VERIFY_OK exact=true finite_checks_do_not_replace_proof=true
```

The general theorem is proved by the exact finite dual identity followed by algebraic residue-class lifting for **every** power of two. The exhaustive binary checks are only an independent finite corroboration, not a certificate of all possible real coefficients or of the unbounded parameter. No independent audit has yet been performed.
