---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For alpha,lambda>0 and a compact invariant measure, antiderivatives in x,z imply E[y|x]=0 and E[x²|z]=alpha*z. Orthogonality gives Var(x²)=alpha² Var(z)+E[(x²-alpha z)²] and Cov(x²,z)=alpha Var(z). The generator applied to xy gives E[y²]=alpha E[z(z-1)]; vanishing y² forces support on precisely (0,0,0),(±sqrt(alpha),0,1), and otherwise z≥0 implies positive mass in z>1. Backward variation of constants proves the height-memory representation for bounded complete trajectories. No ergodic hypothesis needed; finite checks are not the proof.

## originality

FAIL

DECISIVE PRIOR COVERAGE. The publicly indexed 2026-10-04 Shimizu–Morioka result already proves the identical all-compact-invariant-measures identity E[x²|z]=alpha*z, positivity z≥0, and the exact past-memory law, and publishes the xy generator formula. Combining its displayed formulas yields E[y²]=alpha E[z(z-1)] and thus the z>1 barrier by positivity, with no new structural lemma. The separately published Rucklidge full theorem directly covers the same variance, positive-height excursion and speed laws under the exact linear/time conjugacy tau=alpha t, v=alpha^(-3/2)x,u=alpha^(-5/2)y,w=alpha^(-2)z, a=lambda/alpha,b=alpha^(-2); sympy independently verified all three transformed ODEs and the moment identity. This is mathematical implication, not merely same topic or title.

## value

FAIL

The heightwise identity, variance decompositions and outer-height excursion are mathematically meaningful as dynamical observables, but the submitted entire final claim is already a direct corollary of genuinely earlier published same-system findings and the conjugate Rucklidge theorem; repackaging the same exact moments and barrier does not fill an unknown gap. Neither correctness nor a second verification certificate restores independent value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
