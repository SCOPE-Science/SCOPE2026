---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For a≠0 normalize H=t³+bt. The highest possible degree is 9, 6 or 3, and b is recovered respectively from f7/(3f9), f4/(2f6), or the ratio of the t and t³ coefficients of F itself. The remaining fiber coordinates are uniquely obtained in the independent basis H,H²,H³. For a=0 the fiber maps linearly and isomorphically onto P⟨t,t²,t³⟩. These charts overlap in image exactly on L minus [t]; the projective bundle gives a proper birational morphism with finite fibers, hence the finite normalization. The degree also follows from c1(O(1))³=1+2+3 on the bundle of lines. On the a=1 chart order the six columns as t,H,tH,H²,tH²,H³: the distinct highest degrees 1,3,4,6,7,9 give a triangular unit minor (the permutation to the record's order is even). On b=1,a=0, the varying-base column modulo the fiber is 2c₂t⁴+3c₃t⁵, which vanishes only over [t]; two fiber directions always survive. Off L, the sole preimage and injective tangent map imply m_B=m_AB by Nakayama; B=A+m_AB and finiteness imply B/A=0. On L a double fiber or the exceptional rank drop precludes smoothness. Finite properness isolates the two analytic germs at each double-fiber point, and each is a smooth embedded germ by immersion. Their vector tangents share exactly ⟨t,t³⟩ because the determinant with the four additional columns t²,t⁵,F²,F³ has factor α⁵, from the leading terms in degrees 6 and 9. On the [t] chart the inverse image is λ=aμ=0 and the two globally described P¹s meet there and nowhere else. These exact arguments check the content of the supplied symbolic certificates without executing the uploaded verifier. The result is over C and does not determine the Jacobian scheme, conductor, or completed local algebra.

## originality

PASS

Credit the coefficient bundle, birationality and degree to Piene–Shapiro. Moreover, finiteness and normalization alone are routine consequences of that bundle model: the dual bundle splits into positive line bundles, so the pulled-back hyperplane class is ample, precluding positive-dimensional fibers. The distinct result supported here is the exact reduced projective singular line and its full branch, fiber and exceptional differential geometry, not degree or finiteness in isolation. Neither the known affine classification nor the overlapping projective infinity-cycle calculation supplies this result.

## value

PASS

This computes the locus and manner in which the projective compactification loses normality in the first cubic-after-cubic example, a boundary question singled out by the source. The complete double line and its exceptional one-preimage point are meaningful input for further local and conductor calculations and are not numerical degree recomputations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
