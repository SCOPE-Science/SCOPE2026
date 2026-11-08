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

# Direct finite-field verification

Run `python3 verify.py` with the standard library. For each \(q\in\{2,3,4,5,7\}\), enumerate all \(q^6\) upper-triangular matrices. Form the three linear commutator equations on the five-dimensional quotient by scalar matrices, reduce their coefficient rows to a unique canonical row echelon basis, and count distinct row spaces. Matching row spaces is equivalent to equal kernels and thus equal centralizer subalgebras.

Observed output:

```
q=2: 31 centralizers; commutator-rank census {0: 1, 1: 1, 2: 16, 3: 13}
q=3: 91 centralizers; commutator-rank census {0: 1, 1: 1, 2: 33, 3: 56}
q=4: 173 centralizers; commutator-rank census {0: 1, 1: 1, 2: 56, 3: 115}
q=5: 291 centralizers; commutator-rank census {0: 1, 1: 1, 2: 85, 3: 204}
q=7: 659 centralizers; commutator-rank census {0: 1, 1: 1, 2: 161, 3: 496}
VERIFY_OK
```

The arithmetic for \(\mathbb F_4\) explicitly uses its quadratic polynomial model. Every test iterates the entire specified finite algebra, not a sample. These checks establish the formula only in those five fields; the proof in `RESULT.md` establishes the all-prime-power statement using symbolic classification. No independent mathematical audit has been performed.
