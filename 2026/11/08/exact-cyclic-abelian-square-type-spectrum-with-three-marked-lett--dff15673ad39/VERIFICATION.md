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

The theorem is proved by an integer-start interval lemma for consecutive marked zeros, followed by the exact union of two half-length intervals and a parity argument. See `RESULT.md` for hypotheses, all endpoint comparisons, and the infinite proof.

Reproduce finite checks using Python 3 with no external dependencies:

```shell
python3 verify_threezeros.py
```

Expected observed output:

```
EXHAUSTIVE_WORDS_PASS 14665 odd lengths 3..29
RANDOM_GAPS_PASS 250 max length 391
ALL_TESTS_PASS
```

The checker enumerates 14,665 binary three-zero circular words at all odd lengths at most 29 and cross-compares direct factor enumeration, the independently implemented cyclic-gap prediction, the exact total formula and every prefix inequality. It then tests 250 seeded random positive triples with odd sum and length at most 391. Tests cannot prove the infinite family; the mathematical proof must be checked separately. No independent mathematical audit or certification has been performed.
