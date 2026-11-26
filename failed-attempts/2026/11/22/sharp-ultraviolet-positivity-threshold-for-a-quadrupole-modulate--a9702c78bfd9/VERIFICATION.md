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

For the classical S² Poisson kernel and probability area measure, two uses of the Legendre recurrence give λ_n/r^n=1+bR_n with incoming degrees n−2,n,n+2. Write R_n=A_n/t+B_n+C_nt, t=r². The coefficients sum to one at t=1, A_n increases from 0 to 3/8 (with A_0=A_1), and C_n strictly decreases to 3/8; writing R_n=1+A_n(1/t−1)+C_n(t−1) proves strict increase in n for t<1, including n=0. Independently, at v=(r+r⁻¹)/2 and b=−1/P₂(v), the critical kernel is 3(1−r²)(v+u)(1−2ru+r²)^(-1/2)/(4rP₂(v)). Its generating function and the Legendre recurrence give strictly positive coefficients and the claimed normalized eigenvalue asymptotic: the coefficient of P_n divided by r^n tends to 3(1−r⁴)/(4r²P₂(v)), and dividing by 2n+1 gives precisely the stated constant. Schoenberg implies necessity below the threshold (the limiting ratio is P₂(v)) and sufficiency on the stated half-line; harmonic density separates nonzero measures with distinct finite support. The gap for every finite set of degrees gives the missed-cutoff result by continuity. Differentiating b_* gives the stated strict monotonicity and endpoint limits. No source script was run.

## originality

FAIL

The core sharp threshold, strict boundary and infinity-only obstruction are covered by the earlier indexed mixed dipole–quadrupole Poisson theorem, at the level of its explicit scientific statement. In its zero-dipole section the ratios in the three advertised tests are r², (2+3r²)/5 and (3+2r²+3r⁴)/(8r²). The last is positive and strictly greater than both low-degree ratios, so these tests give exactly the submitted bound with both low-degree tests slack. The indexed strictness/universality claim then also covers the endpoint behavior. This is positive evidence of a stronger prior result, not a verdict based on a retrieval failure, nor inferred from the distinct same-date paper. The exact coefficient of the critical eigenvalue asymptotic is not established to have been printed earlier.

## value

FAIL

The ultraviolet obstruction and strict boundary would be useful, but they are already furnished by the earlier three-test cone. The isolated explicit leading constant uses only factorization at the known endpoint and the first Legendre recurrence applied to the usual generating function. No independently useful unknown problem is established for this routine remainder; narrowing to it would not preserve a valuable new claim at this standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
