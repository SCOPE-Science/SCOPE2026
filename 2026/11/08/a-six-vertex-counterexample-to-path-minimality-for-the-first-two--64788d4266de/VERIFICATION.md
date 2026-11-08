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

# Exact reproducibility

Run `python3 verify.py` with Python 3 and no additional packages.

The script evaluates both \(P_6\) and the arm-length-\(2,2,1\) tree by all \(720\) vertex orders, independently computes the same distributions by partial-colouring dynamic programming, and asserts the displayed exact integer counts. It then enumerates all labelled trees of orders one to five through Prüfer sequences and verifies the path bound for every one. The full script was executed and completed successfully.

The six-vertex check gives expected values \(397/72\) and \(131/24\), with strict gap \(1/18\). The smaller-order minima are respectively \(1\), \(2\), \(3\), \(15/4\), and \(14/3\). These are exhaustive finite results, not extrapolations beyond six vertices.

No stochastic simulation, unexecuted computational dependency, or third-party certificate is required. Independent validation remains unperformed.
