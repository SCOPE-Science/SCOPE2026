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

# Verification notes

The symbolic proof uses weighted matrix-tree differentiation, a directly checked inverse of the cyclic tridiagonal reduced Laplacian, and elementary finite geometric sums for two Fourier-transformed square kernels. In the latter sums the \(k=0\) mode has an extra geometric-series term, which is retained explicitly. The resulting two-by-two symbols yield all eigenvalues, including the forced zero and the positive anti-diagonal constant mode. Positivity and the exact weakest mode are proved for every \(n\ge3\); the cubic limit follows by Taylor expansion.

`checker.py` independently enumerates all \(n\)-element edge subsets of the wheel and retains precisely acyclic subsets, thereby constructing all spanning trees for \(n=3,4,5,6,7,8,9,10\). It builds each Walsh character vector directly, sums its outer products in integers, and compares the full computed Gram eigenvalue multiset to the theoretical formulas. The respective tree counts are \(16,45,121,320,841,2205,5776,15125\). All eight computed spectra agree to a maximum absolute error below \(3\times10^{-15}\) in double precision; integer trace/linear-dependence checks and direct tree counts agree. The checker requires Python 3 and NumPy; run `python checker.py` in a directory containing this file.

These tests are not an exhaustive check for all graph sizes and are not independent mathematical certification. The exact proof, rather than numerical extrapolation, establishes the universal statement.
