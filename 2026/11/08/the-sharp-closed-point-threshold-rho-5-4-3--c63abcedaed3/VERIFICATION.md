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

# Verification and reproducibility

Run `python3 verify_quadratic.py` and `python3 verify_extensions.py` using standard-library Python 3 from the directory containing the scripts. These programs are standalone and contain no external data dependencies.

The first enumerates the 25 values in \(\mathbb F_5[w]/(w^2-2)\), independently computes the norm/character table, and checks \(N_1=N_2=8\), so \(B_2=0\). The second implements polynomial-basis fields in extension degrees one through four, verifies field multiplicative identities, computes \((N_1,N_2,N_3,N_4)=(8,8,152,592)\), and checks the complete zeta numerator and its listed factorization.

The all-curve assertion \(B_r(X)>0\) for every integer \(r\ge3\) follows from exact symbolic inequalities of the Weil bounds, explained in `RESULT.md`. No finite enumeration purports to prove the universal quantifier. The characteristic-five squarefreeness calculation is algebraic and the finite-field witness count is exhaustive.

No machine-readable evidence of an independent mathematical audit is claimed. Historical-priority uncertainty is disclosed in the result and review.
