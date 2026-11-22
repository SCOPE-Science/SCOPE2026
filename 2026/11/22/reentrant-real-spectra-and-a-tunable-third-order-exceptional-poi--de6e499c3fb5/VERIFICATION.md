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

Run `python verify_symbolic.py` and `python verify_numeric.py` from the directory containing these files. The first requires SymPy and checks exact quartic algebra, the repeated-root parameterization, the coupling turning points, the third-order factorization, and the full Hamiltonian for \(m=3,4,5,6,7\). The second requires NumPy and SciPy and checks the full Hamiltonian for every integer \(3\le m\le16\), including all four real-spectrum phases, the order-three eigenvalue coefficients and a one-dimensional eigenspace at the degeneracy. The two programs independently construct the exact Hamiltonian in different representations.

The mathematical proof is in `RESULT.md`. Numerical tolerances and finite checks are not used as arguments for universal validity. The gain/loss onsite terms, neutral-leaf normalization and dark modes are held fixed according to the stated Hamiltonian; interpretation as a stochastic generator is outside the scope. Independent external audit is not yet performed.
