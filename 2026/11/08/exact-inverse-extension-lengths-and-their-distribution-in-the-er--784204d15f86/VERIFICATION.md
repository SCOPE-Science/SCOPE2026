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

# Reproduction

The included `checker.py` requires Python 3 and no external dependencies. From the directory containing the file, execute:

```
python3 checker.py
```

The program independently constructs the forward transition maps of the Černý automaton and computes the preimage of a subset under an entire word. It uses breadth-first search of the reverse-image subset graph to determine the true minimum extension length without invoking the theorem's run-start formula. It compares those lengths to the formula for every nonempty proper subset for state counts three through eleven, checks the uniqueness of the proposed optimal word by enumerating all words of that length for state counts through eight, and verifies the exact length-count histograms.

The observed expected output is:

```
VERIFY_OK
bfs_exact_cases=4070
unique_shortest_word_cases=492
histogram_coefficients=63
```

The test is an exhaustive *finite* cross-check on the stated state-count range, not a proof of the unbounded theorem or a proof of historical novelty. The abstract proof in `RESULT.md` establishes the all-state quantifiers. No independent mathematical audit has been performed.
