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
# Reproducibility and limits

Run `python3 artifacts/verify_triple.py` using Python 3.9 or newer and no external dependencies. It checks 4,605 normalized three-point supports over 40 finite abelian direct products (cyclic groups of orders 3 through 23 and 19 explicitly selected products), 499,659 unordered character pairs admitting exact double zeros, and 69 supports with Klein-four difference group. Expected output: `VERIFY_OK fixed_supports= 4605 double_zero_coefficient_lines= 499659 klein_four_supports= 69`.

The checker uses rational phases modulo one to decide equality of character evaluations exactly. The analytic proof uses only character restriction, planar circle-line intersection, rank of two Fourier rows and subgroup inclusion-exclusion. A finite checker does not verify the theorem for unbounded group size; the proof does. Bibliographic completeness and independent audit are not claimed.
