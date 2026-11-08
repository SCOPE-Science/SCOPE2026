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

# Reproducibility

From the root of this extracted package run:

```sh
python -m pip install -r requirements.txt
python verification/check.py
```

The test script reconstructs each Venn incidence pattern independently. It applies the seven Hall inequalities to a finite symbolic probability sum, checks the exact optimizer polynomial and all three difference factorizations, and separately enumerates survival subsets for degrees \(d=3,4,5,6\). It also exhausts 500 row-unlabeled, pollinator-labeled spanning configurations at \(d=3\). The included script ran with SymPy 1.14.0 and reported 532 targeted consistency cases passing, including four symbolic comparisons, 16 distribution checks, 12 coefficientwise checks, and 500 exhaustive configurations.

The symbolic Hall calculation, together with the exhaustive four-type argument in RESULT.md, addresses every integer \(d\ge3\) and real \(0<q<1\). The finite computations do not themselves prove the infinite-parameter claim. The mathematical review is not an independent audit. Historical priority and ecological external validity remain unverified.
