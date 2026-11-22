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

# Reproduction instructions

Run `python3 verify.py` alongside `RESULT.md`, with an unmodified Python 3 standard-library installation. No network, external database, or nonstandard package is needed. The program enumerates all relevant finite permutation-products used in the proof's small-case lemmas, computes complete cyclic-control distributions for orders 6 through 18, computes the explicit 48-state transfer trace for orders 6 through 12, and independently enumerates all proper four-colourings of cycle squares through order 15. It checks the exact three-periodic maxima and multiplicities at every tested order.

The expected final line is:

`VERIFY_OK group_relations=checked finite_gap_table=checked transfer_orders=6..12 direct_coloring_orders=6..15 binary_products_orders=6..18 extremal_counts=6..18`

The all-length theorem is established by the fixed finite group multiplication classifications and the counting bijections in `RESULT.md`; testing finitely many graph orders does not prove all orders. The published-paper comparisons are bibliographic/statement comparisons, not independent mathematical certification.
