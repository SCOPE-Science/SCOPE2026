---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The beta integral gives the scalar resolvent representations for exponents s and -s with 0<s<1, hence the matrix representations by spectral calculus. Sherman–Morrison factors (A+tI)^(-1)-(B+tI)^(-1) as tau/(1+tau u^T R_t u) times (R_t u)(R_t u)^T, where R_t=(A+tI)^(-1). Subtract the positive-power formulas using X(X+tI)^(-1)=I-t(X+tI)^(-1); subtract the negative-power ones in the opposite order. The two resulting weights are positive and proportional to t^s and t^(-s). Integrability follows from bounded R_t near zero and O(1/t) decay at infinity. Nonnegative continuous quadratic forms under the integrals vanish precisely when x^T R_t u vanishes for every t>0. Multiplying by the product of distinct denominators and evaluating at each negative eigenvalue then shows x orthogonal to each P_lambda u. Polynomial interpolation gives equality of their span with K(A,u), and spectral orthogonality gives exactly the stated active count even with repeated eigenvalues. Symmetry gives the common range and the endpoints s=1 give the rank-one forms directly. The square-root example checks by Cayley–Hamilton, (B+3I)^2=13B, and det(D)=5-18/sqrt(13)>0 since 325>324. The checker was inspected, not executed; its tolerance-based ranks are corroborative, not exact certificates for the theorem.

## originality

FAIL

The distinct Resultary record for exact active-spectrum rank and pole budget states the very same fractional-power saturation, with strict definiteness after sign normalization on K and vanishing on K-perp, under weaker signed-update assumptions. It also states the endpoint ranks and the full-rank simple-spectrum consequence. Thus this is demonstrated substantive coverage, not a negative literature search or an inference based merely on dates.

## value

FAIL

The structural invariant is meaningful for exact versus approximate rank, but the existing active-spectrum theorem already supplies it with broader hypotheses and the same boundary ranks. No noncovered useful portion was established: the scalar-matrix and square-root examples are direct parameter substitutions and the closed-form two-dimensional witness only illustrates already established saturation. A certificate or exposition change does not create a new exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
