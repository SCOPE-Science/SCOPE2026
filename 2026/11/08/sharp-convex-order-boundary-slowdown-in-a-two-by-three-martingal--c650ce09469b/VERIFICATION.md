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

PASS: Exact KL projection for the reflected row weights (z^-1,t,z) imposes mean a through s=z+z^-1 and d=z-z^-1=a(s+t), giving s=(a²t+sqrt(a²t²+4(1-a²)))/(1-a²). Column rescaling returns t+=(1-b)s/b; t0=2(1-b)/b. For b>a, the fixed point t*=2(1-b)/sqrt(b²-a²) satisfies q0=1-b; F is increasing/strictly convex with sharp global sup derivative L=a(1-b)/[b(1-a)]<1 and local rho=a²(1-b)/[b(b-a²)]. Taylor expansion of row KL about q0(t*) yields successive relative-entropy ratio rho². At feasible boundary b=a, the positive recurrence has t_{k+1}-t_k=2(1-a)/(a²t_k)+O(t_k^-3), giving t_k/sqrt(k)→2sqrt(1-a)/a and kq_-(t_k),kH(pi*|pi_k)→a(1-a)/4. KL is measured at the martingale half-steps, not column-restored steps. This is an exact finite-state proof, not a general claim for all martingale Sinkhorn instances.

## originality

PASS

PASS best of knowledge. The primary Kazeykina–Ren–Wang (2026) exponential theorem assumes terminal convex support and strict convex order; this ν has disconnected three-point support and boundary b=a violates strictness. Chen–Conforti–Ren–Wang establish general exponential convergence under their own interior hypotheses, not the explicit t recursion and sharp boundary constants. SISTA is a different approximate martingale-potential gradient step. Published Resultary searches on two-by-three exact martingale projections did not find a covering scalar or boundary theorem.

## value

PASS

PASS: A minimal nontrivial martingale optimal transport instance exhibits an exact geometric-to-1/k convergence transition at the convex-order feasibility edge, with a sharp global contraction constant and explicit entropy coefficient. This is a motivated boundary diagnostic for entropy projections; the precise rate and normalization are not routine numerical checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
