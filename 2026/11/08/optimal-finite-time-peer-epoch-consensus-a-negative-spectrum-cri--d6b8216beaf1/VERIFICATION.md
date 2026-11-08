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

## Executed checks

Executed the standalone `VERIFY.py` using Python 3 with NumPy and NetworkX. The checker reported:

- `PASS: 15 connected regular graph types, 360 spectral/filter comparisons`
- `PASS: weighted complete three-node example has two distinct negative eigenvalues [-0.48027756377319947, -0.11972243622680057, 1.0000000000000002]`
- `PASS: two FJ one-inner-step epochs yield exact rank-one averaging (floating) [0.675548981132308, 0.8930784698480841]`
- `PASS: exact rational three-node rank-one product ('[Fraction(-1, 12), Fraction(-1, 6)]', '[Fraction(12, 13), Fraction(6, 7)]')`

The code checks the matrix polynomial independently of its rational eigenvalue expression; it also checks the spectrum sign of connected simple regular noncomplete versus complete graphs. Exact rational arithmetic proves the indicated finite three-node instance without numerical tolerances.

## Proof checks and limitations

The finite checks do not establish universal quantification. The proof requires a reversible similarity transform, the exact scalar peer-filter identity, the sign and uniqueness of odd-horizon zeros, and principal-submatrix interlacing. These steps are explicitly proved in `RESULT.md`. No formal machine proof or external mathematical validation is claimed. Any conclusion about exact finite-time reachability is specific to fixed-network shared-susceptibility peer epochs, not more general social networks.
