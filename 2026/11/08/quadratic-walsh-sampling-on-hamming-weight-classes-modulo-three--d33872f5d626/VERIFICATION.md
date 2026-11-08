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

# Reproducibility and boundaries

The standalone source `verify.py` uses only the Python standard library. Running `python3 verify.py` recomputes the exact restriction Gram matrices on the full selected point sets in all 18 cases given by \(4\le n\le9\) and the three residues. It compares every Gram entry with an independently computed binomial Fourier moment, checks the trivial and standard invariant actions, verifies the pair-harmonic eigenvalue, and compares actual modular ranks with the predicted rank formula.

Expected successful output:

`QUADRATIC_MOD3_WALSH_VERIFY_PASS exact_spectrum_blocks_and_modular_rank 18`

Modular elimination cannot by itself certify every rational rank, and 18 cases cannot establish an infinite theorem; both are finite corroboration of the algebraic proof in `RESULT.md`. For arbitrary \(n\), the exact spectrum is obtained by evaluating the displayed moments and diagonalizing the two small real symmetric blocks. The asymptotic squared condition ratio concerns positive definite matrices; it is not defined when a sampling mask has a null direction. No independent external audit has been performed.
