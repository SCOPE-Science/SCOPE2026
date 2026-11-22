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

Run `python verify.py` with Python 3 and SymPy. The checker separately derives stationary moment recurrences from the two-state generator and verifies the cumulants, angular identity, global inverse equations and a strict two-versus-three-moment ambiguity example. The current package-specific run produced `PASS: 197 exact symbolic/rational checks`.

These finite checks do not prove global injectivity or the sharp feasible region; the analytic derivations in `RESULT.md` do so. The entropy-production identification uses an explicitly stated even-orientation convention. No independently performed scientific audit is claimed.
