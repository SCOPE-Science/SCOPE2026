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

Run `python3 verify.py` in a standard Python 3 interpreter. It enumerates all \(3^4\) local ternary signatures for each pair relation, directly verifies the expected 16-state local mask distributions, constructs the transfer matrices, and checks the exact integer row-polynomial identities \(e_0p(M)=0\) at degree six (ordered comparable) and seven (incomparable). The resulting recurrence plus the explicitly checked initial values proves the all-parameter formulas; there is no reliance on an unbounded empirical extrapolation.

An independently formulated transitive-closure routine checks all extensions through three old matching blocks and compares actual finite-poset admissibility against the 16-state constraints. Exactly 8,421 and 18,279 local configurations, respectively, were checked. The recorded output `verification_output.txt` ends `EXACT_RECURRENCE_AND_TRANSITIVITY_OK`. Further arithmetic checks test the positive comparability gap through 24 blocks, while its all-index positivity is proved symbolically in `RESULT.md`.

This package carries no independent audit or external formal certification. The priority assessment remains provisional and only the stated parameter geometry is proved.
