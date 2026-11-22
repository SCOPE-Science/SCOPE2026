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

The following are exact reproducible checks of the mathematical claim. Run from the directory containing the two accompanying programs:

```
python check_walks.py
python check_matrix.py
```

`check_walks.py` uses only the Python standard library and exhausts all 560 possible three-vertex initial states, counting every closed walk through length eight. `check_matrix.py` requires NumPy and SciPy and independently constructs both base adjacency matrices and their complete three-token Hamiltonians. It checks the strongly regular matrix identity, the four-clique counts 8 and 0, and the exact moments through length eight. Each was executed successfully with the asserted output: common moments through seven and difference 2193408 at eight.

These programs are exact finite arithmetic, not random tests. Their completeness depends on the explicit enumeration of all 560 subsets and all allowed single-edge exchanges. The analytic conclusion follows from the finite exponential Taylor series. This is neither an independent external audit nor a proof concerning arbitrary graphs or higher excitation numbers.
