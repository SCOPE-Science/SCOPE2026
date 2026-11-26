---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In characteristic 2 the three off-diagonal derivatives vanish and Euler's formula puts the cubic in the ideal of the three principal minors. On a≠0 write x=b/a, y=d/a, η=f/a+xy; the chart is exactly k[x,y,η]/(η²). The three diagonal charts cover since the diagonal equations force all entries to vanish if a=c=e=0. The reduced charts are the Veronese charts. On the two overlaps with a≠0 the other nilpotent generators become x^−3η and y^−3η, the transition laws of O_P²(−3); the local algebra splittings give no global splitting. Independently the graded quotient is free over k[a,c,e] on the eight monomials b^i d^j f^l with i,j,l∈{0,1}, by the three monic square equations. This gives dimension 3 and the Hilbert series (1+t)^3/(1−t)^3, hence the height-three complete intersection, degree 8 and Hilbert polynomial 4n²+2; the degree-four Veronese is its support. The coefficient ac+b² of e is irreducible and cannot divide the constant term af²+cd² (check after localizing at a), so the cubic is irreducible. The complete hypersurface satisfies S₂, and its singular support of dimension 2 in dimension 4 gives R₁ and normality. These chart substitutions and the graded free basis are a replay path for the claimed geometry. CHECK.py and VERIFICATION.md were inspected, not executed; the supplied checks are not a proof of the overlap transitions or a priority check.

## originality

FAIL

An earlier indexed Resultary theorem gives the same intrinsic characteristic-two Jacobian double and its invariants using the permanent formulation. The permanent and determinant agree for this matrix in characteristic two, so the coverage is an equality of schemes, not just a similar surface or an overlap in reduced supports. This is a finding of existing statement-level coverage, not an inference of provenance or authorship from dates.

## value

FAIL

The characteristic-two nonreduced singular scheme is mathematically useful in itself, but the frozen record repeats that exact known scheme calculation and invariants. The additional normality conclusion is a routine consequence of the already determined singular support. No independently useful new invariant or structural refinement survives within the stated finding, so no substantive repair is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
