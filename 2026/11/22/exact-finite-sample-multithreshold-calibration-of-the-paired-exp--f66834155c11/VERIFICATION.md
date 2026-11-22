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

The accompanying `CHECK.py` evaluates nested conditional-uniform prefix sums by exact SymPy polynomial antiderivatives, using rational breakpoints. Assertions replay six nontrivial and baseline rational probabilities, including the \(m=4\) simultaneous \(\{2,3,4\}\) bound \(5221/6144\) at \(c=3/4\). Run `python CHECK.py` with a Python environment providing `sympy`.

The infinite family and exact type-I error are verified by the mathematical induction and probability-integral-transform argument in `RESULT.md`; finite examples do not certify infinite claims independently. The conditional calibration requires prespecified independent pairing and rank selection measurable solely in the pair-sum vector. An independent audit has not been performed.
