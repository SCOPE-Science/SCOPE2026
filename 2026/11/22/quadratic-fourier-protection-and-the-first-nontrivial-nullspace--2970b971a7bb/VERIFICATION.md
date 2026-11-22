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
# Exact verification

The supplied `verify.py` was executed with Python 3. It reported 35,011 exact coefficient checks passed. Its first route generates every restricted-growth set partition, converts blocks into consecutive arcs, and performs an integer Walsh--Hadamard transform. Its second route processes staircase-board columns as a rook-placement dynamic program. The two routes agree on every one of the 1024 five-label Fourier coefficients and on every degree-at-most-two coefficient of the six-label board.

The five-label input has 52 placements in an ambient Boolean group of order 1024. The exact zero-degree histogram is 10, 12, 42, 48, 33, 14, 3 for degrees 3 through 9, respectively, hence 162 zero coefficients and rank 862. The cubic witness consisting of cells \((1,3),(2,3),(1,4)\) has signed counts 23, 26, 3 for zero, one and two selected arcs.

The finite computation verifies only orders at most six. The infinite parity and quadratic-band statements are proved analytically in `RESULT.md` using the Stirling recurrence, an injective deletion bound, and the Bell moment inequality. No numerical limit is used as a proof for all orders. Publication priority and larger-order nullity remain outside this verification.
