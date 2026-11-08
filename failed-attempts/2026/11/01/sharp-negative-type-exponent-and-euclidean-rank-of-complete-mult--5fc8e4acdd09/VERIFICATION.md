---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Reconstructed exact zero-sum decomposition -x^T D_rho x = rho sum within-block y^2 + sum_i(1-rho(1-1/n_i)) S_i^2. Tied maximum gives k-1 null directions; unique maximum gives a one-dimensional zero via the rank-one Schur complement, with a fixed critical vector demonstrating failure for all higher rho. Complete graphs have strict type for every finite p. Independent rational and symbolic test cases agree; general proof is analytic.

## originality

FAIL

Prior-covered by Nobuaki Obata (2022), Complete Multipartite Graphs of Non-QE Class, Proposition 3.11 and Theorem 3.12. On the zero-sum space D_rho=rho(J-I)-(rho-1)A, so the constrained maximal quadratic form is exactly -rho-(rho-1)alpha_min, where alpha_min= min_{x perp 1, ||x||=1} x^T A x is explicitly computed by Obata for arbitrary multipartite parts. Hence rho*=alpha_min/(alpha_min+1) and all boundary null vectors are the alpha_min eigenspace. Obata even gives (m_i+alpha)xi=constant and tied-largest eigenvectors in Lemmas 3.7-3.10. The submitted reciprocal sum is the same equation: with alpha=rho/(1-rho), 1-rho(1-1/m_i)=(1-rho)(m_i+alpha)/m_i. The proposed all-part threshold, nullity, Euclidean rank and polynomial rule are direct algebraic restatements of this earlier complete classification, not just the previously cited bipartite case.

## value

FAIL

The parameter p and Euclidean embedding threshold are natural invariants, but after Obata 2022 the entire multipartite result is a one-line affine matrix transform of a known constrained adjacency eigenvalue and standard Schoenberg rank. This mathematical statement adds no independent structural lemma, classification or motivated new invariant beyond that transformation; source novelty and claimed advance are unsupported. This is a scientific prior-coverage rejection, not a failure of the proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
