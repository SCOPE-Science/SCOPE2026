---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Choose the active coordinates uniformly, then sample independent signs and uniform simplex weights. A coordinate is active with probability s/d, and its conditional second moment is 2/[s(s+1)], so the affine kernel is 1+c x·y with c=d(s+1)/2. The row mass is convex on the entire polytope and equal at all vertices. Distinct vertex rows have opposite signs near the negative of one vertex on a set of positive skeletal measure, which makes every nontrivial combination strictly submaximal. The sign row attains the essential supremum by full support and continuity; L1 follows by symmetry. At a vertex the excess is (s/d) times the integral of (cU−1)_+ for U~Beta(1,s−1); integrating the tail (1−u)^(s−1) gives c/d times (1−1/c)^s, including s=1 by taking U=1. The logarithmic derivative in s+1 is strictly positive using log(1−u)>−u/(1−u) with u=2/[d(s+1)], and Taylor with bounded second derivative gives remainder at most s(s−1)/[d²(s+1)]≤1/d. Both limits and rational benchmarks follow. Replay: RESULT.md lines 32–93; verify.py and VERIFICATION.md describe 1,984 finite checks, inspected but not executed.

## originality

FAIL

The substantive intermediate-rank claim has complete equivalent coverage in a distinct published catalogue result inspected at statement level. The November 8 record gives the identical measure, norm, norming locations, rank hierarchy and a stronger dimension band; sign extremization and L1 equality do not furnish a distinct remainder (it specifies the sign extremizers and the projector is self-adjoint). This is a finding of overlap as of review, not that the later-dated result anticipated the October frozen work or proof of historical priority. The earlier facet and simplex records alone would not establish this failure. The frozen evidence is correct and is preserved.

## value

PASS

As a mathematical invariant, the sharp projector norm on these equal-area skeleta is useful: it quantifies the effects of a natural change in observation support, identifies precisely the most amplifying evaluation locations, and gives a joint dimension–rank law. This assessment of the result's usefulness does not give additional novelty credit to complete overlapping coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
