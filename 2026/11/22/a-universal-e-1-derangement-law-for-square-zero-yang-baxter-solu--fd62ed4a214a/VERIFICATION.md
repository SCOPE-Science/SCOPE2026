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

# Reproducibility

Run `python verification.py` in the directory containing the extracted files. The program uses only the Python standard library and exact arithmetic. It enumerates all permutations of the underlying 4-, 8- and 9-element sets, checks the complete defining preservation equation, calculates group orders, and compares the fixed-point histograms with coefficients extracted from the asserted generating function. The successful output terminates with `YB_SQUARE_ZERO_AUTOMORPHISMS_VERIFIED`.

Actual checks: \((p,n,r)=(2,2,1)\) gives 4 automorphisms and 1 derangement; \((2,3,1)\) gives 64 automorphisms and 25 derangements; \((3,2,1)\) gives 54 automorphisms and 8 derangements. The exact histograms are in `RESULT.md`. Finite tests are not proof for arbitrary dimension; the algebraic normal-form and probability-generating-function arguments provide that proof. No independent audit is claimed.
