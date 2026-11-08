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

# Reproduction of the finite homotopy calculation

Run `python3 verification/verify_morse.py` and `python3 verification/verify_mod2.py` with Python 3.9+; no third-party packages are required. The exact outputs are included as `verification/morse_output.txt` and `verification/mod2_output.txt`.

The first program enumerates all vertex masks of the binary four-cube, compares two face predicates, enumerates the 96 minimal nonfaces, builds the acyclic matching on all nonempty simplices, verifies every Hasse covering relation, certifies uniqueness of all five selected gradient paths, reverses them, repeats the complete acyclicity checks, then evaluates every signed integral incidence of the final critical four-cell against the critical three-cells. The direct cell-boundary sign is determined by increasing-vertex orientation. The empty face is excluded from the ordinary nonempty face-poset matching.

The second program constructs the complex independently from its forbidden triples, reduces the full ordinary boundary matrices over the two-element field and checks reduced Betti ranks in every degree. The field calculation corroborates but does not imply the integral homotopy claim; the signed Morse differential and Hurewicz argument are essential to the latter.

The scripts are finite, fully enumerative checks for the stated 16-vertex graph. They do not prove any larger-hypercube statement or establish publication priority. Independent audit has not been performed.
