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

The finite census is reproducible with `python verify_compare.py` using only Python's standard library. It constructs each surjection indicator by visiting all inputs, computes the full tensor-product character transform using exact Gaussian integers, compares every coefficient against a declared histogram and checks Parseval, fourth moments and the first-divergence comparison for lengths four through six. Independently written integer transform tests `check_klein.py` and `check_cyclic.py` verify all frequencies through length eight under their respective group structures. Both output complete successful check records when run. There is no all-length fourth-moment comparison and no independent audit.
