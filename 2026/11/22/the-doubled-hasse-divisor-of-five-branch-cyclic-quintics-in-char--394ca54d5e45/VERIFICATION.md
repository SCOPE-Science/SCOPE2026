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

Simple roots give smoothness at the finite ramification points, the Y derivative handles the other affine points, and the Z derivative handles infinity. The order of x, y and dx at infinity is -5, -4 and -6, respectively; at finite branch points dx has order 4. These orders give the stated six independent holomorphic forms. Rewriting with denominator y^(11j) and extracting exponents 11k+10 gives the three coefficient blocks. Independent multinomial extraction, exact determinants, gcd and localized ideal calculation reproduce the factors and show middle block rank exactly one on the support; the other ranks there are zero and three. H=0 is reduced; the map from the ordered coordinates (a,b) to (s,t) is étale away from the discriminant, so pullback does not change the multiplicity two. The divisor uses the linearized Frobenius determinant, not entrywise rooted functions on parameter space. Over F121 the square of the semilinear middle block is represented, up to conjugation by field Frobenius, by B3 times its field conjugate. Its rank one and nonzero trace imply that powers have rank one. A replay over a third quadratic presentation verifies 72 and 0 over F11, 13832 and 210 over F121, and relabeling by four generating adjacent swaps gives orbit sizes 30,60,120.

## originality

PASS

Credit the existing five-branch model and the related doubled-divisor examples. The distinct result is the explicit characteristic-11 two-parameter Hasse divisor with its geometric rank and split-field arithmetic stratification. Nothing in the accessible comparisons supplies those statements for this family.

## value

PASS

The full smooth two-dimensional five-point configuration family is natural. The multiplicity, rank rigidity, and contrasting split-field censuses provide more than an example or a rerun of a published arithmetic table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
