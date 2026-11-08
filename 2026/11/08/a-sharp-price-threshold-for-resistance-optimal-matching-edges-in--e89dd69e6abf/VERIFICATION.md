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

# Verification record

Run the included `verify_crown.py` using Python with SymPy, NumPy, and SciPy installed:

```bash
python3 verify_crown.py
```

Expected output in the tested environment: `VERIFY_OK 972`.

Six symbolic checks include derivative zero at the stated screening price, derivative at equal conductances, rational factorization of the price premium, its large-size series, the boundary index, and its equality with the previously known crown-graph index. Thirty exact checks cover direct rational Laplacian inverses and independent eigenvalue multiplicities, including zero matching conductance. The remaining 936 checks compare normalized budgets, full-matrix spectral sums, sign regimes, and nonsymmetric feasible alternatives on a range of finite sizes and prices.

The proof is in `RESULT.md`. Finite verification is not exhaustive over infinite parameter families; strict convexity, exact diagonalization, and derivative analysis are the essential proofs. Numerical comparisons do not prove originality or global optimality on their own. The uninspected full text of a relevant 2016 involution paper remains a literature limitation.
