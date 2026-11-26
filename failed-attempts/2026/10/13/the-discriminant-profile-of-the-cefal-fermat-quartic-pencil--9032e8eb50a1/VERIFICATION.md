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

Over C the gradient is 4 z_i(S+t z_i^2), so for t nonzero every singular projective point has k nonzero coordinates of the same square and t=-k. Each such point lies on the fibre; the support/sign count is binomial(4,k) 2^(k-1) and signed permutations act transitively. In a chart with one supported coordinate set to 1, at the all-positive representative the affine Hessian splits into 8(J_(k-1)-kI) and 4k I_(4-k). Both blocks are invertible when present. The resulting finite singular locus rules out repeated factors and reducibility, and gives normality by the hypersurface Cohen–Macaulay property and regularity in codimension one. At zero the equation is the square of a smooth quadric, and the Fermat member at infinity is smooth. At each node Q takes the value k after normalization, giving order one on its local discriminant branch; locally the different nodes contribute one factor each. The degree 108 of the quartic discriminant then leaves order 68 at zero. The explicit resultant specialization in the originality assessment independently gives all orders without using transversality. The submitted verification code was not executed.

## originality

FAIL

The frozen record advertises the complete discriminant multiplicity profile as a main new result. Busé–Karasoulou's stronger published symmetric discriminant factorization evaluates to the entire claimed polynomial on this pencil, by four low-degree resultant substitutions. This is demonstrated prior implication, not an inference from title similarity. The verdict does not assert that all four baskets are printed verbatim in the sources.

## value

FAIL

The geometry is natural, and the explicit numbers are useful reference data, but the asserted discriminant invariant is a direct low-degree evaluation of a general published formula. The support and the notable sixteen-node fibre are already recorded for this exact pencil, and the other baskets follow by elementary support/sign counts and the two scalar Hessian blocks. The frozen package does not establish a distinct nonroutine contribution beyond this specialization and its local checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
