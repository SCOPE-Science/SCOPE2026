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

# Reproducible checks

All commands below use Python 3's standard library. The three scripts are embedded in full alongside this file.

```text
python3 code/verify_shadow.py
python3 code/verify_lcs.py
python3 code/verify_fractional.py
```

- `verify_shadow.py` enumerates the 90 source words and all distinct length-four deletion outputs from two deleted positions; verifies every pairwise compatibility bit, exact increasing-clique counts, the stated four-word witness, and the entire fourteen-orbit classification under alphabet permutations and reversal.
- `verify_lcs.py` independently constructs source words by choosing symbol positions and derives all pairwise compatibilities from a conventional dynamic-programming longest-common-subsequence computation; it verifies every compatible pair, triple and quadruple, and checks each possible fifth vertex extension.
- `verify_fractional.py` checks all primal packing and dual covering constraints with exact fractions on all source words and reads. Both objective totals equal five.

Executed results:

```text
word_count=90
compatible_k_set_histogram=[1, 90, 1164, 1788, 144, 0]
maximum_size=4
maximal_codebook_count=144
orbit_counts={6: 4, 12: 10}
independent_lcs_exhaustion: counts=90,1164,1788,144; five_sets=0
primal_sum=5 dual_sum=5: rational LP optimum exactly 5
positive_primal_words=48
positive_dual_reads=30
```

The certificate proves only a finite exact claim. Two different algorithmic formulations reduce correlated coding mistakes but do not substitute for an external mathematical audit. For historical originality, the 2014 *Deletions in Multipermutations* full paper remains an uninspected risk, and no assertion of priority is absolute.
