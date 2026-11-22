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

The proof of global optimality and the no-unused-sensor assertion is mathematical, not computational. The standalone `verify_ou_budget.py` uses SciPy root-finding and NumPy Gaussian conditioning and separately evaluates the closed-form risk and optimal weights. It also tests the exact \(P=n\) equispacing identity across parameter samples, the strict margin transition, and a finite set of arbitrary competing times/precisions including optimized precision splits at random fixed sites. Run `OPENBLAS_NUM_THREADS=1 python verify_ou_budget.py` with versions compatible with `requirements.txt`.

Expected successful output: `PASS 656 formula and design assertions; 4788 finite competitor comparisons`.

The tests do not establish uniqueness, exhaustive comparison over the continuous design space, or publication priority. The analytical proof uses Gaussian Markov interpolation, the inverse-positivity property of symmetric positive-definite matrices with nonpositive off-diagonals, a strict point-splitting improvement and a unique crossing of a scalar monotone equation. The scientific model excludes adaptive sampling, discrete replication costs, unknown covariance parameters, and other covariance families.
