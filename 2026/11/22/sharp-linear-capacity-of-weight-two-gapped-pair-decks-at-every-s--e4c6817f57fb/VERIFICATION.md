---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The frozen Finding overstates the classification by saying 'exact marker separation'. At n=10,s=3, the zero-based pairs (2,7) and (3,6) have separations 5 and 3 but both yield (G00,G01,G10,G11)=(19,4,4,1) and identical singleton counts. The complete corrected RESULT.md in repairs/2 replaces that assertion with the observed long/short indicator and explicitly exhibits the collision; the formulas, scope and threshold are unchanged. The corrected proof was re-audited: fixing length and weight makes (e,G01,G10) equivalent to the whole observation. With r=s-1,H=n-2s+1 the boundary layer j is G01+G10+2e-2H and the remaining coordinate is G01. Short central gaps 1 and 2 fill the parity ranges when r>=2; for r=1 only adjacent pairs occur. Positive-excess short pairs cannot cross the two boundaries for H>=r. For 1<=j<=r the left range is [0,r-j] and the reflected range starts at 2H-r+2j. For r<j<2r each side has one value and j=2r is impossible. Central long pairs reduce to sums of two integers 0<=x<=y'<=H-r-1 (all intermediate sums occur). For j=1,...,r the long-pair left/central, opposite-boundary and central/right runs have consecutive G01 ranges [r-j,H-1], [H,H+j-2], [H+j-1,2H+2j-r-2], with the middle empty for j=1. For j>r, only opposite boundaries work and their split gives 2r-j+1 values. The sums give both asserted linear branches. When H=r all counts just listed remain valid except central long pairs, now absent rather than the formal linear count -1; this proves the exact +1 correction. One representative per deck is a maximum distinguishable code. Independently ran `python3 /workspace/review_checks.py 2`: 35 parameter cases from s=2 through 8 and n=3s-2 through 3s+2, using literal position-pair enumeration, plus the exact separation collision. Neither this finite reproduction nor static inspection of the frozen checker substitutes for the interval argument.

## originality

PASS

The repaired claim is the exact fixed-weight-two output census for all gaps in the sharp length regime, not the definition of the gapped deck or identification of exact marker separation. Existing inspected statements cover the channel, other weights or limited lengths/run classes. One-skip equivalence and four-run formulas may cover portions of s=2, but neither available statement gives or directly implies the full census, especially at arbitrary gap and the first exceptional length.

## value

PASS

The exact image size measures a natural noiseless sparse reconstruction limit: quadratically many inputs collapse to linearly many distinguishable ones. The exact slopes, change at the first nontrivial gap and shared sharp onset across all spacings are not explained by order-of-growth reasoning. The result supplies a precise benchmark without claiming recovery of exact spacing or a noisy-channel guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
