---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Every stable-set 0/1 indicator is a polytope vertex; transfer trace gives Lucas number L_n, Fibonacci two-point kernel, and exact Fourier eigenvalues including the n-dependent zero-mode correction. For n>=5 these expressions follow by the same transfer matrix as earlier work. Independent direct stable-set enumeration and exact moments over n=3..18 corroborated the candidate. Extremal Fourier orders and limit five follow analytically; finite checks are not proof for all n.

## originality

FAIL

FAIL: the published November 1 Lucas-cube Fourier-precision theorem uses exactly the same uniform cyclic no-adjacent-ones configurations and centered Walsh functions ψ_j=(-1)^X_j−mean =−2(X_j−mean). Consequently its Gram eigenvalues γ_nj equal four times this candidate covariance eigenvalues, with the same zero-mode correction. The earlier theorem includes both extremal mode classification, sharp bound κ<√5 and parity convergence; candidate ratio limit five is its square. n=3,4 are routine boundary checks.

## value

FAIL

FAIL as independently new work: despite a correct Fourier formula, the entire all-n nontrivial spectrum is a direct rescaling of a prior exact theorem; tiny n=3,4 extensions are not a substantive motivated new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
