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

The command `python3 verify.py` checks exact rational sine moments and performs independent high-accuracy numerical Poincaré-return tests on the family \((N,m,n,a_1)=(2,2,3,1)\). The script also checks scaling of the critical return-map displacement and agreement of rescaled iterates with the scalar slow equation. The parameter values and tolerances are stated inside the script.

These are finite computations. They cannot prove the analytic return-map expansion, the global uniqueness statement, or the asymptotic limits. The latter are supplied by the proof in `RESULT.md` and, for the cited global count, by Chen–Lu–Wang–Zhang (2026). The literature comparison is provisional with the stated residual-priority risk.
