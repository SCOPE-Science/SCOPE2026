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

The script `scripts/check.py` uses integer finite-field arithmetic for primes \(5\) and \(7\), constructs the evaluation matrix of the five monomials and exhaustively enumerates reduced-row-echelon representations of all subspaces of \(\mathbb F_q^5\). It computes the number of torus points simultaneously annihilated by each subspace and records both the maximum and the number achieving it. The recorded outputs are in `checks/output.txt`; the script asserts every theoretical value and prints `ALL_CHECKS_PASSED` for each field.

The general proof does not rely on finite-field enumeration. Its decisive ingredients are the ruling-fiber decomposition, uniqueness of two affine-line intersections, and the degree-three determinant obstruction for dimension-three subspaces when \(q-1\ge4\). The finite verifications do not cover extension fields of nonprime order; the algebraic proof does. No independent external audit has been performed.
