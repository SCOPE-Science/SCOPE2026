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

Run `python3 verify.py` from the directory containing that standalone file. The verification uses Python's standard library and compares exactly solved stationary probabilities of the full resource/consumer chain with a separately constructed killed-chain renewal resolvent. It validates the flux and richness identities and consecutive-guild monotonicity over six rational rate profiles and all integer guild sizes \(0\le m\le10\). Observed output:

```text
PASS: 66 exact stationary/renewal comparisons; 60 strict monotonicity comparisons
large-guild L_m*sqrt(m)/sqrt(pi/(2*k*u)): [(100, 0.99480264), (400, 0.99872427), (1600, 0.99968423)]
```

The exact tests are finite and cannot establish the universal claim without the analytic proof. The asymptotic numerical comparison tests three guild sizes only. Analytical verification of the full theorem is in RESULT.md. The original ecological paper was read in accessible full HTML form; historical catastrophe literature was partially inaccessible. Independent audit and independent validation are not reported as performed.
