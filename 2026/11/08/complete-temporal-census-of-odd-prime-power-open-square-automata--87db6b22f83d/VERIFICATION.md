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

# Reproducibility and limits

Run `python verify_grid.py` with Python 3 and NumPy, and run `python verify_lefschetz.py` and `python verify_determinant.py` using the Python 3 standard library. `grid_output.txt`, `lefschetz_output.txt`, and `determinant_output.txt` capture the actual outputs of all three standalone scripts.

The direct matrix checker tests the path polynomial, the nullities of powers of the full open-square adjacency operator, and the dimensions of all fixed subspaces for exponents 1 to 24, on grid sizes \(2,4,6,8\) in their corresponding characteristics. It also enumerates every one of the \(81\) ternary states of the \(2\times2\) grid. The third script checks 171 exact binomial Toeplitz determinant identities and 64 unit-valuation cases. The separate homogeneous-algebra checker verifies power ranks for \(m=1,2,3,4,12,13,24\), including cases where the characteristic is smaller than the block size.

These computations do not exhaust infinitely many odd primes, exponents, field extensions or configurations. The proof in `RESULT.md` supplies the general argument by Frobenius, exact determinant valuations and Fitting decomposition. No machine execution is a substitute for checking those algebraic steps.
