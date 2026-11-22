---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Proved P={x>=0:sum block infinity norms<=1} using convex hull of independent-class unit cubes. Reconstructed active-edge rank: fractional F vertices have all nonzero entries 1/2 on support occupying at least three parts, or are integral. Every other fractional vertex is coordinatewise truncated h; clipping the unique projection p(h) to that vertex strictly decreases each removed-coordinate squared error. KKT on sum s_i=(r-2)/2 yields unique s_i=min(1/2,lambda/a_i), all s_i>0; strict symmetric concavity gives class-balance extremizers; four-part threshold at 3a=b follows by cap activation. Domain r>=3, every a_i positive integers, standard vertex-coordinate Euclidean metric.

## originality

PASS

Best-of-knowledge original surviving contribution: Priority assessed by comparing precise mathematical implications and acknowledging stronger partial coverage; historical first priority is not certified.

## value

PASS

The exact Hausdorff gap between common fractional edge and integral stable-set relaxations is a natural optimization stability invariant. The singular full-half extremizer, optimal class-size profiles and contact transition are new geometric structure, not just a graph parameter renaming. General half-integrality alone does not determine metric separation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
