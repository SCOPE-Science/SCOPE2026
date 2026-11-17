---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The purported result follows correctly by exact spread-chamber integration for K_d(t)=[-1,1]^d+[-t,t]1: vol=2^d(1+dt), lambda_parallel=(1+2t+dt²)/3 and lambda_perp=[1+(d+2)t]/[3(1+dt)], and the determinant defines the volume-normalized isotropic constant. Independently verified symbolic logarithmic derivative 2d(d−1)t(t−1)/[(1+dt)(1+(d+2)t)(1+2t+dt²)] and minimum ratio (d+3)^d/(d+1)^(d+1). d>=2, t>=0; unique t=1. The all-dim conditional-integration argument is independent of the finite exact convex-hull checker. The theorem is mathematically correct but this alone does not mean novel.

## originality

FAIL

Exact dominating published Resultary October 25 work already gives ALL of the submitted uniform-volume covariance eigenvalues, the identical normalized isotropic function, logarithmic derivative and unique optimizer, for K_old=[−1/2,1/2]^d+[−t/2,t/2]1=K_submitted/2. Homothety multiplies covariance by 1/4 but leaves isotropic constant invariant, so this is statement-for-statement exact coverage, not merely matching parameters or a coincidental table. The previous theorem additionally gives anisotropy and curvature; the stronger Kipp result also establishes symmetric minimizing shape among d+1-generator zonotopes. The submitted original cannot pass via disclaimers or another certificate.

## value

FAIL

The submitted finite-dimensional covariance and optimizer would be a natural nontrivial invariant, but under this assignment its exact complete continuum answer is an already published theorem for the very same homothetic family. Recomputing that table and optimization by a different integration has no separate unknown mathematical content. No motivated original remainder is supplied, so distinct V fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
