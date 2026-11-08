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

Compile `verify_direct.cpp` with a C++17 compiler, for example `c++ -O3 -std=c++17 verify_direct.cpp -o verify_direct`, and run `./verify_direct`. This program constructs integer chip labels from independently enumerated edge-gap vectors, applies the actual synchronous diffusion rule twice, then counts equality with the input. The chosen finite gap margins exceed the maximum degree-sum bound for an initially periodic edge; it checked 31,946,794 normalized configurations across six pairs of arm sizes.

Run `python3 verify_orientation.py`. This is a separately programmed exact arithmetic enumeration of every three-valued edge-sign assignment and its admissible gap multiplicity on all 25 pairs of arm sizes from 1 through 5. It checks the closed formula without iterating the diffusion map.

Compare output to `direct_output.txt` and `orientation_output.txt`, respectively. Both captured outputs were produced from the bundled source code and the reported checks passed. The proof in `RESULT.md`, rather than the finite search, establishes the formula for arbitrary positive arm sizes.

The recurrence classification is modulo common integer translation: the left hub is normalized to zero. Initial chip labels need not be nonnegative; any translation class can be shifted to nonnegative labels. The accompanying files contain no implementation of an independent scientific audit.
