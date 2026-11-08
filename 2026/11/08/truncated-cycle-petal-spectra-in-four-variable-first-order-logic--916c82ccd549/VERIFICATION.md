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

# Verification and limits

The self-contained `verify_cycle_bouquets.py` requires Python 3 and the standard library only. Run it from the directory holding the script and `verification_output.txt`, then compare its full stdout byte-for-byte with the recorded output. Its internal graph construction, hub identification, petal-path recovery, and non-counting finite-variable tuple refinement are independent of the prose proof. The refinement assigns colors to variable tuples (including unassigned variables), repeatedly replacing each variable and considering the **set** of resulting colors; it reaches the greatest stable non-counting finite-pebble equivalence on each finite pair.

The recorded execution inspected 95 bouquets structurally, 13 selected bounded-width game comparisons at widths three and four, and 12 direct cardinality enumerations for sets of one to four permitted petal lengths and widths four through six. It returned `ALL_FINITE_CHECKS_PASSED` with no failed assertion. Selected four-variable comparisons include the sharp boundary between four and five triangle petals, where no four-variable sentence distinguishes them.

The checker is finite corroboration only. It does not enumerate every bouquet, prove a global negative search result, or replace the proof that applies at unrestricted quantifier depth. The first-order formulas distinguishing a particular pair may have a depth dependent on the maximum path length in that pair. No independent mathematical audit has been performed.
