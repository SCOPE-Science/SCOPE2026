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

From a directory containing the three provided scripts, run:

```
python3 verify_arborescences.py
python3 verify_tours.py
python3 verify_spectral_identity.py
```

The first script builds the target set and directed overlap graph directly and verifies balanced degrees, a \(12\)-circle ternary boundary, an exact quaternary arborescence cofactor \(1{,}177{,}583{,}616\), and three modular quinary cofactor comparisons. The second lists all twelve ternary rotation classes by backtracking from a distinguished edge and verifies an independent 72-symbol quaternary Hierholzer witness by its complete cyclic four-window multiset. The third independently verifies the full spectral factorization for \(q=4,5\), at \(t=1,2,3\) modulo two different large primes. All three use only standard Python 3 libraries.

The finite checks do not certify the theorem for infinitely many alphabet sizes by themselves. The all-parameter argument is the direct-sum determinant factorization and BEST-theorem calculation in `RESULT.md`. Independent mathematical audit was not performed.
