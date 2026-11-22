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

The theorem is proved by exact additive-character orthogonality, the annihilator of the product-one multiplicative subgroup, and a strict convexity argument for occupation counts. The eigenpolynomial is valid for every finite field, dimension and nonzero product parameter in its stated scope. Finite computations are checks of definitions and implementation, not substitutes for the quantified proof.

Run `python check.py` with NumPy installed (`requirements.txt`) in the directory containing this package. The checker constructs complex Fourier sampling matrices directly from field addition and multiplication, calculates all Hermitian row-Gram eigenvalues, and independently compares them with the occupancy-polynomial formula. It checks every exact frequency shell and every cumulative frequency band in the tested dimensions: \(q=2\), \(2\le d\le6\); \(q=3\), \(2\le d\le5\); \(q=4\), \(2\le d\le4\); \(q=5\), \(2\le d\le4\); and \(q=7\), \(2\le d\le3\). The extension field \(\mathbb F_4\) is implemented as \(\mathbb F_2[t]/(t^2+t+1)\), with its trace additive character. Six additional tests use a nonidentity product parameter. The script also checks full-rank thresholds, identical shell/band ranks, last-band sharp extrema, and endpoint eigenspace multiplicities.

The observed output on the actual supplied program is:

```
PASS spectral_cases=148 nontrivial_coset_cases=6 maximum_absolute_error=1.9327e-12
```

All checks use numerical eigenvalue comparison with a relative threshold of \(5\times10^{-9}\); no inference from finite testing to all fields is made. Each coefficient and rank formula is established symbolically in `RESULT.md`. A rigorous independent audit has not been performed. The generality does not extend to incomplete observation varieties or arbitrary frequency masks.
