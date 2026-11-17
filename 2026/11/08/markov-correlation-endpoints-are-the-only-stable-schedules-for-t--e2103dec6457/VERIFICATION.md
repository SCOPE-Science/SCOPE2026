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

The two-block 6-dimensional covariance transfer correctly conditions on the next Markov state, rather than assuming independent steps. If the positive block sum is rank one, positive cross-transition probabilities make the next two image lines M(a)v and M(b)v distinct because trace(M(b)^(-1)M(a))=2-(a-b)^2 lies in (-2,2); thus L_s^2 is strictly positive on the PSD product cone. Strong finite-dimensional Perron–Frobenius supplies a simple dominant positive eigenvalue with positive-definite eigenblocks. Applying logdet concavity to both determinant-one congruence equations gives rho>=1, with equality requiring a common positive invariant C; the unique normalized invariants C_h=[[1,h/2],[h/2,1]] differ for a!=b, so rho>1 for every 0<s<1. At s=1 fixed elliptic maps are bounded; at s=0 a stable alternating product is bounded iff its trace lies strictly between -2 and 2. For a=1/2,b=3/2 independently computed trace -23/16 and symbolic det(I-L_s)=-9s(1-s)^2/4. The determinant example is a corroborating special certificate and does not establish the all-parameter theorem by itself.

## originality

PASS

Best-of-knowledge PASS for genuinely correlated symmetric Markov switching with two bounded correlation endpoints and all-interior strict mean-square instability. The published iid random-step symplectic-Euler dichotomy proves the uncorrelated s=1/2 slice and supplies the determinant-concavity technique, not the Markov-dependent 6-dimensional cone theorem for arbitrary s or the bounded alternating s=0 endpoint. Earlier stochastic timestepping results control finite-horizon error, not all infinite updates under Markov correlation.

## value

PASS

This resolves a natural stability-versus-correlation question in geometric numerical integration: both a fixed step and perfectly alternating stable timetable can be bounded yet every partially randomized correlated timetable has positive exponential second-moment growth. The all-parameter dichotomy and explicit covariance/endpoint argument, not the standard lifted spectral-radius test, form a nontrivial structural stability result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
