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

# Reproducible verification

Run `python3 verify.py` with SymPy. The exact checks include the third-iterate factorization and coprimality, degree-preserving irreducible reductions modulo five, the three cycle-sum identities, the two quadratic discriminants, the quartic discriminant and resolvent, and the squarefree factorization of type \((1,1,2)\) at 13. Successful execution prints `PASS: period-three polynomials, cycle-sum fields and squarefree Frobenius certificate`.

The mod-13 factorization is the Frobenius certificate in the proof; the reduction at seven has a multiple root. The computations on their own do not establish the descent interpretation or historical priority.
