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

# Reproducibility and proof checks

`verify_coarse_rankone.py` is a standalone Python 3 script using NumPy and SymPy. Run it from any directory with these installed:

```bash
python verify_coarse_rankone.py
```

The script passed **4,216** assertions on the reviewed package content. The tests include exact rational inequalities and tuning identities across many distinct positive kernel/regularization/block parameters; direct construction of the normal matrix and block denominator; floating-point generalized symmetric spectra; exact symbolic spectra in dimensions four and six; checks for a sample of nonaligned rank-one positive corrections; and the explicit inverse-update identity.

The proof does not depend on those finite tests. The main checks are exact decomposition of all vector directions, positivity/strict ordering, the generalized Rayleigh min-max bound for arbitrary positive semidefinite rank-one updates and an exact construction attaining equality. The computed checks neither claim independent validation nor establish any result for arbitrary matrices, incomplete sketches or finite-precision implementations.
