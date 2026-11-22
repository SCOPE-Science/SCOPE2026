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

# Reproducible checks

Run `python3 verification.py` using Python 3 and its standard library. The checker generates the ten orbit representatives from the four-element alphabet-symmetry group, evaluates the quotient transfer matrix exactly, calculates the determinant coefficients using rational-free Faddeev--LeVerrier traces in the polynomial ring over integers, verifies the rational numerator identity to a degree exceeding the algebraic degree bound, enumerates all admissible strings of lengths zero through eight independently, checks the exact composition symmetry, and exhaustively verifies strong connectivity for all 36 legal suffix triples. It checks that the periodic walks `012` and `0121` avoid the two forbidden squares.

The determinant/adjugate argument in RESULT.md turns the finite exact symbolic comparison into an all-length identity. The analytic central/local limit theorem follows from the mathematical strong-connectivity, lattice-periodicity, and pole arguments given there; the checker does not constitute an independent infinite-limit certification. No independent mathematical audit has been performed.
