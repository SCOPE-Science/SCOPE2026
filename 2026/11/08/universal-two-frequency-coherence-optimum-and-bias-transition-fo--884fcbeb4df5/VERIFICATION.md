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

# Reproducibility and scope

The proof establishes the exact product bound for all odd integer bases, all positive finite depths, and all strictly positive level-dependent digit probabilities. Its decisive steps are: reduction to independently minimized root-of-unity factors, uniqueness from the largest modulus, direct diagonalization of a two-by-two Gram matrix, and convergence of infinite products whose logarithms are summable.

Run `python CHECK.py` using only Python's standard library. The checker enumerates all nonzero frequency residues in several odd moduli, evaluates the Fourier transform independently from the finitely supported probability measure and checks its predicted minimizer set; it also checks the two-character eigenvalue and the factor formula. Floating-point testing is finite evidence only, not the universal proof.

Independent validation has not been performed. The theorem does not cover zero-one deterministic digit weights, even bases, noninteger frequency differences, general larger frame families, or reconstruction robustness.
