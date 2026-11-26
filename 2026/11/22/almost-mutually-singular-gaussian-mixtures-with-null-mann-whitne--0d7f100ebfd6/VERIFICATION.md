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

# Verification record

Run `python3 verify.py` with NumPy and SciPy installed. The script integrates the two oriented overlap functionals using the explicit convention \(J(A,B)\) with integration against \(B\), along with the Mann–Whitney functional and total variation at six positive widths. These finite diagnostics do not certify the all-width result or the asymptotic test claim. The proof in `RESULT.md` uses Gaussian comparison identities, a separating event, and the joint-effect CLT at each fixed positive width.
