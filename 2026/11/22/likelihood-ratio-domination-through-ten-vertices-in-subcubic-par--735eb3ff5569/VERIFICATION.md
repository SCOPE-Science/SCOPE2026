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

# Reproducibility checks

Using a standard-library Python interpreter, run `python3 verify_census.py 10` in the folder containing the companion files. It regenerates every connected simple maximum-degree-three graph up to ten vertices, removes duplicates only by exact graph isomorphism, computes the greedy and uniform-maximal-independent-set size distributions with exact rational values, and asserts nondecreasing ratios at every adjacent support pair.

The recorded output in `census_output.txt` gives class counts 1, 1, 2, 6, 10, 29, 64, 194, 531 and 1733 for orders one to ten, for 2571 classes in total; all likelihood-ratio checks passed. The verifier treats graph signatures as isomorphism invariants rather than as collision-free unique labels.

As a second method, `python3 verify_orders.py` enumerates every distinct vertex priority permutation for all 49 isomorphism classes on at most six vertices, computing the terminal cardinality by a direct greedy simulation rather than the first-pick recurrence. The exact distributions agree with an independently written recurrence, as captured in `orders_output.txt`.

The finite checker cannot establish a statement for order eleven or larger, cannot eliminate every unknown historical publication, and is not a substitute for independent external validation.
