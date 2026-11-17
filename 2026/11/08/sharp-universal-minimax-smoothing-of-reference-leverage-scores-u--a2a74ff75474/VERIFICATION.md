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

For 0<eta<=1 each mixture p_i=(1-eta)u_i²+eta/m satisfies exactly F(eta)=cos²θ/(1-eta+eta/m)+m sin²θ/eta by Cauchy–Schwarz, with an explicit u,z,w saturating coordinate 1. Optimize F to eta*=m sinθ/[sqrt(m-1)cosθ+(m-1)sinθ] until tanθ=sqrt(m-1), then eta=1. The uniform reference u_i=1/sqrt(m) forces some p_j<=1/m for every arbitrary policy and a feasible w achieves the same lower bound; hence the entire policy infimum is proved, not just mixtures. The θ=0 and π/2 endpoints, zero reference entries, and uniqueness restricted to mixture η are treated correctly. Independent analytic formula/random-vector checks across m=2,3,4,10,30 and 250 trials confirm constraints; finite checks are not the proof.

## originality

PASS

Best-of-knowledge exact rank-one angular-uncertainty minimax inflation with unrestricted p(u) and the sharp leverage/uniform transition is absent from the inspected distinct leverage sampling, robust design and tensor ALS results. The highly pertinent current-target tensor sampling paper could only be inspected through abstracts: authorized Oxford full-text access reported VPN disconnected after unsuccessful arXiv/OA attempts. This unresolved literature risk is explicit, not an automatic failure or invented source reading.

## value

PASS

The exact robustness penalty for stale rank-one leverage scores and the unavoidable smoothing cutoff answer a concrete importance-sampling design question. Showing global optimality across arbitrary discontinuous reference policies adds substantial strength beyond optimizing a convenient mixture; exact constants diagnose infinite inflation from reference zeros.

The dated certificate retains the supplied scientific assessment, sources and limitations.
