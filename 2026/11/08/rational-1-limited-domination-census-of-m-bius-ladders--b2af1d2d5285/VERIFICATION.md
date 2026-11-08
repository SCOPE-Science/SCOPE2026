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

The file `verify.py` is self-contained and uses only the Python 3 standard library. Execute `python3 verify.py` in a directory containing the file. Its complete successful replay prints `VERIFY_OK` after the checks below.

The script constructs the 16 ordered-pair states and their 26 valid transitions directly from the vertex predicate. It exactly computes ordinary and twisted traces through exponent 16, uses integer Newton identities to verify every coefficient of the characteristic polynomial, reconstructs the full rational numerator from the adjugate degree bound, and verifies the two coefficient-diagonal identities. These steps are finite algebraic certificates for the all-width transfer formula.

It separately builds the simple cubic 2n-vertex Möbius ladder as a 2n-cycle plus opposite chords and enumerates *every* vertex subset for each width from 2 through 9. Both entire weight polynomials agree with the transfer calculation. Widths 10 through 16 are additionally checked through transfer arithmetic. This exhaustive finite subset test is supporting evidence, not the reason the theorem holds for every width.

The full argument depends on the exact definition of the graph, the local transfer bijection and standard adjugate/characteristic-polynomial algebra. The calculation does not certify literature priority or count distinct automorphism orbits. No independent audit has been performed.
