---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The two supplied antisymmetric test vectors have the same Dirichlet energy for each independent edge weight, and squared mass norms 4s(s+1) and 4s(s-1) for s=sqrt(1+t)>1. Rayleigh–Ritz then bounds the positive extreme eigenvalue ratio from below. At the stated ray the two generalized eigenpairs and the even nonconstant eigenpair give strict ordering for every s>1. Equality in the ratio requires equality in both Rayleigh bounds; the endpoint eigenvector equations force w1=w3 and the next equation gives 2w2=s^2w1. A separate edge-Gram calculation reproduced the optimal ray, eigenvalues and a full-support extremal eigenvector exactly. No symmetry restriction, stochastic step or finite grid is needed.

## originality

FAIL

The optimizer ray and exact minimum follow mechanically from classical optimal congruence-scaling of an SPD matrix with Young's property A, after passing to the three-dimensional weighted edge Gram. The accessible classical quotation establishes optimality rather than explicitly asserting uniqueness; nevertheless uniqueness here is an immediate Rayleigh equality test in the same classical scaling orbit, using an everywhere-nonzero extremal eigenvector. This is positive prior-coverage evidence, not an inference from inaccessible papers.

## value

FAIL

The conductance choice is well-motivated as a model, but in this unconstrained four-site setting the claimed exact invariant is a routine normalization and spectrum of a property-A Gram. The observed weak/equal/strong central link is the comparison of its normalized diagonal entries, and the rigidity is immediate from standard equality. There is no separate surviving nonroutine claim under stochastic-step, capacity or other design constraints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
