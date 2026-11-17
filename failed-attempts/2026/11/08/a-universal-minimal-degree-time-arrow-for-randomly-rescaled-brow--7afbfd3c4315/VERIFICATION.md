---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The generator L x^k=Dk(k-1)x^(k-2)-lambda_k x^k gives v=2D/lambda2 and w=12Dv/lambda4. Polynomial semigroup P_t x^3=e^-lambda3 t x^3+6D H(t)x and P_t x=e^-lambda1 t x imply I(t)=w(lambda3-lambda1-lambda4/2)H(t)=-r w E[(1-A)^2(1-A^2)]H(t)/2. Uniform strict contraction ensures positive factor, finite moments and H(t)>0. The divided-exponential kernel has one and only one maximum, including equal-rate H=t e^-lambda1 t. Spatial sign symmetry and stationarity rule out all antisymmetric polynomial moments of total degree below four. Independently checked the coefficient map to an earlier full derivation, and the example A=+/-1/2 gives -16 t e^-t.

## originality

FAIL

Decisive direct coverage. Oct 18 theorem uses H_old=E[X_t^3 X_0]-E[X_t X_0^3]=-I_new; its exact amplitude is 12D^2 r F/(lambda2 lambda4), equal to r*w*F/2 with w=24D^2/(lambda2 lambda4). F=(1-A)^3(1+A)=(1-A)^2(1-A^2). It already gives strict sign for all bounded signed contractions, the same unique t*, covariance matching, and even overshoot sign reversals. Nov 2 theorem repeats the exact strict signed-law specialization with added reversible-noise invariance. The alleged degree-four minimality is the elementary parity/stationarity observation, not a distinct substantive remainder.

## value

FAIL

A degree-four temporal arrow is meaningful physically, but this exact sign, amplitude, optimal lag and mark-uniform behavior were already established in stronger published results. The only additional degree-minimality sentence follows immediately from spatial sign symmetry and stationarity for low bidegrees, so it is not an independent motivated research result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
