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

# Verification and reproducibility

Run `python3 verify_cycle.py` using Python 3 and its standard library. The program checks all bounded-composition representatives for the seven listed odd-cycle parameter pairs, verifies the exact inverse-matrix inequalities, checks coefficient symmetry and lattice volume, and directly counts lattice points in thirty-two dilated simplices for agreement with the derived Ehrhart coefficients. The verified run produced `PASS exact checks: 3686 interior candidates plus 32 independent lattice-point dilations`.

Proof-level checks are the determinant identity, the alternating-sum extreme values, exact exhaustion by index, compatibility of the affine grading and uniqueness of simplex coefficients. The computer tests concern finitely many cases only. The first-failure statement requires uniform integral weight \(2\le w\le n-2\); other cases are outside that assertion. Independent audit has not been performed.
