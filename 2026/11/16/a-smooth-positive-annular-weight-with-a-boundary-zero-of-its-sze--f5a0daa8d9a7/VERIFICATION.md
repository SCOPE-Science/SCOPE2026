---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The domain is exactly 1/4<|z|<1 with Euclidean boundary arclength and positive smooth nonradial phi=|z-2/3|^2. Multiplication by z-p is an isometry onto unweighted H^2 functions vanishing at p, and the rank-one compressed reproducing kernel has numerator D(w)=H(w)H(p²)-H(p)H(pw). The two selected negative test values and p²,p,pw fall in Laurent convergence annulus; exact Fraction evaluations give D32(-3/8)>19/100 and D32(-3/4)<-9/100. Explicit bilateral tails imply |D-D32|<24E32<1/125, so the intermediate value theorem gives genuine boundary-to-interior zero. The result asserts existence only, not uniqueness.

## originality

PASS

The explicit nonradial positive weight yielding a boundary-to-interior weighted Szegő kernel zero directly supplies an example requested in Jain–Verma Remark 5.7(1). Their Example 5.3 assumes a holomorphic factor nonvanishing on the closed domain, whereas q=z-2/3 has an interior zero and forces a rank-one compression. The related published rotation-invariant annular family and derivative-zero theorems do not cover the same assertion. Best-of-knowledge PASS.

## value

PASS

A concrete smooth strictly positive analytic boundary weight witnessing a formerly explicit boundary-to-interior Szegő zero question is a mathematically motivated counterexample. Its exact certified interval is reusable even without a full classification of weights and without a closed-form root.

The dated certificate retains the supplied scientific assessment, sources and limitations.
