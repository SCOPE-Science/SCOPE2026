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

FAIL

The central identities are correct: exchangeability makes the average 1/T and gives a common diagonal v and off-diagonal b. The fixed sum forces b=−v/(T−1), so pushing the covariance through the matrix of gradients gives vT/(T−1) times the centered scatter; the trace and the pairwise sum agree by expanding centered squares. The positive-v range and kernel claims hold, and λ_i²≤λ_i with equality exactly for binary coordinates proves that uniform one-hot is uniquely maximal for v. However, Finding lines 90–105 makes two unconditional claims that are false under the stated assumptions. With T=2, g₁=0, g₂=1 and Λ=(1/2,1/2) deterministically, the gradients differ but v=0 and the covariance has rank zero, not rank one. With equal task gradients, deterministic uniform and uniformly one-hot weights give the same zero aggregate covariance, so uniform one-hot is not the unique law maximizing Cov(Z) as stated (it uniquely maximizes v, or Cov(Z) when the scatter is nonzero). The tight-frame characterization of nontrivial noise on the centered-gradient span likewise needs v>0: deterministic uniform weights give no noise even for g=(2,0),(−1,1),(−1,−1), whose scatter diag(6,2) is not scalar on its span. The NumPy checker was inspected, not executed; it selects v>0 in its two-task test and does not test uniqueness at zero scatter.

## originality

FAIL

Even after correcting the degeneracies, the central finite-weight covariance identity is a direct corollary of a published, more general uniform-permutation variance formula. The fact that the RLW paper uses the weights without locally restating this covariance does not remove that coverage. The remaining support, tight-frame and extremality observations add only immediate algebraic consequences and a scalar bounded-variance bound.

## value

FAIL

The covariance interpretation can be useful for explaining RLW, but it is a direct reuse of a known exact permutation variance, followed by trace and Gram-matrix identities. The coordinate-variance endpoint is an elementary bounded-variable inequality and the attaining optimizer is an already described special case. Correcting the degenerate cases would improve exposition but would not leave a distinct valuable mathematical result to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
