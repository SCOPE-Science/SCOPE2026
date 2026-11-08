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

# Reproducibility and verification

Run the accompanying standalone program with Python 3: `python verify.py`. It requires no third-party packages, network connection or external input data. All of its numerical results use exact integer or rational arithmetic.

The graph-level checker constructs all rook-graph vertex pairs, derives pairwise graph distances, and tests each selected triple against the shortest-path equality. Inclusion maximality is checked by adding every excluded square and examining validity. The exponential-generating-function calculation is implemented independently, using a coefficient recurrence and exact rational arithmetic rather than graph enumeration. It compares both complete polynomials on eight boards: \((m,n)=(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4)\). Together these checks cover \(104272\) vertex subsets, of which \(3543\) are in general position and \(665\) are inclusion maximal.

A further \(41\) pairs of board dimensions are tested against the complete maximal-cardinality spectrum and the minimum/maximum-degree coefficients, with a separate recursive implementation of restricted Stirling partition numbers. The expected output begins `VERIFY_OK` and reports all these counts and `spectrum=PASS extremal_counts=PASS`.

**Limits:** Exhaustive enumeration covers only the specified finite boards. The exponential-series checks and coefficient tests cover additional finite ranges and do not independently certify unrestricted quantifiers. The all-parameter result depends on the explicit structural proof in RESULT.md. Publication priority has not been independently certified, and independent mathematical audit has not been performed.
