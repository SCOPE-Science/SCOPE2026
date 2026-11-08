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

# Verification instructions

Execute `python3 checker.py` in the folder containing the source. The program uses only the Python standard library. It independently constructs circular trigram histograms for every binary word of length \(1\) through \(17\), enumerates the stated connected balanced-flow parameter families, and checks exact cardinalities against the rational-series coefficient formula. It then compares the coefficient sum with the exact periodic quasipolynomial through length \(84\).

Expected leading lines:

```
PASS: all cyclic words of lengths 1..17 262142
PASS: flow-profile sets and exact counts 1460
PASS: exact quasipolynomial coefficients for lengths 1..84
```

The first comparison exhausts \(262142\) input words, but the bound is finite. The theorem for all positive lengths rests on the Eulerian-support classification and the exact finite rational-function calculation in `RESULT.md`. No independent mathematical audit, formal proof assistant check, or verification for other alphabets is claimed.
