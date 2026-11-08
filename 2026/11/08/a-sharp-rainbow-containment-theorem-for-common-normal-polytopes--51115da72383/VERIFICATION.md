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

# Reproducibility and limits

Run `python verify.py` with Python 3.9 or newer and no third-party dependencies. The script independently maximizes assignments on finite integer matrices; tests the cycle-lemma consequence; constructs random interval/box families; checks the chosen rainbow inequalities against the complete winning color; and exhaustively tests the sharpness example in dimensions one through three. The recorded pass output is `PASS: 10323 deterministic checks (including all reduced-color tuples).`

The proof of the universal result is the finite maximum-assignment exchange argument given in RESULT.md, not an extrapolation from the computational checks. The certificate is self-reviewed; independent mathematical audit has not been performed. Historical priority of the strengthened selection form remains provisional.
