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

For the complete block 0 <= N < 3^L, the L ternary digits are independent and uniform. Legendre gives Y=s_3(N) since multiplying by 3 shifts digits; Kummer counts the outgoing carries of N+N, including a carry out of the highest sampled digit. An additional leading zero cannot produce a new carry. With incoming carry 0, digits 0,1 stay at 0 and digit 2 goes to 1; with incoming 1, digit 0 goes to 0 and digits 1,2 stay at 1. Weighting by u for an outgoing carry and v to the digit power gives the stated matrix and the endpoints (1,0) and (1,1)^T. For an independent covariance check, tilt each digit by weights 1,v,v^2; if q_j is the resulting digit probability, the carry probability obeys p_i=q_2+q_1 p_{i-1}. Hence p_i=[v^2/(1+v^2)](1-q_1^i). At v=1, d(q_1)/d(log v)=0 and the derivative of v^2/(1+v^2) equals its value, giving Cov(X,Y)=E X by differentiating the tilted E X. The carry transition has second eigenvalue 1/3, so Cov(c_i,c_j)=3^{-(j-i)}(1-3^{-2i})/4 for i<=j. Its geometric sum gives the stated exact variance; the independent digits give the moments of Y. For the CLT, tilt the matrix at u=e^s,v=e^t and divide by 3. Its simple leading eigenvalue is 1 at the origin, separated from 1/3. Locally the MGF is a leading eigenvalue to power L times an analytic prefactor equal to 1 at the origin, plus an exponentially small relative remainder. The second-order log expansion therefore uses the limiting per-L covariance in the record and yields its nondegenerate Gaussian limit; the bounded difference in the X center is immaterial. Independently replayed with Python 3 at /tmp/opencode/frozen_review_4.py: floor-sum factorial valuations for every input at each L=1..11, compared with polynomial propagation and exact rational moments. All matched (133 joint cells at L=11). This computational check is bounded; the digit argument establishes all L. The frozen verifier was inspected, not run.

## originality

FAIL

Exact indexed coverage, not a correctness defect or a priority finding. Put Z=nu_3(binomial(3N,N)). The factorial identity binomial(3N,N) binomial(2N,N)=(3N)!/(N!)^3 gives Y=X+Z identically. The indexed record gives the full joint law of (X,Z) for the same uniform blocks, explicitly gives Cov(X,s_3(N))=E X, and gives the corresponding joint CLT. Changing coordinates mechanically recovers the complete frozen result. The index path date does not determine who obtained the mathematics first.

## value

FAIL

The pairing of two natural arithmetic valuations and the exact covariance are mathematically useful, but the frozen record offers no independently useful unknown invariant beyond the indexed joint law and its explicitly stated digit-sum covariance. The change of variables is a factorial cancellation and a direct shear, not a new contribution. No distinct surviving claim is available for a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
