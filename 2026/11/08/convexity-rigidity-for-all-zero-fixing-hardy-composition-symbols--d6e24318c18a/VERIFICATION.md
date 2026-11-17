---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

For φ(0)=0, write A(z)=φ(z)/z; Schwarz–Pick gives lower control on |1-A|/(1-|z|²) when b=A(0)≠1, hence any Berezin values approaching 1 have preimages approaching zero. Expansion Bφ(z)=1+(b-1)|z|²+O(|z|³) forces all range points onto the same affine real line under convexity. For each r<1 the auxiliary holomorphic F_r(ζ)=(1-r²)/(1-r²A(ζ)) takes its radius-r boundary values on that line; the harmonic maximum principle and open mapping force F_r and A constant. Real-line containment and the limit Bφ→0 imply b real; direct monotone parametrization gives (0,1] for -1≤b<1, singleton {1} for b=1. The estimates also handle |b|=1 and the identity case. Finite diagnostics are not the universal proof.

## originality

PASS

The all-zero-fixing symbol classification is not implied by the Oct 2026 published linear-symbol theorem, nor by prior nonconvexity for restricted real-derivative nonlinear symbols. The motivating paper’s full text was unavailable and could contain a stronger result; this is an explicit best-knowledge priority risk, not grounds for an access-only rejection.

## value

PASS

A natural complete family of Hardy disk symbols is classified by a simple geometric property of the Berezin image. The rigidity method replaces local jet-by-jet checks by an endpoint localization plus harmonic continuation argument, and includes arbitrary complex derivative and arbitrary nonlinear symbols.

The dated certificate retains the supplied scientific assessment, sources and limitations.
