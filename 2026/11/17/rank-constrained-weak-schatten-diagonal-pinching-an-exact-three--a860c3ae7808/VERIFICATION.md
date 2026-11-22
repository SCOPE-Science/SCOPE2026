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

PASS: Ky Fan/von Neumann diagonal submajorization bounds k-th largest |A_ii| by H_min(k,r)(q)/k when max_j j^q s_j(A)=1. The normalized output is consequently bounded by max_{1<=k<=n} k^(q-1) H_min(k,r)(q). For k<=r, positive Laplace integral f_k=(1/Gamma(q)) int_0^infty t^(q-1)(1-e^-t)/[k(e^(t/k)-1)]dt strictly increases with k because (e^x-1)/x increases; for k>=r, k^(q-1) H_r monotone by sign(q-1). This yields n^(q-1)H_r for q>1, H_r at q=1, r^(q-1)H_r for q<1. Fourier-unitary conjugation of diag(1,2^-q,...,r^-q) produces sharp flat diagonals on support m. Equality in all Ky Fan and trace-norm duality inequalities forces prescribed singular values, flat nonzero diagonal modulus on support m, and a diagonal-unitary multiple of a positive semidefinite matrix. I independently checked the optimizing finite scalar sequences for q=1/2,1,2,7/3 and n/r=3/1,5/3,7/7. The 22604-case checker source was inspected, not used as proof. Boundary p=1 and r=n correctly included; no p=infinity claim.

## originality

PASS

PASS best-of-knowledge: the diagonal singular-value weak submajorization is classical and McDonald–Sukochev–Zanin directly study Schur boundedness/submajorisation, but neither their qualitative infinite-ideal pattern classification nor Kaftal–Weiss Schur–Horn diagonal realization gives the rank-budget sharp weak-Schatten multiplier formula and full nonnormal equality classification as a stated or immediate consequence. The finite optimization uses those prior tools nontrivially. Older Lorentz/Hardy sharp-constant literature remains a possible equivalence risk.

## value

PASS

PASS: The rank budget is natural in low-rank approximation/operator-ideal theory, and the exact amplification of diagonal observation in weak Schatten quasi-norms is a useful sharp invariant. A qualitative boundedness statement would not tell which support is worst or how rank one can diverge for p<1. The phase transition p=1 and all-extremizer classification give mathematical content beyond textbook restatement of Ky Fan/Schur–Horn and are meaningful across all finite ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
