---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

The claim is mathematically correct for the stated real or complex ell_p^3 smooth range 1<p<infinity. The unique normalized duality map gives the quotient (A u^(p-1)+B v)/(1+u^p+v^p), with interior global maximizer for A,B>0 by epsilon perturbation on boundary and compactness. Stationarity yields p w u=(p-1)A, p w v^(p-1)=B and u^p/(p-1)+(p-1)v^p=1, hence a unique strictly decreasing positive scalar root and the exact mixed-Luxemburg norm. Zero-weight cases are rank-one limits; p=2 gives sqrt(A^2+B^2)/2. Continuous image of connected sphere plus phase rotations supplies full disk over C and interval over R. For p=4 the stated identity H^3-(CH+D^3)^2=CD(C^4+3C^3D+3C^2D^2+3CD^3+D^4)>0 and uniqueness of positive cubic roots rigorously imply v_4(A,B)>v_4(B,A) for all A>B>0. Independent symbolic polynomial expansion verified the quartic factorization; 56 parameter cases with KKT witness and independent optimization gave max numerical violation 0, duality and witness discrepancies below 9e-16. Numerical cases do not establish universal proof; that follows from the analytic chain in RESULT.md.

## originality

FAIL

FAIL by decisive exact published mathematical coverage. The published Resultary 2026/10/11 b6805f9f0272 result states and proves exactly the same h_p times the mixed (p,q) gauge as the assigned result for complex arbitrary weights, with full disk and duality. The published b3244292cab1 result independently gives an equivalent universal scalar-root radius on real/complex ell_p^3 with positive weights and maximizing phases. These match objects, parameters, normalization and statements, not just title/keywords. The quartic all-weight order statement is a consequence of comparing the prior universally exact radius functions, and thus cannot rescue an otherwise covered theorem. Both published source texts were actually read; older journal work is only narrower background. Date-order uncertainty between same-day published records is preserved as a historical risk, not used to assert independence or originality.

## value

PASS

The underlying exact two-weight numerical-radius invariant remains mathematically substantive: three sites are the smallest nilpotent chain with interacting adjacent coefficients, and the all-parameter gauge, duality, full numerical-range geometry and strict non-Hilbert orientation are natural useful structural facts. This earns intrinsic V=PASS separately from novelty; the work is not an arbitrary numerical table or a trivial one-link substitution. Its established prior publication makes the submitted claim ineligible as an original finding (O=FAIL), regardless of this intrinsic mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
