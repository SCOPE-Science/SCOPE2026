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

# Reproducible verification

Execute `python3 verify_rosenhain.py` next to `rosenhain_80.csv`, with Python 3.8 or newer. The script requires no third-party package. It reconstructs all eighty Rosenhain tetrads, validates the incidence/parity identities, calculates the fixed maximal minor using exact integer arithmetic, and verifies the adjacent eighty-row enumeration certificate. The determinant together with the explicit surjective congruence homomorphism establishes the complete claimed lattice equality.

An independent arithmetic route uses integer Smith normal form on the same generated incidence matrix and produces eleven unit factors, four factors equal to two, and one factor equal to eight. This latter calculation was performed for comparison, not substituted for the mathematical index argument. No extrapolation from a finite experiment to an unbounded family is needed, since the complete geometric indexing set has exactly eighty members and the proof is uniform for all specified curves.

The work does not certify an actual Néron--Severi or divisor-class quotient, and no independent review has been performed.
