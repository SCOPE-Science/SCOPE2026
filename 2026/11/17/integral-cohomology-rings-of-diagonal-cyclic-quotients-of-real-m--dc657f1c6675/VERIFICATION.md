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

Run `python verify_diagonal.py` with Python 3 and SymPy installed. The code independently constructs all geometric orbit cells, checks their counts, evaluates the rank predictions, and calculates integral Smith forms after a spanning-tree reduction for widths three and four. Its expected final line is `DIAGONAL_MOMENT_ANGLE_QUOTIENT_EXACT_PASS`; the included `CHECKS.txt` gives the output of the packaged verifier.

The infinite-family proof is mathematical rather than computational. Critical deductions are the fixed-vertex path-lifting surjection on fundamental groups, the two coordinate-axis maps and their retraction in first homology, the trivial stabilizers of positive-dimensional cells, and the split surjection onto second homology of the product of necklace quotient graphs. The latter proves a primitive integral cup-product sublattice, not only a rational rank.

The exact Smith checks cover widths three and four. Widths five and six are checked for orbit counts and Euler arithmetic only. This is not a finite certification of infinitely many cases; no claim is made for an uncomputed fundamental group or a homotopy decomposition. Independent mathematical validation has not been performed.
