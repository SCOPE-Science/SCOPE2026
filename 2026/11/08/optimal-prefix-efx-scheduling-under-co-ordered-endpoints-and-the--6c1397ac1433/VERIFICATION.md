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

# Reproducibility and verification boundaries

Run `python CHECK.py` with Python 3 and no external packages in the folder containing the seven delivered files. The exact-rational test uses offline exhaustive subset enumeration for co-ordered interval examples and fair-load exhaustive search for the minimal thin-nesting obstruction. Its observed output was `PASS: 14965 finite instances (greedy, fairness and obstruction).`

The universal claims are verified by the written proof in `RESULT.md`: ordered-subsequence capacity criterion, an earliest-acceptance index dominance induction, cyclic load balancing, a forced machine-load vector for the nested family, and a capacity/pigeonhole lower bound for all inputs with at most \(m+1\) jobs. All start/end inequalities use half-open intervals and permit jobs ending exactly as others start.

The verifier tests finitely many rational instances; it cannot prove the claims for arbitrary real endpoints or arbitrary machine counts. No external audit or separate validation is asserted.
