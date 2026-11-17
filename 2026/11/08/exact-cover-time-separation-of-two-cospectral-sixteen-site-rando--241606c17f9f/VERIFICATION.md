---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Both adjacency matrices defined on (Z/4Z)^2 are 6-regular and satisfy A²=4I+2J, yielding the common (16,6,2,2) parameters and spectrum. Hitting-time inclusion–exclusion over 2^15-1 nonempty forbidden subsets correctly converts max vertex-hit times to first exit times, and Cramer ratios of (6I-A[B]) give exact rationals. Distinct visited-set Bellman equations were independently implemented here with descending subset order and Gaussian elimination for both 16-vertex graphs: rook 55.120239522685985, Shrikhande 55.120643817526684, difference 0.000404294840699, matching the certificate interval (40429484,40429485)/10^11. This numerical solver independently corroborates the value/sign, not the many-digit certificate. Source exact_cover.cpp, cover_dp.cpp, verify.py and CERTIFICATE.json were inspected as supplied; exact 32767-subset determinant generation, not mere VERIFY_OK, is the claimed finite exhaustive certificate.

## originality

PASS

The exact expected cover-time distinction for the canonical rook/Shrikhande strongly regular pair was not found in published Resultary or targeted primary-source searches. Standard exact cover-time algorithms and inclusion–exclusion are explicitly prior; the result is a mathematically motivated exact finite counterexample to cover time being determined by adjacency spectrum or strong-regularity parameters. Historical exact numerical tables remain a residual risk.

## value

PASS

The Shrikhande/4x4-rook pair is the canonical nonisomorphic pair with identical SRG parameters; exact covering-time separation probes a natural non-spectral transport invariant. The 0.0004-jump difference is small but a strict exact inequality establishes a clean natural counterexample rather than an arbitrary tiny improvement. The finite case is fully specified, reproducible, and motivated independently of numerical size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
