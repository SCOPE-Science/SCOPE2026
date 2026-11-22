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

The proof establishes the all-parameter formula for \(q\ge2\), \(n\ge3\). Computation is an independent finite stress test and not an infinite proof.

Run from the extracted package root:

```sh
python3 verify/exhaustive.py
python3 verify/construct.py
```

`verify/exhaustive.py` generates all words of Hamming weight two (nonzero means a symbol different from zero), filters out self-overlapping words, creates the pairwise compatibility graph, and maximizes its clique size by exhaustive branch-and-bound with a greedy-coloring upper bound. It compares with the claimed formula in \(17\) parameter cases up to \(q=5\), \(n=9\) (not all combinations at those extrema). Its standard output is recorded in `verify/exhaustive.out`.

`verify/construct.py` independently generates the balanced-partition family and checks all proper overlaps between every pair of its words, including self-pairs, over \(84\) parameter cases \(2\le q\le7\), \(3\le n\le16\). It separately enumerates primitive two-marker cyclic rotation orbits for \(35\) cases \(2\le q\le6\), \(3\le n\le9\). Its output is in `verify/construct.out`. Both outputs conclude `PASS`.

The finite checks do not enumerate arbitrary alphabet sizes, lengths, or all possible optimum codebooks. The symbolic upper bound and construction argument in `RESULT.md` address those quantifiers. The review reported here is not independent external validation.
