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

# Reproducibility and scope

Python 3.8 or later, standard library only; execute these two commands in the same directory as the files:

```sh
python3 verify_direct.py
python3 verify_search.py
```

`verify_direct.py` generates each finite Tribonacci word by literal substitution, enumerates every substring occurrence and constructs exact factor-to-position incidence bit sets. It tests every three-position subset, compares the complete resulting solution set to the literal disjoint box specification, and asserts word lengths and factor counts. The test totals are 85,320; 540,274; and 3,391,024 triples.

`verify_search.py` instead enumerates factor-position coverage masks and uses complete branch-and-cover search through all possible positions of an uncovered factor. It derives the exact same optimal-triple sets with independent internal factor-coverage construction. This program imports only the shared input definitions and expected boxes from `verify_direct.py`; it does not reuse its incidence or triple-scanning algorithm.

Every word has all three alphabet symbols and therefore no attractor with fewer than three positions. These finite exhaustive checks establish the theorem only for substitution orders 8, 9, 10. The checker output is not a certificate of any all-order conjecture. Self-review was performed; independent audit has not been performed.
