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

Run `python3 verify.py` with the standard library. The checker computes exact updates by inversion and explicit products, and tests the four spectral entry types at the sampled positive steps and integer powers. It checks the exact hub threshold at \(m=2,k=1,h=2\) and at \(m=8,k=3,h=2/3\). It brackets the leaf threshold \(D_{2,1}=2+2\sqrt2\) with exact rational sign tests at steps 4 and 5. It also checks a step where only the hub diagonal is negative, the later simultaneous negativity of the diagonals at \(m=2,k=1,h=6\), and the four-vertex path counterexample. These finite checks supplement the analytic monotonicity and root arguments in `RESULT.md`.
