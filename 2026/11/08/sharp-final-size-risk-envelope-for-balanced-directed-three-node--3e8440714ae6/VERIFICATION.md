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
The formula follows from a three-state competing-risk argument and its two tail probabilities, not a finite enumeration assumed to prove an infinite-parameter theorem. The standalone `CHECKER.py` independently constructs the exact CTMC recurrence over all infection/recovery subsets using infectious and recovered bitmasks; it confirms the global rational probability identity by symbolic reduction. It then checks the closed-form gap, derivative, unique positive maximizing ratio, maximal value, and exact rational endpoint examples. The proof itself establishes all \(b>0\) and \(0\le p\le1\), including zero-rate boundary arcs. `CHECKER.py` requires Python 3 with SymPy and can be executed as `python3 CHECKER.py`.

The model does not cover repeated outbreaks, heterogeneous individual recovery distributions, dynamic contacts, or populations larger than three. The 2016 unweighted undirected triangle result is a known endpoint. Complete independent scientific auditing remains unperformed.
