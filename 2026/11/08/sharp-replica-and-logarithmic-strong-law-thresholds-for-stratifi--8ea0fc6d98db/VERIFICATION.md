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

# Verification and limits

Run `python3 verify.py` with a standard Python 3 interpreter. The program is standalone and uses only `math`, `random`, and `fractions`; it runs deterministic, rational and finite-series checks of the first-stratum inversion, median survival identity, variation estimates, and the critical parameter arithmetic. The result of the included run is preserved as `verification_output.txt` and records **889 passing checks**. Re-run the file against the embedded standalone package to reproduce those computations.

For an analytical verification, decompose each quadrature estimate into the first random stratum and a remainder bounded uniformly by the total variation of the integrand away from zero, divided by the number of strata. Invert the exact first-stratum threshold and insert the resulting probability into the exact binomial median survival formula. Apply the power-log series criterion to these two-sided equivalent probabilities. The first and second Borel–Cantelli lemmas give the two almost-sure regimes; the second requires the stipulated independence between complete designs for distinct sample sizes. A separate fixed-sample power-log tail integration yields the moment threshold. These infinite arguments are in `RESULT.md`, not in a numerical certificate.

Boundary checks: \(0<\alpha<1\), \(r\ge1\) integer, real \(\beta\); the critical case \(\alpha=r/(r+1)\) converges strongly exactly when \(\beta>1/(r+1)\), with equality divergent. Independent audit and independent validation have not been performed. Precedence risk remains in any unavailable specialist literature.
