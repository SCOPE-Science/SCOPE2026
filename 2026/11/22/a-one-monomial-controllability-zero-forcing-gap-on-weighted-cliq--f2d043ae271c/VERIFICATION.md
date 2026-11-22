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
# Verification details

The exact argument in `RESULT.md` supplies the infinite parameter-range proof. From the extracted files, execute:

```sh
python symbolic_certificate.py
python verify.py
```

The first requires SymPy and checks the quotient characteristic polynomial, the two decisive eigenvalue evaluations, and the algebraic identity equating the resonant polynomial with the previously established zero-forcing polynomial. The second uses only the Python standard library, enumerates every labelled vertex subset for eleven small weighted two-clique graphs, and compares a direct prime-field Krylov rank computation with the analytic subset criterion. A successful run reports 3136 comparisons. Prime-field rank is not interpreted as an all-real spectral proof, and no incomplete search is treated as exhaustive beyond its finite stated domain.

The parameter ranges, eigenspace collisions, and eigenvector support at resonance are established by exact symbolic mathematics in the proof. Any numerical conditioning, control energy, and publication priority outside inspected sources remain unverified. No independent mathematical audit is represented.
