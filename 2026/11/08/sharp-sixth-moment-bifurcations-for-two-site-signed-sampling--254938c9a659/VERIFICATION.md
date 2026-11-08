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

# Verification of the reported sixth-moment theorem

Run `python3 verify_sparse_pairs.py` with a standard Python interpreter. The script is standalone and uses only `fractions`, `itertools` and `random` from the standard library. It checks the sixth- and second-moment formulas by exact enumeration over all pairs and all four independent sign choices for 420 seeded rational coefficient vectors. It also checks the exact lower and upper equality witnesses for dimensions 2 through 100, two-coordinate algebraic identities on thousands of rational instances, and the Euclidean-distance arithmetic formulas.

Expected terminal line: `ALL_SPARSE_PAIR_SIXTH_MOMENT_CHECKS_PASSED`. Exact output from this package was:

```
INDEPENDENT_EXACT_SIGN_AND_PAIR_ENUMERATION_OK 420
EXACT_ALL_ENDPOINT_CONFIGURATIONS_OK 99
EXACT_TWO_COORDINATE_VARIATION_IDENTITY_OK
EXACT_EUCLIDEAN_DISTORTION_FORMULAS_OK
ALL_SPARSE_PAIR_SIXTH_MOMENT_CHECKS_PASSED
```

The universal claims are not inferred from finite tests. The proof in `RESULT.md` uses an exact algebraic variation identity, a global support argument and symmetry averaging for arbitrary integer dimension. No formal external audit, computational certification of the infinite argument or independently performed mathematical validation is asserted.
