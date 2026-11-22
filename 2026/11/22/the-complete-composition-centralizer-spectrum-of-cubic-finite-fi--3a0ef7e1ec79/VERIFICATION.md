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

# Verification
The exact theorem follows from a two-equation coefficient calculation in the proof. These are checks of the derived formula, not an independent proof of infinite-family validity.

Running `python verification/jet4_check.py` exhaustively evaluates the \(q^6\) ordered substitution pairs for \(q=2,3,4,5,7,8,9\), with explicit polynomial-basis arithmetic in \(\mathbb F_4\), \(\mathbb F_8\), and \(\mathbb F_9\). For each fixed endomorphism it counts all commuting partners and compares the complete histogram with the theorem, combining formula terms that have equal centralizer cardinalities. It independently totals the ordered commuting pairs.

The executed program reports `JET4_FULL_CENTRALIZER_CENSUS_VERIFIED`. Tested values, all matching the formula: \(q=2\): 64 pairs; \(q=3\): 387; \(q=4\): 1216; \(q=5\): 2725; \(q=7\): 9751; \(q=8\): 20224; \(q=9\): 25353. Detailed histograms are in `verification/finite_checks.json`.

These computations do not test every finite field or the possibility of historically broader published statements. Independent audit status remains not performed.
