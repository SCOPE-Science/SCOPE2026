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

The mathematical proof establishes the unrestricted equivalence criterion using a permanent pebble-game invariant and explicit distinguishing sentences. The computations below are finite corroboration only.

Run `python3 verify_pebble.py` using Python 3 standard library from the package directory. `verify_output.txt` records its exact stdout. The script constructs orbit representatives of \(k\)-tuples under binary linear automorphisms, identifies orbits by the subspace of linear dependencies, and verifies equality of all one-move proper-dependency signatures for the width-four \((3,4)\)-dimensional, width-five \((4,5)\)-dimensional, and width-six \((5,6)\)-dimensional cases. It checks every five-element subset of the sixteen-element group for dependence and demonstrates five independent vectors in dimension five, including a direct evaluation of the displayed six-variable five-term relation formula.

Passing these tests does **not** prove the quantification over all dimensions and all pebble-game rounds. The independent audit has not been performed. Priority is qualified by the possibility of an unlocated covering theorem and the lack of access to the full 2010 journal text.
