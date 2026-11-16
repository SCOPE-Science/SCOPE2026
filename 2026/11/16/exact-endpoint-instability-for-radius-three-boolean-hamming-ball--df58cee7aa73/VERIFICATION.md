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

`python3 CHECK.py` uses only the Python standard library. It independently computes exact Fourier transforms of every radius-three indicator through dimension fifteen and compares all coefficients with the claimed polynomial, plus all zero multiplicities. It computes the projection-kernel norm directly by inverse integer Walsh transforms in five nonsquare odd dimensions and compares rational results with the exact formula. A separate combinatorial calculation verifies 3,315 Krawtchouk dualities up through dimension eighty.

Expected output: `HAMMING_RADIUS3_RANGE_PROJECTION_PASS walsh= 65528 norms= 5 dualities= 3315`.

The proof works for all indicated dimensions; finite experiments alone cannot establish that. General projection minimality is already a standard fact, and the arithmetic root classification is elementary. Independent mathematical audit: not performed.
