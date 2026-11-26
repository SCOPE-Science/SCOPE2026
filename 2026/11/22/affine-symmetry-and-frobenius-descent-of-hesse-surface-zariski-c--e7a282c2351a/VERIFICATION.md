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

Adjunction with the nef fiber F=-K forces a negative curve to be a rational section of square -1 or a vertical component of square -2. Four I3 fibers give 12 components; the rank-zero section group has order 9 from the unimodular Néron–Severi lattice and discriminant 3^4 of the fiber root lattice. The nine exceptional curves exhaust the sections. The four exclusions are necessary by non-negative-definite principal submatrices (the I3 triple, the two types of three-vertex chains, and the chain with two terminal sections); otherwise each connected block has positive definite negative intersection form. Independently enumerating unions of point and line permutation cycles, with each occupied parallel class admitting at most one selected incident section and all multiply incident section points excluded, reproduces all 11 class sizes and the complete fixed-size table in the frozen JSON. The two Burnside sums are 103248 and 64584, giving 239 and 299. In the nonsplit standard model inversion of cube roots fixes exactly one base point on each coordinate axis and swaps the other six points in three pairs. It is the reflection class, for which the independent count is 1037. To make the descent argument explicit: for a stable negative support with intersection matrix M and a rational ample A, solve (-M)c=(A·C_i)_i. Positive definiteness and nonpositive off-diagonals of -M give c_i>0 (test the negative part of c against the system). The resulting P=A+sum c_i C_i is big nef, orthogonal to exactly the support; the coefficients are constant on Frobenius orbits. Add the reduced support to P to obtain a rational big divisor with precisely the desired negative part. This justifies the rational-chamber interpretation, not just the finite permutation computation.

## originality

PASS

The geometric support count, incidence criterion and projective Hessian symmetry are known, as the frozen record acknowledges. The supported distinction is the Hesse support action, with the full distribution by support size for each affine class, both orbit censuses, and the nonsplit chamber count. The strongest matching same-day record counts fixed graph Jacobian groups rather than fixed negative supports. General support enumeration and the older ordinary generating polynomial do not provide the classwise enumeration; the identity row alone is old.

## value

PASS

The ordinary Hesse census cannot answer how many supports survive an arithmetic action or identify chamber orbits under the natural symmetries. The classwise data answer both questions and distinguish finer fixed-support distributions even when totals coincide. The exact nonsplit count for the standard pencil is a concrete geometric use of this complete finite classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
