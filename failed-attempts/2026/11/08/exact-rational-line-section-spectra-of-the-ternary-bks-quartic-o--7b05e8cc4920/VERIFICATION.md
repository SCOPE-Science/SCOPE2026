---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The quartic is the same F3 plane curve as the earlier paper after multiplication of its equation by 2 (an invertible scalar). The supplied verify_bks.py uses two irreducible field presentations for each of Q=27,81, enumerates all Q²+Q+1 canonical projective points and dual lines, exactly evaluates homogeneous quartic and complete incidences, and checks the four-secants against pair-generated lines. Complete finite enumeration is an exhaustive certificate for the two fields, unlike a sample. Independent arithmetic checks verify line-spectrum counts sum to 757 and 6643, weighted sums equal 31*28 and 79*82, and the separate on/off multiplicity counts partition the planes. The already published full census matches every table exactly. No general extension-degree claim is made.

## originality

FAIL

FAIL: the October 25, 2026 published SCOPE result has the SAME ternary BKS quartic up to multiplication by the nonzero scalar 2, the SAME two extension fields F27 and F81, and prints identical complete line-weight spectra, complete on-curve and off-curve four-secant multiplicity distributions, and precisely 282 and 108 uncovered external points. The new program’s alternate field polynomials and duplicate enumeration are verification implementations, not new mathematical invariants or results. The older Korchmáros–Nagy–Szőnyi r=3,4 open boundary had already been closed by the October 25 prior.

## value

FAIL

FAIL: while the F27/F81 exceptional arithmetic census was motivated and valuable at its first publication, all exact numbers and covering conclusions are now known from the earlier complete census. An independently rerun enumeration of already published tables, with no new mathematical classification or extension, adds reproducibility but not an original valuable mathematical fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
