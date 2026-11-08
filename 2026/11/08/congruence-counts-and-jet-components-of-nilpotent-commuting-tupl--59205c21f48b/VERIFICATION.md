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

# Reproducibility and verified scope

Run the three self-contained programs using Python 3 from the containing directory:

```
python3 verify_arithmetic.py
python3 verify_gf9.py
python3 verify_geometry.py
```

`verify_arithmetic.py` builds truncated polynomials directly, selects traceless square-zero matrices, checks all literal ring commutators, counts compatible ordered pairs and triples, and compares with the claimed full formula. It covers prime fields of orders three and five and truncation lengths up to three in the tested cases. `verify_gf9.py` independently implements \(\mathbb F_9\) using a quadratic irreducible polynomial and checks pair and triple counts. `verify_geometry.py` performs finite-field Gaussian elimination on the full Jacobian of all defining quadrics at every field-valued solution in the specified cases; every nonzero solution has the expected Jacobian rank, confirming local tangent dimension.

All reported checks passed; see `verification_output.txt` for exact executed test output. These are finite tests and do not establish the all-length theorem; the valuation splitting, smooth-lifting proof, and irreducible-component induction supply the unrestricted argument. No tests are claimed for characteristic two, arbitrary nilpotent matrices over nonreduced rings, or mixed-characteristic rings. No independent audit was performed.
