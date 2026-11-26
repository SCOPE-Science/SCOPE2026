---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

At each s>0 the finite transformed kernel has maximal row sum rho<1; in particular, the probability of at least m jumps by time t is at most exp(st) rho^m by iterating the discounted jump kernel. The Laplace renewal system is valid even for deficient rows, and D_S has positive diagonal. Its noninitial occupation equations are y=qZ and (I-R)Z=D_S+ry, so Z=B+hy. The inequality r<=(I-R)1 and the nonnegative inverse give 0<=h<=1 entrywise and qh<1. Hence y(1-qh)=qB, and z=yB^(-1) satisfies q=z/(1+zh). A single s recovers one transform vector; a complete occupation profile supplies all such vectors, which determine the finite measures by Laplace uniqueness. Multiplication of homogeneous rows (q,1) by the invertible block matrix with top row blocks B,-h and bottom blocks 0,1 gives nonzero rescalings of (y,1), preserving affine ranks. The initial-state transform, if included, is redundant by total occupation 1/s. Under independent rate-r resets that also restart age, the equilibrium elapsed reset time is exponential, giving pi_j(r)=r y_j(r). At K prescribed rates, K+2 positive support times allow a nonzero weight perturbation satisfying K Laplace constraints plus normalization; small opposite perturbations give two different genuine laws in a single exit channel and the same observed occupations.

## originality

PASS

The supported distinct content is the one-entry, full-view local joint-kernel inverse, the converse and full affine-rank assertion on arbitrary admissible families, and the reset-sampling interpretation including finite nonidentification. The forward renewal representation, one-dimensional sufficiency and Poisson reset transform are not new. The closest cited full texts could not be independently retrieved and the known forward method makes the residual implication risk substantial, but available statements do not establish prior coverage of the complete inverse and rank result.

## value

PASS

Occupations do not directly measure waiting times or exit events, so exact reconstruction of an unrestricted joint row from one start provides a meaningful identifiability boundary under stated information assumptions. Full affine-rank preservation identifies when the entire response can appear mutually linear, not merely when one selected pair happens to align. The reset interpretation distinguishes an ideal continuum scan from every finite prescribed scan without imposing parametric waiting laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
