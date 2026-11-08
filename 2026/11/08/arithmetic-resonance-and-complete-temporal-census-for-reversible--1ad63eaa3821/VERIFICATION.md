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

# Reproducible finite checks

Run `python check_matrix.py` and `python check_states.py` with an ordinary Python 3 interpreter in the same directory as the files. No external packages, generated input data, or network access are needed.

`check_matrix.py` represents GF(2) linear transformations as integer bit rows, independently constructs the rim/hub adjacency from the graph definition, forms the doubled transition, verifies the exact global matrix order, and compares kernel dimensions of \(T^t-I\) with the formula. It checks rim sizes 3 through 50, all divisors of the asserted global order and selected additional times, producing 751 exact comparisons.

`check_states.py` independently computes every vertex's neighbor parity directly from bits, iterates all 349440 paired configurations for rim sizes 3 through 8, measures primitive return periods, and recombines them to recover the claimed fixed-point populations.

The text files `check_matrix.out` and `check_states.out` contain the actual captured successful process outputs. These finite tests do not establish the all-size theorem; the structural proof in RESULT.md supplies the infinite argument. Binary test fields do not sample all extension fields, but all proof steps are valid over any finite field of characteristic two.
