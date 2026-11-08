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
# Reproducibility and proof boundaries

Run `python3 verify.py` (Python 3 standard library) in the directory containing the complete research files. It independently enumerates cyclotomic multiplicities from the defining product, and verifies the predicted negative spectrum and exact denominator across 4,500 parameter triples. It also evaluates the original rational product at \(q=2\) and \(q=3\) and compares with a separately computed cyclotomic-factor product for ten chosen triples.

The observed stdout from local execution was:
```
VERIFY_OK cases=4500 d_levels=1..kn+j polynomial=3473 nonpolynomial=1027
negative_cyclotomic_exponents=exact_all_cases independent_rational_evaluations=20 PASS
counterfamilies n=j=p^a k=p for a>=2: proven symbolically in RESULT.md
```

The full mathematical proof requires no large computation: equations (6)–(9) in RESULT.md establish every cyclotomic exponent for arbitrary positive parameters. The finite tests do not prove that no larger counterexample exists; that conclusion follows from the proof. The source-comparison record is a same-model scholarly assessment, not an independent priority certificate.
