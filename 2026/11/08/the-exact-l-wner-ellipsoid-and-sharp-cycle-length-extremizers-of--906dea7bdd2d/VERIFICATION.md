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

From the directory containing the standalone checker, run `python3 verify_cactus.py` under Python 3. Only the standard library is used.

Observed successful output:

`CACTUS_ROOT_ELLIPSOID_EXACT_CHECKS_PASSED 110 1274 75`

The checker generates 110 deterministically seeded cacti by attaching cycles and bridges, computes their weighted reduced Laplacians with exact rational arithmetic, and verifies that the cofactor determinant equals the product of cycle factors and that every edge has exact weighted effective resistance \(1\). It evaluates 1,274 such edge contacts. It then exhaustively enumerates the feasible cycle-length multisets in 75 prescribed small \((n,c)\) profiles and checks both sharp value/equality formulas.

The proof of arbitrary-order correctness is not an exhaustive computation. Its critical certificates are the weighted matrix-tree factorization, the exact determinant derivatives \(a_e^{\mathsf T}M^{-1}a_e=1\), the identity \(\sum_e w_e=n-1\), and the unrestricted-center trace/AM–GM comparison. The code independently checks the determinant and contact identities for finite examples and the extrema for small orders; it does not verify the universal quantifiers, which rest on the supplied proof. No external or independent mathematical audit was performed.
