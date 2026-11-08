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

# Verification instructions

The complete theorem and its quantified proof are in `RESULT.md`. For an independently reproducible finite diagnostic check, extract the adjacent standalone `verify_attractors.py` file and run:

```sh
python3 verify_attractors.py
```

The checker uses only the Python 3 standard library. For each small parameter triple it constructs, directly from the word, the set of every distinct nonempty contiguous factor, and the union of all intervals on which each factor appears. It compares this actual definition against the four specified factor occurrence unions for every candidate position subset. It checks all \(330960\) subsets of \(37\) parameter triples whose total length is at most 15 (with \(a,b\le5\), \(t\le7\)). It also counts all two-position sets passing the four-factor criterion for all \(150\) parameter triples in that parameter box, and compares against the claimed formulas.

Expected results: two `PASS` lines, reporting 330960 subset comparisons and 150 pair-count parameter cases. The diagnostics were replayed successfully on the included source. The tests do not prove the infinite statement; the logical argument in `RESULT.md` proves every integer parameter and every candidate set. The certificate is a factor-hitting equivalence, not an independently certified minimum-cardinality factor-family result. Independent mathematical audit has not yet been performed.
