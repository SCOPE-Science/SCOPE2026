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

Execute `python verify_path_angles.py` using Python with SymPy and NumPy. The checker runs two independently constructed Gram matrices: (1) the explicit signed Dirichlet inverse corrected for the affine sum constraint and (2) the inverse metric of vertex differences. Exact agreement for dimensions indexed \(3\le m\le15\) tests all 559 unordered ridge pairs, parity signs and the right-angle endpoint exception. The numerical asymptotic test evaluates the actual centered facet-normal cosines for \(m=650\) and compares five Green-kernel CDF thresholds and three actual cosine absolute-CDF thresholds. It is corroboration only.

Expected output from package replay:

```
EXACT_AFFINE_GRAM_PASS dimensions=3..15 ridge_pairs=559
LIMIT_DISTRIBUTION_CORROBORATION_PASS m=650 max_unsigned_CDF_gap=0.00267
```

The all-dimensional result and the limiting distribution instead follow from the exact tridiagonal inverse and parity-resolved Riemann sums in RESULT.md. Reproduction does not provide independent mathematical review or a certification of historical novelty.
