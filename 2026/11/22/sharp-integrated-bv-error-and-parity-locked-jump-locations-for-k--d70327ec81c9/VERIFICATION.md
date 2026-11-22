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

# Verification

The exact formula follows from the signed-jump representation and two binomial identities, not numerical extrapolation. Run `python3 check_kantorovich.py` with Python 3. The checker tests all degreewise single-cell maxima and their parity structure for degrees zero through 28, exact rational kernel marginals and the derivative identity at rational inputs, and (when NumPy/SciPy are installed) numerical signed multijump inequalities for degrees zero through twenty. Exact rational arithmetic guarantees only the tested finite cases. Numerical integration approximates the multijump error. The asymptotic limit is proved via Stirling's formula in RESULT.md. There is no external mathematical or independent certification.
