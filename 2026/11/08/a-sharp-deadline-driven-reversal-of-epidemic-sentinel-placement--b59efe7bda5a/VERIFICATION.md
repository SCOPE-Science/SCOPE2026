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

Execute `python3 verify_k34.py` using a standard Python 3 interpreter. No packages beyond the standard library, external data, network services or files other than the checker are needed. The reproduced output is:

```
PASS: full independent 15-state exact-generator derivative matching, term spectra, mean values, polynomial identities; checks= 89
```

The checker independently constructs the actual seven-vertex SI process for each of four allocations with three monitored vertices, enumerates the fifteen nonempty subsets of the four unmonitored vertices, and derives their exact rational generator. It checks all fifteen Taylor derivatives of each displayed survival expression, as well as exponential spectral multiplicities. These finite algebraic identities and the characteristic-polynomial uniqueness theorem establish the closed forms for every nonnegative time. Polynomial factorizations, the discriminant and mean-delay exact fractions are checked separately. The proof in `RESULT.md` supplies the strict inequality and uniqueness arguments for all positive deadlines; a finite checker alone would not establish these global inequalities. Numerical critical time is a noncertifying decimal approximation to an exactly specified unique root.

Independent external mathematical validation has not been performed.
