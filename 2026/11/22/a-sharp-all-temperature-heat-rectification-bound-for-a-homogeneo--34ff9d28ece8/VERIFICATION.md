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

# Verification notes

All heat currents are defined as the stationary Markov expectation of each spin-flip energy change times its flip rate, and the two ends share one reservoir. The proof uses the exact pair-correlation moment closure, rational heat-current identity, strict derivative inequalities, and the separate two-spin baseline. The denominator \(2(1+u^2)-tu\) is positive for \(0\le t,u<1\); no zero denominators are hidden.

Run `python3 verify.py` with Python 3 (standard library only). The test exhaustively solves the full 8-state generator at a specified 10-by-10 set of rational transformed temperatures, and the 4-state dimer generator on the same set. Required console results: `EXACT_THREE_SPIN_CURRENT_OK 100` and `EXACT_TWO_SPIN_BASELINE_OK 100`. Verification over an exact rational finite grid is not a proof of the infinite domain; that proof is in RESULT.md. No independent audit has been performed.
