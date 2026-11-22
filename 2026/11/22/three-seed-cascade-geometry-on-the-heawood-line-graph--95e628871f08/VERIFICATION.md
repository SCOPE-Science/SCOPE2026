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

# Reproducible exact verification

The two standalone programs use only their respective language standard libraries. The Python program constructs the Fano plane from nonzero vectors in a three-dimensional binary vector space; the C++ program constructs it from seven cyclic triples, so the incidence models are not shared as data.

Compile and run `verify_line_heawood.cpp` using C++17. It traverses every one of the 2,097,152 initial seed masks, synchronously updating all possible vertices, and emits 22 integers counting complete activations by initial set size. It also checks that the 392 successful three-seed configurations split into 56, 168 and 168 by completion time and that all successful configurations terminate by round six.

Run `check_line_heawood.py` using Python 3.8+. It enumerates all 1,330 three-element sets, classifies their underlying three Heawood edges by overlap and cross-edge pattern, executes the synchronous closure recurrence, and verifies the six exact rows of the motif census.

Both programs are finite exhaustive tests and finite proofs in the specified bounded state space. They do not certify any analogous assertion for larger graphs. The complete polynomial and motif classifications were cross-checked. Independent external validation has not been performed.
