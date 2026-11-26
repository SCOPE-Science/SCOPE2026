---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

A rank-one B-self-adjoint map is a·uB(u,·); nonzero square-zero maps of this form are precisely the (q−1) scalar choices at each isotropic line. Verified the odd-space zero count by the hyperbolic-plane recurrence, giving N projective points. Normalize the representative of a neighbor by B(u,w)=1; in a hyperbolic decomposition around u this leaves one free residual vector and uniquely determines the coefficient of u, giving K neighbors. For common neighbors of distinct nonorthogonal lines, the coefficient of the second line is fixed and nonzero by this normalization, and being nonorthogonal to the second line means the coefficient of the first is nonzero. The quadratic equation then excludes exactly the q^(2r−2) residual isotropic vectors (including zero), giving (q−1)D. For orthogonal lines use two hyperbolic pairs: the second dual coordinate is freely nonzero, one original coordinate is determined, the other arbitrary, and the residual dimension is 2r−3, giving the same count. Thus A²=DI+(q−1)DJ, with eigenvalue K on constants and A²=D on the zero-sum space. It yields exactly the displayed powers; their constant J terms are integers by comparison with integer entries. A surviving ordered product is a walk with the two endpoint lines fixed, and for any walk the target fixes exactly one scalar after the other k−1 are chosen. Counting all surviving walks gives the zero fiber by subtraction. Trace is the endpoint pairing times the nonzero scalar, and A² is everywhere positive, proving the sharp two/three-factor distinction within the stated target class. For mixing, the conditional endpoint law is A^(k−1)/(NK^(k−1)), times an independent uniform scalar. Subtract J/N² and sum absolute entries: for an even exponent the diagonal contribution is governed by 1−1/N, and for an odd exponent K marked entries per row give 1−K/N times the odd power's residual rate. D/K²=q^(−2r), giving both displayed rates, including k=2. Inspected check.py, VERIFICATION.md and verification_output.txt, without executing code. The dense finite checks compute all products in their sample; pair assertions are histogram/support-size checks, and triple assertions check one scalar per endpoint plus the full multiplicity histogram. This is not a direct test of each scalar's target-specific frequency at each length; scalar symmetry and the symbolic proof supply the full assertion.

## originality

PASS

The geometric matrix identity and its graph-walk consequences are not separately novel, nor is the method for unrestricted minimal nilpotents. The supported distinct result is the complete restricted matrix-product fiber law, where two different endpoint invariants alternate, together with the exact conditional law. The closest same-day claim is compared by statement rather than presumed to precede or follow this one.

## value

PASS

This is an exact word-map invariant for a natural orthogonal-equivariant rank-one factor set, not an arbitrary data slice. It explains a genuine change of the controlling target invariant with parity, shows sharp three-factor coverage, and gives the complete conditional decay profile. The spectral algebra is elementary once the reduction is known, but neither the unrestricted mixing formula nor the individual nilpotent counts answer these restricted target questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
