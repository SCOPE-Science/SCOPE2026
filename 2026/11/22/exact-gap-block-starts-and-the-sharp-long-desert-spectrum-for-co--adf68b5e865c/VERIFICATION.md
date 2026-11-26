---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility check

Run `python3 verify.py`. The program computes membership by unbounded-coin reachability until the first streak of \(a=T_n\) represented integers, so it visits every gap. It compares all intervals of length strictly greater than \(n+1\) to the predicted intervals for each \(n\) from 3 to 40, inclusive. This finite test supplements the proof in `RESULT.md`.
