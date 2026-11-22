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

# Verification steps

Run `python check.py` with NumPy and SciPy installed. The script integrates the exact closed moment ODE using a constant-coefficient matrix exponential on every rate interval, rather than reusing the kernel-energy minimization calculation. It checks 90 optimized pulse cases at varying budgets, horizons, caps and speeds and 250 randomly allocated feasible capped controls. It additionally evaluates exact-value benchmarks for unit parameters and the positive cap-penalty coefficient. Reported output includes `PASS 90 exact segment propagations and 250 feasible randomized controls`.

The global minimization and uniqueness arguments rely on the rigorous density-floor variational inequality and strict Fourier positive definiteness in RESULT.md. Sampled controls do not exhaust all measurable controls and establish no formal numerical certification of the continuum claim.
