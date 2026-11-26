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

The four prime-power rows and the integral finding hold. Independent exact norm/elimination recovers the 22-degree affine polynomial, absolute discriminant 2^42*7^77, the linear subresultant D y+N, and the unit denominator resultants at every factor (including x). Substitution of -N/D satisfies both equations modulo the eliminant. The norm belongs to the affine ideal by the multiplication-matrix adjugate; the linear subresultant then makes the affine Hessian intersection over Z[1/42] exactly the graph over its projection. At the two infinity vertices the local linear parts of the curve and sextic are the two chart parameters in opposite roles, so the sections are étale and separate components of the finite intersection. The fiberwise 24 simple intersections are ordinary, since tangent contacts 3 and 4 give Hessian orders 1 and 2 in the allowed characteristics. Orbit products of the stated cyclotomic generators give degrees 3,6,6,6, with discriminants 7^2,-7^5,-2^6*7^5,-2^6*7^5, so the order indices are units on the base. This proves the relative decomposition and makes q-Frobenius the stated regular actions and quotient action. The standard monic-f resultant is +x times the four factors, not minus as printed; at x=1 the Sylvester determinant is -232 and SymPy 1.14.0 gives +232. Only the unit-normalized eliminant matters. Reproduction: python /workspace/flex_and_octic_reproduction.py (SymPy 1.14.0); frozen VERIFY.py only inspected.

## originality

FAIL

The same-date distinct record e6c7b4b6a579 gives the exact uniform Frobenius law and supplies integral point representatives and separation certificates that imply this record's abstract finite étale decomposition. Its omission of the displayed scheme isomorphism does not leave a separate arithmetic finding. The explicit projection formula is a different certificate, not a new invariant in the Finding. No chronological priority between the two copies is inferred.

## value

FAIL

The flex divisor and its integral arithmetic are naturally useful inputs to descent, but the proposed second finding is a restatement plus immediate scheme-theoretic translation of the already supplied separated integral orbits. The rational coordinate-recovery formula is useful verification data; the submitted Finding does not claim a new independent application or invariant supported by that formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
