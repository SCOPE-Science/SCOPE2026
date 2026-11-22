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

# Reproducible finite verification

Run `python3 verify.py` using Python 3.9 or later. No external packages, papers or downloaded data are required. The script recreates the Fano incidence system from the modular line equation and all 24 perfect matchings twice (permutation and recursive enumeration).

It uses a canonical spanning tree to enumerate exactly all 256 normalized signings. At each of these signings, three independent integer evaluations are compared: direct sum over complete matching masks, recursive signed permanent and fraction-free Bareiss determinant. The exact determinant histogram, Parseval check and character multiplicities are then asserted. Direct and fast eight-coordinate Walsh inversions agree for all 256 coefficients of the projection kernel; the kernel is identified in the binary cycle space. The exact norm \(93/16\), full rank and nullity, and least nonzero multiplier magnitude are checked. Successful execution prints a `PASS` summary; any discrepancy raises an exception.

The script exhausts the **finite** set of all required signings. Translation averaging and uniqueness of the invariant range projection are proved algebraically in RESULT.md, not inferred from computation. No extension to different graphs or independently validated priority is asserted.
