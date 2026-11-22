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

Run `python3 VERIFY.py` using only the Python 3 standard library. The checker builds every specified finite bouquet and enumerates all colour assignments in its bounded test cases, compares observed modal partition refinement with the generator criterion, and directly computes finite Boolean modal subalgebras in selected small cases. A successful execution prints:

```
VERIFY_OK cases=116 exhaustive_labelings=281347 generating_labelings=63202 direct_algebra_checks=5641
```

The proof establishes unrestricted statements for all positive component sizes and branch counts. The finite checks do not certify all sizes or prove originality. Independent audit has not been performed.
