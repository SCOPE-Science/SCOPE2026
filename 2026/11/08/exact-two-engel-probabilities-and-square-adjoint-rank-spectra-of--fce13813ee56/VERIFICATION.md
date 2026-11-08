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

# Verification of star-graph two-Engel rank formulas

Run `python3 verify.py` in the directory containing the standalone checker. No third-party packages or precomputed data are used. Its multiplication tensor is built directly from the bracket presentation in [1]; the subsequent matrix-square calculation does not use the closed expression for the rank. Rank is computed by elimination in the ground field, including a separate explicit model of \(\mathbb F_4\).

The recorded replay checks all \(1,477\) hub/leaf vectors across ten cases: \((q,m)=(2,2),(3,2),(5,2),(4,2),(2,3),(3,3),(4,3),(2,4),(3,4),(5,3)\). For each, it tests \(\operatorname{rank}(\operatorname{ad}_x^2)\) and the entire rank histogram, then compares exact rational Engel probabilities. Because the proof identifies the square-adjoint map as independent of the edge and central coordinates, the checked hub/leaf vectors cover all possible *operator profiles* for those ten finite algebras. Separately, the checker directly evaluates two successive brackets on every one of \(4,096\) pairs over \(\mathbb F_2\) and all \(531,441\) pairs over \(\mathbb F_3\), each with two leaves; exactly \(3,328\) and \(269,001\) pairs satisfy the equation.

The final line of `verify_output.txt` is `VERIFY_OK cases=10 adjoint_square_profiles=1477 extension_field_cases=2 direct_pair_checks=535537`. Finite verification does not prove the uniform theorem over arbitrarily large fields or numbers of leaves; that conclusion is established in `RESULT.md` by a symbolic calculation valid over every field of the stated characteristic.
