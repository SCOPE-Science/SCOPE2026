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

# Verification of the parity-sparsity theorem

The file `verify_hyper_odd.py` was executed as standalone Python from this package with exact integers and no dependencies. Successful output:

```
VERIFY_OK bases=2..11 recurrence+state+direct_checked_terms 1121143 generating_function_bases=2..19 binary_residue_test=65536
```

The verifier constructs `h_b(n)` by the restricted-partition recurrence, independently tallies odd values on base-power intervals, derives the three-state matrix recurrence, checks the rational generating function coefficientwise, and compares the binary mod-three criterion. Its direct enumeration covers every complete level up to 175,000 indices for bases 2 through 11, 22 generating-function coefficients in bases 2 through 19, and 65,536 indices in base two. These are finite experiments. The infinite statements are proved algebraically using the exact digit automaton and characteristic-root analysis in RESULT.md; the script does not establish bibliographic novelty or independent mathematical certification.
