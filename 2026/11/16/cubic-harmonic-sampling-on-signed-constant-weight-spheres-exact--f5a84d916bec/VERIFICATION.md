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

# Reproducibility and verification

Execute `python3 artifacts/check_cubic.py` and `python3 artifacts/check_enumeration.py` using a Python 3 interpreter, with NumPy additionally installed for the second program. The first computes exact rational sphere/orbit Gram entries for all 33 pairs of integers `3 <= d <= 8, 1 <= k <= d`; it verifies all cross terms, three sector ratios, dimensions and trace. The second independently enumerates orbit points for eight representative cases, computes the evaluation Gram matrix directly, and checks the `d=7,k=3` blind zonal sector. Expected completion lines are `PASS: exact all-entry Gram identities, trace, and sector counts on 33 (d,k) pairs` and `ALL_DIRECT_ENUMERATION_CHECKS_PASS`.

These tests were performed and also replayed from the extracted packaged copies. They corroborate finite instances only. The full universal proof appears in RESULT.md, which explains the invariant decomposition and the exact monomial moments. An independent mathematical audit has not been performed. Historical priority remains provisional.
