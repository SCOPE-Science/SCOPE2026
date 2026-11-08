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

# Reproduction and proof checks

Run `python3 verify_windows.py` with Python 3.8+ and no external packages. The observed result is:

`WINDOW_RANK_AND_TRACE_PASS 136 n_r_pairs 272 rank_classes n_max 16 polynomial_n_max 14`

The script builds each finite concept family directly as bitmasks, computes Littlestone depth through the defining maximum/minimum recursion over point queries, and enumerates all supports of sizes one, two and three for all 1 ≤ r ≤ n ≤ 14. Online depth was also checked for 1 ≤ r ≤ n ≤ 16, both with and without the empty concept. The checker file included here is the executed code.

The formal proof depends on (i) at most r distinct windows passing any positive point query, (ii) consecutive blocks of at most r starting positions supporting prefix tests, (iii) the recursive null-completed construction, and (iv) exact one-, two- and three-point trace analysis. These steps are given in RESULT.md, and remain the foundation for the unrestricted theorem.

Finite tests do not establish historical originality, independent audit, or correctness beyond the verified parameter ranges by enumeration alone.
