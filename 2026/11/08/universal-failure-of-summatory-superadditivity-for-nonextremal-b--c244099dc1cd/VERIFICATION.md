---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For a word of integer value v and H=2^h, a bit-window occurrence at position j is exactly the disjoint integer intervals [2^j(Hq+v), 2^j(Hq+v+1)-1], q>=0. For strict interior H/2<v<H-1, counting all j windows below m=v+1, n=H+v+1, m+n=H+2v+2 gives offset 0 contributions (1,2,2), offset 1 (0,2,2), and offsets >=2 none: 4v>=m+n and 2H+v>=m+n close the interval checks. Thus defect=4-1-4=-1 uniformly for all h>=3. The count of words is 2^(h-1)-2, with excluded endpoints not assessed. An independent direct canonical substring-count and bit-window program verified all 240 strict-interior patterns h=3..8; finite test not substituted for interval proof.

## originality

PASS

The published all-one positive theorem concerns the endpoint 1^h, while primary additive block-count fluctuation work proves Gaussian laws for differences under shifts, not deterministic finite counterexamples to a summatory inequality simultaneously for all interior words. The explicit uniform all-length obstruction is neither a corollary of those distributional results nor known-table recomputation on reviewed sources. Best-of-knowledge with bounded coverage.

## value

PASS

A uniform obstruction for all 2^(h-1)-2 nonextremal leading-one binary blocks is a meaningful boundary result in the Graham-style summatory digit inequality problem. The explicit universal witness separates the two genuinely special endpoint candidates, rather than merely computing an arbitrary small exception or taking a limit without motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
