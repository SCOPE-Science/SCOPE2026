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

The complete analytical argument is in `RESULT.md`. Reproduce the bounded diagnostics with:

```bash
python verify.py
```

Using the standard-library verifier supplied with this result, the run reported 2,298 passing checks. These comprised coefficient-level polynomial identities for 39 backbone sizes, exact rational finite-current comparisons, exhaustive short-decoration tests for backbone lengths 3 through 22 and all interior particle numbers, and direct stationary-generator balance on selected small decorated rings. The program also reports bisection approximations to five threshold values, including 1.808911890654 for ring length 4.

The proof, not the finite test range or numerical root estimates, supplies the universal uniqueness, monotonicity, asymptotic, and minimality statements. No independent scientific, authorship, or publication-priority validation was performed. Relevant pre-existing invariant measures and currents were used as stated in the references; finite checks do not independently establish literature novelty.
