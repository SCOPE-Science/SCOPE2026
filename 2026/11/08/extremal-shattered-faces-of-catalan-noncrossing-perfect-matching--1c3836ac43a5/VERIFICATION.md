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

# Reproducibility

Execute `python3 verify_noncrossing_matching.py` using Python 3.9 or later; no nonstandard packages are required. The checker uses recursive Catalan enumeration and an independent all-pairings filter for \(m=1,\ldots,6\). It exhaustively evaluates traces on every possible maximum-size positive support (the all-positive pattern forces any shattered support to lie inside a matching), checks that precisely the near-perfect perimeter matchings are shattered, and tests the size bound. Expected concluding line: `NONCROSSING_MATCHING_EXTREMAL_SHATTERING_PASS`.

Observed counts of top supports at \(m=2,3,4,5,6\) are \(4,9,16,25,36\), respectively. The number of candidate supports tested is \(4,15,56,210,792\), respectively. The verification is finite; the proof in `RESULT.md` establishes all \(m\ge2\). This report contains no external audit or independent certification.
