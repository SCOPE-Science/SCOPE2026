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

Strict Perron left functional w^T x decreases for every nonzero state, proving global extinction by compactness. On the w-orthogonal complement the positive matrix contracts, forcing x/(w^T x)->v. A second-order expansion yields V_{t+1}=V_t-alpha V_t^2+o(V_t^2); reciprocal increments give tV_t->1/alpha. Differentiating explicit alpha gives w_i M_ij v_j^2>0 for every cost. Independent exact 2-patch rational test verified alpha=1/2 baseline and 5/4 altered costs; finite test is not infinite proof.

## originality

FAIL

FAIL: a full-text published November 2 theorem proves global critical 1/t Perron extinction for every positive density-suppressed C2 recruitment and nonincreasing dispersal family. Substituting g_j(z)=R_j/(1+a_j z) and d_ij(z)=p_ij/(1+b_ij z) gives its exact B_ij=-M_ij(a_j+b_ij), hence kappa=alpha, with the same global limit. Cost sensitivity is immediate differentiation and does not constitute a separate original claim.

## value

FAIL

FAIL independently: the specific Beverton–Holt profile is a covered corollary of a stronger published all-recruitment/all-dispersal theorem. Its derivative with respect to a denominator coefficient is an immediate positive product, without a separate structurally motivated new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
