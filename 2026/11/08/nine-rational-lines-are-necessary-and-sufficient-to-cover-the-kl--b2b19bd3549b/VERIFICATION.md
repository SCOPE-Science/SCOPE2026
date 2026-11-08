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

# Verification record

Run `python3 VERIFY.py` in an environment supporting Python 3. It regenerates all \(993\) rational projective points and lines over \(\mathbb F_{31}\), enumerates the \(32\) rational points on the Klein quartic, calculates the complete \((0,1,2,3,4)\)-intersection spectrum, checks all nine cover lines, and exhaustively explores every pairwise rational-point-disjoint four-secant family.

Expected stdout contains three `*_OK` lines, culminating in `MINIMUM_RATIONAL_LINE_COVER_OK: 9 explicit lines, 8 impossible`. This self-contained finite search is exhaustive because projective normalization and the strictly increasing recursion cover every possible rational line and every disjoint family once. No auxiliary tables, stochastic tests, or outside inputs are used.

The statement is only over \(\mathbb F_{31}\). The source paper's full text could not be inspected and independent review remains outstanding.
