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

# Verification record

The dependency-free `artifacts/verify_cube.py` checks two odd-prime instances by independently traversing all quotient matrices and central functionals: \((n,p)=(1,3)\) gives \(48\) and \((1,5)\) gives \(480\). Its characteristic-two linear Lie-algebra sanity check at \((n,q)=(2,2)\) gives \(3240\); that latter computation is explicitly **not** a group example. The arithmetic formula separately reconstructs \(552960\) at \((n,p)=(2,3)\). The checker tests the isotropic image condition, cube-zero composition, and complete map rank and does not derive its observed counts by substituting the closed formula.

The infinite statement follows from the proof's bijections: Lagrangian image \(W\); square-zero restriction \(B=A|_W\); surjective extensions from a complementary quotient; central-functionals vanishing on \(\operatorname{im}B\) but not on \(\ker A\). Each step is exact over every odd prime field and every \(n\ge1\). A finite test cannot establish that general result by extrapolation.

The 2019 foundational paper supplies the endomorphism normal form and counts all maps. The full text of the 2026 square-zero weight-one Rota–Baxter census establishes an equivalent square-zero normal form; its covered statements are expressly excluded from novelty. No independent mathematical audit has been performed.
