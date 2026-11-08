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

The proof uses the complete two-variable extension profile, a three-variable resource-preserving translation of unary-functional atoms to the parent-edge language, and a permanent finite-pebble strategy for every \(k\ge3\). The proof applies uniformly to finite structures of arbitrary size and unbounded local branching.

The included stand-alone Python 3 programs were executed in their final versions. `check_pebble_refinement.py` performs stable joint, noncounting \(k\)-pebble color refinement on an exhaustive bounded sample: it compares 2,346 graph pairs at width one, 2,346 at width two, 595 at width three, and 325 at width four with no mismatches against the theorem's predicted class invariants. `check_invariants.py` validates twelve distinct two-variable extension profiles among 69 structures and 609 instances of the recycled-variable child-count predicate; there were no discrepancies. It computes 256 and 3,125 canonical invariant vectors at widths three and four, respectively. The exact outputs are in the corresponding `*_output.json` files.

The experiments test only bounded finite examples. Their success does not by itself prove the unrestricted statement or historical priority. Mathematical correctness rests on the symbolic argument and the permanent strategy; independent verification of the overall theorem has not been performed.
