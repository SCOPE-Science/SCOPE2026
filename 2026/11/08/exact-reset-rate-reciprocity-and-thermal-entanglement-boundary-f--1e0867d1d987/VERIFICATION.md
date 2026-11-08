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

The analytical proof is in RESULT.md. With Python 3, NumPy, and SymPy, run `python CHECK.py` in the extracted folder. The checker independently assembles the 16-by-16 two-qubit Liouvillian, solves the stationary matrix at a predetermined finite set of parameter values, and reconstructs Wootters concurrence from the spin-flipped spectrum. It also verifies the two stationary balance identities and optimization factors symbolically and checks a finite-temperature numerical example. A local run produced `PASS: 273 assertions; symbolic balance/optimization, 16x16 direct stationary solve, Wootters spin-flip, thresholds.`

These tests are finite diagnostics; the proof's exact parameter-domain claims rest on the displayed equations and inequalities, not numerical extrapolation. Physical scope excludes detuning, decay and non-Poisson or local individual reset processes. No independent scientific audit was performed.
