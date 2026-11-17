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

# Exact reproducibility checks

Execute `python verify_cesaro.py` with standard Python 3. No third-party packages or external documents are required.

The script uses `fractions.Fraction` in all asserted equalities. It independently constructs prefix-Cesàro matrices and their powers, compares the lowest-first matrix entry with an independently convolved geometric survival probability, verifies the exact path-step upper bound and strict maximizers, checks generating functions and moments, and tests general signed finite inputs. Expected successful output:

```
EXACT_GEO_CDF_MATRIX_ENTRY_AND_ALL_STEP_EXTREMIZERS_PASSED 450
EXACT_GEOMETRIC_PGF_MEAN_VARIANCE_IDENTITIES_PASSED 18
EXACT_GENERAL_SIGNED_VARIATION_INEQUALITIES_PASSED 5430
ALL_FINITE_CESARO_VARIATION_CHECKS_PASSED
```

All four lines were observed from the included script before packaging. The program verifies finite cases only (dimensions \(2\)–\(10\), powers \(0\)–\(9\) for the main identity and step cases, and selected signed vectors and moments), and is **not** an exhaustive test over all real signals or all dimensions. The proof of the unrestricted exact norm, uniqueness, independent-geometric factorization, and Berry–Esseen cutoff is in `RESULT.md`. Independent mathematical audit has not been performed.
