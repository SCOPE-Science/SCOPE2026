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
# Verification and limits

The asserted result is proved by exact monomial-basis operator calculations and a controlled Riemann-sum limit. The complete monomial eigenvalue list includes all overlaps; no eigenvalues are inferred from a finite truncation. The trace and Hilbert–Schmidt formulas follow from absolutely convergent geometric sums, and the two-degree recovery relies only on strict monotonicity at known damping. The all-\(p\) limit uses uniform exponential tails and a beta-function substitution for every fixed exponent \(p>0\).

## Reproduce finite diagnostics

Run `python checker.py` using a standard Python 3 installation. Expected final output: `CHECKS_OK 438`. The program independently assembles finite input/output Gram diagonals for a weighted monomial partial permutation, compares them against the proposed spectral formula away from section boundaries, verifies exact ideal identities and trace cancellation over multiple degree pairs, and samples beta-limit convergence for four coprime pairs and five positive exponents.

No floating-point diagnostic is used as an infinite-dimensional proof or as a substitute for an exact sum; the script is supplementary. The literature comparison and mathematical correctness have not received independent external validation. The damping parameter must be known for the inverse classification; the original unreduced integer degrees cannot be recovered.
