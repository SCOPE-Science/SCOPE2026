---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Every phase is feasible by the uniform positive spectral fence. Determinant expansion leaves only the two full directed cycles as phase-bearing terms, giving Q(lambda)-2Rt with the negative sign. Differentiating simple roots gives 2R times the order-(m-1) divided difference of p*x^(p-1). Hermite–Genocchi gives the stated signed derivative, with simplex volume 1/(m-1)!; integrating over length 2 gives both fences and 4mR at p=m. A repeated root satisfies Q'=0, so corresponds to one of finitely many parameters. Continuity of the roots handles these points without losing strict order. The largest simple root has positive characteristic derivative, so its strict monotonicity extends in the same way. The plateau at lower integers, quasi-norm convention, and unique endpoint phase classes outside the plateaux are consistent.

## originality

FAIL

Not an exact indexed duplicate, but the phase ordering and quantitative gap are mechanical consequences of prior Floquet discriminant and coefficient-derivative formulas. Teschl's (7.39)–(7.41) give, for the same twisted finite Jacobi matrix with b_j=1 and a_j=r_j, chi_t=2R(Delta-t). Mitchison–Jozsa's appendix supplies the root derivative in the varying elementary symmetric coefficient and the simplex divided-difference formula. For any smooth trace power, the chain rule and g(x)=p*x^(p-1) immediately give the sign and min/max derivative bounds including the constant derivative at p=m. Positive spectral fencing is row-sum bounding; continuity and selecting the outer root give the remaining assertions. The result is covered by implication, not by an earlier verbatim Schatten-cycle theorem.

## value

FAIL

The phase question is natural and the formula is pedagogically useful, but the claimed theorem is the direct trace-power application of known Jacobi phase dependence and general coefficient calculus. The quantitative bounds use only a row-sum interval and the extremal integrand values; they do not add a nonmechanical invariant or a sharp amplitude-dependent gap beyond the known coefficient identity at p=m.

The dated certificate retains the supplied scientific assessment, sources and limitations.
