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

# Finite verification instructions and scope

Run the accompanying independent standard-library Python 3 and C++17 files:

```sh
python3 verify_pair_masks.py
c++ -std=c++17 -O2 -Wall -Wextra verify_direct.cpp -o verify_direct
./verify_direct
```

The supplied `VERIFY_PYTHON_OUTPUT.txt` and `VERIFY_DIRECT_OUTPUT.txt` record successful runs of the delivered source. The programs construct both 16-vertex graphs from coordinate adjacency rules, check degree six and two common neighbors for every pair, test all 4,368 five-subsets and 8,008 six-subsets, and establish the exhaustive minimum-base counts. They independently construct exchange edges: selected/unselected bit operations versus comparing all unordered accepted-set pairs. Both compute complete connected components, edge counts and all-source shortest-path histograms. The Python implementation additionally enumerates explicit automorphism actions and orbit sizes.

The enumeration is a full finite proof for the two named graphs and the stated move relations. It does not prove statements about larger strongly regular graphs or an infinite family. A failed runtime check is not equivalent to a mathematical contradiction. Independent academic review and unindexed literature priority searches have not been performed.
