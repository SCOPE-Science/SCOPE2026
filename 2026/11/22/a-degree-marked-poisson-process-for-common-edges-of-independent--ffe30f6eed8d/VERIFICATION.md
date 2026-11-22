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

The exact finite calculations are reproducible using `python3 verify_marks.py` with the Python standard library. The script exhaustively enumerates labeled Cayley trees through six vertices for conditional degree-mark distributions and independent pairs of Cayley trees through five vertices for edge-overlap pendant statistics. It compares the calculations to an independently implemented finite weighted-Prüfer distribution with rational arithmetic, and checks the stated finite means. All 156 stated exact rational constraints pass.

The proof of convergence of the full marked point process is analytical: it combines the exact conditional degree generating function, exact forest inclusion probabilities, bounds for overlapping prescribed edges, and convergence of marked factorial moment measures. Finite enumeration alone does not establish any limit theorem. The independently audited status remains unperformed.
