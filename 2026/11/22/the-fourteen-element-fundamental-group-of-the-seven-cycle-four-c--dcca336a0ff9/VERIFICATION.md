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

# Reproducibility

Run `python3 verify_hom_c7_k4.py` with Python 3.10 or later; it uses the standard library only. The script independently constructs all seven-coordinate nonempty colour-subset tuples, filters adjacent-disjoint assignments and takes cyclic representatives with orientation signs. It verifies the entire quotient boundary complex, its products of consecutive boundaries and integral elementary unit-pivot contractions. It separately obtains the full cellular presentation of the fundamental group from the one- and two-skeleton, checks the abelianization of every attaching word against the integral degree-two boundary, and performs the explicit elementary Tietze substitutions. Successful completion prints `ALL_HOM_C7_K4_QUOTIENT_CHECKS_OK`. An actual run transcript is supplied in `verification_output.txt`.

The 3957 integral chain cancellations are exact integer operations, not finite-sample evidence. Their resulting small matrix has determinant of absolute value fourteen and entries of gcd one. The 1140 Tietze eliminations preserve the exact group, ending with one generator and 46 degree-fourteen relators. Source-rotation freeness is proved in the RESULT, not inferred from sample enumeration. Results concern the specified finite seven-cycle and do not imply a homotopy equivalence to a lens space, nor an all-cycle theorem.
