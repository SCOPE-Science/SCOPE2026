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

# Verification record

`verify.py` is the standalone Python-standard-library checker. Execute `python3 verify.py` and confirm the line `VERIFY_OK`.

Observed output:
```
VERIFY_OK
dynamic_programming_cases=1440
exhaustive_distinct_optimal_language_cases=84
constructive_replays=3986
```

The dynamic program optimizes without using the claimed formula. The separate exhaustive routine enumerates ordered subsets of letters, positive output multiplicities summing to the expected optimum length, and greedy subsequence embeddings; it compares the *complete set of distinct labels* against the classified family. The constructive check replayed every predicted optimum string in the selected finite range. No random sampling is needed for these stated finite ranges. Unbounded correctness is supplied by the mathematical proof in `RESULT.md`.

The scope is exactly a finite linear power of one weighted distinct-letter run template. The checker supplies no independent external audit or proof certificate for the infinite parameter range.
