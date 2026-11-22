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

# Reproduction and limits

In the directory containing `verify.py`, run:

```bash
python3 verify.py
```

A successful execution prints `VERIFY_OK hook_inner_products=240 direct_cases=104 fixed_simplices_checked=11570`.

The independent finite tests enumerate all cycle types for \(3\le n\le6\), construct fixed strict inclusion chains directly, and compare their dimensionwise face counts with a separate cycle-assignment formula. For \(3\le n\le10\), they compute exact rational character inner products with every hook character using the cycle-type centralizer denominator, comparing with the claimed multiplicity spectrum. They also check the invariant multiplicities and identity traces against the nonequivariant rank recurrence. No external mathematical software or unshipped data files are needed; only standard Python is used.

This computation does not establish the universal statement. The universal proof uses the earlier established filtered-poset wedge theorem and elementary identities for fixed chains, Young-subgroup invariants and binomial coefficients. The result gives rational representations, not integral module isomorphisms. Independent audit is not yet performed.
