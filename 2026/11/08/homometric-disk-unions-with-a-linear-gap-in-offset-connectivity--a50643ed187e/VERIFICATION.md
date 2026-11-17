---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The six base centers A={0,1,4,10,12,17} and B={0,1,8,11,13,17} have identical 36 ordered signed differences: nonzero positive distances are exactly 1..13,16,17 once each. With H_m={22k:0<=k<m}, the disjoint center blocks form convolution measures, preserving the entire signed autocorrelation for every integer m>=1. Initial radius-1/4 disks do not overlap, so their indicators equal delta-center convolution with the disk indicator; convolution with reflection therefore gives identical full planar covariograms and independent pair-displacement laws. Dilation by r turns them into disks radius R=r+1/4, and for 11/4<r<13/4 the center contact threshold 2R lies strictly between 6 and 7. A has within-block gaps (1,3,6,2,5) and block gap 5: all connected; B has gaps (1,7,3,2,4) and block gap 5: exactly one separating 7-gap in each of m blocks, giving m+1 components. An independent difference-counter and gap-counter check confirmed m=1,2,3,10,30. The all-m proof is exact convolution and ordered-gap reasoning; 6m original components bound the growth order.

## originality

PASS

The six-point homometric pair, direct-sum convolution and covariogram/Fourier equivalence are known from classical homometry literature, not new. No inspected primary source or Resultary published record was shown to establish the *new combination* of equal direction-sensitive positive-area disk-union covariograms with fixed-radius offset Betti-0 discrepancy m and a nonzero stable interval for every m. Averkov–Langfeld direct-sum homometry provides a tool but not this specific controlled persistent connectivity difference. This is a best-of-knowledge special geometric separation with residual older morphology/persistence risk.

## value

PASS

A covariogram is the full two-point translation correlation (and diffraction intensity) of a planar domain, a strong natural observable. Exact fixed-scale connectedness remains unidentifiable even from this data: for equal-distribution unions of 6m smooth congruent disks, offset component counts differ by m, the maximum possible order in input component count, uniformly over a nontrivial open radius interval. This sharp-order topological obstruction is motivated and not just a renamed homometric pair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
