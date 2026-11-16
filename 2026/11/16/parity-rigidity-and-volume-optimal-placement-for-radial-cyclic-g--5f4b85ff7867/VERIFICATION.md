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

# Reproducible checks and limits

Run `python3 CHECK.py` from the directory containing this document. The standard-library rational tests compare the exact geometric block determinant product and design-volume ratio for every shorter separation in sizes \(N=2m\), \(2\le m\le12\), as well as parity ranks for seven independent strictly radial profiles. NumPy, when present, additionally constructs and diagonalizes the actual full complex-valued Gabor synthesis matrices for \(2\le m\le9\), checking the eigenvalues of the block frame operators and the precise rank for every cyclic separation. In the recorded execution, 1,143 tests passed.

The proof covers all \(m\ge2\), \(0<\rho<1\), and strictly decreasing positive radial profiles, while testing covers only the displayed finite cases. The determinant formula assumes **unnormalized** synthesis columns; normalizing the entire window rescales volumes by a fixed positive factor and leaves the optimizer unchanged. Independent audit is not performed, and published-priority verification is bounded by the cited literature inspections.
