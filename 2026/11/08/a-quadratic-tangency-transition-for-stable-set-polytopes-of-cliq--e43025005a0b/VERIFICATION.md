---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Reconstructed stable-set convex hull as join of cycle stable-set polytope and clique singleton vertices, yielding N nonnegative facets, m lifted edge-clique facets and one lifted cycle rank facet. Each lifts a true facet by affine independence. Radius upper bounds follow c_j>=r and normal lengths sqrt(t+2),sqrt(m+a^2t); uniform c=r1 attains min. Active all-positive row(s) force each center coordinate to r, proving uniqueness. Difference F_a(t)=a sqrt(t+2)-sqrt(a^2t+2a+1) strictly decreases; F=1 solves t=a^2-2a-1. Independent numerical contact computations: (a,t)=(2,1) only odd-hole; (3,1) edge, (3,2) both with radius 1/6, (3,3) odd; (4,7) both with radius 1/12. Direct small cases do not establish arbitrary facets.

## originality

PASS

The genuinely new portion of the complete claim survived statement-level search and primary-source comparisons to best of knowledge; the named known special cases and inaccessible priority risks are explicit.

## value

PASS

The complete inball contact classification and exact integer tangency locus for a two-parameter family of standard 0/1 polytopes is a natural precise convex-geometric invariant; the jump from N+m contacts to all facets to N+1 is motivated by competition of lifted clique and rank barriers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
