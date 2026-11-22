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

All dimensions \(d\ge2\) are covered by the analytic proof in RESULT.md. For reproducible supplementary tests run `python3 verify_hypercube.py` with a standard CPython interpreter; only Python's standard library is used.

The checker constructs the grounded Dirichlet Laplacian for the complement of \(\{0,e_1,\ldots,e_d\}\) in \(Q_d\), computes every column of the harmonic extension in exact rational arithmetic, and forms its full Gram matrix for each dimension \(d=2,3,4,5,6\). It separately solves the permutation-symmetry recurrence, evaluates the closed binomial formula, compares all Gram entries and checks the harmonic equation for every interior vertex in each tested dimension. The verified contrast eigenvalues are respectively \(1,10/9,58/49,824/675,3548/2883\); the largest eigenvalue is exactly \((2^d-1)/d\). Small-instance replay is not a proof of the all-dimensional formula; the Walsh-resolvent proof supplies that. Numerical floating tolerances and external proof systems are not required.

The supplied data do not include tests of other graph embeddings, alternate edge weights, or incomplete host filter banks. The discrete-wavelet result uses only the stated Parseval identity of the full host map.
