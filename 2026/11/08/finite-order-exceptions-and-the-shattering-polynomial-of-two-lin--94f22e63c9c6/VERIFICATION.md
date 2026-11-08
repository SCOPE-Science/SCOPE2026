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

# Finite verification and proof scope

Run `python3 verify_projective_two_lines.py` from this directory using Python 3.9 or later, with no external packages. The file `verification_output.txt` is the captured output of this exact program.

The code checks that four hardcoded cyclic difference sets realize projective planes of orders 2, 3, 4, and 5; generates every union of two lines; then directly enumerates the traces on every possible support of size 0 through 6 for orders 2, 3, and 4. For order 5 it enumerates every support up through size 5 and samples 350 size-6 supports with a fixed random seed. At each support it compares direct trace shattering with the stated incidence characterization, then checks the predicted coefficients on each fully enumerated support size. The aggregate count is 293101 tested supports. Its final line is `ALL_TWO_LINE_PROJECTIVE_SHATTERING_CHECKS_PASS supports=293101`.

The computational tests are exhaustive only over those explicit finite orders and indicated support sizes. They do not certify the all-order theorem nor all non-Desarguesian planes. The universal result follows instead from the projective-plane incidence axioms, private-line isolation proof, six-point obstruction, and design double-counts in `RESULT.md`. No independent mathematical audit has occurred.
