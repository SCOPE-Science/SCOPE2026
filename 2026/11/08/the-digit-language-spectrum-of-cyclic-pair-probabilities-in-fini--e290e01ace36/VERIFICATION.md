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

# Verification and scope

The proof in `RESULT.md` is self-contained and establishes the infinite-family theorem. `CHECK.py` is a supplementary executable using only Python standard-library integer, rational, tuple and set operations. It was run using Python 3 as `python CHECK.py`. Actual captured output is in `CHECK_OUTPUT.txt`:

```
PARTITION_CASES 3445
DISTINCT_CASES 3445
BRUTE_GROUP_CASES 40
VERIFY_OK
```

The checker implements two independent count routes, one from cyclic-subgroup sizes and one from nonoverlapping base-\(p\) blocks. It confirms reduced-denominator valuations, unique value counts in the tested range, and exact recovery of all partitions. It additionally constructs all elements of forty small groups and directly counts pairs generating cyclic subgroups. Direct-pair enumeration checks the cyclic-subgroup counting formula without assuming it in the test.

Test ranges are \(p=2\) with \(n\le20\), \(p=3\) with \(n\le14\), and \(p=5\) with \(n\le12\), plus independent direct pair tests for \(p=2\) up to \(n=6\) and \(p=3\) up to \(n=4\). None of these finite tests is an exhaustive proof for all primes or orders. The source counts, congruence, inverse algorithm and boundary cases are proved algebraically in `RESULT.md`.

Independently reproduced mathematical audit has not been performed.
