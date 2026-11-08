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

# Computational and exact verification

With `g++` (C++17) and `python3` available, run `python3 verify.py` in the same directory as the two source files. The script compiles the programs in a temporary directory, executes them, and checks that each enumerates exactly 14,348,907 labeled configurations. They independently agree on the sixteen minimum penalties and all sixteen counts. The subset-program construction explicitly verifies equality between all 180 enumerated zero-field minimizers and the 180-element two-star-plus-four-clique family. Rational arithmetic checks all possible field-minimizing sectors against the exact lower-envelope claim, including four critical-field multiplicities.

The two finite search programs are complete because `recursion.cpp` assigns each of three labels to each of fifteen vertices once, and `subsets.cpp` enumerates every choice of first and second colour sets, with the third forced. The induced-edge subset recurrence is exact for finite simple graphs. The proof therefore needs no statistical uncertainty. The code does not establish priority over all historical literature, any infinite-size phase transition, or independent scientific validation.
