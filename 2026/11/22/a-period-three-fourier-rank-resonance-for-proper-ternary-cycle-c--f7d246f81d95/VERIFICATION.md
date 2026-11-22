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

# Exact reproducibility

Run `python3 check_increments.py` and `python3 check_vertices.py` using Python 3.8 or later. No packages beyond the standard library are needed. Both programs check the complete signed Fourier multiplier, not just the zero count. The first enumerates nonzero independent edge differences for \(3\le n\le9\), and the second directly enumerates valid vertex colourings for \(3\le n\le8\) using exact residue buckets. Each must print `PASS`.

The proof for all \(n\ge3\) is algebraic and independent of finite enumeration. The direct checks do not certify any larger palette or graph class. The exact rank calculation uses complex Fourier diagonalization with unnormalized group convolution. Published-source priority remains subject to the specified bounded literature comparison.
