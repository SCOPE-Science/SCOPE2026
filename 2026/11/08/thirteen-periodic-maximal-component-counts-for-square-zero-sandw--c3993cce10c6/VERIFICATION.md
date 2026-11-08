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

`verify.py` independently enumerates idempotents and square-zero matrices over finite prime fields, computes the original products, and records the rank of \(NP\). All tested individual \((r,h,t)\)-cells agree with the Gaussian-binomial formula; the exact test transcript is `checks.txt`. Tested cases are all matrices in dimensions one, two, and three over \(\mathbb F_2\), plus dimensions one and two over \(\mathbb F_3\) and dimension two over \(\mathbb F_5\). A separate exact integer scan checks the dimension and top-component formulas through dimension 59. The proof in `RESULT.md`, not the finite program, establishes the unrestricted mathematical quantifiers.

Run `python3 verify.py` using the included files. The executable needs no third-party packages. The calculations do not address scheme nilpotents, lower-dimensional components, conjugacy classes, or historical priority; independent audit has not been performed.
