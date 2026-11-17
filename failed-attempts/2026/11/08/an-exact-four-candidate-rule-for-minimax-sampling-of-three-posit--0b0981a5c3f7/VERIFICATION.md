---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The precise objective is max_p lambda_min(C^(1/2) diag(p) C^(1/2)) for a unit-diagonal SPD 3x3 correlation C with a,b,c>0 and p on the probability simplex. Its reciprocal minimization over w>0, C-diag(w) positive semidefinite, has a unique optimizer from strict convexity and Slater. KKT gives Z>=0 with Z_ii=1/w_i^2 and MZ=0. Since M nonzero singular with positive off-diagonal entries, rank M is one or two. Rank-one M=rr^T forces r_i^2=ab/c,ac/b,bc/a and the triangle/Heron condition on lengths r_i/w_i; rank-two M forces a rank-one Z=vv^T, Cv=s, and the three sign vectors. The two ranks exhaust the exact global KKT candidates and all boundaries. Exact rational witness formulas in both branches agree with submitted rational verifier logic. The proof is universal; 1000-point grid is only supplementary.

## originality

FAIL

FAIL. The earlier (2026-11-02) signed-triangle closed-form theorem for minimax three-row randomized Kaczmarz already solves precisely the same optimized one-step minimum-eigenvalue problem for EVERY real SPD unit-diagonal Gram matrix. For any C here, take invertible unit-row A with AA^T=C. Nonzero spectra of A^T diag(p) A and C^(1/2) diag(p) C^(1/2) coincide; therefore the already-published unique p*(C) and exact lambda*(C) cover the entire positive-correlation subclass. The submitted four-candidate representation is a change of coordinates for a known answer, not a novel additional theorem.

## value

PASS

The sharp worst-case expected decrease per exact coordinate step is a natural convergence-rate invariant; exact optimal sampling across frustrated sign patterns and a spectral multiplicity transition is mathematically useful and nontrivial. This would be valuable independent of the decisive priority rejection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
