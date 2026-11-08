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

The proof is fully symbolic and valid for every integer \(n\ge2\) over every field with \(2\neq0\). The essential steps are the invertible block-upper-triangular structure matrix, the exact two-solution base system, and the two-state recursive quadratic equation.

From a clean directory containing `verify.py`, run `python3 verify.py`. No external Python libraries are needed. The script checks the actual displayed rational matrices for dimensions \(2\) through \(12\), including the determinant block, every listed idempotent, all recursion equations, and independence of the squared-coordinate vectors. The script then checks the **whole** underlying finite vector space for each of the twelve combinations \(p\in\{3,5,7\}\), \(2\le n\le5\). This is 23,860 tested vectors. The recorded output is in `verification_output.txt`.

Finite exhaustive checks in small dimensions are not a proof in unbounded dimension or arbitrary characteristic. No independent validation or formal proof certification has been performed. The definition of a distinct idempotent ignores nonreduced multiplicities of the idempotent scheme.
