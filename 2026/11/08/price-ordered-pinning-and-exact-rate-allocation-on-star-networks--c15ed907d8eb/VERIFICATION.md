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

The positive Schur complement of pinned star L+diag u−λI makes t_i=1+u_i−λ>0 and hub constraint u0≥λ−m+Σ1/t_i necessary and sufficient. Convex target-cost minimization with 0≤α≤p0 produces t_i=max(1−λ,sqrt(α/p_i)); complementary slackness determines α as upper endpoint or unique interior gλ root. Irreducible Z-matrix ground vector has strictly positive coordinates, and equality in concavity of λ_min excludes distinct budget maximizers. gλ(p0) and αλ are nondecreasing in λ, proving irreversible hub/leaf activation. All-active α=p0 gives the affine cost F=(p0+Σp_i)λ−mp0−Σp_i+2sqrt(p0)Σsqrt(p_i). Independently computed secular eigenvalues and constrained numerical optima for four heterogeneous instances agree; numerical checks are bounded.

## originality

PASS

Best-of-knowledge original star-specific all-budget arbitrary-vertex-price theorem with irreversible support transitions, subject to a serious near-coverage risk from a contemporaneous Kp,q bipartite-pinning theorem whose proof plausibly extends to p=1.

## value

PASS

The unweighted star with independently priced hub and leaves is a natural boundary network where support may change over budgets. Its exact unique allocation and irreversible activation, including hub turn-on and two-price transitions, give a meaningful complete structural solution instead of only a generic SDP. The value depends on the star-specific support and explicit phases, not on claiming the shared KKT machinery as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
