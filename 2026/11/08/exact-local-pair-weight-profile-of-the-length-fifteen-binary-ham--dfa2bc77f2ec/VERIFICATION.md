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

A pair-weight-four nonzero word must be a Hamming-weight-three codeword supported on three cyclic consecutive coordinates, equivalent to xor-zero of the three corresponding nonzero F₂⁴ columns. GL(4,2) acts freely and transitively on fixed ordered distinct starting columns; fixing (1,2) leaves 13! permutations, and dividing the resulting generating polynomial coefficients by 96 counts distinct indexed codes. The acyclic subset/last-two columns DP counts each tail and both wrap-around triples exactly once. An independent C++ implementation of this recurrence reproduced the full exact seven unnormalized coefficients [1642251264,2567162880,1512023040,434319360,65617920,5492736,153600], sum 13!; integer division gives claimed profile, sum 64864800. Zero-triple condition and any two adjacent columns yield pair distance exactly five, while any B>0 yields four. This is an exhaustive finite algorithm, not samples.

## originality

PASS

The 15-coordinate projective STS(15) incidence problem is a naturally motivated indexed Hamming interleaver histogram. Existing symbol-pair coding bounds and cyclic block-avoiding sequencing results give existence or distances, not a seven-value histogram across all 64,864,800 indexed code spaces. Earlier length-7 and extended-length-8 complete spectra have different finite universes. Best-of-knowledge priority with unindexed-tabulation risk.

## value

PASS

The projective geometry PG(3,2) Hamming code is canonical; cyclic ordering changes symbol-pair performance and the complete seven-value distribution measures the availability and abundance of optimal interleavers. Counting all indexed configurations exactly via a meaningful finite recurrence gives a reusable natural design invariant not supplied by existence statements or length-seven tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
