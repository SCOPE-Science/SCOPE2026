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

# Verification record

The standalone `check.py` was executed against the delivered update map with the Python standard library. It completed 68 checks: exact log-ratio updates at representative positive states and parameters, coordinate order reversals, second-order Taylor residual bounds, and long but finite iterates in all three regimes.

Run: `python3 check.py`.

The proof in `RESULT.md` establishes global extinction, the universal quadratic two-step expansion, the exact ratio increment, all three asymptotic profiles and the existence of the strictly positive minority constant. The executable is a supplementary finite consistency check and does not replace the proof or verify priority. Full text of the closest 2023 original paper remained inaccessible; independent audit has not been performed.
