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

# Verification procedures and boundaries

The proof rests on the coordinatewise permanent \(k\)-pebble strategy and on distinguishing clique/independent-set formulas. To reproduce finite corroboration, run `python rook_logic_checker.py` and `python rook_extremal_checker.py` with a standard Python 3 installation; both use only the Python standard library. Compare their stdout to `rook_logic_checker.stdout.txt` and `rook_extremal_checker.stdout.txt`, respectively.

The first program refines atomic \(k\)-tuple types by *sets* of possible replacement types rather than their cardinalities, as required for counting-free first-order logic. It runs at widths \(2,3,4\) on bounded families and exhaustively compares the resulting stable type spectra for each ordered pair of test graphs. It checks algebraic theory counts at widths \(3\) through \(10\) and truncated-parameter identities over finite ranges. This is an implementation-level check of finite equivalence classes, not a proof that every larger board obeys the classification.

The second program independently enumerates candidate subsets for all six boards with parameters between two and four, confirming exact clique and independent-set maxima and common-coordinate cliques of size at least three. It prunes subsets too small to improve either current extremum, so the stated subset-check count is after pruning rather than a claim that every subset was reexamined.

The finite calculations have no role in certifying historical priority. No independent mathematical audit has been performed. Generalizations to three or more Cartesian factors, counting logics, and arbitrary line graphs remain unproved here.
