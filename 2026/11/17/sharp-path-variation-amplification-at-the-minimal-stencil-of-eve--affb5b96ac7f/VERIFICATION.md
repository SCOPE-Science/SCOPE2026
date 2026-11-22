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

For n=p+1, D_p is one row d, so Sherman–Morrison gives S=I-alpha d^T d with alpha=lambda/(1+lambda*binom(2p,p)). Factoring d=v^T D yields the onto-gradient induced operator I-alpha u v^T. Each diagonal stays positive because alpha*u_j*v_j<1; its maximum absolute column sum is 1+alpha M_p, attained by the unique-jump step. M_1=-2, M_2=0, M_p>0 for p>=3 (j=0), and the central binomial bounds plus Stirling prove M_p/binom(2p,p)->sqrt(2). Exact rational inversion independently matched all step norms for p=1..8, lambda=1/11 and 3/4; that finite check does not prove the limit.

## originality

PASS

The min-stencil all-order sharp adjacent-TV norm and universal 1+sqrt(2) limit are not implied by earlier range-preservation statements, the p=1 or p=2 finite-length theorems, or the standard smoother representation. Originality is best-of-knowledge; unindexed BV operator norm calculations for WH filters could overlap.

## value

PASS

Minimal p+1 is the canonical first feasible sample length for the pth-order difference penalty. The sharp perturbation-stability invariant and its order-dependent trichotomy/high-order limit diagnose when a quadratic smoother amplifies signal variation; a binary-step extremizer makes the instability operationally interpretable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
