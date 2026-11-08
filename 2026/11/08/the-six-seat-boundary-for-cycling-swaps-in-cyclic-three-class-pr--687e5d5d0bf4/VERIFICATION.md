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

Run `python3 verify.py` in the same directory. This executes an exhaustive finite construction of all \(3^n\) length-\(n\) type words for each \(n\in\{3,4,5,6\}\), every unordered pair of distinct seats, exact integer utility comparisons, a Tarjan SCC decomposition, symmetry-orbit checks and the explicit six-step strict cycle.

Expected totals: \(n=3\): 27 states / 0 directed edges / 0 nontrivial SCCs; \(n=4\): 81 / 24 / 0; \(n=5\): 243 / 180 / 0; \(n=6\): 729 / 882 / 6 SCCs of six states each. The check confirms precisely 36 states in the one symmetry orbit and the separate welfare-maximal stable word.

All assertions passed in the present run. The audit is a self-review of a finite exact certificate; no external independent audit was performed. The certificate does not search \(n>6\) or establish global novelty.
