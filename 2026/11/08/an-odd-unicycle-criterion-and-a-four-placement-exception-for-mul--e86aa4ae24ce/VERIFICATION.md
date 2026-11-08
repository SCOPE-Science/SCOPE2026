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

The mathematical proof in `RESULT.md` establishes the universal result for all integers \(r\ge3\) and \(k\ge2\). `verify.py` is a standalone exact-arithmetic checker (standard Python only); run `python verify.py` in the same directory. It exhausts the \(\binom{12}{6}=924\) small-case complements with rational ranks and separately computes the graph-theoretic odd-unicyclic condition. It also tests selected larger cases.

Recorded run output:

```
EXHAUSTIVE r=3,k=2: 924 tested; 500 odd-pseudoforests; 496 controllable; 4 excluded.
CONSTRUCTION/SAMPLES r=3,k=3: 80 sampled complements; determinant=5038848.
CONSTRUCTION/SAMPLES r=4,k=2: 80 sampled complements; determinant=995328.
CONSTRUCTION/SAMPLES r=4,k=3: 80 sampled complements; determinant=167365651248.
CONSTRUCTION/SAMPLES r=5,k=2: 80 sampled complements; determinant=679477248.
ALL CHECKS PASSED
```

The exhaustive certificate covers only the finite exceptional graph. No collection of sampled larger graphs is claimed to prove the all-parameter theorem; that assertion rests on the analytic PBH, cut and incidence arguments.
