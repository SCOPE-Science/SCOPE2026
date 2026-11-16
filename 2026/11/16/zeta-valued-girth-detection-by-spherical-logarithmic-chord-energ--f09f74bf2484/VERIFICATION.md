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

# Reproduction

Run `python3 CHECK.py` in this directory with SymPy and mpmath installed. Its 91 assertions calculate exact shifted-Legendre log-moment coefficients, symbolic zeta-cycle traces for orders 3–5, numerical signs and tails for higher orders, and exact centered-exponential cumulants. These finite tests supplement the full Legendre/trace/cumulant argument in `RESULT.md`; they cannot prove the universal result. The earlier fourth-cycle case is not claimed new. No independent audit or publication-priority certification has been done.
