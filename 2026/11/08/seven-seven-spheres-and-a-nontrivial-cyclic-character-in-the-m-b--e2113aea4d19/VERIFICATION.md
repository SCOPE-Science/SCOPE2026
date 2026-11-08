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

# Reproducible finite verification

Run `python3 mk_dominance_verify.py`. Its only dependency is the Python 3 standard library. The complete recorded output is `mk_dominance_verify_output.txt`; it ends in `VERIFY_OK`.

The program enumerates all 65,536 sixteen-bit subsets and independently tests both face predicates. It counts all 32,390 nonempty faces and their dimensions, constructs forward and reverse pivot matchings, and checks their full directed Hasse graphs for acyclicity on 218,672 incidences each. It computes signed simplicial Lefschetz numbers for every element of the order-eight rotation group and checks the eight character values against the claimed rational module. It also verifies the graph and its cover-number witness.

Mathematical theorem used: an acyclic discrete Morse matching gives a CW homotopy model with one cell for each critical simplex. A unique zero-cell plus seven seven-cells and no other critical dimensions gives the asserted integral wedge of seven seven-spheres. This is a finite exhaustive certificate, not a sample or a computational extrapolation. No independent audit has been undertaken.
