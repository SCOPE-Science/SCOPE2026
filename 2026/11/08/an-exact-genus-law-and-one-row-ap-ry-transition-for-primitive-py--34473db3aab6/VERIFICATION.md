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

The exact integer-only reproduction program `verify.py` independently computes Apéry representatives by Dijkstra on each residue modulo \(2mn\) with the three nonmultiplicity generators, then compares the entire array with the theorem's boundary-updated formula. It checks the resulting gap count independently via \(\sum\operatorname{Ap}\) and the simplified closed genus expression. The bundled `verification_output.txt` is a contemporaneous execution record:

```
EXACT_DIJKSTRA_AND_APERY_OK 512 nonzero_corrections 76 max_modulus 2086
```

This finite sample covers coprime \(1\le n,p\le7\), a substantial range of admissible \(m>Q\), and examples on both sides of the boundary; it does not exhaust the infinite parameter domain. The proof in `RESULT.md` establishes the asserted general quantifiers. Source-priority comparison remains provisional, and no independent mathematical audit or certification is claimed.
