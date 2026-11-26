---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The Hermitian part of A is −(aP₁+bP_N)/2. A nondecaying eigenvector would have zero endpoint amplitudes, and the nonzero hopping in the path recursion forces it to vanish. The integrated endpoint effects are therefore positive, sum to I by differentiating the survival norm, and are the unique solutions of the adjoint Lyapunov equations. For the proposed E_L, the diagonal equations are ad₁+2Jc=a and bd_N=2Jc. For N≥3 the first and last bond equations are J(d−d₁)+ac/2=0 and J(d_N−d)+bc/2=0. For N=2 they merge into J(d_N−d₁)+(a+b)c/2=0. In the interior the diagonal is constant and the potential two-step entries cancel because the bond entries are constant. Substituting the displayed coefficients satisfies all equations; the upper-bond sign is −ic for A=−iH−(aP₁+bP_N)/2. The trace formula applies to arbitrary density matrices, but interior-site flatness only to site starts and their diagonal mixtures. For each fixed b>0 and an interior start, differentiating the reported rational probability yields the sign of 4J²−a², giving a unique optimum a=2J and the stated probability and zero end limits. Setting a=b yields 1/2. Inspected RESULT.md, VERIFICATION.md, artifacts/verify.py and artifacts/requirements.txt; the reported finite matrix and rational checks were not executed or used as proof of length-uniform claims.

## originality

FAIL

The exact unequal-rate XX-chain solution of Žnidarič (arXiv:1006.5368) already determines the same full matrix by transpose Lyapunov duality, including all complex bond entries and zero further entries. Its printed magnetization and current formulas give the site-resolved splitting and reduce the rate optimization to differentiation of the known current factor. This is stronger evidence than shared use of a Lyapunov method or a comparison with projective monitoring. The two physical protocols differ, but the mathematical correspondence is exact.

## value

FAIL

The competing absorption observable is physically motivated, but its proposed full effect, flat interior, and sharp rate optimum are a transpose and elementary optimization of an already solved covariance. No additional nonroutine observable or mathematical consequence survives as a separate repairable claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
