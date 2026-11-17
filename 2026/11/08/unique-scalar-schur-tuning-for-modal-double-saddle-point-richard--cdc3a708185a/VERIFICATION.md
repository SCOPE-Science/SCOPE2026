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

Read complete frozen proof, assumptions, and check.py. Direct block multiplication independently gave per-mode characteristic z[z²-(1-c²/q)z+b_i²/q]. For largest B the root product implies q>=B²/r²; for smallest beta the real quadratic at r is nonnegative and implies q r(1-r)<=c²r+beta², hence r>=r* for r<1. At q*=B²/r*², sum r*(1+beta²/B²) and products in [r*² beta²/B²,r*²] put every real or conjugate mode within radius r*, with equality at both extremes. Equality in the two necessary inequalities gives q=q*. Independently computed exact eigenvalues for beta=1,B=3,c=4: radii 1/2 at q=36 and 3/5 at q=25. Repeated-root beta=B case and finite dimension root-limit are explicitly accounted for; numerical sample checks are not the proof.

## originality

PASS

Best-of-knowledge distinct claim after actual primary-source and published-record comparisons. The source paper supplies a relevant preconditioning structure and broad eigenvalue estimates, but an extra scalar minimax argument is essential. Scope is exact commuting modal subfamily, not arbitrary Schur blocks.

## value

PASS

Scalar Schur tuning for an actual three-block indefinite system offers a sharp, unique rate-optimal preconditioning scale depending only on extremal modal couplings, including a real/complex spectral phase; it is more informative than an unoptimized spectral enclosure and can be used as a parameter benchmark. Noncommuting general systems are explicitly excluded.

The dated certificate retains the supplied scientific assessment, sources and limitations.
