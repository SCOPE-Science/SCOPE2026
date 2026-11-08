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

To replay the computations, place `verify_unimodal.py` beside this file and run `python3 verify_unimodal.py` with a standard Python 3 installation. Only the Python standard library is required. The script builds the odd strongly unimodal generating-function coefficients modulo four using exact polynomial multiplication, tests the prime-factor criterion independently for every odd positive index through \(5000\), and counts prime/square representations with an exact sieve at three larger heights. Its output at review was:

```text
GF_EXACT_OK odd_n<= 5000 residues= {'odd': 58, 'two': 622, 'zero': 1820} p_fifth_power_case= 2
SIEVE_EXACT X= 10000 count_two= 1138 main_term= 892.98 ratio= 1.274381
SIEVE_EXACT X= 100000 count_two= 8785 main_term= 7143.86 ratio= 1.229728
SIEVE_EXACT X= 1000000 count_two= 70499 main_term= 59532.15 ratio= 1.184217
VERIFY_OK separate_computational_routes=yes modular_arithmetic=exact
```

These tests do not certify the full 2026 pointwise characterization, the prime number theorem, or an infinite asymptotic. The proof of the displayed two-term law is the exact prime-class and multiplier-sum argument in `RESULT.md`; its key analytic premise is the standard prime number theorem in arithmetic progressions. The historical-priority assessment is limited by incomplete access to sections beyond the statement of the motivating theorem. Independent audit has not been performed.
