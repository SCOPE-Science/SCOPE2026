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

For N=2m normalized unweighted path S, Chebyshev recurrence gives T_0(S)e0=e0, T_j(S)e0=e_j/sqrt(2) for 1<=j<=N-2, and T_(N-1)(S)e0=e_(N-1). Thus W_N has the explicit inverse by Chebyshev monomial coefficients. The left/right blocks of B_N observe disjoint halves before time m, so B_N is equivalent to C_m direct sum C_m with diagonal products yielding |det B_N|=2^(-(m-1)^2). For rho=1+sqrt2, Chebyshev coefficient row norms lie between (rho^j-rho^-j)/(2sqrt(j+1)) and rho^j, via unit-circle Parseval and evaluation at i; forward row norms are bounded polynomially. Inverse operator row-vs-Frobenius bounds imply kappa(W_N)^(1/N)->rho and kappa(B_N)^(1/N)->sqrt(rho). Independently constructed N=4,6,8,10 finite observation matrices and checked propagation, disjoint blocks and determinant identities; these checks support, not prove, the all-m limits.

## originality

PASS

The earlier determinant-only endpoint placement theorem and classical polynomial coefficient growth do not determine the exponential smallest-singular-value improvement of this two-end graph observation design. Full text of a plausible recent dynamical sampling paper was unavailable; its priority risk is retained without automatically failing originality.

## value

PASS

A natural equal-total-budget sensor placement comparison has sharp distinct exponential noise amplification rates, explicit inverses and an exact two-end determinant. This is not mere reparameterization of a known determinant theorem because small singular values are independent of determinant alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
