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

# Exact arithmetic verification

Run both unchanged standard-library Python programs with `certificates.json` in the same directory:

```text
python3 verify.py
python3 verify_independent.py
```

`verify.py` recursively generates the Dyck languages and reconstructs their deletion shadows. It checks the domains and signs of the certificate entries, every primal and dual inequality, the exact objective totals, and the size and shadow disjointness of each codebook. `verify_independent.py` enumerates balanced bit masks and deletes bits using shifts. It independently checks disjointness, the variable domains, primal and dual row sums, and equality of the rational objectives. It prints the objective totals and checks their floors against the corresponding codebook sizes. The two success markers are `EXACT_DYCK_CERTIFICATES_OK` and `INDEPENDENT_DYCK_OK`.

Each layer is exhausted, not sampled; equality of feasible primal and dual values establishes the fractional optimum. The floor bounds match the explicit codebooks. The first strict cardinality-objective gap is \(29/3-9=2/3\) at semilength five. Equality of objectives at smaller semilengths does not prove polyhedral integrality. The fractional-vertex example at semilength four is verified separately by the explicit three deletion shadows and tight pair constraints in `RESULT.md`.
