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

Run `python3 verify.py` from the unpacked artifact directory. It requires only standard-library Python 3.10 or later and prints `VERIFY_OK` on success. The script computes the first-kind Dickson polynomial recursively, exact modular quadratic characters, all \(\mathbb F_q\)-curve points and all fixed complement-classes in the even-subset model of \(2\)-torsion for ten genus-three-through-six examples. It also verifies the order and factor exponents of each stated finite group. Among the field sizes, \(41,83,167,223\) test four distinct \(2\)-adic valuations. All ten completed successfully in the reviewed package.

**Scope of verification:** Explicit finite-field examples do not certify the claim for arbitrary prime powers or genera. The general result follows from the exact Frobenius/Tate-module, Weierstrass-permutation and Hensel arguments in RESULT.md. The published maximality theorem is a stated hypothesis from the cited primary literature. The group structure is not a claim of independent specialist validation; independent audit status is not performed.
