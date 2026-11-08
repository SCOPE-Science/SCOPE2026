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

# Independent reproducibility instructions

Run `python3 checker.py` from the directory containing this file. Its only dependency is the Python standard library. A successful replay must print `VERIFY_OK` and the following counters:

```
{'param_cases': 432, 'entry_checks': 6762, 'full_decoding_checks': 3258, 'tropical_rank_checks': 252, 'tropical_nonsingular_witness_checks': 4902}
```

The direct decoding tests enumerate all codewords of spheres and balls over alphabets 2, 3 and 4, up to lengths 6, 4, and 3 respectively. The row-template factorization is checked for all side lengths at most 5 and all admissible radii; compressed tropical ranks are independently searched for each side-length pair of total at most 6, and all permutations of the predicted witness block are inspected. These finite tests verify the checker and illustrate the theorem; they do not establish the infinite-parameter claim. The algebraic proof in RESULT.md provides the general argument, including the proof that no smaller rank is possible.

Mathematical scope: exact Hamming weight spheres and balls over a finite alphabet of at least two letters. No statement about independent verification, completeness of the historical-priority search or computational hardness is implied by this replay.
