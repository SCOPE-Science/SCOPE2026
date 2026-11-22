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

The submitted certificate is the exact algebraic argument in `RESULT.md` together with `verify.py`; it makes no claim of machine certification for all ring sizes. Running `python3 verify.py` from an extracted copy checks every indexed source over \(\mathbb F_5\) through ring length eight, counting output multiplicities independently of the formula. It also checks the full ambient output partition, nonnegative counts and source-incidence identity for lengths two through 201 using exact integers. The determinant identity, character orthogonality, subset inversion and asymptotic comparisons are reconstructed in the paper, independently of experiments.

The checker does not prove anything about alphabet sizes other than five, nor about all possible prior literature. Independent mathematical audit has not been performed.
