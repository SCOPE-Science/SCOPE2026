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

# Reproducibility and scientific limitations

The proof uses all-pairs closed-neighborhood parity and degree-sum classifications, not an untested extrapolation from finite computation.

Run `python3 check_direct.py` to enumerate all selected sets of cardinalities 1, 3, and 5 for the rank-two Kneser graphs at ground-set orders 5 through 10. This computes closed neighborhoods and induced connectedness directly, without the parity-reduction lemma. The code separately exhausts all twelve Petersen five-cycle optima and checks the six-crown two-replacement graph.

Compile `check_parity.cpp` with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic check_parity.cpp -o parity_check` and run `./parity_check`. This independently enumerates the same small support sizes using the auxiliary parity test. Representative expected console output from successful runs appears in `expected.txt`.

The verified minimum counts for orders 5, 6, 7, 8, 9, and 10 are 12, 15, 252, 1512, 1512, and 3969, respectively. The Petersen two-replacement graph has 12 vertices, 30 edges, crown structure, and distance layers 1, 5, 5, 1. Both programs were executed successfully; they do not independently certify arbitrary orders.

The symbolic proof in RESULT.md covers all ground-set orders \(n\ge5\). Source priority is evaluated only to the extent of available indexed and inspected literature. Some potential older full-text sources and archival histories could not be completely read. Independent scholarly review has not been performed.
